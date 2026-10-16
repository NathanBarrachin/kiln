# Backlog

Everything left to do on kiln, in a single list ordered by priority. Started on
**2026-10-15**. What is done is in the "✅ Done" section at the bottom; what was turned
down is in [rejected.md](rejected.md). **Nothing else is open.**

North star: **kiln v0.4.0, in English, launched publicly: pleasant for a Claude Code newcomer,
reliable for a team with huge repos** (free mandate given by antoine, 16 October 2026).

---

## How to use (humans and agents)

**A ticket** = a `### T-NN · Title` heading, then five fixed lines, then the details:

    ### T-NN · Short title that says what to achieve
    - **Type**: task
    - **Status**: todo
    - **Opened**: YYYY-MM-DD
    - **Effort**: S · **Owner**: … · **Due**: —
    - **Origin**: where it comes from

    Why, what to do (as a `- [ ]` checklist when there are several steps), where to look.

- **ID** `T-NN`: stable, never reused, quoted as is in commits and branches (tickets opened
  before 16 October 2026 were `AF-NN`, same number). **Next free: T-44.**
- **Type**, one of: `bug` (something is broken); `improvement` (it works, it could work
  better); `idea` (nothing exists yet, to be explored); `task` (work that is neither: a release,
  a decision, a check).
- **Status**, one of: `todo`; `in progress — branch <name>, since YYYY-MM-DD`;
  `blocked — waiting for <who or what>`; `to verify — <where>`.
- **Priority** = the section the ticket lives in; changing it means moving the ticket.
  🔴 critical (now), 🟠 important (before the north star), 🟡 normal, ⚪ background
  (long-running work, debt, ideas still to be explored).
- **Effort**: XS (under an hour), S (half a day), M (one or two days), L (more).
- **Closing a ticket**: remove it from its section and add a line at the top of the "✅ Done"
  log: `- **YYYY-MM-DD** · T-NN · Title — what was done (branch) · opened YYYY-MM-DD`.
- **Locations quoted are hints, not addresses.**
- Overview: `grep -E '^(## |### T-|- \*\*Status)' docs/backlog/backlog.md`.
- **Good first issues**: keep 3 open on GitHub, reserved for outside contributors (skill
  `base:good-first-issues`); their tickets have **Owner**: `contributor — #NN`.

---

## 🔴 Critical

### T-14 · Promote v0.3.1, the first release on PyPI
- **Type**: task
- **Status**: blocked — waiting for antoine (delete the old token)
- **Opened**: 2026-10-16
- **Effort**: XS · **Owner**: antoine, then Claude · **Due**: —
- **Origin**: promotion of v0.3.0, 16 October 2026

