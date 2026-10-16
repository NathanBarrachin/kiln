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
  before 16 October 2026 were `AF-NN`, same number). **Next free: T-96.**
- **Type**, one of: `bug` (something is broken); `improvement` (it works, it could work
  better); `idea` (nothing exists yet, to be explored); `task` (work that is neither: a release,
  a decision, a check).
- **Status**, one of: `todo`; `in progress — branch <name>, since YYYY-MM-DD`;
  `blocked — waiting for <who or what>`; `to verify — <where>`.
- **Priority** = the section the ticket lives in; changing it means moving the ticket.
  🔴 critical (now), 🟠 important (before the north star), 🟡 normal, ⚪ background
  (long-running work, debt, ideas still to be explored).
- **Effort**: XS (under an hour), S (half a day), M (one or two days), L (more).
- **Releases**: the `## 🚀 Releases` section at the top places every open ticket in a planned
  release (`/kiln:backlog plan`); numbers are planned, not promised, until the candidate is cut.
- **Closing a ticket**: remove it from its section and add a line at the top of the "✅ Done"
  log: `- **YYYY-MM-DD** · T-NN · Title — what was done (branch) · opened YYYY-MM-DD`.
- **Locations quoted are hints, not addresses.**
- Overview: `grep -E '^(## |### T-|- \*\*Status)' docs/backlog/backlog.md`.
- **Good first issues**: keep 3 open on GitHub, reserved for outside contributors (skill
  `base:good-first-issues`); their tickets have **Owner**: `contributor — #NN`.

---

## 🚀 Releases

### v0.3.4 · A newcomer gets through the first run
Candidate tagged (`v0.3.4-rc.1`): frozen.
- T-22 · Release v0.3.4 and promote v0.3.3 (S)

### v0.3.5 · Releases that run themselves
Shipping is a dozen manual steps; after this, `kiln version` drives the plan and the promotions.
- T-29 · GitHub Release at each promotion, `kiln version` does the mechanical steps (M)
- T-44 · `/kiln:backlog plan`, read by `kiln version` and `/kiln:release` (M)
- T-14 · Promote v0.3.1, the first release on PyPI (XS) (blocked: antoine, old token)
- T-05 · Check the first real run of the workflows on GitHub (XS) (blocked: GitHub billing)
- T-04 · Decide whether annski quotes kiln's workflows at a tag (XS) (blocked: antoine)

### v0.4.0 · kiln speaks English
The milestone decided by antoine: every rename at once, converted by `kiln update`.
⚠ breaking: CLI names, `copier.yml` questions, charter rule IDs, workflow inputs, skill names.
- T-23 · kiln in English (L)
- T-25 · Plugin `kiln` with English skills, released with kiln (M)
- T-08 · Copier migrations for breaking releases (M)
- T-27 · The edit hook checks only the edited file (S)

### v0.4.1 · Nothing to trip on for a beginner
A first project without a question to answer, a flow to learn or a French default to undo.
⚠ breaking: the size question goes away.
- T-39 · Start light, grow with the repo (M)
- T-42 · The git flow grows with the size (M)
- T-36 · `kiln new` recommends the stack, the user decides (S)
- T-31 · Neutral defaults instead of AnnSki's (S)
- T-28 · Quiet session hook outside kiln repos (S)

### v0.4.2 · Everything settable, and you find it
The other half of T-41: the expert sets anything in one command, the newcomer is told when it matters.
- T-41 · Beginner with nothing to set, expert with everything settable (M)
- T-40 · kiln tells you what is possible, once, at the right moment (M)
- T-10 · Interface polish (S)
- T-45 · Update reminders at the pace you choose (S)
- T-95 · `kiln why` and `/kiln:onboard` (M)

### v0.4.3 · Instructions that fit the repo, for any agent
A script stops carrying a service's 400-line charter; rules load by path and by size, and other coding agents read them too.
⚠ breaking: generated tree (`.claude/rules/kiln/`).
- T-24 · Generated instructions in `.claude/rules/kiln/`, by path and by size (L)
- T-52 · `AGENTS.md` too: ready for every coding agent (M)

### v0.4.4 · From idea to live app
Every project type deploys from `kiln new`, on docker or podman, with a live example to prove it.
- T-37 · Docker or podman: the engine the machine has (M)
- T-32 · Every project type deployable from `kiln new` (L)
- T-35 · A site and an example app made by kiln, online (M)

