# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versioning follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- `AGENTS.md`: cross-agent guidance file (identical to `CLAUDE.md`, for OpenAI Codex, Gemini CLI, Cursor, Copilot, and others)

### Changed
- Technical internal files (CLAUDE.md, CONTRIBUTING.md, CHANGELOG.md) translated to English

## [1.0.2] — 2026-05-31

### Added
- `README.it.md` and `oh-my-nino/README.it.md`: Italian versions of the READMEs
- Language navigation badges at the top of all READMEs (`🇬🇧 English · 🇮🇹 Italiano`)

### Changed
- `README.md` and `oh-my-nino/README.md` translated to English as the primary language
- `CLAUDE.md`: added bilingual EN/IT documentation convention

## [1.0.1] — 2026-05-31

### Changed
- GitHub Actions updated to Node.js 24-native versions: `actions/checkout@v6`, `actions/setup-python@v6`, `softprops/action-gh-release@v3`

## [1.0.0] — 2026-05-31

### Added
- `oh-my-nino` skill: sanity-check at three severity levels (🟥 Real blunders / 🟧 Half-assed stuff / 🟦 Oversights of the precise)
- Bluette-meter with three verdicts: ⚪ Faded · 🩵 Bluette · 🔵 Full blue
- Packaging script `scripts/package_skill.py` with YAML frontmatter validation
- 6 evaluation cases in `oh-my-nino/evals/evals.json`
- GitHub Actions CI/CD: automatic publishing on `v*` tag push
- Dev container with Python 3.12
- Installation via `npx skills add gabrieletassoni/oh-my-nino` documented as primary method

[Unreleased]: https://github.com/gabrieletassoni/oh-my-nino/compare/v1.0.2...HEAD
[1.0.2]: https://github.com/gabrieletassoni/oh-my-nino/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/gabrieletassoni/oh-my-nino/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/gabrieletassoni/oh-my-nino/releases/tag/v1.0.0
