"""`kiln dev`: the Procfile.dev, the background (`-d`, status, logs, stop) and its arguments."""

import subprocess
import time
from collections.abc import Iterator
from pathlib import Path

import pytest

from kiln import cli
from kiln.dev import background, run_dev
from kiln.dev.processes import dev_processes, procfile_commands
from kiln.shell import KilnError
from kiln.stack import Command


@pytest.fixture
def project(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Path]:
    """A git repo without stack nor compose: only its Procfile.dev runs, ready at once."""
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / "backend").mkdir()
    monkeypatch.setattr(background, "SETTLE_SECONDS", 0.5)
    yield tmp_path
    background.stop(tmp_path)


def test_a_procfile_line_runs_in_its_folder_and_replaces_a_server_of_the_same_name(
    tmp_path: Path,
) -> None:
    (tmp_path / "backend").mkdir()
    (tmp_path / "backend/manage.py").touch()
    (tmp_path / "backend/Procfile.dev").write_text(
        "# Celery reloaded at each change\n"
        "worker: uv run watchfiles 'celery -A core worker'\n"
        "django: uv run python manage.py runserver 8001\n"
        "not a process\n",
        encoding="utf-8",
    )

    assert procfile_commands(tmp_path, "backend")[0] == Command(
        "worker", "backend", ("sh", "-c", "uv run watchfiles 'celery -A core worker'")
    )
    assert [(command.label, command.argv[-1]) for command in dev_processes(tmp_path)] == [
        ("django", "uv run python manage.py runserver 8001"),
        ("worker", "uv run watchfiles 'celery -A core worker'"),
    ]


def test_detached_processes_are_read_then_stopped(
    project: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (project / "backend/.env").write_text("GREETING=hello\n", encoding="utf-8")
    (project / "backend/Procfile.dev").write_text(
        'worker: echo "$GREETING from $(basename $PWD)"; sleep 60\n', encoding="utf-8"
    )

    run_dev(project, detached=True)
    run_dev(project, "logs")
    pid = background.records(project)["worker"]["pid"]
    with pytest.raises(KilnError, match="already running"):
        run_dev(project)
    run_dev(project, "stop")

    output = capsys.readouterr().out
    assert "running" in output
    assert "hello from backend" in output
    assert "stopped: worker" in output
    assert not _alive_after_stop(pid)
    assert background.running(project) == []


def test_a_process_that_dies_at_start_stops_the_others_and_shows_its_log(project: Path) -> None:
    (project / "backend/Procfile.dev").write_text(
        "worker: sleep 60\ncrash: echo database refused; exit 3\n", encoding="utf-8"
    )

    with pytest.raises(KilnError, match="crash stopped at start:\ndatabase refused"):
        run_dev(project, detached=True)

    assert background.running(project) == []


@pytest.mark.parametrize(
    "arguments",
    [
        ["dev", "status", "django"],
        ["dev", "-f"],
        ["dev", "stop", "-d"],
        ["dev", "logs", "--containers"],
    ],
)
def test_options_go_with_their_action(arguments: list[str]) -> None:
    with pytest.raises(KilnError):
        cli._check_dev_arguments(cli.build_parser().parse_args(arguments))


def _alive_after_stop(pid: int) -> bool:
    deadline = time.monotonic() + 5
    while background.is_alive(pid) and time.monotonic() < deadline:
        time.sleep(0.1)
    return background.is_alive(pid)
