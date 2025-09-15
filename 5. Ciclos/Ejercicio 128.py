print("\nContar ocurrencias con bucle:")
lista_con_duplicados = [1, 2, 2, 3, 1, 4, 2]
conteo = {}
for elemento in lista_con_duplicados:
    conteo[elemento] = conteo.get(elemento, 0) + 1
print(f"   Conteo de elementos: {conteo}")