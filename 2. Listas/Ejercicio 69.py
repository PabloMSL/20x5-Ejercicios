datos = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10]
# Obtener el cuadrado de los números positivos pares
resultados = [x**2 for x in datos if x > 0 and x % 2 == 0]
print(f"Cuadrado de números positivos pares: {resultados}")