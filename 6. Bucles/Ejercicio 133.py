print("\nBucle for con slicing (procesando en grupos):")
lista_larga = list(range(20))
tamano_grupo = 4
for i in range(0, len(lista_larga), tamano_grupo):
    grupo = lista_larga[i : i + tamano_grupo]
    print(f"   Grupo: {grupo}")