tupla_desordenada = ((3, 'c'), (1, 'a'), (2, 'b'))
tupla_ordenada_simulada = tuple(sorted(tupla_desordenada)) # sorted() retorna lista, luego se convierte a tupla
print(f"\nTupla de tuplas ordenada: {tupla_ordenada_simulada}"