### v0.4.5 · Your existing repo, welcome
The second door: adopt a repo as it is, say what kiln does not know, give it a fine README.
- T-34 · kiln for the repo you already have (M)
- T-38 · `kiln adopt` reports the technologies kiln does not know yet (M)
- T-07 · Better support for Java projects (M)
- T-43 · A skill that helps write a fine README, like kiln's own (M)

### v0.4.6 · Try kiln with nothing installed
A visitor gets from the README to a running project in minutes: one install line, a container
in the browser, no database to set up, a fast first run.
- T-49 · `kiln bootstrap`: from a bare machine to the first repo (M)
- T-48 · A devcontainer in every repo, kiln in Codespaces (M)
- T-51 · SQLite first, PostgreSQL when the project grows (M)

### v0.4.7 · Any repo scored, any repo free to leave
The launch hook: useful on any repo in one command, and the answer to "what if I want out?".
- T-46 · `kiln score`: any repo graded out of 100, with a badge (L)
- T-47 · `kiln eject`: leave kiln cleanly in one command (M)

### v0.4.8 · Every release proven on real repos, and fast
Reliability a team can rely on before the launch brings strangers in.
- T-54 · Upgrade paths, full end-to-end, Claude Code versions (L)
- T-50 · `kiln new` in under 30 seconds, and offline (M)

### v0.4.9 · Proof in numbers
The benchmark the launch post stands on.
- T-53 · kiln vs Claude Code alone, measured and published (L)

### v0.4.10 · Public launch
Proposed as **v0.5.0**: the public stability promise starts here (antoine decides).
- T-33 · One promise everywhere: tagline, About, PyPI, social preview (S)
- T-30 · README, English reference in `docs/`, demo of `kiln new` (M)
- T-55 · README in Chinese, Japanese, Spanish and Portuguese (S)
- T-56 · A configurator on kiln's site, and a gallery (M)
- T-03 · Launch kiln publicly, then list it in the Claude Code directories (S)
- T-12 · Homebrew formula in a tap (S) (blocked: demand)

### v0.4.11 · Never lets it rot, even without you
The repo stays current while nobody looks, and every change can be previewed and undone.
- T-59 · kiln-bot: `kiln update` as a scheduled pull request (L)
- T-60 · `kiln update --dry-run` and `--undo` (M)

### v0.4.12 · Major upgrades done for you
Where repos really rot: the framework major that breaks the code.
- T-61 · `kiln migrate`: framework major upgrades done by Claude Code (L)

### v0.4.13 · Add a feature, not a pile of files
Features that `kiln update` keeps current, starting with the one every app needs.
- T-62 · `kiln add <feature>` (L)
- T-63 · Add-on `auth` (M)

### v0.4.14 · A SaaS on day one
Mail, payments, then the project type that bundles them.
- T-64 · Add-on `email` (M)
- T-65 · Add-on `payments` (M)
- T-66 · Project type `saas` (L)

### v0.4.15 · Claude closes the loop on a ticket
From a ticket to a reviewed merge, with fast feedback at each edit.
- T-72 · `/kiln:feature` and `/kiln:fix` (L)
- T-73 · Subagents per stack (M)
- T-77 · Tests in seconds after each edit (M)

### v0.4.16 · Red to green without a human, on a lean context
- T-76 · `kiln ci --fix` (M)
- T-75 · `@claude` in pull requests and issues of generated repos (M)
- T-78 · Context budget, measured and capped (M)

### v0.4.17 · kiln as a tool for agents
- T-71 · `kiln mcp`, with `--json` everywhere (M)
- T-74 · `kiln autopilot` (L)

### v0.4.18 · Build for AI
The projects Claude Code users build most, with tests and evals as a matter of course.
- T-79 · Project type `mcp` (M)
- T-80 · Project type `agent` with evals in CI (L)

### v0.4.19 · More kinds of projects
JavaScript developers get a backend, two more fronts, and Python authors a library type.
- T-82 · A TypeScript backend: Hono and Drizzle (M)
- T-83 · SvelteKit and React (Vite) fronts (M)
- T-81 · Project type `library` (M)

### v0.4.20 · Know what production is doing
- T-67 · Add-on `observability` (M)
- T-93 · Database safety: migration linting, seed data, anonymised dumps (M)

### v0.4.21 · Ship every pull request with confidence
- T-88 · A preview environment for each pull request (M)
- T-89 · `kiln secrets` (M)

