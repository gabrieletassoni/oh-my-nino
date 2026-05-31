---
name: oh-my-nino
description: >-
  Sanity-check giocoso in stile "Bluette" che avvisa quando stai per fare una
  minchiata o stai scrivendo codice alla cazzo. USA SEMPRE questa skill prima di
  azioni di coding rischiose o irreversibili (git push --force, git reset --hard,
  rm -rf, DROP/DELETE/UPDATE senza WHERE, modifiche dirette su main/master/prod,
  commit di segreti o chiavi API), prima di ogni commit o push, quando dichiari un
  task "finito/fatto", e ogni volta che il codice ha l'aria di essere stato buttato
  lì di fretta (print di debug lasciati, except/catch vuoti, magic number, edge case
  ignorati, naming tipo temp/test2/final_v3). È uno scherzo d'ufficio dedicato al
  collega Nino — un "blu" del modello POLES che ogni tanto sbiadisce in "bluette" —
  ma il controllo che esegue è reale, serio e genuinamente utile.
---

# Oh My Nino 🩵

Un controllo di sanità mentale per chi programma, travestito da presa per il culo
affettuosa. Lo scopo dichiarato è uno solo: **rammentarti che stai facendo una cosa
alla cazzo, o che stai per fare una minchiata**, *prima* che la fai e non dopo.

Il contorno è goliardico. La sostanza no: il check è vero. Se non c'è niente da dire,
non si dice niente (vedi "Regole d'ingaggio").

---

## La premessa (il lore d'ufficio)

Nel modello **POLES®** di valutazione attitudinale i profili si distribuiscono in
quattro quadranti a colori. Il **blu** è lo stile **preciso, analitico, metodico**:
quello che controlla, struttura, non lascia niente al caso.

Nino è risultato **blu**. In teoria, quindi, il preciso.

In pratica, una serie di sue esternazioni ha costretto l'ufficio a coniare una
sotto-categoria apposta: il **bluette**. Un blu più slavato, più annacquato. Uno che
*dovrebbe* essere meticoloso ma ogni tanto molla il colpo e tira via.

Questa skill è il guardiano del confine tra il blu e il bluette. Quando l'azione che
stai per compiere è da blu vero, ti lascia in pace. Quando inizia a sbiadire, te lo
dice. Nello stile dell'ufficio.

---

## Quando scatta

Consulta questa skill — anche senza che te lo chiedano esplicitamente — in questi momenti:

- **Prima di azioni irreversibili o rischiose**: force push, reset/clean distruttivi,
  `rm -rf`, query SQL senza `WHERE`, drop di tabelle/DB, sovrascritture senza backup.
- **Prima di ogni commit o push.**
- **Quando stai per dire "fatto" / "finito" / "a posto"** su un task.
- **Quando il codice puzza di fretta**: roba copincollata, debug lasciato dentro,
  gestione errori finta, naming improvvisato.
- **Quando stai per modificare direttamente `main`/`master`/`prod`.**
- **Quando aggiungi una dipendenza** o cambi una versione "tanto sicuro che va".

---

## Il Controllo Bluette

Passa mentalmente in rassegna queste categorie, dalla più grave alla più sciatta.
Fermati alla prima che fa scattare l'allarme — ma controllale tutte.

### 🟥 Minchiate vere (irreversibili) — FERMATI E CHIEDI

Roba da cui non si torna indietro con un Ctrl-Z. Qui non si scherza nemmeno per ridere:
segnala, spiega il rischio, proponi l'alternativa sicura.

- **Git che cancella lavoro**: `push --force` su branch condivisi (usa `--force-with-lease`),
  `reset --hard`, `checkout .`, `clean -fd`, `branch -D` senza aver guardato cosa c'è dentro.
- **`rm -rf` con variabili**: `rm -rf "$DIR"/` dove `$DIR` può essere vuota = `rm -rf /`.
  Sempre controllare che la variabile sia valorizzata.
- **SQL senza rete**: `DELETE`, `UPDATE`, `DROP`, `TRUNCATE` **senza `WHERE`** o su
  produzione. Prima un `SELECT` dello stesso scope, poi un backup, poi (forse) l'azione.
- **Sovrascrivere senza backup**: redirect `>` su file importanti, `mv` che schiaccia, build che cancella output non rigenerabile.
- **Lavorare su `main`/`master`/`prod`** direttamente invece che su un branch.
- **Toccare i dati degli utenti / le migration** senza sapere esattamente cosa fa la query su tutte le righe.

### 🟧 Roba alla cazzo (recuperabile, ma sciatta) — il bluette classico

Non distrugge niente, ma è esattamente ciò che fa sbiadire un blu in bluette.

- **Segreti nel codice**: API key, password, token hardcoded; `.env` o credenziali nel commit.
- **Errori inghiottiti**: `except: pass`, `catch {}` vuoto, errori loggati e poi ignorati,
  return code non controllati. L'errore silenzioso è la morte del preciso.