`v0.3.1` is promoted and `kiln-cli 0.3.1` is on PyPI (16 October 2026); `v0.3.2-rc.2` is the
candidate followed by annway, sweep and vision.
- [x] Cut `v0.3.2-rc.1`, then `-rc.2` (tests independent of the machine's git config); the
  `CHANGELOG.md` entry credits #39 (@SakarPaisen). `kiln update --all` done.
- [x] Promote `v0.3.1`, `pypi` run green, `uvx --from kiln-cli==0.3.1 kiln` works on an empty
  uv cache.
- [x] README (English and French): `uv tool install kiln-cli` as the main install.
- [x] Token scoped to `kiln-cli` in `.pypi/token`, `PYPI_TOKEN` secret updated (16 October
  2026); first used by the promotion of `v0.3.2` (16 October 2026): `kiln-cli 0.3.2` is on
  PyPI. `v0.3.3-rc.2` is now the candidate followed by annway, sweep and vision.
- [ ] antoine deletes the old account-wide token on https://pypi.org/manage/account/token/

### T-22 · Release v0.3.4 (first-run fixes) and promote v0.3.3
- **Type**: task
- **Status**: in progress — branch fix/first-run, since 2026-10-16
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: free mandate, 16 October 2026

A newcomer could not get through `kiln new`: owner `antoine-tena` offered by default (taken
silently outside a terminal), immediate failure without `gh`, generated README installing kiln
from git. v0.3.4 fixes the first run; its candidate makes v0.3.3 ready for promotion.
- [x] Template never newer than the installed tool (migrations live in the tool).
- [x] Owner from the machine settings or the gh account; GitHub optional; `kiln publish`.
- [x] `secrets.yml`: gitleaks without the organisation licence of gitleaks-action.
- [x] CLI imports on demand (0.5 s → 0.12 s); T-09.
- [x] End-to-end tests (`pytest -m e2e`): every framework generated, installed, checked; a
  project of the previous releases updated without conflict. CI: release branches, nightly.
- [ ] Cut `v0.3.4-rc.1`, promote `v0.3.3` (PyPI, GitHub Release), `kiln update --all`.

### T-23 · kiln in English (v0.4.0)
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: T-06 and T-13 merged here; plan accepted by antoine, 16 October 2026

Main obstacle to adoption outside France and to the Claude Code directories. Decisions
(antoine, 16 October 2026): the command and the plugins in English only; generated
instructions in English for every project, the project's language only rules what is human
(conversation, comments, commits, docs, UI texts); every rename at once, converted by
`kiln update`; v0.4.0 is the milestone.
- [x] Command: messages, help, `kiln set` keys; English command and option names
  (`contrat` → `contract`, `--poste` → `--global`, `ci --sauter` → `--skip`…), old ones
  accepted and flagged until the next minor.
- [ ] `copier.yml`: English questions and keys (`envergure` → `size`, `proprietaire` →
  `owner`…), values (`aucun` → `none`…); `language` asked at `kiln new` (en, fr), per-use
  overrides by `kiln set` (comments, commits, docs, tickets, UI).
- [ ] Rule engine `charte` → `charter` (`charter.toml`, English sections, keys and rule IDs);
  `charte`, `charte.toml` and the old IDs still read, so annski (adopted, no update) keeps
  working.
- [ ] Workflows: English names and inputs; the old files stay as relays for `@develop` users.
- [ ] `kiln update` converts a v0.3 project: answers, `charte.toml`, waivers, rule IDs quoted
  in the code, project additions to the old `CLAUDE.md` files carried over.
- [ ] Changelog translated; README, CONTRIBUTING, kiln's own `CLAUDE.md` in English.

## 🟠 Important

### T-32 · From idea to live app: every project type deployable from `kiln new`
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: positioning, 16 October 2026 (antoine: "without knowing anything, a modern repo
  from A to Z, all the way to production"); issue #43

kiln's strongest promise, the one a launch can sell, is "from idea to live app with Claude
Code, no experience needed". Today it stops at the repo: deployment is not among the three
questions, and only exists for Django (a VPS, SSH, domain and DNS set up by hand: not for a
newcomer) and Nuxt (Vercel). A content site, Next, FastAPI, Streamlit: nothing, although they
are the easiest to put online. Whoever tries the promise on launch day must get a URL.
- [ ] A fourth question, "Where should it run?", whose choices follow the stack and whose
  default is the zero-knowledge host: Vercel for `site`/`next`/`nuxt`/`astro`, Render for
  Python backends and dashboards (Django, FastAPI, Streamlit, Dash, with its PostgreSQL), PyPI
  for `cli`, none for `analysis`; the VPS stays the expert choice. Decided by Claude
  (16 October 2026, antoine: "when there is a choice, decide"): Render has a free tier without
  a card and deploys from GitHub, so a newcomer gets to the end; Fly.io asks for a card,
  Railway only has a paid trial.
- [ ] `kiln deploy`: one login when missing (with its direct link), project linked, deployed
  from a pushed commit whose CI is green, URL printed; secrets set without being shown.
- [ ] The URL in the generated README and in the status line ("prod ✓").
- [ ] `kiln new --deploy`: generation, GitHub repo and first deployment in one go.
- [ ] End-to-end test on a throwaway account per host; close #43.

### T-33 · One promise everywhere: tagline, About, PyPI, social preview
- **Type**: task
- **Status**: in progress — branch docs/standout-plan, since 2026-10-16
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude, antoine for the social preview upload · **Due**: —
- **Origin**: positioning, 16 October 2026

"Make Claude Code build production-grade repos" says what dozens of Claude Code starter kits
already say. The promise is the outcome for someone who knows nothing: a project set up the
way a senior engineer would, then (with T-32) online. Same words in the README hero, the GitHub
About (shown in search results and link previews), the PyPI summary and the launch titles.
- [ ] Today's honest version everywhere: "Start every project like a senior engineer would,
  even if you're not one."
- [ ] Once T-32 ships: "From idea to live app with Claude Code. No experience needed."
- [ ] Right under it, the two lines that answer "kiln forces too much" before anyone says it:
  "Strong defaults, chosen for you — every one of them yours to change." and "Starts light.
  Grows with your project. Never lets it rot." (T-36, T-39, T-41).
- [ ] Social preview 1280×640 (kiln pixel art, the promise, `uvx kiln-cli new`), uploaded by
  antoine (no API): https://github.com/antoine-tena/kiln/settings (Social preview).
- [ ] GitHub About homepage = the T-35 site; PyPI version and downloads badges.

### T-34 · A second door: kiln for the repo you already have
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: positioning, 16 October 2026

The most starred Claude Code projects (claude-mem, 100,000+ ★) install in one command into the
repo people already have. `kiln new` only speaks to whoever starts a project today. `kiln adopt`
and the plugins are the door for everyone else, but the README hides them.
- [ ] README: "Already have a repo?" next to the quick start, one command, what you get in
  30 seconds (guardrails checked after each edit, worktree/merge/release skills, backlog).
- [ ] `kiln adopt` shows, at the end, the three things it found and what it set up.
- [ ] The plugins alone (`claude plugin marketplace add antoine-tena/kiln`) are useful outside
  kiln repos, and the README says which.
- [ ] `kiln adopt` à la carte: the charter alone by default; backlog, branch flow, status line
  each one `kiln set` away, never imposed on an existing repo.

### T-35 · Living proof: a site and an example app made by kiln, online
- **Type**: task
- **Status**: blocked — waiting for T-32
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: positioning, 16 October 2026

A real example convinces more than any badge.
- [ ] kiln's own site generated by `kiln new` (content site), deployed by `kiln deploy`, set as
  the GitHub homepage: "this site took three questions".
- [ ] A public example app (`app` type, the first prompt of `kiln new` done by Claude Code),
  live, CI green, linked from the README.
- [ ] The README says that a non-profit's production site runs on kiln (annski), with its link.

### T-36 · `kiln new` recommends the stack, the user decides
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: positioning, 16 October 2026 (antoine: "what if the user wants to choose their
  frameworks?")

The three questions never show the stack: what you build picks it silently (an app gets
Django + Nuxt). Choosing is possible (`--backend`, `--frontend`, `--all-questions`, `kiln set`)
only for whoever already knows it is. A recommendation one keystroke away from a choice serves
both the newcomer and the expert, the way `create-vite` does.
- [ ] After "What are you building?": "Recommended stack: Django + Nuxt", Enter accepts, a
  menu lists the other backends and frontends valid for that type (validator of `copier.yml`
  respected), each with its one-line pitch.
- [ ] Machine-wide preferences for the expert: `kiln set --global backend=fastapi
  frontend=next` become the recommendation on this machine (`machine.py`).
- [ ] Outside a terminal and with `--backend`/`--frontend`: no question, as today.

### T-37 · Docker or podman: the engine the machine has
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: positioning, 16 October 2026 ("kiln forces too much")

"docker forbidden, podman required" is the choice most likely to make a newcomer close the tab
(almost everyone has Docker Desktop) and the first comment on Hacker News. Decided by Claude
(16 October 2026): the generated files work with both engines, and kiln uses the one the machine
has; podman when both or neither are there (rootless, daemonless: still the better default).
- [ ] `containers=podman|docker` setting, chosen at `kiln new` by detection, changeable with
  `kiln set containers=docker`; `compose.yaml` and the Containerfiles stay engine-neutral.
- [ ] `kiln dev --containers`, `kiln ci`, the `infra.yml` and `services` actions and the
  deployment scripts run the chosen engine.
- [ ] The charter rule no longer forbids `docker`: it forbids the engine the repo did not
  choose (no mix); `pip` stays forbidden (uv is the norm now, nobody will miss it).
- [ ] `kiln doctor` says which engine is used and how to change it.

### T-39 · Start light, grow with the repo: no size question, promotion suggested
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: positioning, 16 October 2026 (antoine: "the smallest level at creation, and
  rules that grow with the repo?"); builds on T-24

Nobody knows at creation how big a project will get. Two kinds of rules, decided by Claude
(16 October 2026): **foundations** from day one whatever the size (formatting, lint, strict
typing, tests that run, CI, no secret in the code, protected branches: cheap now, weeks to
retrofit, and Claude Code pays for them, not the human); **ceremony** that grows with the repo
(coverage floor, reviewers, release candidates, OpenTelemetry, SLO, CSP, mutation tests,
SBOM). The charter's ratchets make moving up painless: new code meets the rule, existing debt
can only shrink.
- [ ] `kiln new` asks two questions (what you build, language); every project starts at
  `spark` = the foundations, nothing more; `--size` stays for whoever knows.
- [ ] Coverage floor by size (none at `spark`, then rising); strict typing stays everywhere.
- [ ] Promotion suggested, never automatic (real users in production cannot be read from the
  code): at `kiln update` and at session start, from signals (lines of code, contributors in
  the last 90 days, a deployment, several services): "This repo looks like a flame now: 3
  contributors, deployed. It would add: coverage floor 80 %, 1 required reviewer. `kiln set
  size=flame`?" Paced like the other questions (`reminders.py`), "Never for this repo" kept.
- [ ] Moving up applies the new rules as ratchets on existing code, never a wall of errors.

### T-40 · kiln tells you what is possible, once, at the right moment
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: antoine, 16 October 2026 ("sometimes kiln should say that this or that is
  possible")

Everything an expert can set is there, but a newcomer only finds it by reading the docs.
- [ ] Contextual tips after a command, one at a time, each shown once per machine, paced (no
  tip after a failure, at most one a day): after `kiln new` "Changed your mind on the frontend?
  `kiln set frontend=next`"; after a charter failure "Disagree with this rule? `kiln waive
  RULE`"; on a second repo "Update all your repos at once: `kiln update --all`"…
- [ ] The same tips offered to Claude at session start (hook), so it can mention them when
  they fit what the user is doing.
- [ ] `kiln set tips=off` (machine), and a test that every tip names a command that exists.

### T-41 · Beginner with nothing to set, expert with everything settable
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: antoine, 16 October 2026 ("someone who knows nothing can use it, someone who
  knows everything can set everything, easily")

The rule for every kiln feature: a default that works without a question, changeable in one
command, findable without the docs.
- [ ] `kiln set` with no argument lists every setting of the repo grouped by topic, current
  value, choices, one line each; `kiln set KEY` explains one; the same with `--global` for the
  machine.
- [ ] Audit: each default of `copier.yml`, of the charter and of the plugins reachable by
  `kiln set`, `kiln waive` or a machine setting; what is not becomes a ticket.
- [ ] `kiln new --all-questions` presented as "expert mode" in the help and the README.
- [ ] Generated README: a short "Your choices" section listing the stack and how to change it.
- [ ] Every refusal (hook, charter, branch guard, pre-commit) says why in one line and the one
  command that lifts it (`kiln waive …`, `kiln set …`), like ruff or prettier: opinionated,
  never a dead end.
- [ ] Every session question can be switched off for good on the machine:
  `kiln set --global reminders=off` (updates, adoption, promotion of T-39, tips of T-40).

### T-42 · The git flow grows with the size: branch → main first, develop and candidates later
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: "kiln forces too much" review, 16 October 2026

`develop`, release branches, `-rc` candidates and a worktree per branch are antoine's way of
working; a newcomer alone on a weekend project expects a branch merged into `main`. Decided by
Claude (16 October 2026), with T-39: `spark` and `ember` use the GitHub flow (work branch →
`main`, never a direct commit on `main`: the one guard that stays); `flame` and `blaze` get
`develop`, release branches and candidates. Worktrees stay how Claude works (parallel
sessions), never something the human has to learn.
- [ ] Template, skills (`merge`, `release`), branch guard and status line read the flow from
  the size; moving up to `flame` creates `develop` and says what changes.
- [ ] mypy stays before each push (CI minutes are limited, see T-05; with its cache it is fast)
  and its message says how to skip once (`--no-verify` is not offered: `SKIP=mypy`).

### T-03 · Launch kiln publicly, then list it in the Claude Code directories
- **Type**: task
- **Status**: blocked — waiting for T-23 to T-25, T-27, T-30, T-32 to T-37 and T-39 to T-42
- **Opened**: 2026-10-15
- **Effort**: S · **Owner**: antoine · **Due**: —
- **Origin**: GitHub showcase, 15 October 2026; "Claude Code's workshop" positioning,
  16 October 2026

antoine's goal: lots of stars. Directories take projects that already have users: the launch
comes first. Hacker News and Reddit: posted by antoine (no API for HN, Reddit vets new apps),
Claude drafts the texts. Elsewhere, Claude posts directly on antoine's accounts, with no review
(antoine's call, 16 October 2026), saying the text is written with Claude where the platform
asks, then gives the links.
- [x] Accounts with an API key, ready (16 October 2026): dev.to (`.devto/`, user
  `antoine-tena`) and Bluesky (`.bluesky/`, `antoine-tena.bsky.social`, app password).
- [ ] On launch day: article on dev.to, post on Bluesky (Mastodon dropped, antoine's call,
  16 October 2026).
- [ ] A demo of `kiln new` at the top of the README (T-30).
- [ ] Launch only once v0.4.0 is promoted on PyPI (English CLI) and T-32 to T-35 are done:
  stars come in a burst, and the launch happens once.
- [ ] Show HN (https://news.ycombinator.com/submit), suggested title "Show HN: Kiln – from
  idea to live app with Claude Code, in three questions"; the same day, dev.to, Bluesky,
  Reddit.
- [ ] r/ClaudeAI (https://www.reddit.com/r/ClaudeAI/submit) and r/ClaudeCode
  (https://www.reddit.com/r/ClaudeCode/submit).
- [ ] awesome-claude-code (55,000 ★): not before **29 October 2026** (repo at least 14 days
  old, or 100 ★), one recommendation at a time, **through the issue form only** (no PR):
  https://github.com/hesreallyhim/awesome-claude-code/issues/new/choose
- [ ] Anthropic's official directory (claude-plugins-official, loaded by default in Claude
  Code): https://clau.de/plugin-directory-submission — after T-06, French plugins are
  unlikely to get in.

### T-24 · Generated instructions in `.claude/rules/kiln/`, by path and by size
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: free mandate, 16 October 2026

A `spark` script got the same ~400-line charter as a `blaze` service, loaded in every session
(OpenTelemetry, SLO, CSP, feature flags…); the size only chose podman. Claude Code now loads
`.claude/rules/*.md` at start, or only when a matching file is touched (`paths:` front matter),
and advises CLAUDE.md files under 200 lines.
- [ ] kiln-owned rules in `.claude/rules/kiln/` (regenerated by `kiln update`, never edited:
  deviations through `kiln waive`), one file per topic, scoped by path (`backend/**`…).
- [ ] The size chooses the rules: `spark` the essentials, `blaze` everything.
- [ ] The root `CLAUDE.md` belongs to the project (generated once): what Claude cannot guess.
- [ ] The size also tunes CI jobs and GitHub protections.

### T-25 · Plugin `kiln` with English skills, released with kiln
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: free mandate, 16 October 2026

Public users of the catalogue got `develop` live, and skills are called `/base:fusion`.
- [ ] `base` → `kiln` (`/kiln:worktree`, `/kiln:merge`, `/kiln:release`, `/kiln:cleanup`…),
  `pile-django` → `django`, `pile-nuxt` → `nuxt`, `vps-podman` → `vps`; `renames` map in
  `marketplace.json` so Claude Code migrates existing installs.
- [ ] Plugin versions = kiln version, bumped by the release; generated repos pin the
  catalogue to `main` (`ref`), the released state.
- [ ] Hooks and skills in English; git config keys in English, old ones still read.

### T-30 · README, English reference in `docs/`, demo of `kiln new`
- **Type**: task
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: T-03 prerequisites; issues #37 and #38

README rewritten around a 60-second start and an animated demo; full reference in `docs/`
(getting started, commands, charter, plugins, workflows, versions) instead of `README.fr.md`.
- [ ] First screen: the T-33 promise, the demo, one install line, the two doors (T-34), proof
  (T-35); nothing else. The intro paragraph ("stale on day ninety") right after.
- [ ] Demo recorded with vhs (a `.tape` file in `docs/assets/`, re-recorded at each release):
  `kiln new` → three questions → `claude` and its first prompt → green CI → live URL (T-32).
  Issue #38 is too central for a good first issue: done here, another one opened instead.
- [ ] A "kiln vs Claude Code alone vs starter kits vs Copier" table, outcome by outcome.
- [ ] "Every default is yours to change": a table of what kiln chooses (stack, uv, pnpm,
  containers, strict typing, coverage, branches…), why, and the one command that changes it
  (T-41).
- [ ] Commands, plugins, workflows and versions move to `docs/`; no outdated names (`base`,
  `pile-django`, `tableau`).

### T-12 · Homebrew formula in an `antoine-tena/homebrew-kiln` tap
- **Type**: improvement
- **Status**: blocked — waiting for demand (an issue asking for it) or homebrew-core notability
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: distribution, 16 October 2026

`brew install antoine-tena/kiln/kiln` for macOS and Linux, formula updated on each
promotion. Not now (antoine, 16 October 2026): kiln needs uv anyway, so
`uv tool install kiln-cli` covers its users, and a formula lists ~30 dependencies to keep up
to date. The tap https://github.com/antoine-tena/homebrew-kiln is created to keep the name
(README only, issues off). The official homebrew-core requires an already known project.

### T-04 · Decide whether annski quotes kiln's workflows at a tag
- **Type**: task
- **Status**: todo
- **Opened**: 2026-10-15
- **Effort**: XS · **Owner**: antoine · **Due**: —
- **Origin**: move to semver, 15 October 2026

annski is adopted (no template) and quotes the workflows at `@develop`: it gets everything that
lands on `develop`, before any candidate. Pinning it to a tag (`@v0.3.0`) would protect it, at
the cost of a manual update on each release. The user's condition: never break annski.

## 🟡 Normal

### T-43 · A skill that helps write a fine README, like kiln's own
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: antoine, 16 October 2026

kiln's README (showcase in English, reference in `README.fr.md`, home screen capture in
`docs/assets/`) took real work; generated repos get none of that help. Give them a skill
(`/kiln:readme`) that writes or refreshes the README the same way.
- [ ] Draw the recipe from kiln's README: promise in one line, badges, capture or demo,
  quick start in three commands, what it does, link to the full reference, contributing.
- [ ] The skill reads the repo (stack, commands of `CLAUDE.md`, `kiln dev`) and proposes the
  README, never invents a feature; a capture of the app when there is one (`run` skill).
- [ ] Optional: `kiln check` notes a missing or bare README (rule of the charter, warning only).

### T-38 · `kiln adopt` reports the technologies kiln does not know yet
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: antoine, 16 October 2026 (adopters should tell kiln what it lacks); issue #42

Each adopted repo shows what kiln lacks (Svelte, Go, Rails…): the best roadmap there is, and
public issues show visitors that kiln has users.
- [ ] `kiln adopt` (and `kiln doctor`) detects the frameworks from the manifests
  (`package.json`, `pyproject.toml`, `pom.xml`, `go.mod`, `Gemfile`, `Cargo.toml`…).
- [ ] For what kiln does not support, one question, once per repo: "Svelte is not in kiln yet.
  Tell kiln? (opens an issue with the name and version only, nothing from your code)"; yes goes
  through `/kiln:report`.
- [ ] An existing issue for the same technology gets a 👍 instead of a duplicate; close #42.

### T-27 · The edit hook checks only the edited file
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: free mandate (teams with huge repos), 16 October 2026

`controle-fichier.py` runs the whole charter after every edit: on a big repo, seconds per
edit. The hook runs the bans on the edited file only; ratchets and floors run at commit and in
CI. Kept as a check after each edit (decided by Claude, 16 October 2026): it is feedback to
Claude, which fixes at once, not a block on the human, and it is the heart of the guardrails;
it only has to be fast (under 200 ms) and say how to waive.

### T-28 · Quiet session hook outside kiln repos
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: free mandate, 16 October 2026

In any repo, at each session, the hook creates `.claude/kiln`, writes to `.git/info/exclude`
and offers to adopt kiln: the shortest way to get a public plugin uninstalled. Outside kiln
repos: nothing. Adoption on request only (`kiln adopt`, `/kiln:adopt`). The goodwill score of
`relances.py` goes; a plain backoff for update reminders stays.

### T-29 · GitHub Release at each promotion, `kiln version` does the mechanical steps
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: free mandate, 16 October 2026

A release is a dozen manual steps and no GitHub Release (what watchers and the repo page
show). `pypi.yml` also creates the GitHub Release from the changelog entry; `kiln version`
cuts a candidate (branch, number, changelog skeleton, tag) and promotes one.

### T-31 · Neutral defaults instead of AnnSki's
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: free mandate, 16 October 2026

Europe/Paris in the rules, `.fr` domains, Java package `fr.<name>`, GDPR wording: a time zone
answer (default from the machine), `example.com` placeholders, a Java package derived from the
owner (existing projects keep `fr.<name>`).

### T-05 · Check the first real run of the workflows on GitHub
- **Type**: task
- **Status**: blocked — waiting for GitHub billing (CI stopped)
- **Opened**: 2026-10-15
- **Effort**: XS · **Owner**: Claude · **Due**: —
- **Origin**: actions at the workflow's commit, 15 October 2026

kiln's workflows clone kiln at `job.workflow_sha` (an April 2026 property, unknown to
actionlint) with a fallback to `develop`. On the first run, check that the version taken is the
tag's, and that `.kiln` is removed before the project's checks.

### T-07 · Better support for Java projects
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-15
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: handover of the kiln1 session, 15 October 2026
- [ ] Maven dependency audit in CI (`securite.yml`).
- [ ] `kiln update` bumps the versions in `pom.xml` (today only Dependabot does).
- [ ] `kiln ci` replays `maven.yml`.

## ⚪ Background — long-running work, debt and ideas

### T-08 · Copier migrations for breaking releases
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-15
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: move to semver, 15 October 2026

In 0.x, any release can break (patch-first numbering, CLAUDE.md "Versions"). Copier can run a migration when a version is crossed
(`_migrations` in `copier.yml`), but `kiln update` runs Copier with `unsafe=False`, so they do
not run: today a migration lives in kiln's Python code, after Copier (see `src/kiln/backlog.py`
for `docs/a-faire/` → `docs/backlog/`). Watch out: Copier deletes a file the template no longer
has even when the repo edited it; its content is still in the last commit.

### T-10 · Interface polish
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-15
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: interface redesign, 15 October 2026
- [ ] `kiln check`: the step title and the `✓` line say the same thing (one command per step).
- Bash completion moved to T-20.

---

## ✅ Done

- **2026-10-16** · T-26 · A friendlier `kiln new` — three questions (what you are building, size, language), the rest by default or option, `--all-questions` for the whole questionnaire; ends on the next steps and a first prompt (feat/cli-en) · opened 2026-10-16
- **2026-10-16** · T-09 · Tests running in the main tree during a merge — `.claude/worktrees/` in kiln's `.gitignore`, so a template copied from a dirty tree never sees the nested worktrees (fix/first-run) · opened 2026-10-15
- **2026-10-16** · T-06, T-13 · Translation and project language — merged into T-23 · opened 2026-10-15
- **2026-10-16** · T-21 · Credit #41 in the notes of the next release — line in the `v0.3.3` entry of `CHANGELOG.md` (release/v0.3.3) · opened 2026-10-16
- **2026-10-16** · T-20 · Bash completion (`kiln completion bash`) — PR #41 by @HarshRajSinghania, fixed up and merged, issue #40 closed · opened 2026-10-16
- **2026-10-16** · T-18 · Promoting a release makes `kiln update` conflict on `ci.yml` — cause confirmed (Copier's old render takes the promoted tag from `git describe`); the three-way merge is redone with the project's tag, reproduced in a test (fix/conflit-promotion) · opened 2026-10-16
- **2026-10-16** · T-19 · kiln has no pre-push hook — `.pre-commit-config.yaml` (ruff at commit, mypy before push), set by `kiln install` (chore/pre-push-kiln) · opened 2026-10-16
- **2026-10-16** · T-16 · A failed `kiln update --all` leaves a worktree that blocks the next
  run — a worktree with no change and no commit of its own is removed after the failure and
  before the next run; one with work in it is kept and named (`fix/update-reseau`) · opened 2026-10-16
- **2026-10-16** · T-15 · `kiln update --all` crashes with a Python traceback when GitHub is
  unreachable — Copier's git failure becomes one line in the summary, "GitHub injoignable"
  when the network is down (`fix/update-reseau`) · opened 2026-10-16
- **2026-10-16** · T-11 · Publish kiln on PyPI as `kiln-cli` — distribution and `kiln-cli`
  command, install source and update through PyPI, `pypi.yml` on the promotion tag, README;
  the first upload is checked by T-14 · opened 2026-10-16

- **2026-10-16** · T-01 · Promote v0.3.0, the first public release — `v0.3.1-rc.1` cut, then
  `v0.3.0` tagged on the commit of `v0.3.0-rc.1`, merged into `main`, back into `develop`;
  annway, sweep and vision moved to `v0.3.1-rc.1` (`kiln update --all`) · opened 2026-10-15
- **2026-10-16** · T-02 · Review PR #39 (`kiln --version`) from an outside contributor —
  reviewed with the new skill `base:contribution`, version computed only on demand (commit
  pushed on top of the contributor's), merged (`b71f91a`), issue #35 closed; credit to add to
  the next changelog entry (T-01) · opened 2026-10-15
- **2026-10-16** · Backlog in English: `docs/a-faire/` becomes `docs/backlog/` (`backlog.md`,
  `rejected.md`, `urgent.md`), `T-NN` tickets with a type and an opening date, skill
  `base:backlog`, status line reading both formats, old trackers converted by `kiln update`
  (`feat/backlog`).
- **2026-10-16** · "Claude Code's workshop" positioning: tagline "Make Claude Code build
  production-grade repos — and keep them that way." (README, `pyproject.toml`, `CLAUDE.md`,
  welcome subtitle), GitHub repo description and topics (`docs/positionnement`).
- **2026-10-15** · Semver in 0.x, candidates (`-rc.N`) and promotion, `interne` channel,
  `kiln version`, workflows quoted at the exact tag, actions at the workflow's commit
  (`feat/semver`); candidate `v0.3.0-rc.1` adopted by annway, sweep and vision; gitleaks and
  `workflow_call` brought up from annway into the template (`feat/secrets-scan`).
- **2026-10-15** · Interface (banner, welcome screen, spinner, summary), `kiln doctor`, prefixed
  output of `kiln dev`, debt (typed status line and `charte`), command tests and pytest-xdist,
  English GitHub showcase.
