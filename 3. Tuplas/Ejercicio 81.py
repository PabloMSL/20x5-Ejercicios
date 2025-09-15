tupla_datos = ((1, 'par'), (2, 'par'), (3, 'impar'), (4, 'par'))
tupla_filtrada_simulada = tuple(item for item in tupla_datos if item[1] == 'par')
print(f"\nTupla filtrada (pares): {tupla_filtrada_simulada}")