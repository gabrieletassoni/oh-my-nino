# oh-my-nino 🩵

[🇬🇧 English](README.md) · [🇮🇹 Italiano](README.it.md)

---

> A joke skill for Nino. Playful in tone, serious in substance.

## What it is (and what it's NOT)

`oh-my-nino` is a skill designed for AI coding assistants (Claude Code, Cowork, and
others) that does one thing: **reminds you that you're doing something sloppy or are
about to make a serious blunder** — before you actually do it.

It is, explicitly, **an office joke** dedicated to colleague **Nino**. But behind the
ribbing there's a real check: a sanity-check on dangerous operations, sloppy code, and
classic mistakes. So yes, it's a fully functional skill, not an empty toy.

**Important**: no offence, no malice. It mocks the *moment of sloppiness*, not the
person. Nino, if you're reading this: we love you. It's just that you fade sometimes. 💙

## The lore (why "bluette"?)

In the **POLES®** behavioural assessment model (automaticforms.it/poles-model) profiles
are distributed across four colour quadrants. **Blue** is the **precise, analytical,
methodical** style.

Nino scored **blue**. In theory: the meticulous one.

In practice, after a memorable collection of his remarks, the office had to coin a
brand-new sub-category: **bluette**. That is, a more *washed-out*, more *watered-down*
blue. Someone who should check everything but every now and then just cuts corners.

This skill guards the boundary between **blue** and **bluette**. Nothing personal:
it's applied POLES science. 🧪

## What it actually checks

Three severity levels, with tone proportional to actual gravity:

- 🟥 **Real blunders (irreversible)** → STOP. Force push on main, `rm -rf` with empty
  variables, SQL without `WHERE`, drop/truncate, working directly on prod, overwrites
  without backup.
- 🟧 **Half-assed stuff (recoverable)** → classic bluette. Hardcoded secrets,
  `except: pass`, debug left in, magic numbers, copy-paste, naming like `final_v3`.
- 🟦 **Oversights of the precise** → ignored edge cases, unread/unrun code, project
  conventions skipped.

And a final verdict on the **Bluette-meter**: 🔵 Full blue · 🩵 Bluette · ⚪ Faded.

## How to use it

1. Copy the `oh-my-nino/` folder (containing `SKILL.md`) where your agent looks for skills.
   - **Claude Code / filesystem-based agents**: into your skills directory.
   - **Claude.ai / Cowork**: upload it as a skill / package it into a `.skill` file.
2. The agent will consult it **automatically** at the right moments (before a push, a
   destructive action, when declaring "done", etc.), thanks to the `description`.
3. You can also invoke it manually: *"run a bluette check before I commit"*.

## What to expect as output

When there's something to flag:

```
🩵 CONTROLLO BLUETTE
Verdetto: Bluette
Nino, it works on the surface, but you have an API key in plaintext and an except that
swallows errors silently.
Per tornare blu: move the key to an environment variable and handle the exception.
```

When everything is fine:

```
🔵 Tutto blu, Nino. Procedi pure.
```

## The golden rule

The joke only holds **if the check is accurate**. The skill doesn't invent flaws to make
a quip: if the code is clean, it says 🔵 and leaves you alone. A false alarm in Nino's
style isn't funny — it's annoying. Accuracy before comedy, always.

## Files

- `SKILL.md` — the actual working skill. All the logic lives there.
- `README.md` — this file, to explain the tone and silence anyone who takes offence. 😄
- `README.it.md` — Italian version of this file.

---

*Made with 💙 (yes, blue) for Nino and for everyone who fades every now and then. It happens to all of us.*
