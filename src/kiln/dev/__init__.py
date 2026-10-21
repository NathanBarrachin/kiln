"""`kiln dev`: the project running on the machine, in the foreground or in the background.

What is edited runs on the machine, reloaded at each change: the stack's servers and the
processes of the `Procfile.dev`s (`processes`). What is never edited runs in podman: the
databases of the compose file (`backing`). In the foreground, Ctrl+C stops the processes and
keeps the databases (`foreground`); `-d` leaves everything in the background, read with
`kiln dev status` and `kiln dev logs [service] [-f]`, stopped with `kiln dev stop`
(`background`). `--containers` runs the whole stack in podman instead (`containers`).
"""

from pathlib import Path

from kiln import ui
from kiln.dev import background, containers
from kiln.dev.backing import start_backing_services, stop_backing_services
from kiln.dev.foreground import run_foreground, service_prefix
from kiln.dev.processes import dev_processes, read_env_file
from kiln.shell import KilnError, step

ACTIONS = ("status", "logs", "stop")

__all__ = ["ACTIONS", "read_env_file", "run_dev", "service_prefix"]


def run_dev(
    root: Path,
    action: str | None = None,
    *,
    in_containers: bool = False,
    detached: bool = False,
    follow: bool = False,
    service: str | None = None,
) -> None:
    if action is None:
        _start(root, in_containers=in_containers, detached=detached)
    elif action == "status":
        _status(root)
    elif action == "logs":
        _logs(root, service, follow=follow)
    elif action == "stop":
        _stop(root)


def _start(root: Path, *, in_containers: bool, detached: bool) -> None:
    if background.running(root) or containers.is_detached(root):
        raise KilnError("already running in the background: kiln dev status, kiln dev stop")
    if in_containers:
        containers.up(root, detached=detached)
        return
    commands = dev_processes(root)
    if not commands:
        raise KilnError("nothing to run: a command-line tool runs with uv run")
    start_backing_services(root)
    step(" · ".join(f"{command.label} ({command.directory}/)" for command in commands))
    if not detached:
        run_foreground(root, commands)
        return
    background.start(root, commands)
    background.show_status(root)
    ui.note("kiln dev logs [service] [-f] · kiln dev status · kiln dev stop")


def _status(root: Path) -> None:
    if containers.is_detached(root):
        containers.show_status(root)
    else:
        background.show_status(root)


def _logs(root: Path, service: str | None, *, follow: bool) -> None:
    if containers.is_detached(root):
        containers.show_logs(root, service, follow=follow)
    else:
        background.show_logs(root, service, follow=follow)


def _stop(root: Path) -> None:
    if containers.is_detached(root):
        containers.stop(root)
        return
    stopped = background.stop(root)
    stop_backing_services(root)
    ui.success(f"stopped: {', '.join(stopped)}" if stopped else "nothing was running")