### v0.4.22 · Secure supply chain, a charter that fixes
- T-90 · Pinned actions, signed releases, OpenSSF Scorecard (M)
- T-91 · The charter fixes, annotates and accepts custom rules (L)

### v0.4.23 · Fronts tested like a user, in every language
- T-92 · End-to-end, accessibility, performance budgets (M)
- T-68 · Add-on `i18n` (M)

### v0.4.24 · Huge repos, and many of them
- T-86 · Monorepos: several services in one repo (L)
- T-87 · Fleet dashboard for an organisation (M)

### v0.4.25 · Your company's kiln
- T-70 · Org profiles (L)

### v0.4.26 · An ecosystem around kiln
Others build on kiln, see where it goes, and learn it from tutorials.
- T-69 · Community add-ons and stacks from any git repo (L)
- T-58 · A public roadmap on GitHub Projects, Discussions open (M)
- T-57 · A tutorial series: from idea to a live SaaS in an afternoon (M)

### v0.4.27 · Go and Rust
- T-84 · Go and Rust backends (L)

### v0.4.28 · Mobile apps
- T-85 · Mobile apps with Expo (L)

### v0.4.29 · Windows without WSL
- T-94 · Windows without WSL (L)

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
- **Status**: blocked — waiting for T-23 to T-25, T-27, T-30, T-32 to T-37 and T-39 to T-42,
  T-46 to T-54
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

