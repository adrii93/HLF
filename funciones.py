
import numpy as np
from variables import BARCOS
from variables import Dim

class Tablero:
    def __init__(self, ID):
        self.jugador_id = ID
        self.dimensiones = (Dim, Dim)
        self.barcos = BARCOS
        self.tablero= np.full(self.dimensiones, " ")
        self.tablero_disparos = np.full(self.dimensiones, "&")

    def disparar(self, x, y):
            if self.tablero[x, y] == "O":
                print(f"Impacto en ({x}, {y})!")
                self.tablero_barcos[x, y] = "X"
                self.tablero_disparos[x, y] = "X"
                return True
            else:
                print(f"Agua en ({x}, {y}).")
                self.tablero_disparos[x, y] = "-"
                return False
            

    def quedan_barcos(self):
        return np.any(self.barcos == "O")
    