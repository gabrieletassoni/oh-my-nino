# Come contribuire

## Cosa si può migliorare

- **Nuovi check in `SKILL.md`**: aggiungi pattern pericolosi o sciatti non ancora coperti
  nelle sezioni 🟥/🟧/🟦. Rispetta la proporzione gravità → tono.
- **Nuovi eval in `evals.json`**: ogni nuovo check dovrebbe avere almeno un caso di test.
- **Script di packaging**: estendi le validazioni in `scripts/package_skill.py` se il formato
  del frontmatter evolve.

## Flusso di lavoro

1. Modifica `oh-my-nino/SKILL.md` e/o aggiungi eval in `oh-my-nino/evals/evals.json`.
2. Verifica che il packaging funzioni ancora:
   ```bash
   pip install pyyaml
   python scripts/package_skill.py oh-my-nino dist
   ```
3. Testa manualmente i nuovi eval: sottoponi i prompt a un agente con la skill caricata e
   confronta l'output con le `expectations` nel JSON.
4. Apri una Pull Request con una descrizione sintetica del check aggiunto e del perché.

## Vincoli del frontmatter di SKILL.md

Il packaging rifiuta il file se non rispetta questi limiti (vedi `scripts/package_skill.py`):

| Campo | Regola |
|---|---|
| `name` | kebab-case, max 64 caratteri, no trattini iniziali/finali/doppi |
| `description` | obbligatoria, max 1024 caratteri, no `<` o `>` |

## Tono

La skill è uno scherzo d'ufficio: il tono goliardico è parte integrante del progetto.
I nuovi check devono restare proporzionati — gravità reale → gravità del tono — e non
inventare difetti per fare la battuta. Un falso allarme rompe lo scherzo prima ancora del codice.

## Release

Le release le gestisce il maintainer tramite tag `v*` (vedi README.md § CI/CD).