### T-46 · `kiln score`: any repo graded out of 100, with a badge to show
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026 (antoine: "lots of stars, stand out, complete and
  ultra functional")

The single best star lever: something useful on the repo people already have, in one command,
with a result they want to share (Lighthouse, OpenSSF Scorecard). `uvx kiln-cli score` on any
repo, kiln or not: "How production-grade is your repo? 62/100". It is also the second door of
T-34 made concrete: the score shows what `kiln adopt` would fix.
- [ ] Around 30 checks in six families (tests and coverage, typing and lint, CI, security and
  secrets, git hygiene and protections, docs and agent readiness), each weighted, each with
  the one command or change that fixes it; reuses the charter and `kiln doctor`.
- [ ] Works without kiln installed in the repo and without network; GitHub checks (branch
  protection, CI status) when `gh` is logged in.
- [ ] Output: score, the three fixes that gain the most points, `--json`, and a Markdown
  badge (shields.io endpoint) to paste in the README.
- [ ] A GitHub Action (`antoine-tena/kiln/score@vX`) that comments the score and its delta on
  each pull request, listed on the GitHub Marketplace.
- [ ] "`kiln adopt` would fix 12 of these" at the end, on a repo kiln did not generate.

### T-47 · `kiln eject`: leave kiln cleanly in one command
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

"What if I want out?" is the question that stops a team from trying an opinionated tool. An
answer in one command removes the fear of lock-in, and the README can say it on the first
screen.
- [ ] `kiln eject` on a work branch: reusable workflows inlined at the tag they quote, kiln
  plugins and hooks unwired from `.claude/settings.json`, `.copier-answers.yml` kept (plain
  Copier still works), charter kept or removed (`--keep-charter`).
- [ ] The repo passes its own CI afterwards (test on every stack).
- [ ] README: "No lock-in: `kiln eject` and you are a plain repo again."

### T-48 · Try it in the browser: a devcontainer in every repo, kiln in Codespaces
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

Most visitors will not install anything to try a tool. An "Open in Codespaces" button that
lands in a terminal where `kiln new` and `claude` already work turns a visit into a try.
- [ ] Generated `.devcontainer/` per stack: uv, pnpm, JDK, podman or docker (T-37), gh,
  Claude Code, ports forwarded, `kiln install` as `postCreateCommand`.
- [ ] kiln's own devcontainer with kiln preinstalled, and the button at the top of the README.
- [ ] Works the same in VS Code "Reopen in Container" and in DevPod; test that it builds in CI.

### T-49 · `kiln bootstrap`: from a bare machine to the first repo
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

"Needs uv and git" already loses the newcomer the README targets. One line that installs what
is missing, then starts the first project.
- [ ] `curl -LsSf https://…/install.sh | sh` (and a PowerShell line for WSL users): uv, then
  `uv tool install kiln-cli`, then `kiln bootstrap`.
- [ ] `kiln bootstrap`: installs or points to git, gh (and its login), Claude Code, pnpm and
  the container engine when the chosen stack needs them, each with its direct link; ends on
  `kiln doctor` all green and `kiln new`.
- [ ] Idempotent, never `sudo` without saying why; tested on fresh Ubuntu, Debian, Fedora,
  macOS containers or runners.

### T-52 · `AGENTS.md` too: generated repos ready for every coding agent
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

`AGENTS.md` is the shared format read by Codex, Cursor, Gemini CLI, Copilot and others. Teams
mix agents; a kiln repo should not care which one a teammate runs. It multiplies the audience
without diluting the Claude Code focus.
- [ ] One source for the rules, rendered as `AGENTS.md` (portable part) and imported by
  `CLAUDE.md` (`@AGENTS.md`), Claude-only parts (skills, hooks) staying in `.claude/`.
- [ ] Optional thin adapters (`.cursor/rules/`, `GEMINI.md`) by `kiln set agents=…`.
- [ ] README: "Built for Claude Code, readable by any agent."

### T-53 · Proof in numbers: kiln vs Claude Code alone, measured and published
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

Every starter kit claims better code; none measures it. A reproducible benchmark is the thing
a launch post and Hacker News comments can argue about, and what keeps kiln's own changes
honest.
- [ ] `evals/`: a dozen realistic tasks (add a model and its API, fix a bug, add a page,
  upgrade a dependency…), each run by headless Claude Code on a bare repo and on a kiln repo of
  the same stack.
- [ ] Measured: tests passing, CI green, lint and type errors, secrets or forbidden patterns,
  regressions caught, tokens and minutes spent.
- [ ] Results page in `docs/`, a chart in the README, the harness runnable by anyone
  (`uv run evals`), rerun at each minor release.

### T-54 · Every release proven on real repos: upgrade paths, full end-to-end, Claude Code versions
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026 (north star: "reliable for a team with huge repos")

Rendering every combination is tested; installing, checking, building and updating them is
not. The promise "kept up to date for as long as the project lives" rests on `kiln update`
from any old release.
- [ ] Nightly workflow: every stack generated, `kiln install`, `kiln check`, containers built,
  `kiln dev` answering on its port.
- [ ] Upgrade paths: repos generated by each of the last five releases updated to the
  candidate, checks green, no conflict marker; a candidate cannot be promoted otherwise
  (`kiln version` reads the result).
- [ ] The hooks, skills and status line run against the current and the previous Claude Code
  release; `claude plugin eval` suites for the main skills.

## 🟡 Normal

### T-45 · Update reminders at the pace you choose
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: antoine, 16 October 2026

Asking at every release annoys; letting users skip releases is worse in 0.x (each patch can
break, skipped conversions pile up). So space the question, never the updates.
- [ ] `kiln set update-reminders=each|daily|weekly` (machine setting, default from
  `reminders.py`'s current backoff); when accepted, the repo goes to the latest release.
- [ ] From 1.0 (strict semver): `update-level=patch|minor|all` to follow only some releases.

### T-44 · `/kiln:backlog plan`: group the open tickets into the next releases
- **Type**: improvement
- **Status**: in progress — branch feat/backlog-plan, since 2026-10-16
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: antoine, 16 October 2026

Deciding which tickets ship together is done by hand. A `plan` mode of the backlog skill (not
a new skill: one name less to learn, T-41) proposes the next releases.
- [x] Read open tickets: priority, effort, status, dependencies (`blocked — waiting for T-xx`).
- [x] Group them into releases: dependencies first, one theme per release, small releases
  (each one bumps the patch); breaking changes flagged, they open the release note.
- [x] May propose a minor bump when a group forms a milestone (allowed by antoine,
  16 October 2026); antoine decides.
- [x] Once agreed, write the plan into the backlog ("🚀 Next releases" section).
- [x] Every open ticket in a release, named after its outcome; new tickets placed anywhere in
  the plan (antoine, 16 October 2026).
- [ ] `kiln version`
  and `/kiln:release` say what is missing before the next candidate.

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

### T-50 · `kiln new` in under 30 seconds, and offline
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

The first run is the demo. Every second spent on network and installs is a visitor gone.
- [ ] Measure each step of `kiln new` (`--timings`), then cut: template cached locally, uv and
  pnpm caches shared, lockfiles pre-resolved at release time, installs in parallel.
- [ ] `kiln new --offline` works from the cache (plane, flaky network).
- [ ] Budget checked in the nightly run of T-54: an `app` under 30 s with a warm cache.

### T-51 · SQLite first, PostgreSQL when the project grows
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

A newcomer's first app should run without a database container. Django and FastAPI work on
SQLite; PostgreSQL earns its place when there are users.
- [ ] `database=sqlite|postgres` setting; `sqlite` by default at `spark` and `ember`, no
  container needed for `kiln dev`.
- [ ] `kiln set database=postgres`: compose service, settings, data moved over with the
  framework's dump and load, said in one line.
- [ ] The charter keeps the code portable (no raw SQL tied to one engine without a waiver).

### T-55 · README in Chinese, Japanese, Spanish and Portuguese
- **Type**: task
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: S · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

A large share of the stars on developer tools come from Chinese, Japanese and Brazilian
communities, who share translated READMEs widely.
- [ ] `README.zh-CN.md`, `README.ja.md`, `README.es.md`, `README.pt-BR.md`, linked from the
  language line of the README.
- [ ] A check at release time: same sections and same commands as `README.md`, otherwise the
  release lists which translation is behind.

### T-56 · A configurator on kiln's site, and a gallery of what was built
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; builds on T-35

start.spring.io made Spring approachable: pick, see, copy. The same on kiln's site, plus the
proof that people build real things.
- [ ] Configurator page: project type, stack, options, built from `copier.yml` at release time;
  shows the generated tree and the exact `uvx kiln-cli new …` command to copy.
- [ ] Gallery: public repos generated by kiln (GitHub code search on `.copier-answers.yml`),
  opt-in through a `kiln` topic; a "Built with kiln" badge offered in the generated README.

### T-57 · A tutorial series: from idea to a live SaaS in an afternoon
- **Type**: task
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

Tutorials keep bringing visitors long after a launch; a series also tests the newcomer path for
real.
- [ ] Five parts in `docs/tutorials/`, published on dev.to (`.devto/`): `kiln new`, first
  feature with Claude Code, auth and payments (T-63, T-65), deploy (T-32), keeping it alive
  (`kiln update`, T-59).
- [ ] Each part replayed at each minor release by a script; a broken step is a bug.

### T-59 · kiln-bot: `kiln update` as a scheduled pull request, no machine needed
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026 ("Never lets it rot")

`kiln update` only runs when someone remembers. Renovate and Dependabot update dependencies,
nothing updates the rest of the repo. A weekly pull request with the template, dependencies and
checks is the promise kept without anyone in the loop.
- [ ] Reusable workflow `update.yml` (cron in each generated repo): `kiln update`, checks,
  pull request with the release notes crossed and the dependency changes; nothing when
  nothing changed.
- [ ] Conflicts left as a draft pull request that says which files and why.
- [ ] Replaces Dependabot in generated repos (one pull request instead of twenty), `kiln set
  update_bot=weekly|monthly|off`.

### T-60 · `kiln update --dry-run` and `kiln update --undo`
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

Teams with big repos want to see a change before it lands, and a way back.
- [ ] `--dry-run`: the diff of the template and the dependency changes, nothing written; same
  for `kiln set`.
- [ ] `--undo`: the last update or set reverted (its commits are known), the lockfiles and
  `.copier-answers.yml` back as they were.

### T-61 · `kiln migrate`: framework major upgrades done by Claude Code
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

`kiln update --major` bumps the version; the code that breaks is left to the human. That is
where repos rot (Django 5 → 6, Nuxt 3 → 4, Next majors).
- [ ] `kiln migrate django` on a work branch: official codemods first (`django-upgrade`,
  `nuxi upgrade`, Next codemods), then headless Claude Code with the upstream migration guide
  until `kiln check` passes, then a pull request with what was changed and why.
- [ ] Budget cap (tokens, minutes), stops and reports instead of looping.

### T-62 · `kiln add <feature>`: features on an existing repo, updated like the rest
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

Stacks are files; a product needs features (accounts, payments, mail). Boilerplates ship them
once and leave them to rot; kiln can ship them as add-ons that `kiln update` keeps current.
- [ ] Add-ons as Copier sub-templates with their own answers file (Copier supports several
  per repo), applied, updated and removed (`kiln remove <feature>`) like the main template.
- [ ] `kiln add --list`: what fits this stack, one line each; each add-on adds its rules to
  `.claude/rules/kiln/` and its tests.
- [ ] Contract test: every add-on on every stack it declares, then `kiln check` green.

### T-63 · Add-on `auth`: accounts, social login, passkeys
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; needs T-62

The first thing every app needs and the first thing done wrong.
- [ ] Django (allauth, headless) and FastAPI backends, Nuxt and Next pages: sign up, sign in,
  reset, email check, GitHub and Google login, passkeys.
- [ ] Rate limits, secure cookies, CSRF, and their tests; charter rules that keep them.

### T-64 · Add-on `email`: transactional mail, templates, a local inbox
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; needs T-62

- [ ] Templates (MJML or plain HTML plus text), a send function, a provider by setting
  (Resend, Postmark, SMTP), Mailpit in `compose.yaml` so every mail is visible in dev.
- [ ] Sent in a background task, retried; a test helper that asserts on the sent mails.

### T-65 · Add-on `payments`: Stripe checkout, subscriptions, webhooks
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; needs T-62, builds on the `stripe` plugin

- [ ] Checkout, customer portal, subscription state on the user, webhooks verified and
  idempotent, test-mode keys through `/kiln:token`.
- [ ] Stripe CLI forwarding started by `kiln dev`; webhook tests replaying recorded events.

### T-66 · Project type `saas`: accounts, billing, mail and admin, ready on day one
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

SaaS boilerplates are the most starred project templates, and most are sold. A free one that
stays maintained and that Claude Code knows how to grow stands out.
- [ ] `kiln new --type saas`: `app` plus T-63, T-64, T-65, an admin dashboard, a landing
  page, terms and privacy pages to fill, deployment of T-32.
- [ ] The example app of T-35 is this type.

### T-67 · Add-on `observability`: structured logs, OpenTelemetry, error tracking
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; needs T-62

- [ ] JSON logs with request IDs, OpenTelemetry traces and metrics, Sentry (or GlitchTip)
  with releases tagged by commit; a local Grafana stack in `compose.yaml` on demand.
- [ ] On by default from `flame` (T-39), with the rule that keeps it.

### T-68 · Add-on `i18n`: a translated interface from day one
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; needs T-62

Retrofitting translations means touching every string; starting with them costs nothing.
- [ ] Nuxt i18n, next-intl, Django gettext wired; languages by setting.
- [ ] A charter rule against hard-coded UI strings; a skill that translates the missing keys.

### T-70 · Org profiles: a company's defaults and rules on top of kiln
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026 (north star: big teams)

A company adopts a tool it can bend: its own registry, its rules, its plugins, without
forking kiln and falling behind.
- [ ] `kiln new --profile github:acme/kiln-profile` (or a machine setting): default answers,
  extra charter rules, extra rules for Claude, private plugins, required CI jobs.
- [ ] `kiln update` applies kiln then the profile; the profile can forbid a waiver.
- [ ] An example profile repo and its docs.

### T-71 · `kiln mcp`: kiln as tools for Claude, with `--json` everywhere
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

Claude Code drives kiln by reading terminal output meant for humans. Structured results make
it reliable and cheaper.
- [ ] `--json` on every command with a documented schema (status, checks, findings, next
  command), tested.
- [ ] `kiln mcp`: an MCP server (shipped in the `kiln` plugin) exposing `status`, `check`,
  `set`, `waive`, `doctor`, `score` as tools.

### T-72 · `/kiln:feature` and `/kiln:fix`: a ticket done the way a senior would
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

Skills cover git and releases; the actual work on a ticket is left to Claude's habits.
- [ ] `/kiln:feature T-NN`: worktree, short spec in the ticket (acceptance criteria), tests
  that fail, code, `kiln check`, review (`/kiln:review`), merge or pull request, ticket done.
- [ ] `/kiln:fix`: reproduce, a regression test that fails first, the fix, the cause written
  in the ticket.
- [ ] Both stop and ask when the spec is ambiguous, never guess a product decision.

### T-73 · Subagents per stack: reviewer, test writer, security auditor
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] `agents/` in the plugins: `reviewer` (reads the diff against the charter and the stack
  rules), `test-writer`, `security-auditor` (OWASP, secrets, auth), `migration-checker`
  (Django), each with a narrow toolset and a cheap model where it fits.
- [ ] Called by T-72 and `/kiln:review`, never spawned in fleets (token cost).

### T-75 · `@claude` in pull requests and issues of generated repos, reviewing against the charter
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] Optional reusable workflow wiring the Claude Code GitHub Action, with kiln's rules and
  skills loaded: `@claude` in an issue opens a pull request, every pull request gets a review
  quoting rule IDs.
