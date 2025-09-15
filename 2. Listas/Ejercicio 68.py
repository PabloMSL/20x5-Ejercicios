tablero = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", " ", "O"]
]
# Verificar si hay tres en raya en la primera fila
gana_fila0 = all(celda == "X" for celda in tablero[0]) or all(celda == "O" for celda in tablero[0])
print(f"Tablero de juego:\n{tablero[0]}\n{tablero[1]}\n{tablero[2]}")
print(f"¿Hay ganador en la primera fila?: {gana_fila0}")