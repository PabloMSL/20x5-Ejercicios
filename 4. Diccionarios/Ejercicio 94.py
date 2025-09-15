dic_datos = {'a': 10, 'b': 25, 'c': 5, 'd': 30}
dic_filtrado = {k: v for k, v in dic_datos.items() if v > 15}
print(f"\nDiccionario filtrado (valores > 15): {dic_filtrado}")