- [ ] `kiln set claude_review=on`, the key set through `/kiln:token`, monthly cost cap said in
  the docs.

### T-76 · `kiln ci --fix`: a red CI made green by Claude Code, locally
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; builds on `kiln ci`

- [ ] Reads the failed job (GitHub logs or local replay), runs headless Claude Code on a work
  branch with the failure as the prompt, replays the job until green or budget spent.
- [ ] Never touches a test to make it pass without saying so in the commit message.

### T-77 · Tests in seconds after each edit: only those the change touches
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; complements T-27

Claude Code learns from fast feedback; a full suite after each edit is too slow on big repos.
- [ ] `kiln test --changed`: pytest-testmon, `vitest related`, Maven incremental; full suite
  stays in `kiln check` and CI.
- [ ] Offered to Claude as the default test command in the generated rules.

### T-78 · Context budget: what Claude loads at session start, measured and capped
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; complements T-24

Instructions, skills descriptions, MCP tools and hooks output eat the context before the first
prompt, and nobody measures it. A number makes kiln repos visibly lean.
- [ ] `kiln doctor` and the charter count the tokens loaded at start (CLAUDE.md, rules without
  `paths:`, skills and MCP tool definitions); a ceiling by size, a ratchet like file sizes.
- [ ] The figure in `kiln score` (T-46) and optionally in the status line.

