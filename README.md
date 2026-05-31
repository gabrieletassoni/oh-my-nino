# oh-my-nino 🩵

[🇬🇧 English](README.md) · [🇮🇹 Italiano](README.it.md)

---

A **joke skill** for AI coding assistants, dedicated to colleague **Nino**. Playful tone,
serious substance: it **reminds you that you're about to do something sloppy or make a
serious blunder** before you actually do it (force push on `main`, `rm -rf` with empty
variables, SQL without `WHERE`, hardcoded secrets, ignored edge cases...).

> In the **POLES®** behavioural model, **blue** is the precise, analytical, methodical
> style. Nino scored blue. In practice, he occasionally fades into **bluette** — a
> washed-out blue. This skill guards that boundary. Full lore in
> [`oh-my-nino/README.md`](oh-my-nino/README.md).

## Repository structure

```
.
├── README.md                       # this file (overview + CI/CD)
├── .github/workflows/release.yml   # GitHub Action: publishes .skill on tag
├── scripts/package_skill.py        # validation + packaging into .skill
└── oh-my-nino/                     # THE SKILL (what gets packaged)
    ├── SKILL.md                    # the skill itself
    ├── README.md                   # skill README (tone / lore)
    └── evals/evals.json            # 6 test cases (excluded from package)
```

## Installation

### Via npx (recommended)

Works with Claude Code, Cursor, Cline, Copilot and 50+ other agents. Requires Node.js only:

```bash
npx skills add gabrieletassoni/oh-my-nino
```

The [skills](https://skills.sh) CLI auto-detects the installed agent and copies the skill
to the right directory. After installation the agent consults it automatically at the right
moments, or you can invoke it manually: *"run a bluette check before I commit"*.

### Manual installation

Download `oh-my-nino.skill` from the [Releases](../../releases) page:
- **claude.ai / Cowork** → Settings → Capabilities → Skills → upload the `.skill` file
- **Claude Code / filesystem-based agents** → unzip the `oh-my-nino/` folder into your
  skills directory

## Local build

```bash
pip install pyyaml
python scripts/package_skill.py oh-my-nino dist
# -> creates dist/oh-my-nino.skill (evals/ folder is excluded)
```

The script **validates** `SKILL.md` (kebab-case name, description present, no `<`/`>`,
length limits) and fails with a clear error message if anything is wrong.

---

## CI/CD — how to publish a release 🚀

Publishing is automatic: **every push of a `v*` tag creates a new GitHub Release** with
the `.skill` file attached. The workflow is in `.github/workflows/release.yml` and does:
checkout → Python setup → `pip install pyyaml` → validation + packaging → release.

### First-time setup (once only)

1. Create the repo on GitHub and push the code:
   ```bash
   git init
   git add .
   git commit -m "oh-my-nino: skill + CI/CD"
   git branch -M main
   git remote add origin git@github.com:<user>/oh-my-nino.git
   git push -u origin main
   ```
2. Make sure **Actions** are enabled and the token has write permissions:
   **Settings → Actions → General → Workflow permissions → "Read and write permissions"**.
   (The workflow already requests `contents: write`, but if the org default is read-only
   you need to unlock it here.)

### Publishing a release (every time)

Just create and push a tag starting with `v`:

```bash
git tag v1.0.0           # lightweight tag
# or annotated (recommended):
git tag -a v1.0.0 -m "First oh-my-nino release"

git push origin v1.0.0   # <-- this triggers CI/CD
```

To push all tags at once: `git push origin --tags`.

### What happens after the tag push

1. The Action runs (visible in the repo's **Actions** tab).
2. It validates and packages `oh-my-nino/` into `dist/oh-my-nino.skill`.
3. It creates a Release named `oh-my-nino v1.0.0` with auto-generated notes and the
   `.skill` attached as a downloadable asset.

### Updating / redoing a release

Tags are immutable by convention: for a new version use a **new** tag
(`v1.0.1`, `v1.1.0`, ...). If you really need to redo the same tag:

```bash
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0   # delete remote tag
git tag -a v1.0.0 -m "..." && git push origin v1.0.0
```

### If the release doesn't trigger

- The tag **must** start with `v` (the filter is `v*`). A bare `1.0.0` won't fire.
- Did you push the **tag**, not just the commit? (`git push origin v1.0.0`)
- Workflow permissions set to **Read and write** (see setup above).
- Validation error in the Action → read the *"Valida e impacchetta"* step log:
  it tells you exactly what's wrong in `SKILL.md`.

---

*Made with 💙 (yes, blue) for Nino and for everyone who fades every now and then.*
