#!/usr/bin/env python3
"""
Packager per la skill oh-my-nino.

Valida la SKILL.md e crea il file `.skill` (uno zip con dentro la cartella della
skill), pronto per essere pubblicato come GitHub Release o installato a mano.
La cartella `evals/` e gli artefatti di build vengono esclusi dal pacchetto.

Uso:
    python scripts/package_skill.py <cartella-skill> [cartella-output]

Esempi:
    python scripts/package_skill.py oh-my-nino
    python scripts/package_skill.py oh-my-nino dist

Dipendenze: PyYAML  ->  pip install pyyaml
"""

import re
import sys
from fnmatch import fnmatch
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

try:
    import yaml
except ImportError:
    print("❌ Manca PyYAML. Installa con:  pip install pyyaml")
    sys.exit(1)

# Cosa NON deve mai finire nel .skill
EXCLUDE_DIR_NAMES = {"evals", "__pycache__", ".git", "node_modules"}
EXCLUDE_GLOBS = ("*.pyc", "*.skill")
EXCLUDE_FILES = {".DS_Store"}


def fail(msg: str) -> None:
    print(f"❌ {msg}")
    sys.exit(1)


def validate(skill_dir: Path) -> str:
    """Valida il frontmatter della SKILL.md e ritorna il name della skill."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"SKILL.md non trovato in {skill_dir}")

    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        fail("Frontmatter YAML non trovato (manca il blocco --- ... ---)")

    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        fail(f"Frontmatter YAML non valido: {e}")

    if not isinstance(fm, dict):
        fail("Il frontmatter non e' un dizionario YAML")

    name = str(fm.get("name", "")).strip()
    desc = str(fm.get("description", "")).strip()

    if not name:
        fail("Manca 'name' nel frontmatter")
    if not re.match(r"^[a-z0-9-]+$", name) or name.startswith("-") or name.endswith("-") or "--" in name:
        fail(f"'name' deve essere kebab-case (a-z, 0-9, trattini): {name!r}")
    if len(name) > 64:
        fail(f"'name' troppo lungo ({len(name)}, max 64)")
    if not desc:
        fail("Manca 'description' nel frontmatter")
    if "<" in desc or ">" in desc:
        fail("La description non puo' contenere < o >")
    if len(desc) > 1024:
        fail(f"description troppo lunga ({len(desc)}, max 1024)")

    print(f"✅ SKILL.md valida  ·  name: {name}  ·  description: {len(desc)} caratteri")
    return name


def should_exclude(rel: Path) -> bool:
    if any(part in EXCLUDE_DIR_NAMES for part in rel.parts):
        return True
    if rel.name in EXCLUDE_FILES:
        return True
    return any(fnmatch(rel.name, g) for g in EXCLUDE_GLOBS)


def package(skill_dir: Path, out_dir: Path, name: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{name}.skill"
    if out.exists():
        out.unlink()

    added = 0
    with ZipFile(out, "w", ZIP_DEFLATED) as z:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_dir():
                continue
            rel = f.relative_to(skill_dir)
            if should_exclude(rel):
                print(f"  · escluso: {rel}")
                continue
            arcname = f"{name}/{rel.as_posix()}"
            z.write(f, arcname=arcname)
            print(f"  + {arcname}")
            added += 1

    if added == 0:
        fail("Nessun file da impacchettare")
    print(f"✅ Creato {out}  ({added} file)")
    return out


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    skill_dir = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path.cwd()
    if not skill_dir.is_dir():
        fail(f"Cartella skill non trovata: {skill_dir}")
    name = validate(skill_dir)
    package(skill_dir, out_dir, name)


if __name__ == "__main__":
    main()