### T-79 · Project type `mcp`: an MCP server, tested and published
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

MCP servers are what Claude Code users build most right now, mostly without tests or releases.
- [ ] `kiln new --type mcp`: Python (FastMCP) or TypeScript SDK, example tools, tests through
  an in-process client, MCP Inspector in `kiln dev`.
- [ ] Release to PyPI or npm and to the MCP registry by the release skill; `.mcp.json`
  snippet in the README.

### T-80 · Project type `agent`: a Claude Agent SDK app with evals in CI
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

LLM apps without evals are where "it worked on my prompt" lives. A kiln repo for them makes
evals as normal as unit tests.
- [ ] `kiln new --type agent`: Agent SDK app, prompts as versioned files, tools typed and
  tested, an eval suite (datasets, graders) run in CI with a score floor, cost per run logged.
- [ ] Charter rules: no API key in code, model IDs in one place, a budget cap.

### T-81 · Project type `library`: a Python package on PyPI, done right
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] `kiln new --type library`: `src/` layout, typed (`py.typed`), tests on supported Python
  versions, docs site, changelog, PyPI trusted publishing on the release tag.
- [ ] API break detection between releases (griffe) in CI.

### T-82 · A TypeScript backend: Hono and Drizzle, types end to end
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

JavaScript developers are the largest audience and kiln offers them only fronts.
- [ ] `backend=hono`: Hono, Drizzle (SQLite or PostgreSQL, T-51), Zod, Vitest, OpenAPI
  exported so `kiln contract` types the front; pnpm workspace with the front.
