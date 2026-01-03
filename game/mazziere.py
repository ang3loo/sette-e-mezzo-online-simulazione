from .giocatore import Giocatore
from .carta import Carta

class Mazziere(Giocatore):
    def __init__(self, nome="Mazziere"):
        super().__init__(nome)

    def gioca_turno(self, mazzo, giocatore):
        """
        Logica automatica del mazziere:
        - Pesca finché valore < 5
        - Si ferma quando valore >= 5
        - Non gioca se il giocatore ha sballato
        """
        # Se il giocatore ha sballato, il mazziere non pesca
        if giocatore.sballato():
            print("-------------Giocatore SBALLATO, MAZZIERE non pesca------------")
            return

        while self.valore() < 5:
            carta = mazzo.pesca()
            self.pesca(carta)
        
        if self.valore() > 7.5:
            print(self.__repr__())
            print("-----------------Mazzaro SBALLATO----------------")
            return
