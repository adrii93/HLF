import numpy as np
import funciones
from funciones import Tablero
from variables import NUM_BARCOS

tablero_disparos = np.full((10,10), "&")
tablero = np.full((10,10), " ")

tablero[0, 0] = "O"
tablero[4, 3] = "O"
tablero[7, 9] = "O"
tablero[7, 4] = "O"

tablero[2, 1:3] = "O"
tablero[3:5, 5] = "O"
tablero[6:8, 0] = "O"

tablero[1:4, 7] = "O"
tablero[9, 1:4] = "O"

tablero[6:, 7] = "O"

print("Tablero con barcos:")
print(tablero)

while tablero_jugador and tablero_maquina [NUM_BARCOS >0]:
        print("\n=== Tu turno ===")
        funciones.Tablero(tablero_jugador.tablero_disparos)
        x, y = funciones.obtener_coordenadas()
        impacto = tablero_maquina.disparar(x, y)

        while impacto:  # Si aciertas, te toca de nuevo
            funciones.mostrar_tablero(tablero_jugador.tablero_disparos)
            x, y = funciones.obtener_coordenadas()
            impacto = tablero_maquina.disparar(x, y)

        print("\n=== Turno de la máquina ===")
        x, y = funciones.generar_coordenadas_aleatorias()
        impacto_maquina = tablero_jugador.disparar(x, y)

        while impacto_maquina:  # Si la máquina acierta, le toca de nuevo
            x, y = funciones.generar_coordenadas_aleatorias() #Después tengo que crear una funcion para esto
            impacto_maquina = tablero_jugador.disparar(x, y)

if not tablero_jugador.quedan_barcos():
        print("\n¡Has perdido! Te han hundido todos tus barcos.")
else:
        print("\n¡Felicidades! Has hundido todos los barcos.")