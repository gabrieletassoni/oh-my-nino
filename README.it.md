# oh-my-nino 🩵

[🇬🇧 English](README.md) · [🇮🇹 Italiano](README.it.md)

---

Una **skill-scherzo** per le IA di coding, dedicata al collega **Nino**. Tono goliardico,
sostanza seria: ti **rammenta che stai facendo una cosa alla cazzo o che stai per fare una
minchiata** prima che la combini (force push su `main`, `rm -rf` con variabili vuote, SQL
senza `WHERE`, segreti hardcoded, edge case ignorati...).

> Nel modello attitudinale **POLES®** il **blu** è lo stile preciso e metodico. Nino è
> uscito blu. In pratica, ogni tanto sbiadisce in **bluette** — un blu più slavato. Questa
> skill fa la guardia a quel confine. Tutta la lore è in [`oh-my-nino/README.it.md`](oh-my-nino/README.it.md).

## Struttura del repository

```
.
├── README.md                       # versione inglese (panoramica + CI/CD)
├── README.it.md                    # questo file
├── .github/workflows/release.yml   # GitHub Action: pubblica il .skill su tag
├── scripts/package_skill.py        # validazione + packaging in .skill
└── oh-my-nino/                     # LA SKILL (è ciò che viene impacchettato)
    ├── SKILL.md                    # la skill vera e propria
    ├── README.md                   # README della skill in inglese
    ├── README.it.md                # README della skill in italiano
    └── evals/evals.json            # 6 casi di test (esclusi dal pacchetto)
```

## Installazione

### Via npx (metodo consigliato)

Funziona con Claude Code, Cursor, Cline, Copilot e altri 50+ agenti. Richiede solo Node.js:

```bash
npx skills add gabrieletassoni/oh-my-nino
```

Il CLI [skills](https://skills.sh) rileva automaticamente l'agente installato e copia la skill
nella directory giusta. Dopo l'installazione l'agente la consulta da solo nei momenti opportuni,
oppure puoi invocarla a mano: *"fammi un controllo bluette prima che committo"*.

### Installazione manuale

Scarica `oh-my-nino.skill` dalla pagina [Releases](../../releases):
- **claude.ai / Cowork** → Settings → Capabilities → Skills → carica il `.skill`
- **Claude Code / agenti da filesystem** → scompatta la cartella `oh-my-nino/` nella tua
  directory delle skill

## Build in locale

```bash
pip install pyyaml
python scripts/package_skill.py oh-my-nino dist
# -> crea dist/oh-my-nino.skill (la cartella evals/ viene esclusa)
```

Lo script **valida** la `SKILL.md` (name kebab-case, description presente, niente `<`/`>`,
limiti di lunghezza) e fallisce con un errore chiaro se qualcosa non torna.

---

## CI/CD — come far partire una release 🚀

La pubblicazione è automatica: **ogni push di un tag `v*` crea una nuova GitHub Release**
con il file `.skill` allegato. Il workflow è in `.github/workflows/release.yml` e fa:
checkout → setup Python → `pip install pyyaml` → validazione + packaging → release.

### Primo setup (una volta sola)

1. Crea il repo su GitHub e fai push del codice:
   ```bash
   git init
   git add .
   git commit -m "oh-my-nino: skill + CI/CD"
   git branch -M main
   git remote add origin git@github.com:<utente>/oh-my-nino.git
   git push -u origin main
   ```
2. Assicurati che le **Actions** siano abilitate e che il token abbia i permessi di
   scrittura: **Settings → Actions → General → Workflow permissions → "Read and write
   permissions"**. (Il workflow chiede già `contents: write`, ma se il default dell'org è
   read-only va sbloccato qui.)

### Pubblicare una release (ogni volta)

Basta creare e pushare un tag che inizia per `v`:

```bash
git tag v1.0.0           # tag leggero
# oppure annotato (consigliato):
git tag -a v1.0.0 -m "Prima release di oh-my-nino"

git push origin v1.0.0   # <-- questo fa partire il CI/CD
```

Per pushare tutti i tag in un colpo solo: `git push origin --tags`.

### Cosa succede dopo il push del tag

1. La Action parte (la vedi nella tab **Actions** del repo).
2. Valida e impacchetta `oh-my-nino/` in `dist/oh-my-nino.skill`.
3. Crea la Release chiamata `oh-my-nino v1.0.0` con note generate in automatico e il
   `.skill` allegato come asset scaricabile.

### Aggiornare / rifare una release

I tag sono immutabili per convenzione: per una nuova versione usa un **nuovo** tag
(`v1.0.1`, `v1.1.0`, ...). Se proprio devi rifare lo stesso tag:

```bash
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0   # cancella il tag remoto
git tag -a v1.0.0 -m "..." && git push origin v1.0.0
```

### Se la release non parte

- Il tag **deve** iniziare per `v` (il filtro è `v*`). `1.0.0` da solo non scatta.
- Hai pushato il **tag**, non solo il commit? (`git push origin v1.0.0`)
- Workflow permissions impostate su **Read and write** (vedi setup sopra).
- Errore di validazione nella Action → leggi il log dello step *"Valida e impacchetta"*:
  ti dice esattamente cosa non va nella `SKILL.md`.

---

*Made with 💙 (sì, blu) per Nino e per chiunque ogni tanto sbiadisca.*
