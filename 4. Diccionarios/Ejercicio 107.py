from operator import itemgetter
lista_personas = [
    {'nombre': 'Carlos', 'edad': 35},
    {'nombre': 'Ana', 'edad': 28},
    {'nombre': 'Pedro', 'edad': 40}
]
# Ordenar por edad usando itemgetter
lista_personas_ordenada = sorted(lista_personas, key=itemgetter('edad'))
print(f"\nLista de diccionarios ordenada por edad: {lista_personas_ordenada}")