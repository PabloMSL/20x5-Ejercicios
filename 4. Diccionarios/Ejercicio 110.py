dic_principal = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic_subconjunto = {'b': 2, 'c': 3}
dic_no_subconjunto = {'b': 2, 'e': 5}

es_subconjunto_valido = all(item in dic_principal.items() for item in dic_subconjunto.items())
es_subconjunto_invalido = all(item in dic_principal.items() for item in dic_no_subconjunto.items())

print(f"\n¿Es {{'b': 2, 'c': 3}} un subconjunto válido? {es_subconjunto_valido}")
print(f"    ¿Es {{'b': 2, 'e': 5}} un subconjunto válido? {es_subconjunto_invalido}")