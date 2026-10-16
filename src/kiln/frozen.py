"""Fichiers figés : les dérogations `file = "…"` de `kiln-waivers.toml`. `kiln update` et
`kiln set` n'y touchent plus ; mais un fichier figé ne doit pas dériver en silence, d'où le
rapport de ce que kiln y a changé entre deux versions."""

import difflib
import tempfile
from pathlib import Path

import copier
from copier.errors import CopierError
from packaging.version import Version

from kiln import renames, ui
from kiln.charter.waivers import WAIVERS_FILE, load
from kiln.stack import read_answers
from kiln.versions import release_version

DIFF_LINES = 40
# First release whose template speaks English (answer keys included).
ENGLISH_TEMPLATE = Version("0.4.0")


def frozen_files(root: Path) -> list[str]:
    """Fichiers figés par une dérogation active (une dérogation échue ne fige plus rien)."""
    return [waiver.file for waiver in load(root).actives if waiver.file]


def report_frozen_drift(root: Path, source: str, previous: str, current: str) -> None:
    """Ce que kiln a changé, de `previous` à `current`, dans les fichiers que le repo a figés."""
    frozen = frozen_files(root)
    if not frozen or not previous or previous == current:
        return
    answers = {k: v for k, v in read_answers(root).items() if not k.startswith("_")}
    try:
        with tempfile.TemporaryDirectory() as tmp:
            before = _render(source, previous, answers_for(previous, answers), Path(tmp) / "before")
            after = _render(source, current, answers_for(current, answers), Path(tmp) / "after")
            diffs = {f: _diff(before / f, after / f, f) for f in frozen}
    except (CopierError, OSError) as error:  # OSError : révision introuvable (git)
        ui.note(f"Fichiers figés : comparaison des versions de kiln impossible ({error}).")
        return
    changed = {f: d for f, d in diffs.items() if d}
    if not changed:
        return
    ui.panel(
        f"kiln a changé des fichiers figés ({WAIVERS_FILE}) : {previous} → {current}",
        [f"- {f}" for f in changed]
        + ["Reporter ce qui convient, ou lever la dérogation pour reprendre le modèle."],
    )
    for diff in changed.values():
        print("\n".join(diff[:DIFF_LINES]))
        if len(diff) > DIFF_LINES:
            print(f"… et {len(diff) - DIFF_LINES} ligne(s) de plus")


def answers_for(ref: str, answers: dict[str, object]) -> dict[str, object]:
    """The answers as the template at `ref` names them: French before kiln 0.4.0."""
    version = release_version(ref)
    if version is not None and version < ENGLISH_TEMPLATE:
        return renames.legacy_answers(answers)
    return answers


def _render(source: str, ref: str, answers: dict[str, object], destination: Path) -> Path:
    copier.run_copy(
        source,
        destination,
        data=answers,
        vcs_ref=ref,
        defaults=True,
        quiet=True,
        unsafe=False,
    )
    return destination


def _diff(before: Path, after: Path, name: str) -> list[str]:
    old, new = (p.read_text().splitlines() if p.exists() else [] for p in (before, after))
    return list(
        difflib.unified_diff(old, new, f"kiln {name} (avant)", f"kiln {name} (après)", lineterm="")
    )
