# Contributing

## What can be improved

- **New checks in `SKILL.md`**: add dangerous or sloppy patterns not yet covered in the
  🟥/🟧/🟦 sections. Keep the severity → tone proportion consistent.
- **New evals in `evals.json`**: every new check should have at least one test case.
- **Packaging script**: extend validations in `scripts/package_skill.py` if the
  frontmatter format evolves.

## Workflow

1. Edit `oh-my-nino/SKILL.md` and/or add evals in `oh-my-nino/evals/evals.json`.
2. Verify the packaging still works:
   ```bash
   pip install pyyaml
   python scripts/package_skill.py oh-my-nino dist
   ```
3. Manually test new evals: submit the prompts to an agent with the skill loaded and
   compare the output against the `expectations` in the JSON.
4. Open a Pull Request with a concise description of the check added and why.

## SKILL.md frontmatter constraints

The packaging script rejects the file if it doesn't meet these limits
(see `scripts/package_skill.py`):

| Field | Rule |
|---|---|
| `name` | kebab-case, max 64 characters, no leading/trailing/double hyphens |
| `description` | required, max 1024 characters, no `<` or `>` |

## Tone

The skill is an office joke: the playful tone is a core part of the project.
New checks must remain proportional — real severity → tone severity — and must not
invent flaws just to make a quip. A false alarm breaks the joke before it breaks the code.

## Releases

Releases are managed by the maintainer via `v*` tags (see README.md § CI/CD).
