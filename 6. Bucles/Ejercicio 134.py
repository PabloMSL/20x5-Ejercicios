print("\nBucle while anidado para búsqueda 2D:")
matriz_busqueda = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elemento_buscar = 5
encontrado = False
fila_idx = 0
while fila_idx < len(matriz_busqueda):
    col_idx = 0
    while col_idx < len(matriz_busqueda[fila_idx]):
        if matriz_busqueda[fila_idx][col_idx] == elemento_buscar:
            print(f"   Elemento {elemento_buscar} encontrado en ({fila_idx}, {col_idx})")
            encontrado = True
            break # Salir del bucle interno
        col_idx += 1
    if encontrado:
        break # Salir del bucle externo
    fila_idx += 1