# Changelog

Tutte le modifiche rilevanti a questo progetto sono documentate qui.
Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/),
il versionamento segue [Semantic Versioning](https://semver.org/lang/it/).

## [Unreleased]

### Changed
- Installazione via `npx skills add gabrieletassoni/oh-my-nino` promossa a metodo principale nel README

## [1.0.0] — 2026-05-31

### Added
- Skill `oh-my-nino`: sanity-check in tre livelli di severità (🟥 Minchiate vere / 🟧 Roba alla cazzo / 🟦 Dimenticanze del preciso)
- Bluette-meter con tre verdetti: ⚪ Sbiadito · 🩵 Bluette · 🔵 Blu pieno
- Script di packaging `scripts/package_skill.py` con validazione frontmatter YAML
- 6 casi di valutazione in `oh-my-nino/evals/evals.json`
- CI/CD GitHub Actions: pubblicazione automatica su tag `v*`
- Dev container con Python 3.12

[Unreleased]: https://github.com/gabrieletassoni/oh-my-nino/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/gabrieletassoni/oh-my-nino/releases/tag/v1.0.0
