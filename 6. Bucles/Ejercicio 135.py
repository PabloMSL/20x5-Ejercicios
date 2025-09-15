print("\nBucle for con list comprehension y filtro:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_duplicados = [num * 2 for num in numeros if num % 2 == 0]
print(f"   Pares duplicados: {pares_duplicados}")