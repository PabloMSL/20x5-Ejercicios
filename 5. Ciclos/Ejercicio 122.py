print("\nLlenar lista con resultados condicionales (simulado):")
numeros = range(1, 11)
pares_cuadrado = []
for num in numeros:
    if num % 2 == 0:
        pares_cuadrado.append(num ** 2)
print(f"   Cuadrados de números pares: {pares_cuadrado}")