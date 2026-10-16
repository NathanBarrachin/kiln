"""Versions of kiln: three-number semver, `vMAJOR.MINOR.PATCH`.

In 0.x, each release bumps the patch, breaking ones included (`0.3.4 → 0.3.5`); the minor only
moves for a milestone (CLAUDE.md, Versions). Two channels: a release first ships as a candidate
(`v0.3.5-rc.1`), followed by the machines on the `internal` channel (`kiln set
channel=internal`); it is promoted (`v0.3.5`, merged into `main`) when the next one is ready.
The `public` channel, the default, only sees promoted releases. Each release has its entry in
`CHANGELOG.md`, which `kiln update` shows when moving from one version to the next.
"""

import json
import re
import subprocess
from dataclasses import dataclass
from importlib import resources
from importlib.metadata import Distribution, PackageNotFoundError, distribution
from pathlib import Path

from packaging.version import InvalidVersion, Version

from kiln.config import INTERNAL_CHANNEL, load_config

KILN_GIT_URL = "https://github.com/antoine-tena/kiln"
# Package name on PyPI; `kiln` before, still there on machines not yet updated.
PYPI_NAME = "kiln-cli"
DISTRIBUTIONS = (PYPI_NAME, "kiln")
CHANGELOG_FILE = "CHANGELOG.md"
# `v0.4.0`, `v0.4.0-rc.2`, and what `git describe` appends (`v0.4.0-3-gabc1234`).
RELEASE_TAG = re.compile(r"^v(\d+\.\d+\.\d+(?:-rc\.\d+)?)(?:-(\d+)-g([0-9a-f]+))?$")
RELEASE_HEADING = re.compile(r"^## (v\d+\.\d+\.\d+)(?:\s+[-—·]\s+(.+))?$")
NETWORK_TIMEOUT = 5
# Before the first release, projects followed a commit: everything is new to them.
BEFORE_FIRST_RELEASE = Version("0")


@dataclass(frozen=True)
class ReleaseNotes:
    tag: str
    date: str
    lines: list[str]


def release_version(ref: str) -> Version | None:
    """Version of a tag or of a `git describe` output; None for a plain commit."""
    match = RELEASE_TAG.match(ref.strip())
    if match is None:
        return None
    try:
        return Version(match.group(1))
    except InvalidVersion:
        return None


def tag_of(ref: str) -> str | None:
    """The release tag of a revision: `v0.4.0-rc.2` for `v0.4.0-rc.2-3-gabc1234`."""
    match = RELEASE_TAG.match(ref.strip())
    return f"v{match.group(1)}" if match else None


def follows_candidates() -> bool:
    """Does this machine follow the candidates (`internal` channel)?"""
    return load_config().channel == INTERNAL_CHANNEL


def latest_release(source: str = KILN_GIT_URL, *, candidates: bool | None = None) -> str | None:
    """Tag of the repo's latest release, candidates included on the `internal` channel; None
    without network or release."""
    if candidates is None:
        candidates = follows_candidates()
    try:
        listing = subprocess.run(
            ["git", "ls-remote", "--tags", "--refs", source],
            capture_output=True,
            text=True,
            timeout=NETWORK_TIMEOUT,
            check=False,
        ).stdout
    except subprocess.TimeoutExpired, OSError:
        return None
    tags = [line.rsplit("refs/tags/", 1)[-1] for line in listing.splitlines()]
    releases = [
        (version, tag)
        for tag in tags
        if (version := release_version(tag)) is not None
        and (candidates or not version.is_prerelease)
    ]
    return max(releases)[1] if releases else None


def _installed_distribution() -> Distribution | None:
    for name in DISTRIBUTIONS:
        try:
            return distribution(name)
        except PackageNotFoundError:
            continue
    return None


def install_source() -> str:
    """Where the tool comes from: `pypi`, `git` (a GitHub revision) or `folder` (a checkout)."""
    dist = _installed_distribution()
    direct_url = (dist.read_text("direct_url.json") or "") if dist else ""
    if not direct_url:
        return "pypi"
    return "folder" if _source_dir(direct_url) is not None else "git"


def upgrade_command(version: str) -> str:
    """Command that installs version `vX.Y.Z` of the tool, the way it was installed: PyPI only
    has promoted releases, a candidate goes through GitHub."""
    release = release_version(version)
    if install_source() == "pypi" and release is not None and not release.is_prerelease:
        return f'uv tool install --force "{PYPI_NAME}=={release}"'
    return f'uv tool install --force "git+{KILN_GIT_URL}@{version}"'


