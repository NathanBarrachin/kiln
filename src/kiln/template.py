"""Access to the Copier template: default source and tracked revision."""

import os

from kiln.versions import tool_release_tag

DEFAULT_TEMPLATE_SOURCE = "https://github.com/antoine-tena/kiln.git"
TEMPLATE_SOURCE_VARIABLE = "KILN_TEMPLATE"
# Revision of a local or explicit template (kiln development): its last commit.
LOCAL_TEMPLATE_REVISION = "HEAD"


def template_source(explicit_source: str | None) -> str:
    """Template source: option, then environment variable, then the GitHub repo."""
    if explicit_source:
        return explicit_source
    return os.environ.get(TEMPLATE_SOURCE_VARIABLE, DEFAULT_TEMPLATE_SOURCE)


def template_revision(source: str) -> str | None:
    """The published template is taken at the installed tool's version, never newer: the
    conversions from one version to the next live in the tool's code. If the tool cannot place
    itself, the latest version (None: Copier picks the most recent tag). A local or explicit
    template is taken at its last commit."""
    if source != DEFAULT_TEMPLATE_SOURCE:
        return LOCAL_TEMPLATE_REVISION
    return tool_release_tag()
