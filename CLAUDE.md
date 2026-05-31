# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Cos'è questo progetto

Una skill per agenti AI di coding (Claude Code, Cowork, claude.ai) che esegue un sanity-check prima di azioni pericolose o codice sciatto. È un gioco d'ufficio dedicato al collega Nino (lore POLES®: blu → bluette), ma il controllo è reale e funzionante.

Il cuore del progetto è `oh-my-nino/SKILL.md`: un file Markdown con frontmatter YAML che definisce la skill. Lo script di packaging la valida e la zipa in un `.skill` distribuibile.

## Build

```bash
pip install pyyaml
python scripts/package_skill.py oh-my-nino dist
# → dist/oh-my-nino.skill
```

Lo script valida il frontmatter di `SKILL.md` prima di creare il pacchetto. Se la validazione fallisce, stampa l'errore esatto e termina con exit code 1.

## Release

Il CI/CD pubblica automaticamente su GitHub Releases a ogni push di un tag `v*`:

```bash
git tag -a v1.0.0 -m "descrizione"
git push origin v1.0.0
```

Il tag **deve** iniziare per `v`. Il workflow (`.github/workflows/release.yml`) fa: checkout → Python 3.12 → `pip install pyyaml` → packaging → creazione Release con il `.skill` allegato.

Per rifare un tag esistente: cancellarlo in locale e in remoto, poi ricreare.

## Architettura

**`oh-my-nino/SKILL.md`** — la skill vera e propria. Struttura:
- Frontmatter YAML (`name`, `description`) — il `description` funge da trigger automatico: l'agente la consulta da solo quando lo scenario corrisponde
- Corpo Markdown con: lore/contesto, tre livelli di severità (🟥/🟧/🟦), il Bluette-meter (⚪/🩵/🔵), formato output fisso, regole d'ingaggio

**`scripts/package_skill.py`** — validazione + zip. Vincoli sul frontmatter:
- `name`: kebab-case, max 64 caratteri, no trattini iniziali/finali/doppi
- `description`: obbligatoria, max 1024 caratteri, no `<` o `>`
- Esclusi dal pacchetto: `evals/`, `__pycache__/`, `.git`, `*.pyc`, `.DS_Store`

**`oh-my-nino/evals/evals.json`** — 6 casi di test con prompt, output atteso e liste di `expectations`. Non finisce nel `.skill`. Copre i tre verdetti: ⚪ Sbiadito (test 1, 4, 6), 🩵 Bluette (test 2, 5), 🔵 Blu pieno (test 3).

## Convenzioni della skill

Il blocco di output della skill ha un formato fisso — non cambiarlo:
```
🩵 CONTROLLO BLUETTE
Verdetto: <Blu pieno | Bluette | Sbiadito>
Nino, <una/tre righe>
Per tornare blu: <azione concreta>
```
Per il verdetto "Blu pieno" basta: `🔵 Tutto blu, Nino. Procedi pure.`

Tono: goliardico ma proporzionato alla gravità reale. Nessun falso allarme per fare la battuta.

## Lingua della documentazione

Tutta la documentazione rivolta agli utenti va scritta **sia in inglese che in italiano**:
- `README.md` → inglese (primario, target sviluppatori internazionali)
- `README.it.md` → italiano (stessa cartella del README inglese)

Questo vale per ogni cartella che contiene un README (es. `oh-my-nino/`). La convenzione è
`README.md` (EN, primario) + `README.it.md` (IT), con badge di navigazione in cima a entrambi:

```markdown
[🇬🇧 English](README.md) · [🇮🇹 Italiano](README.it.md)
```

I file tecnici interni (SKILL.md, CLAUDE.md, CONTRIBUTING.md, CHANGELOG.md) restano in italiano
in quanto rivolti al team di sviluppo.

## File del progetto

| File | Scopo |
|---|---|
| `oh-my-nino/SKILL.md` | La skill (frontmatter YAML + logica in Markdown) |
| `oh-my-nino/evals/evals.json` | Casi di test — esclusi dal `.skill` |
| `scripts/package_skill.py` | Validazione frontmatter + creazione `.skill` |
| `.github/workflows/release.yml` | CI/CD: tag `v*` → GitHub Release |
| `README.md` / `README.it.md` | Documentazione radice EN/IT |
| `oh-my-nino/README.md` / `oh-my-nino/README.it.md` | Documentazione skill EN/IT |
| `CHANGELOG.md` | Storia delle versioni (Keep a Changelog) |
| `CONTRIBUTING.md` | Come aggiungere check, eval e rilasciare |
| `LICENSE` | MIT |
