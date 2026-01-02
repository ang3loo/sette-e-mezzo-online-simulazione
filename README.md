# Simulatore Gioco 7.5 Online

## Descrizione

Questo progetto è un simulatore del gioco **Sette e Mezzo** online.  
Permette di simulare molte partite tra un giocatore e il mazziere, raccogliendo statistiche utili per analizzare strategie, probabilità di vincita e guadagni medi.

Il simulatore è utile per:
- Testare diverse strategie del giocatore.
- Valutare statisticamente il comportamento del mazziere.
- Misurare guadagno o perdita media in scenari ripetuti.

---

## Come funziona

1. **Configurazione**
   - Impostare in `main.py`:
     - `NUM_PARTITE`: quante partite simulare per run.
     - `NUM_SIMULAZIONI`: quante simulazioni consecutive eseguire.
     - `SOGLIA_GIOCATORE`: soglia sotto cui il giocatore pesca carta.

2. **Simulazione**
   - Ogni partita utilizza un **mazzo nuovo e mischiato**.
   - Il giocatore può essere controllato in due modi:
     - **Simulazione automatica**: il giocatore decide secondo una strategia predefinita, come `strategia_prova`.
     - **Giocatore reale**: usando `strategia_giocatore_reale`, il programma chiede all’utente ogni volta se vuole pescare carta o stare.
   - Il mazziere gioca automaticamente seguendo le regole del gioco online.
   - Si calcola il vincitore considerando 7.5 royal, sballi e pareggi.

3. **Raccolta statistiche**
   - Vittorie di giocatore e mazziere
   - Pareggi
   - Sballi
   - Valore medio delle mani
   - Carte medie pescate
   - Guadagno totale e medio (ipotetico $)

4. **Output**
   - Console: stampa le statistiche della simulazione corrente.
   - Excel: salva i dati in **“statistiche simulazioni 50.xlsx”**, aggiungendo ogni simulazione come nuova riga senza sovrascrivere le precedenti.

---

## Struttura del progetto

- `carta.py` → definisce le carte del mazzo.  
- `mazzo.py` → gestisce il mazzo e la pesca delle carte.  
- `giocatore.py` → gestisce la mano e il punteggio del giocatore.  
- `mazziere.py` → estende Giocatore con le regole del mazziere.  
- `gioco.py` → coordina la partita, distribuendo carte e determinando il vincitore.  
- `excel_writer.py` → salva i risultati delle simulazioni in Excel.  
- `main.py` → esegue le simulazioni, calcola le statistiche e le scrive su Excel.

---

## Scopo

Il programma serve per **analizzare statisticamente il gioco 7.5 online**, valutare strategie, guadagni e perdite medie, e studiare il comportamento del mazziere in simulazioni ripetute.
