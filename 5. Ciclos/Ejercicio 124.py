print("\nBuscar elemento y detenerse:")
lista_busqueda = [10, 20, 30, 40, 50]
elemento_buscar = 30
encontrado = False
for elemento in lista_busqueda:
    if elemento == elemento_buscar:
        print(f"   Elemento {elemento_buscar} encontrado.")
        encontrado = True
        break
if not encontrado:
    print(f"   Elemento {elemento_buscar} no encontrado.")