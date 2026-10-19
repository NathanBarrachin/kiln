# What's new in kiln

One entry per release, the most recent first: `## vX.Y.Z — date`, then one line per visible
change (`- …`), breaking changes first (`**Breaking**`). `kiln update` shows the entries of the
releases a project crosses; `kiln version cut` drafts the entry of the release it cuts, on the
`release/vX.Y.Z` branch, rewritten before its first candidate. Names are those of their release:
entries before v0.4.0 quote kiln's former French names.

## v0.3.4 — 2026-10-16
- The template is never newer than the installed tool: `kiln update` applies the installed kiln release (conversions from one release to the next live in the tool), refuses to take a repo back to a release older than its own, and says when a newer release is out.
- `kiln new` without `gh`, or outside a terminal without a login, creates the project locally, and `kiln publish` creates the GitHub repository afterwards. The default owner comes from the machine's settings or from the account logged in to gh; a project without a team has neither CODEOWNERS nor a "Team" section.
- The generated CI looks for secrets through the `secrets.yml` workflow (gitleaks pinned and verified, without the license gitleaks-action requires for an organization); `kiln ci` replays it with the machine's gitleaks.
- `kiln` answers in 0.12 s instead of 0.5 s (commands imported on demand); the generated README installs kiln from PyPI.
- Reliability: end-to-end tests (each framework generated, installed and checked; a project of the previous releases updated without conflict), run on every release branch; kiln's CI on macOS too.

## v0.3.3 — 2026-10-16
- `kiln completion bash`: completion script drawn from kiln's commands and options, enabled by `eval "$(kiln completion bash)"` in `~/.bashrc` (#41, thanks @HarshRajSinghania).
- `good-first-issues` skill: keeps a few beginner issues open on GitHub, drawn from the backlog and reserved for outside contributors.
- Fixes: `kiln update` no longer stops on a conflict in `ci.yml` after a release is promoted (only the `@<tag>` of kiln's workflows differed); `base:worktree` no longer trips on a repo without a `.env` file; updating a kiln installed from a folder also removes the former `kiln` tool.

## v0.3.2 — 2026-10-16
- `kiln adopt` makes an existing repo follow kiln, without regenerating it; the `adoption` skill sorts out with the user what the charter finds there, and the session start offers it in a repo of one's own that does not follow kiln yet.
- Charter waivers in `kiln-waivers.toml`, with a reason and a deadline that grows at each renewal: `kiln waive` adds, renews or lists them, `kiln update` spares frozen files and says what it would have changed, `kiln status` counts each repo's.
- `relecture` skill: a branch's commits and diff reviewed and tidied before the merge (`fusion` runs it), the whole repo before a release (`version` runs it); the `garde-branche` hook refuses a commit message signed by Claude.
- kiln's questions at session start follow a common policy: each "no" spaces out the next one, each "yes" brings it closer.
- `kiln --version` (#39, thanks @SakarPaisen, first outside contribution).
- Fixes: `kiln update --all` says "GitHub unreachable" in one line instead of a Python traceback, and a failed run no longer blocks the next one with a worktree left empty.

## v0.3.1 — 2026-10-16
- **Breaking**: work tracking moves to English, `docs/a-faire/` becomes `docs/backlog/` (tickets `T-NN`, skill `base:backlog` instead of `base:a-faire`); `kiln update` moves the old folder.
- Numbering like Claude Code: in 0.x, each release bumps the patch, breaking ones included; the minor only moves for a milestone (`kiln version --minor`). A release is promoted as soon as the next one is ready as a candidate, without a waiting period.
- kiln installs from PyPI: package `kiln-cli` (the command stays `kiln`), published at the tag of each promoted release; `kiln doctor` and `maj-kiln` offer the update that way.
- New skills: `report-to-kiln` (a defect of kiln met in a repo becomes an issue or a PR, posted only with the user's consent), `token` (a service's token in `.<service>/`, pasted without showing), `contribution` (handling an outside contributor's PR).
- The generated CI runs gitleaks and can be called by other workflows (`workflow_call`).
- Status line: four styles in kiln's colours, in English (`kiln set statusline=…`), session name, RAM and busy cores.
- Fixes: `kiln doctor` offers the update at the release's tag, `kiln status` template column wide enough.

## v0.3.0 — 2026-10-15
- First published release. Semver in 0.x: a release first comes out as a candidate (`-rc.N`) for machines on the `interne` channel, then is promoted when the next one is ready and it has held for three days; `kiln version` says where the candidates stand.
- Projects quote kiln's workflows at the exact tag they start from; `kiln update` moves it forward and shows what is new in each release crossed. The session-start hook offers the tool, then the repo, at each release.
- `kiln status` says which release each repo starts from (`f611f82 → v0.3.0`); `kiln set canal=interne` (machine setting) follows the candidates.
- New interface: laughing kiln as a banner, sectioned welcome screen, spinner and duration for each external command, boxed recap of the steps; no colour outside a terminal, `KILN_VERBOSE=1` for the full output.
- `kiln doctor`: diagnosis of the machine and the repo, each problem with the command that fixes it.
- `kiln dev`: servers' output interleaved, prefixed by service in colour.
- `kiln update --all` merges each repo whose checks pass directly, without a PR.
- Java backend (Maven), `maj-kiln` skill, `.claude/kiln` link to the plugin, machine settings through `kiln set`.
