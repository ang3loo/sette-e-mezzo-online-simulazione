import random
from .carta import Carta

class Mazzo:
    """
    Rappresenta un mazzo italiano da 40 carte.
    Ogni partita utilizza un mazzo nuovo e mischiato.
    """
    semi = ["Denari", "Coppe", "Spade", "Bastoni"]
    nomi_carte = ["Asso", "2", "3", "4", "5", "6", "7", "Fante", "Cavallo", "Re"]

    def __init__(self):
        self.carte = self._crea_mazzo()
        self.mischia()

    def _crea_mazzo(self):
        mazzo = []
        for seme in self.semi:
            for nome in self.nomi_carte:
                # Asso → 1, carte 2-7 → valore numerico, Fante/Cavallo/Re → 0.5
                if nome == "Asso":
                    valore = 1
                elif nome in ["Fante", "Cavallo", "Re"]:
                    valore = 0.5
                else:
                    valore = int(nome)
                # Matta: Re di Denari
                is_matta = (nome == "Re" and seme == "Denari")
                mazzo.append(Carta(nome, seme, valore, is_matta))
        return mazzo

    def mischia(self):
        random.shuffle(self.carte)

    def pesca(self):
        """
        Pesca l'ultima carta del mazzo.
        Rimuove la carta dal mazzo.
        """
        if not self.carte:
            raise ValueError("Il mazzo è vuoto!")
        return self.carte.pop()

    def __len__(self):
        return len(self.carte)

    def __repr__(self):
        return f"Mazzo({len(self.carte)} carte rimanenti)"
