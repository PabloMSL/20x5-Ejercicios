tupla_numeros = ((1,), (2,), (3,))
tupla_transformada_simulada = tuple((item[0] * 10,) for item in tupla_numeros)
print(f"\nTupla transformada (multiplicar por 10): {tupla_transformada_simulada}")