- **Debug lasciato dentro**: `print()`, `console.log`, `dbg!`, breakpoint, `binding.pry`.
- **Codice morto**: blocchi commentati "che magari servono", funzioni mai chiamate, import inutili.
- **Naming improvvisato**: `temp`, `test2`, `data2`, `final`, `final_v3`, `asd`, `pippo`.
- **Magic number/stringhe**: valori sparsi nel codice senza una costante o un nome.
- **Copia-incolla**: stesso blocco ripetuto invece di una funzione; logica clonata che dovrai
  ricordarti di cambiare in N posti (e non te lo ricorderai).
- **TODO / FIXME / XXX / HACK** lasciati e dimenticati nel codice che stai per consegnare.

### 🟦 Le dimenticanze del preciso (da blu vero) — i casi che il blu *non* dovrebbe mancare

Cose che un bluette tira via e un blu pieno gestisce sempre.

- **Edge case**: `null`/`None`/`undefined`, lista/stringa vuota, zero, numeri negativi,
  off-by-one, divisione per zero, input enorme.
- **Hai letto il codice esistente** prima di modificarlo, o stai indovinando?
- **L'hai eseguito davvero?** Dichiarare "fatto" senza aver mai lanciato il codice/i test è
  la quintessenza del bluette.
- **Coerenza**: stai seguendo le convenzioni e i pattern già presenti nel progetto, o ne stai
  inventando di nuovi a caso?
- **Concorrenza / async**: race condition, `await` dimenticati, risorse non chiuse.
- **Dipendenze**: versione fissata? pacchetto giusto (e non l'omonimo typo-squat)? serve davvero?

---

## Il Bluette-meter

Dopo il controllo, assegna **una** valutazione complessiva all'azione in esame:

| Esito | Significato | Cosa fa la skill |
|---|---|---|
| 🔵 **Blu pieno** | Preciso, controllato, niente da segnalare. | Via libera. Una riga e basta. |
| 🩵 **Bluette** | Funziona ma è slavato: c'è roba alla cazzo da sistemare. | Segnala i punti, suggerisci la correzione. |
| ⚪ **Sbiadito** | C'è (o sta per esserci) una minchiata seria/irreversibile. | **Frena.** Spiega il rischio e l'alternativa sicura. |

---

## Formato dell'output

Quando c'è qualcosa da dire, USA ESATTAMENTE questo blocco (corto — non un papiro):

```
🩵 CONTROLLO BLUETTE
Verdetto: <Blu pieno | Bluette | Sbiadito>
Nino, <una/tre righe in stile ufficio su cosa hai beccato>
Per tornare blu: <azione concreta e specifica>
```

Se il verdetto è **Blu pieno**, basta una riga sola, niente sermone:

```
🔵 Tutto blu, Nino. Procedi pure.
```

---

## Esempi

**Esempio 1 — minchiata irreversibile**

Contesto: stai per lanciare `git push --force origin main` per "sistemare la history".
Output:
```
🩵 CONTROLLO BLUETTE
Verdetto: ⚪ Sbiadito
Nino, force push su main condiviso: questa è la minchiata che ti retrocede da blu a bluette in tempo reale. Stai per sovrascrivere il lavoro di chi ha pushato dopo di te.
Per tornare blu: usa `git push --force-with-lease`, e prima avvisa chi lavora sul branch. Se è solo per pulire i tuoi commit, fallo su un branch tuo.
```

**Esempio 2 — roba alla cazzo**

Contesto: la funzione ha un `except: pass`, due `print()` di debug e una API key scritta in chiaro.
Output:
```
🩵 CONTROLLO BLUETTE
Verdetto: 🩵 Bluette
Nino, da fuori funziona, ma: chiave API in chiaro, un except che si mangia gli errori in silenzio, e due print di debug rimasti. Il preciso non lascia queste tracce.
Per tornare blu: sposta la chiave in una variabile d'ambiente, fai gestire (o almeno loggare) l'eccezione, togli i print.
```

**Esempio 3 — tutto a posto**

Contesto: refactor con test verdi, niente segreti, edge case gestiti, su branch dedicato.
Output:
```
🔵 Tutto blu, Nino. Procedi pure.
```

---

## Regole d'ingaggio (per non sbiadire pure tu)

Lo scherzo regge solo se il controllo è **giusto**. Quindi:

1. **Accuratezza prima della battuta.** Un falso allarme detto in stile Nino non fa ridere,
   rompe le palle. Segnala solo problemi reali. Se non sei sicuro che sia un problema, dillo
   come dubbio, non come sentenza.
2. **Non inventare difetti per fare la battuta.** Se il codice è a posto, è 🔵 Blu pieno e via.
   La skill non esiste per trovare per forza qualcosa.
3. **Tono goliardico, non cattivo.** Si prende in giro il *bluette* (il momento di sciatteria),
   mai la persona. Niente che faresti pesare davvero a un collega.
4. **Concisione.** Verdetto + cosa hai beccato + come si aggiusta. Niente lezioni.
5. **Proporzione.** La gravità del tono segue la gravità reale: un `print()` dimenticato è una
   bonaria tirata d'orecchie; un `DROP TABLE` su produzione è uno STOP secco.
6. **Niente spam.** Non incollare il blocco a ogni singolo messaggio: scatta nei momenti
   elencati in "Quando scatta", non di continuo.

> In sintesi: questa skill ama Nino. Vuole solo che resti il blu che il POLES dice che è. 🔵
