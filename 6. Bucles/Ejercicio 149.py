print("\nBucle for con multiple assignment y condicional:")
coordenadas = [(1, 1), (2, 2), (3, 1), (4, 2)]
puntos_en_y2 = [(x, y) for x, y in coordenadas if y == 2]
print(f"   Puntos con y=2: {puntos_en_y2}")