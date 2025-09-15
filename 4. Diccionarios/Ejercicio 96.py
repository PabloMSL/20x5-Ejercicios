dic_desordenado = {'c': 3, 'a': 1, 'b': 2}
dic_ordenado_por_clave = sorted(dic_desordenado.items()) # Ordena por clave
dic_ordenado_por_valor = sorted(dic_desordenado.items(), key=lambda item: item[1]) # Ordena por valor
print(f"\nDiccionario ordenado por clave: {dic_ordenado_por_clave}")
print(f"   Diccionario ordenado por valor: {dic_ordenado_por_valor}")