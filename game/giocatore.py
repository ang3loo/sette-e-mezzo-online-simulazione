import math
from .carta import Carta

class Giocatore:
    """
    Rappresenta un giocatore (o mazziere, che estenderà questa classe).
    Gestisce la mano, il calcolo del punteggio e lo sballo.
    """

    def __init__(self, nome="Giocatore"):
        self.nome = nome
        self.mano = []  # Lista di oggetti Carta

    def pesca(self, carta: Carta):
        """
        Aggiunge una carta alla mano.
        """
        self.mano.append(carta)



    def valore(self):
        """
        Restituisce il punteggio della mano scegliendo quello ottimale.
        """
        total = 0
        num_matta = 0
        for carta in self.mano:
            if carta.is_matta:
                num_matta += 1
            else:
                total += carta.valore

        # Caso matta da sola
        if num_matta == 1 and len(self.mano) == 1:
            return 0.5

        # Se non ci sono matta, ritorna il punteggio unico
        if num_matta == 0:
            return total

        # Se si ha sballato ritorna il valore della mano
        if total > 7.5:
            return total

        # Miglior valore che la matta può assumere
        valori_matta = [0.5, 1, 2, 3, 4, 5, 6, 7]
        rimanente = 7.5 - total
        indice_miglior_valore = math.floor(rimanente)

        miglior_valore = total + valori_matta[indice_miglior_valore]

        return miglior_valore

    def sballato(self):
        """
        True se il giocatore ha superato 7.5 in tutte le combinazioni possibili
        """
        return self.valore() > 7.5

    def reset_mano(self):
        """
        Pulisce la mano per iniziare una nuova partita
        """
        self.mano = []

    def __repr__(self):
        mano_str = ', '.join([str(carta) for carta in self.mano])
        return f"{self.nome}: [{mano_str}] -> Valore: {self.valore()}{' (SBALLATO)' if self.sballato() else ''}"