- [ ] Reusable workflow and charter rules for it.

### T-83 · SvelteKit and React (Vite) fronts
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; also answers the unknown-technology reports of T-38

- [ ] `frontend=sveltekit` and `frontend=react` (Vite SPA, TanStack Router and Query), with
  their rules, lint, tests and deployment target.

### T-86 · Monorepos: several services in one repo
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026 (north star: huge repos)

kiln knows one backend and one front; real products grow a worker, a second API, a docs site.
- [ ] `kiln add service <name> --backend fastapi`: each service its own folder, rules,
  `CLAUDE.md` and CI job filtered by paths; `kiln dev`, `check`, `update` across all.
- [ ] Shared packages (uv workspace, pnpm workspace) and the contract between services.

### T-87 · Fleet dashboard for an organisation, without cloning anything
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; extends `kiln status`

- [ ] `kiln status --org acme`: through the GitHub API, every kiln repo of an organisation with
  its template lag, CI state, open security alerts, waivers and score (T-46).
- [ ] `--html` report, also produced weekly by a workflow in a `.github` repo.

### T-88 · A preview environment for each pull request
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; needs T-32

- [ ] Vercel and Render previews wired, with a throwaway database seeded (T-93); the URL
  commented on the pull request, removed on merge.
- [ ] Smoke test run against the preview before merge is allowed.

### T-89 · `kiln secrets`: one place for secrets, synced where they are needed
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

