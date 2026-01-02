from game.gioco import Gioco
from excel_writer import scrivi_statistiche_excel


# -----------------------------
# Parametri simulazione
# -----------------------------
NUM_PARTITE = 10
NUM_SIMULAZIONI = 1
SOGLIA_GIOCATORE = 3.5
file_excel = f"statistiche simulazioni {NUM_PARTITE}.xlsx"


# -----------------------------
# Strategia del giocatore
# -----------------------------
def strategia_automatica(giocatore):
    """Pesca se valore < SOGLIA_GIOCATORE, altrimenti sta"""
    if giocatore.valore() < SOGLIA_GIOCATORE:
        return "carta"
    return "stai"

def strategia_giocatore_reale(giocatore):
    print(giocatore)  # mostra la mano e il valore attuale
    decisione = input("Vuoi carta(c) o stare(s)? ").strip().lower()

    if decisione == "c":
        return "carta"
    return "stai"




def simula_partite(strategia):
    # -----------------------------
    # Variabili statistiche
    # -----------------------------
    vittorie_giocatore = 0
    vittorie_mazziere = 0
    pareggi = 0
    sballi_giocatore = 0
    sballi_mazziere = 0
    somma_valore_giocatore = 0
    somma_valore_mazziere = 0
    somma_carte_giocatore = 0
    guadagno_totale = 0

    # -----------------------------
    # Simulazione partite
    # -----------------------------
    for _ in range(NUM_PARTITE):
        gioco = Gioco()
        gioco.fase_iniziale()
        gioco.turno_giocatore(strategia=strategia)
        gioco.turno_mazziere()

        g_val = gioco.giocatore.valore()
        m_val = gioco.mazziere.valore()
        royal = False

        # Controllo 7.5 royal: solo due carte
        if len(gioco.giocatore.mano) == 2 and g_val == 7.5:
            royal = True

        # -----------------------------
        # Calcolo vincitore e guadagno
        # -----------------------------
        if gioco.giocatore.sballato():
            guadagno_totale -= 1
            sballi_giocatore += 1
            vittorie_mazziere += 1

        elif royal:
            guadagno_totale += 1.5
            vittorie_giocatore += 1

        elif gioco.mazziere.sballato():
            guadagno_totale += 1
            sballi_mazziere += 1
            vittorie_giocatore += 1

        elif g_val > m_val:
            guadagno_totale += 1
            vittorie_giocatore += 1

        elif g_val < m_val:
            guadagno_totale -= 1
            vittorie_mazziere += 1

        else:
            # pareggio normale → vince mazziere
            guadagno_totale -= 1
            pareggi += 1
            vittorie_mazziere += 1

        # -----------------------------
        # Somme valori e carte
        # -----------------------------
        somma_valore_giocatore += g_val
        somma_valore_mazziere += m_val
        somma_carte_giocatore += len(gioco.giocatore.mano)

    # -----------------------------
    # Statistiche finali
    # -----------------------------
    valore_medio_giocatore = round(somma_valore_giocatore / NUM_PARTITE, 2)
    valore_medio_mazziere = round(somma_valore_mazziere / NUM_PARTITE, 2)
    carte_medie = round(somma_carte_giocatore / NUM_PARTITE, 2)
    guadagno_medio = round(guadagno_totale / NUM_PARTITE, 2)

    print("---- STATISTICHE ----")
    print(f"Partite giocate: {NUM_PARTITE}")
    print(f"Vittorie Giocatore: {vittorie_giocatore}")
    print(f"Vittorie Mazziere: {vittorie_mazziere}")
    print(f"Pareggi: {pareggi}")
    print(f"Sballi Giocatore: {sballi_giocatore}")
    print(f"Sballi Mazziere: {sballi_mazziere}")
    print(f"Valore medio Giocatore: {valore_medio_giocatore}")
    print(f"Valore medio Mazziere: {valore_medio_mazziere}")
    print(f"Numero medio carte pescate dal Giocatore: {carte_medie}")
    print(f"Guadagno totale (ipotetici $): {guadagno_totale}")
    print(f"Guadagno medio per partita: {guadagno_medio}$")

    # -----------------------------
    # Scrittura su Excel
    # -----------------------------
    dati_excel = {
        "Vittorie Giocatore": vittorie_giocatore,
        "Vittorie Mazziere": vittorie_mazziere,
        "Pareggi": pareggi,
        "Sballi Giocatore": sballi_giocatore,
        "Sballi Mazziere": sballi_mazziere,
        "Valore medio Giocatore": valore_medio_giocatore,
        "Valore medio Mazziere": valore_medio_mazziere,
        "Carte medie pescate": carte_medie,
        "Guadagno totale ($)": guadagno_totale,
        "Guadagno medio ($)": guadagno_medio
    }

    # Scrivi o aggiorna Excel senza sovrascrivere
    scrivi_statistiche_excel(file_excel, SOGLIA_GIOCATORE, dati_excel)

if __name__ == "__main__":
    STRATEGIA = strategia_automatica
    selezione = int(input("Seleziona la modalità di gioco:\n0. gioco con strategia automatica\n1. giochi tu\nScelta:"))
    if selezione == 1:
        STRATEGIA = strategia_giocatore_reale
    for _ in range(NUM_SIMULAZIONI):
        simula_partite(STRATEGIA)