def tool_release_tag() -> str | None:
    """Tag of the kiln release the installed tool is: the template must never be newer than
    it, since the conversions from one version to the next live in its code.

    - PyPI: `v` + the package version (a PEP 440 pre-release `0.4.0rc1` is `v0.4.0-rc.1`);
    - GitHub (`uv tool install git+…@<tag>`): the requested tag, otherwise the installed commit;
    - folder (a checkout of kiln): the release tag nearest its `HEAD`.

    None when the tool cannot place itself (package not found, folder without a tag)."""
    dist = _installed_distribution()
    if dist is None:
        return None
    direct_url = dist.read_text("direct_url.json") or ""
    if not direct_url:
        return _pypi_tag(dist.version)
    try:
        origin = json.loads(direct_url)
    except ValueError:
        return None
    vcs_info = origin.get("vcs_info")
    if isinstance(vcs_info, dict):
        requested = str(vcs_info.get("requested_revision", ""))
        if release_version(requested) is not None:
            return requested
        return str(vcs_info.get("commit_id", "")) or None
    source = _source_dir(direct_url)
    return _nearest_tag(source) if source is not None else None


def _pypi_tag(version: str) -> str | None:
    try:
        parsed = Version(version)
    except InvalidVersion:
        return None
    tag = f"v{parsed.base_version}"
    if parsed.pre is not None and parsed.pre[0] == "rc":
        tag += f"-rc.{parsed.pre[1]}"
    return tag if release_version(tag) is not None else None


def _nearest_tag(source: Path) -> str | None:
    try:
        described = subprocess.run(
            ["git", "-C", str(source), "describe", "--tags", "--abbrev=0", "--match", "v[0-9]*"],
            capture_output=True,
            text=True,
            timeout=NETWORK_TIMEOUT,
            check=False,
        ).stdout.strip()
    except subprocess.TimeoutExpired, OSError:
        return None
    return described if release_version(described) is not None else None


def installed_version() -> str:
    """Version of the tool: `v3`, and for a tool installed from a folder, what git says
    (`v3 +4 · abc1234`: four commits after v3)."""
    dist = _installed_distribution()
    if dist is None:
        return "v?"
    package_version = f"v{dist.version}"
    source = _source_dir(dist.read_text("direct_url.json") or "")
    if source is None:
        return package_version
    try:
        described = subprocess.run(
            ["git", "-C", str(source), "describe", "--tags", "--always"],
            capture_output=True,
            text=True,
            timeout=NETWORK_TIMEOUT,
            check=False,
        ).stdout.strip()
    except subprocess.TimeoutExpired, OSError:
        return package_version
    match = RELEASE_TAG.match(described)
    if match is None:
        return f"{package_version} · {described}" if described else package_version
    tag, distance, commit = f"v{match.group(1)}", match.group(2), match.group(3)
    return f"{tag} +{distance} · {commit}" if distance else tag


def _source_dir(direct_url: str) -> Path | None:
    """Folder the tool was installed from (`uv tool install <folder>`), if any."""
    try:
        origin = json.loads(direct_url) if direct_url else {}
    except ValueError:
        return None
    url = str(origin.get("url", ""))
    if "dir_info" not in origin or not url.startswith("file://"):
        return None
    return Path(url.removeprefix("file://"))


def read_changelog() -> str:
    """`CHANGELOG.md` shipped with the tool; otherwise the repo's (tool in development)."""
    packaged = resources.files("kiln") / CHANGELOG_FILE
    if packaged.is_file():
        return packaged.read_text(encoding="utf-8")
    in_repo = Path(__file__).resolve().parents[2] / CHANGELOG_FILE
    return in_repo.read_text(encoding="utf-8") if in_repo.is_file() else ""


def parse_changelog(text: str) -> list[ReleaseNotes]:
    """`## vN — date` entries of the changelog, in file order (latest first)."""
    notes: list[ReleaseNotes] = []
    for line in text.splitlines():
        heading = RELEASE_HEADING.match(line)
        if heading:
            notes.append(ReleaseNotes(heading.group(1), heading.group(2) or "", []))
        elif notes and line.strip():
            notes[-1].lines.append(line.rstrip())
    return notes


def notes_between(old_ref: str, new_ref: str, changelog: str) -> list[ReleaseNotes]:
    """Releases passed between two revisions of the template: after `old_ref`, up to `new_ref`."""
    new = release_version(new_ref)
    if new is None:
        return []
    # A candidate already carries its release's changes: final versions are compared.
    old = Version((release_version(old_ref) or BEFORE_FIRST_RELEASE).base_version)
    target = Version(new.base_version)
    return [
        notes
        for notes in parse_changelog(changelog)
        if (version := release_version(notes.tag)) is not None and old < version <= target
    ]
