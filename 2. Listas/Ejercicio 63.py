lista_a = [1, 3, 5]
lista_b = [2, 4, 6]
# Usar un bucle para combinar alternando
lista_combinada_alternada = []
min_len = min(len(lista_a), len(lista_b))
for i in range(min_len):
    lista_combinada_alternada.append(lista_a[i])
    lista_combinada_alternada.append(lista_b[i])
# Añadir elementos restantes si una lista es más larga
lista_combinada_alternada.extend(lista_a[min_len:])
lista_combinada_alternada.extend(lista_b[min_len:])
print(f"Listas combinadas alternando: {lista_combinada_alternada}")