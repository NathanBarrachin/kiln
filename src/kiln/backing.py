"""The databases a project's backend needs in development, started by `kiln dev`.

They are the `db`, `postgres` and `redis` services of the project's compose file. A container
already created (a stopped `annski-db` after a reboot) is restarted as it is, its data kept;
otherwise `podman-compose up -d` creates it. Without podman, nothing is started.
"""

import re
import shutil
import subprocess
from pathlib import Path

from kiln.shell import run, step
from kiln.stack import PODMAN_MARKERS

COMPOSE_FILES = ("compose.yaml", *PODMAN_MARKERS)
BACKING_SERVICES = ("db", "postgres", "redis")
_SERVICE_LINE = re.compile(r"^  ([\w.-]+):\s*$")
_CONTAINER_NAME_LINE = re.compile(r"^    container_name:\s*[\"']?([\w.-]+)")


def compose_file(root: Path) -> Path | None:
    return next((root / name for name in COMPOSE_FILES if (root / name).is_file()), None)


def backing_services(compose: Path) -> dict[str, str | None]:
    """Backing services of a compose file, each with its `container_name` (None if unnamed)."""
    services: dict[str, str | None] = {}
    in_services = False
    current = ""
    for line in compose.read_text(encoding="utf-8").splitlines():
        if line and not line[0].isspace():
            in_services = line.rstrip() == "services:"
            continue
        if not in_services:
            continue
        if service_match := _SERVICE_LINE.match(line):
            current = service_match.group(1)
            if current in BACKING_SERVICES:
                services[current] = None
        elif (name_match := _CONTAINER_NAME_LINE.match(line)) and current in services:
            services[current] = name_match.group(1)
    return services


def start_backing_services(root: Path) -> None:
    compose = compose_file(root)
    if compose is None or shutil.which("podman") is None:
        return
    services = backing_services(compose)
    if not services:
        return
    step(f"databases ({', '.join(services)})")
    to_create = []
    for service, container in services.items():
        if container and _exists(container):
            run(["podman", "start", container], root)
        else:
            to_create.append(service)
    if to_create:
        run(["podman-compose", "-f", str(compose), "up", "-d", *to_create], root)


def _exists(container: str) -> bool:
    check = subprocess.run(["podman", "container", "exists", container], check=False)
    return check.returncode == 0
