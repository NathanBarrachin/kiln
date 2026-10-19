"""The public docs follow the code: a renamed command, plugin or workflow fails here."""

import argparse
import importlib.util
import json
import re
import tomllib
from pathlib import Path
from types import ModuleType

import pytest

ROOT = Path(__file__).resolve().parent.parent
READMES = ("README.md", "README.fr.md")
# The reference, in each language: everything kiln offers, looked up there.
REFERENCES = ("docs/reference.md", "docs/reference.fr.md")
DOCS = (*READMES, *REFERENCES, "CONTRIBUTING.md")
MARKETPLACE = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())


def docs() -> dict[str, str]:
    return {name: (ROOT / name).read_text(encoding="utf-8") for name in DOCS}


def screenshots() -> ModuleType:
    spec = importlib.util.spec_from_file_location("screenshots", ROOT / "scripts/screenshots.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_every_image_is_what_kiln_shows_today() -> None:
    for path, expected in screenshots().images().items():
        assert path.read_text(encoding="utf-8") == expected, (
            f"{path.name} is out of date: uv run python scripts/screenshots.py"
        )


@pytest.mark.parametrize("readme", READMES)
def test_a_readme_shows_only_current_images_and_existing_commands(readme: str) -> None:
    from kiln import cli

    text = (ROOT / readme).read_text(encoding="utf-8")
    images = re.findall(r'(?:src|srcset)="(docs/assets/[^"]+)"', text)
    assert images and all((ROOT / image).is_file() for image in images), images
    drawn = {path.relative_to(ROOT).as_posix() for path in screenshots().images()}
    assert set(images) <= drawn, "an image the screenshot script does not draw"
    commands = next(
        action
        for action in cli.build_parser()._actions
        if isinstance(action, argparse._SubParsersAction)
    ).choices
    cited = set(re.findall(r"`kiln ([a-z][a-z-]+)", text)) | set(
        re.findall(r"^\$ (?:cd \S+ && )?kiln ([a-z][a-z-]+)", text, re.M)
    )
    assert cited <= set(commands), f"{readme} cites kiln {sorted(cited - set(commands))}"
    reference = REFERENCES[READMES.index(readme)]
    assert f"]({reference})" in text, f"{readme} links its reference"


def test_both_readmes_say_the_same_things() -> None:
    english, french = ((ROOT / name).read_text(encoding="utf-8") for name in READMES)

    def outline(text: str) -> list[object]:
        return [
            len(re.findall(r"^## ", text, re.M)),
            len(re.findall(r"^- ", text, re.M)),
            re.findall(r'src="(docs/assets/[^"]+)"', text),
            len(re.findall(r"^\| ", text, re.M)),
        ]

    assert outline(english) == outline(french), "README.fr.md follows README.md"


def test_installed_plugins_exist_and_former_names_are_gone() -> None:
    plugins = {plugin["name"] for plugin in MARKETPLACE["plugins"]}
    former = "|".join(map(re.escape, MARKETPLACE["renames"]))
    for name, text in docs().items():
        assert set(re.findall(r"plugin install ([\w-]+)@kiln", text)) <= plugins, name
        assert not re.findall(rf"`/?({former})(:[\w-]+)?`", text), name


def test_cited_workflows_exist() -> None:
    workflows = {path.name for path in (ROOT / ".github/workflows").glob("*.yml")}
    for name, text in docs().items():
        cited = set(re.findall(r"`([\w-]+\.yml)`", text)) - {"ci.yml", "copier.yml"}
        assert cited <= workflows, (name, sorted(cited - workflows))


# --- The reference describes everything kiln offers, at the release it is, in both languages
# (antoine, 19 October 2026: "the README kept entirely up to date, every time"). A command,
# option, setting, skill, hook, plugin or workflow added without its line fails here.
# Former names kept for old repos: their new names are documented instead.
LEGACY = frozenset({"--sauter", "--sans-pousser", "--garder", "--statut", "--poste"})


def offered() -> dict[str, str]:
    """What kiln offers, by label, with the text each README must contain."""
    from kiln import cli
    from kiln.settings import SETTABLE_KEYS

    parser = cli.build_parser()
    commands = next(
        action for action in parser._actions if isinstance(action, argparse._SubParsersAction)
    )
    items: dict[str, str] = {}
    for name, command in commands.choices.items():
        items[f"command {name}"] = f"`kiln {name}"
        for action in command._actions:
            for option in action.option_strings:
                if option.startswith("--") and option != "--help" and option not in LEGACY:
                    items[f"option {name} {option}"] = option
    items |= {f"setting {key}": f"`{key}`" for key in SETTABLE_KEYS}
    items |= {
        f"plugin {plugin['name']}": f"`{plugin['name']}`" for plugin in MARKETPLACE["plugins"]
    }
    items |= {
        f"skill {path.parent.parent.name}:{path.name}": f"`{path.name}`"
        for path in (ROOT / "plugins").glob("*/skills/*")
        if path.is_dir()
    }
    items |= {
        f"hook {path.name}": path.name
        for path in (ROOT / "plugins/kiln/hooks").glob("*.py")
        if not path.name.startswith("_")
    }
    items |= {
        f"workflow {path.name}": f"`{path.name}`"
        for path in (ROOT / ".github/workflows").glob("*.yml")
        if "workflow_call:" in path.read_text(encoding="utf-8")
    }
    return items


@pytest.mark.parametrize("reference", REFERENCES)
def test_the_reference_describes_everything_kiln_offers(reference: str) -> None:
    text = (ROOT / reference).read_text(encoding="utf-8")

    missing = [label for label, needle in offered().items() if needle not in text]

    assert missing == [], f"{reference} says nothing of: {', '.join(missing)}"


def test_the_docs_quote_the_release_they_describe() -> None:
    version = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

    assert re.search(r"^## v(\S+) — ", changelog, re.M).group(1) == version  # type: ignore[union-attr]
    for name, text in docs().items():
        quoted = set(re.findall(r"antoine-tena/kiln/\S+?@v(\d+\.\d+\.\d+)", text))
        assert quoted <= {version}, f"{name} quotes kiln at {quoted}, the release is {version}"
