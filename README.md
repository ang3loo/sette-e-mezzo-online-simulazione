- Il valore della matta viene scelto automaticamente per **massimizzare il punteggio senza sballare**

---

## Obiettivo del gioco

Raggiungere **7,5 punti** o avvicinarsi il più possibile **senza superarlo**.

- Se un giocatore supera **7,5**, **sballa** e perde immediatamente.

---

## Svolgimento della partita

### 1️⃣ Fase iniziale (obbligatoria)

1. Il mazziere distribuisce:
 - 1 carta scoperta al **giocatore**
 - 1 carta scoperta a sé stesso

2. Si confrontano i valori iniziali:
 - Se `valore_giocatore > valore_mazziere`  
   → si passa alla fase di gioco normale
 - Se `valore_giocatore ≤ valore_mazziere`:
   - il **giocatore pesca carte forzatamente**
   - finché:
     - supera il valore del mazziere **oppure**
     - **sballa**
   - Se il giocatore sballa in questa fase → **il mazziere vince immediatamente**

---

### 2️⃣ Turno del giocatore

Il giocatore può:
- **Chiedere carta**
- **Stare**

Regole:
- Se supera **7,5**, sballa e **perde subito**
- Può decidere liberamente quando fermarsi

---

### 3️⃣ Turno del mazziere (robot)

Il mazziere gioca **solo se il giocatore non è sballato**.

Comportamento automatico:
- Pesca carte finché il suo valore è **strettamente minore di 5**
- Quando raggiunge un valore **≥ 5**, si ferma
- Può sballare

---

## Determinazione del vincitore

- Se il giocatore sballa → **vince il mazziere**
- Se il mazziere sballa → **vince il giocatore**
- Altrimenti:
- vince chi è **più vicino a 7,5**
- **in caso di pareggio, vince il mazziere**

---

## 7 e Mezzo Royal

- Si verifica quando il giocatore ottiene **7,5 con esattamente 2 carte**
- Paga **3:2**
- Vale solo se il giocatore **non sballa**
- Non modifica le normali regole di confronto con il mazziere

---

## Note di implementazione

- Ogni partita è **indipendente**
- Non esiste memoria tra una partita e l’altra
- Il progetto è strutturato in **classi separate**:
- Carta
- Mazzo
- Giocatore
- Mazziere
- Gioco
- La logica del gioco è separata da output e statistiche

---

## Possibili estensioni future

- Strategie diverse del giocatore
- Strategie alternative del mazziere
- Statistiche e simulazioni Monte Carlo
- Interfaccia grafica o web
- Supporto a più giocatori
