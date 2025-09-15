print("\nBucle for con set comprehension:")
lista_numeros = [1, 2, 2, 3, 4, 4, 5]
cuadrados_unicos = {num ** 2 for num in lista_numeros}
print(f"   Cuadrados únicos: {cuadrados_unicos}")