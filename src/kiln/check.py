"""`kiln check`: runs the stack's checks and the charter, without stopping at the first failure."""

from pathlib import Path

from kiln import ui
from kiln.charter import config as charter_config
from kiln.dev.backing import start_backing_services
from kiln.install import ensure_env_file, moved_from, sync_command
from kiln.shell import KilnError, run, run_status, step
from kiln.stack import BACKEND_DIR, Command, Stack, load_stack


def run_checks(root: Path) -> list[str]:
    """Runs each check and returns the labels of those that failed."""
    failed_checks: list[str] = []
    stack = load_stack(root)
    # A worktree has no backend/.env (ignored by git): without it, Django does not start.
    if stack.has_api and not (root / BACKEND_DIR / ".env").exists():
        ensure_env_file(root / BACKEND_DIR)
    # A repo moved since its venv was created: the tools' scripts call the old folder's Python.
    for directory in stack.python_dirs:
        if moved_from(root / directory / ".venv") is not None:
            step(f"{directory}: venv moved, packages reinstalled")
            run(sync_command(root / directory / ".venv"), root / directory)
    for command in _check_commands(root, stack):
        step(f"Check: {command.label}")
        if run_status(list(command.argv), root / command.directory) != 0:
            failed_checks.append(command.label)
    return failed_checks


def _check_commands(root: Path, stack: Stack) -> list[Command]:
    """The stack's checks; mypy as the CI types, through `charter types`, when the charter
    declares its packages and environment (`[types]`): a bare `mypy .` knows neither."""
    types = charter_config.load(root).get("types")
    typed_directory = types.get("directory", BACKEND_DIR) if isinstance(types, dict) else None
    return [
        Command(command.label, ".", ("charter", "types"))
        if command.label == f"{typed_directory} mypy"
        else command
        for command in stack.check_commands()
    ]


def check_project(root: Path) -> None:
    """Runs each check, then fails listing those that failed; the tests get their databases."""
    start_backing_services(root)
    failed_checks = run_checks(root)
    if failed_checks:
        raise KilnError(f"failed checks: {', '.join(failed_checks)}")
    ui.success("All checks pass.")
