from .mazzo import Mazzo
from .giocatore import Giocatore
from .mazziere import Mazziere

class Gioco:
    """
    Gestisce una partita completa di Sette e Mezzo tra un giocatore e il mazziere.
    Include:
    - Fase iniziale
    - Turno del giocatore
    - Turno del mazziere
    - Determinazione del vincitore
    """

    def __init__(self):
        self.mazzo = Mazzo()
        self.giocatore = Giocatore("Giocatore")
        self.mazziere = Mazziere("Mazziere")

    def fase_iniziale(self):
        """
        Distribuisce una carta al giocatore e al mazziere.
        Gestisce la regola:
        - Se giocatore <= mazziere, il giocatore pesca carte finché supera il mazziere
        """
        # Pesca iniziale
        self.giocatore.pesca(self.mazzo.pesca())
        self.mazziere.pesca(self.mazzo.pesca())

        # Controllo iniziale
        while self.giocatore.valore() <= self.mazziere.valore():
            # Pesca carte finché il giocatore supera il mazziere o sballa
            self.giocatore.pesca(self.mazzo.pesca())
            if self.giocatore.sballato():
                break

    def turno_giocatore(self, strategia=None):
        """
        Turno del giocatore.
        'strategia' è una funzione che decide se chiedere carta o stare.
        Se non viene passata, il giocatore si ferma subito.
        """
        if self.giocatore.sballato():
            return

        while True:
            if strategia:
                decisione = strategia(self.giocatore)
            else:
                decisione = "stai"  # default

            if decisione == "stai":
                break
            elif decisione == "carta":
                self.giocatore.pesca(self.mazzo.pesca())
                if self.giocatore.sballato():
                    break

    def turno_mazziere(self):
        """
        Il mazziere gioca automaticamente.
        Non gioca se il giocatore ha sballato.
        """
        self.mazziere.gioca_turno(self.mazzo, self.giocatore)

    def determina_vincitore(self):
        """
        Determina chi ha vinto la partita seguendo le regole:
        - Se giocatore sballato -> mazziere vince
        - Se mazziere sballato -> giocatore vince
        - Altrimenti chi è più vicino a 7.5
        - In caso di pareggio, vince il mazziere
        """
        g_val = self.giocatore.valore()
        m_val = self.mazziere.valore()

        if self.giocatore.sballato():
            return "Mazziere"
        if self.mazziere.sballato():
            return "Giocatore"

        if g_val > m_val:
            return "Giocatore"
        elif g_val < m_val:
            return "Mazziere"
        else:
            return "Mazziere"  # pareggio

    def reset_partita(self):
        """
        Pulisce mani e ricrea un nuovo mazzo
        """
        self.mazzo = Mazzo()
        self.giocatore.reset_mano()
        self.mazziere.reset_mano()
