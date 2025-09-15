dic_original = {'a': 1, 'b': 2, 'c': 3}
dic_invertido = {value: key for key, value in dic_original.items()}
print(f"\nDiccionario invertido: {dic_invertido}")