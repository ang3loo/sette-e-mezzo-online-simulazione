class Carta:
    """
    Rappresenta una carta del mazzo italiano.
    La matta (Re di Denari) può assumere valori diversi e viene gestita a livello di giocatore.
    """
    def __init__(self, nome: str, seme: str, valore: float, is_matta: bool = False):
        self.nome = nome        # Nome della carta (Asso, 2, ..., Re)
        self.seme = seme        # Seme della carta (Denari, Coppe, Spade, Bastoni)
        self.valore = valore    # Valore numerico della carta
        self.is_matta = is_matta  # True se è la matta (Re di Denari)

    def __repr__(self):
        matta_str = " (Matta)" if self.is_matta else ""
        return f"{self.nome} di {self.seme}{matta_str} [{self.valore}]"