`.env` files drift between machines, GitHub secrets and the host.
- [ ] Encrypted `secrets.enc.env` committed (sops and age, keys per person), `.env`
  generated by `kiln install`.
- [ ] `kiln secrets push`: to GitHub Actions and the host of T-32, never shown; `kiln secrets
  diff` says what is missing where.

### T-90 · Supply chain: pinned actions, signed releases, OpenSSF Scorecard
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

A tool that rewrites many repos must be trustworthy itself, visibly.
- [ ] Third-party actions pinned by SHA in kiln and the template (updated by kiln-bot T-59),
  `permissions:` minimal everywhere (zizmor in CI).
- [ ] PyPI attestations and Sigstore-signed release artifacts; Scorecard workflow and badge on
  kiln, then in generated repos.

### T-91 · The charter fixes, annotates and accepts custom rules
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] SARIF output, uploaded by `charter.yml`: findings shown in the pull request diff and in
  GitHub code scanning.
- [ ] `charter --fix` for the rules that can be fixed mechanically.
- [ ] Repo-local rules (`.kiln/rules/*.py`, a small documented API) with their tests; a rule
  that proves useful is proposed to kiln by `/kiln:report`.

### T-92 · Fronts tested like a user: end-to-end, accessibility, performance budgets
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] Generated Playwright smoke tests (home, sign in when T-63 is there) run in CI against
  the built app.
- [ ] axe accessibility checks and Lighthouse CI budgets, thresholds by size.

### T-93 · Database safety: migration linting, seed data, anonymised dumps
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] Migrations checked for locking or destructive operations before merge
  (django-migration-linter, squawk for raw SQL).
- [ ] `kiln seed`: realistic fake data for dev and previews; `kiln dump --anonymise` from
  production with the personal-data patterns of the charter.

### T-95 · `kiln why` and `/kiln:onboard`: every choice explained, every repo toured
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; complements T-40 and T-41

The newcomer kiln targets learns by asking why. Opinions explained become a reason to stay.
- [ ] `kiln why uv`, `kiln why <RULE-ID>`, `kiln why podman`: two or three lines, the
  alternative and how to switch; sourced from the same data as the docs.
- [ ] `/kiln:onboard`: a guided tour of the repo for a new teammate (stack, commands, where
  things live, open tickets), written from the repo itself.

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

### T-58 · A public roadmap: the backlog on GitHub Projects, Discussions open
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: M · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

Contributors and users want to see where kiln goes and to weigh in, without reading a
Markdown file.
- [ ] `docs/backlog/backlog.md` published one way to a GitHub Project (one card per ticket,
  release as a field) by a workflow at each push on `develop`.
- [ ] GitHub Discussions open (ideas, show and tell, questions), linked from the README and
  from `/kiln:report`.

### T-69 · Community add-ons and stacks from any git repo
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; needs T-62

An ecosystem is what turns a tool into a project people star and contribute to.
- [ ] `kiln add github:someone/kiln-addon-x` and `kiln new --stack github:someone/kiln-stack-rails`,
  with a trust prompt showing what the add-on runs.
- [ ] An index file in kiln listing reviewed add-ons; an author kit (template, contract tests,
  reusable workflow that tests the add-on on each kiln release).

### T-74 · `kiln autopilot`: backlog tickets done unattended, one pull request each
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026; needs T-72

- [ ] Picks tickets marked `autopilot` in the backlog, runs `/kiln:feature` headless in its
  own worktree, opens a pull request when checks pass; never merges.
- [ ] Budget per ticket and per night, one ticket at a time (no fleet), a report in the
  morning.

### T-84 · Go and Rust backends
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] `backend=go` (standard library router, sqlc, golangci-lint) and `backend=rust` (axum,
  sqlx, clippy), their reusable workflows, charter rules and container images.

### T-85 · Mobile apps with Expo
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] `frontend=expo`: React Native app talking to the backend's typed client, tests, EAS
  builds in CI, store submission documented step by step with direct links.

### T-94 · Windows without WSL
- **Type**: idea
- **Status**: todo
- **Opened**: 2026-10-16
- **Effort**: L · **Owner**: Claude · **Due**: —
- **Origin**: growth review, 16 October 2026

- [ ] `kiln` and the generated repos on native Windows (PowerShell, paths, line endings,
  hooks in Python only), a Windows job in kiln's CI; until then `kiln doctor` says WSL clearly.

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
