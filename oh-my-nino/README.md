# oh-my-nino 🩵

> Una skill-scherzo per Nino. Goliardica nel tono, seria nella sostanza.

## Cos'è (e cosa NON è)

`oh-my-nino` è una skill pensata per le IA di coding (Claude Code, Cowork, agenti vari)
che fa una cosa sola: **ti rammenta che stai facendo una cosa alla cazzo o che stai per
fare una minchiata** — prima che la combini.

È, dichiaratamente, **uno scherzo d'ufficio** dedicato al collega **Nino**. Ma sotto la
presa per il culo c'è un controllo vero: un sanity-check su operazioni pericolose,
codice sciatto ed errori classici. Quindi sì, è una skill funzionante a tutti gli
effetti, non un giocattolo vuoto.

**Importante**: nessuna offesa, nessuna cattiveria. Si prende in giro il *momento di
sciatteria*, non la persona. Nino, se stai leggendo: ti vogliamo bene. È che ogni tanto
sbiadisci. 💙

## Il lore (perché "bluette"?)

Nel modello attitudinale **POLES®** (automaticforms.it/poles-model) i profili si
dividono in quadranti a colori. Il **blu** è lo stile **preciso, analitico, metodico**.

Nino è uscito **blu**. In teoria: il meticoloso della situazione.

In pratica, dopo una collezione memorabile di sue esternazioni, l'ufficio ha dovuto
istituire una categoria nuova di zecca: il **bluette**. Cioè un blu più *slavato*, più
*annacquato*. Uno che dovrebbe controllare tutto e invece, ogni tanto, tira via.

Questa skill fa la guardia al confine tra **blu** e **bluette**. Niente di personale:
è scienza POLES applicata. 🧪

## Cosa controlla davvero

Tre livelli di severità, con tono proporzionato alla gravità reale:

- 🟥 **Minchiate vere (irreversibili)** → STOP. Force push su main, `rm -rf` con variabili
  vuote, SQL senza `WHERE`, drop/truncate, lavoro diretto su prod, sovrascritture senza backup.
- 🟧 **Roba alla cazzo (recuperabile)** → il bluette classico. Segreti hardcoded, `except: pass`,
  debug lasciato dentro, magic number, copia-incolla, naming tipo `final_v3`.
- 🟦 **Dimenticanze del preciso** → edge case ignorati, codice non letto/non eseguito,
  convenzioni del progetto saltate.

E un verdetto finale sul **Bluette-meter**: 🔵 Blu pieno · 🩵 Bluette · ⚪ Sbiadito.

## Come si usa

1. Copia la cartella `oh-my-nino/` (con dentro `SKILL.md`) dove il tuo agente cerca le skill.
   - **Claude Code / agenti con skill da filesystem**: nella tua directory delle skill.
   - **Claude.ai / Cowork**: caricala come skill / impacchettala in un file `.skill`.
2. Da lì l'agente la consulta **da solo** nei momenti giusti (prima di un push, di un'azione
   distruttiva, quando dichiara "fatto", ecc.), grazie alla `description`.
3. Puoi anche invocarla a mano: *"fammi un controllo bluette prima che committo"*.

## Cosa aspettarsi come output

Quando c'è qualcosa da dire:

```
🩵 CONTROLLO BLUETTE
Verdetto: Bluette
Nino, da fuori funziona, ma hai una API key in chiaro e un except che si mangia gli errori.
Per tornare blu: sposta la chiave in una variabile d'ambiente e gestisci l'eccezione.
```

Quando è tutto a posto:

```
🔵 Tutto blu, Nino. Procedi pure.
```

## La regola d'oro

Lo scherzo regge **solo se il controllo è giusto**. La skill non inventa difetti per fare
la battuta: se il codice è pulito, dice 🔵 e ti lascia in pace. Un falso allarme in stile
Nino non fa ridere — rompe le palle. Accuratezza prima della comicità, sempre.

## Files

- `SKILL.md` — la skill vera e propria, funzionante. È lì che c'è tutta la logica.
- `README.md` — questo file, per spiegare il tono e zittire chi si offende. 😄

---

*Made with 💙 (sì, blu) per Nino e per chiunque ogni tanto sbiadisca. Capita a tutti.*
