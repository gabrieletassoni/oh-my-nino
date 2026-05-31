# Changelog

Tutte le modifiche rilevanti a questo progetto sono documentate qui.
Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/),
il versionamento segue [Semantic Versioning](https://semver.org/lang/it/).

## [Unreleased]

### Added
- `README.it.md` e `oh-my-nino/README.it.md`: versioni italiane dei README
- `oh-my-nino/README.md` tradotto in inglese come lingua primaria
- Badge di navigazione lingua in cima a tutti i README (`🇬🇧 English · 🇮🇹 Italiano`)

### Changed
- `README.md` tradotto in inglese come lingua primaria per sviluppatori internazionali
- `CLAUDE.md`: aggiunta convenzione per documentazione bilingue EN/IT

## [1.0.2] — 2026-05-31

### Changed
- Installazione via `npx skills add gabrieletassoni/oh-my-nino` promossa a metodo principale nel README
- GitHub Actions aggiornate a versioni Node.js 24-native: `actions/checkout@v6`, `actions/setup-python@v6`, `softprops/action-gh-release@v3`

## [1.0.0] — 2026-05-31

### Added
- Skill `oh-my-nino`: sanity-check in tre livelli di severità (🟥 Minchiate vere / 🟧 Roba alla cazzo / 🟦 Dimenticanze del preciso)
- Bluette-meter con tre verdetti: ⚪ Sbiadito · 🩵 Bluette · 🔵 Blu pieno
- Script di packaging `scripts/package_skill.py` con validazione frontmatter YAML
- 6 casi di valutazione in `oh-my-nino/evals/evals.json`
- CI/CD GitHub Actions: pubblicazione automatica su tag `v*`
- Dev container con Python 3.12

[Unreleased]: https://github.com/gabrieletassoni/oh-my-nino/compare/v1.0.2...HEAD
[1.0.2]: https://github.com/gabrieletassoni/oh-my-nino/compare/v1.0.0...v1.0.2
[1.0.0]: https://github.com/gabrieletassoni/oh-my-nino/releases/tag/v1.0.0
