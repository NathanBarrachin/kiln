<div align="center">

# kiln

**Un repo où Claude Code travaille sans risque, en trois questions — puis tenu à la meilleure façon de travailler, version après version.**

[![PyPI](https://img.shields.io/pypi/v/kiln-cli.svg?color=c2551f)](https://pypi.org/project/kiln-cli/)
[![CI](https://github.com/antoine-tena/kiln/actions/workflows/kiln.yml/badge.svg?branch=develop)](https://github.com/antoine-tena/kiln/actions/workflows/kiln.yml)
[![Python 3.14](https://img.shields.io/badge/python-3.14-3776ab.svg)](https://www.python.org/)
[![Licence : MIT](https://img.shields.io/badge/licence-MIT-4c4c4c.svg)](LICENSE)

[**Référence**](docs/reference.fr.md) · [Journal des versions](CHANGELOG.md) · [Contribuer](CONTRIBUTING.md) · [English](README.md)

<img src="docs/assets/kiln-home.svg" alt="L'écran d'accueil de kiln : un four en pixel art au-dessus de ses commandes, rangées par projet, quotidien, grille et tous les repos" width="620">

<i><code>kiln</code> seul : toutes les commandes, rangées selon ce que l'on fait.</i>

</div>

Claude Code écrit vite. Un repo a besoin de plus pour rester sain : une stack à jour, des règles
qu'un agent ne peut pas contourner à force d'arguments, une façon de travailler avec git qui
résiste à un mauvais après-midi, et quelqu'un pour l'empêcher de vieillir au quatre-vingt-dixième
jour. kiln fait les quatre, pour chacun de vos repos.

## Points forts

- 🧱 **Trois questions, un repo complet.** Ce que vous construisez, sa taille, la langue de
  l'équipe : kiln choisit la stack et écrit le code, les tests, les linters, la CI, les crochets
  pre-commit, les conteneurs et les consignes que Claude lit en premier.
- 🔄 **À jour toute sa vie.** `kiln update` rejoue le modèle, prend les mises à jour compatibles
  des dépendances, convertit ce qu'une version a renommé et lance les contrôles avant que vous
  ne commitiez.
- 🧪 **Essayé avant de rien toucher.** `kiln update --rehearse` joue la mise à jour sur un clone
  jetable et rend un bilan ; `--all` le fait pour chaque repo du dossier de code.
- 📏 **Des règles qui tiennent.** `charter` contrôle chaque fichier que Claude modifie en
  0,15 s environ (outils bannis, noms, tailles, données personnelles dans les logs) ; cliquets
  et seuils de couverture tiennent à chaque commit et en CI. Une dérogation est datée et
  justifiée.
- 🧭 **Le meilleur, sources à l'appui.** `kiln grid` liste les pratiques que kiln défend,
  chacune avec sa raison, ses sources vérifiées et datées, et sa façon d'être détectée.
- 🤖 **Fait pour Claude Code.** Des skills pour les worktrees, les fusions, les versions et les
  relectures ; des hooks qui gardent vos branches ; une status line qui montre la CI, les
  tickets et la production.
- 💸 **Aucune minute GitHub pour un repo privé.** Sa CI tourne sur votre poste (`kiln ci`,
  verdict gardé en note git) ; un repo public tourne sur GitHub, où c'est gratuit.

## Installation

```sh
uv tool install kiln-cli     # la commande est kiln ; uv installe Python 3.14 s'il manque
```

Ou sans rien installer : `uvx kiln-cli new mon-app`. macOS, Linux et Windows par WSL ;
[pnpm](https://pnpm.io/) pour les fronts JavaScript, [podman](https://podman.io/) pour les
conteneurs.

## Démarrage

```console
$ kiln new mon-app            # trois questions, puis un dépôt GitHub privé (--no-github : local)
$ cd mon-app && kiln dev      # les serveurs de la stack, sorties préfixées par service
$ kiln check                  # ruff, mypy, pytest, ESLint, types, puis charter
$ claude                      # Claude Code, avec les règles, skills et hooks de kiln
```

## Ce que vous obtenez

| Vous construisez | Backend | Frontend |
|---|---|---|
| Une application complète (`app`) | Django + Django Ninja | Nuxt + Vue |
| Une API (`api`) | FastAPI | — |
| Un site de contenu (`site`) | — | Astro |
| Un tableau de bord de données (`dashboard`) | polars, marimo, Plotly | Streamlit |
| Une analyse de données (`analysis`) | polars, marimo, Plotly | — |
| Un outil en ligne de commande (`cli`) | Python, installable | — |

Next.js, Dash et Java 25 + Maven sont là aussi, et chaque combinaison est générée et vérifiée
par les tests de kiln. **Django et Nuxt sont complets ; les autres stacks sont figées mais
entretenues** : les nouvelles règles de la grille vont d'abord à Django et Nuxt.

Chaque repo reçoit aussi uv, pnpm et podman (jamais pip, npm ni docker), une CI qui appelle les
workflows réutilisables de kiln, des branches `main` et `develop` protégées, un `docs/backlog/`
de tickets typés, et une taille — `spark`, `ember`, `flame` ou `blaze` — qui décide du
cérémonial qu'il porte. Une application Django peut partir sur un VPS durci (Caddy, conteneurs
en lecture seule, retour arrière automatique, sauvegardes restaurées), un front Nuxt sur Vercel.

## Tenu à jour

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/kiln-flow-dark.svg">
    <img src="docs/assets/kiln-flow-light.svg" alt="Une version, tous les repos à jour : kiln, puis une candidate sur CI verte, la version sur PyPI, une répétition sur un clone de chaque repo, puis kiln update dans chaque repo" width="820">
  </picture>
</p>

Une version de kiln sort d'abord en candidate (`-rc.N`), taguée seulement quand sa CI est verte
sous Linux et macOS, y compris une mise à jour depuis chaque version depuis la v0.3.0, par un
outil installé. Elle est promue quand la candidate suivante est prête, puis répétée sur un clone
de chaque repo avant que `kiln update --all` la fusionne, un worktree par repo. Les repos citent
les workflows de kiln à la version exacte qu'ils suivent : rien ne leur arrive entre deux
versions.

<p align="center">
  <img src="docs/assets/kiln-update.svg" alt="kiln update : un cadre qui liste les nouveautés de chaque version traversée, lues dans le journal de kiln" width="680">
</p>
<p align="center"><i>Ce que montre <code>kiln update</code> en traversant une version, lu dans le journal de kiln.</i></p>

## La grille

<p align="center">
  <img src="docs/assets/kiln-grid.svg" alt="kiln grid : les règles que kiln défend, par thème, chacune avec son niveau" width="680">
</p>
<p align="center"><i><code>kiln grid</code> : les règles que kiln défend aujourd'hui ; <code>kiln grid &lt;ID&gt;</code> en montre une, sources comprises.</i></p>

Un petit fichier TOML par règle, sur deux axes : son thème (chaîne d'approvisionnement,
conteneurs, tests…) et sa portée (universelle, un langage, un framework, un outil). Chacune dit
pourquoi, cite des sources pesées dans un ordre fixe — documentation officielle, alertes de
sécurité, études mesurées, données d'adoption, blogs — et porte un niveau du Technology Radar de
Thoughtworks : adopter, essayer, évaluer, abandonner. Seules les règles adoptées comptent ;
105 brouillons tirés d'un repo en production attendent derrière `kiln grid --level assess`.
Chaque règle notée a un repo qui la respecte et un qui l'enfreint.

## Comparé à Copier et cookiecutter

kiln repose sur [Copier](https://copier.readthedocs.io) : chaque projet garde son
`.copier-answers.yml`, et Copier seul fonctionne toujours dessus. kiln ajoute ce qui vient
après le premier jour.

| | cookiecutter | Copier | **kiln** |
|---|:---:|:---:|:---:|
| Générer un projet | ✅ | ✅ | ✅ |
| Appliquer les évolutions du modèle aux projets existants | ❌ | ✅ | ✅ |
| Choisir la stack d'après ce que l'on construit | ❌ | ❌ | ✅ |
| Changer de stack plus tard (`kiln set frontend=nuxt`) | ❌ | en partie | ✅ |
| Mettre à jour les dépendances et lancer les contrôles d'un coup | ❌ | ❌ | ✅ |
| Répéter, puis mettre à jour tous ses repos d'un coup | ❌ | ❌ | ✅ |
| Des workflows de CI partagés, cités à une version | ❌ | ❌ | ✅ |
| Un moteur de règles aux dérogations datées (`charter`) | ❌ | ❌ | ✅ |
| Skills, hooks et consignes pour Claude Code | ❌ | ❌ | ✅ |

kiln a des opinions, exprès. Pour un moteur de gabarits neutre, prenez Copier ; pour une façon
de travailler qui reste entretenue, prenez kiln, ou forkez-le et faites vôtres ses opinions.

## Référence

Chaque commande et chaque option, chaque clé de `kiln set`, les workflows réutilisables, les
plugins Claude Code, le moteur de charte et la façon dont kiln sort ses versions :
[**docs/reference.fr.md**](docs/reference.fr.md). Dans un terminal, `kiln <commande> --help`.

## État

kiln fait tourner chaque jour une poignée de vrais repos, dont un en production. Il numérote ses
versions comme Claude Code : en `0.x`, chaque version monte le correctif, les changements
cassants en tête du [journal](CHANGELOG.md) et convertis par `kiln update` ; la mineure marque
une étape. Le semver strict commence à la 1.0.

## Contribuer

Les issues et les pull requests sont bienvenues : voir [CONTRIBUTING.md](CONTRIBUTING.md), et
l'étiquette [`good first issue`](https://github.com/antoine-tena/kiln/labels/good%20first%20issue)
pour commencer. Dans un repo kiln, `/kiln:report` transforme un défaut de kiln en issue ou en
pull request prête à poster, envoyée seulement avec votre accord. Si kiln vous fait gagner du
temps, une ⭐ aide d'autres à le trouver.

## Licence

[MIT](LICENSE)
