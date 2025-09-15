from itertools import zip_longest
print("\nBucle for con zip_longest:")
lista_corta = [1, 2]
lista_larga = ['a', 'b', 'c', 'd']
for item1, item2 in zip_longest(lista_corta, lista_larga, fillvalue='-'):
     print(f"   ({item1}, {item2})")