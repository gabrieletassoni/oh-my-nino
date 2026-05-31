# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A skill for AI coding agents (Claude Code, Cowork, claude.ai) that runs a sanity-check
before dangerous actions or sloppy code. It's an office joke dedicated to colleague Nino
(POLES® lore: blue → bluette), but the check is real and functional.

The heart of the project is `oh-my-nino/SKILL.md`: a Markdown file with a YAML frontmatter
that defines the skill. The packaging script validates and zips it into a distributable `.skill`.

## Build

```bash
pip install pyyaml
python scripts/package_skill.py oh-my-nino dist
# → dist/oh-my-nino.skill
```

The script validates the `SKILL.md` frontmatter before creating the package. If validation
fails, it prints the exact error and exits with code 1.

## Release

CI/CD publishes automatically to GitHub Releases on every `v*` tag push:

```bash
git tag -a v1.0.0 -m "description"
git push origin v1.0.0
```

The tag **must** start with `v`. The workflow (`.github/workflows/release.yml`) does:
checkout → Python 3.12 → `pip install pyyaml` → packaging → Release creation with the
`.skill` attached.

To redo an existing tag: delete it locally and remotely, then recreate.

## Architecture

**`oh-my-nino/SKILL.md`** — the skill itself. Structure:
- YAML frontmatter (`name`, `description`) — `description` acts as an automatic trigger:
  the agent consults it on its own when the scenario matches
- Markdown body: lore/context, three severity levels (🟥/🟧/🟦), the Bluette-meter
  (⚪/🩵/🔵), fixed output format, engagement rules

**`scripts/package_skill.py`** — validation + zip. Frontmatter constraints:
- `name`: kebab-case, max 64 characters, no leading/trailing/double hyphens
- `description`: required, max 1024 characters, no `<` or `>`
- Excluded from package: `evals/`, `__pycache__/`, `.git`, `*.pyc`, `.DS_Store`

**`oh-my-nino/evals/evals.json`** — 6 test cases with prompt, expected output and
`expectations` lists. Not included in the `.skill`. Covers all three verdicts:
⚪ Faded (tests 1, 4, 6), 🩵 Bluette (tests 2, 5), 🔵 Full blue (test 3).

## Skill output conventions

The skill output block has a fixed format — do not change it:
```
🩵 CONTROLLO BLUETTE
Verdetto: <Blu pieno | Bluette | Sbiadito>
Nino, <one/three lines>
Per tornare blu: <concrete action>
```
For a "Blu pieno" verdict, one line only: `🔵 Tutto blu, Nino. Procedi pure.`

Tone: playful but proportional to actual severity. No false alarms just to make a quip.

## Documentation language

All user-facing documentation must be written **in both English and Italian**:
- `README.md` → English (primary, target: international developers)
- `README.it.md` → Italian (same folder as the English README)

This applies to every folder that contains a README (e.g. `oh-my-nino/`). The convention is
`README.md` (EN, primary) + `README.it.md` (IT), with navigation badges at the top of both:

```markdown
[🇬🇧 English](README.md) · [🇮🇹 Italiano](README.it.md)
```

Technical internal files (SKILL.md, CLAUDE.md, CONTRIBUTING.md, CHANGELOG.md) are in
English, as they target developers who are comfortable with English.

## Project files

| File | Purpose |
|---|---|
| `oh-my-nino/SKILL.md` | The skill (YAML frontmatter + logic in Markdown) |
| `oh-my-nino/evals/evals.json` | Test cases — excluded from `.skill` |
| `scripts/package_skill.py` | Frontmatter validation + `.skill` creation |
| `.github/workflows/release.yml` | CI/CD: `v*` tag → GitHub Release |
| `README.md` / `README.it.md` | Root documentation EN/IT |
| `oh-my-nino/README.md` / `oh-my-nino/README.it.md` | Skill documentation EN/IT |
| `CHANGELOG.md` | Version history (Keep a Changelog) |
| `CONTRIBUTING.md` | How to add checks, evals, and release |
| `LICENSE` | MIT |
