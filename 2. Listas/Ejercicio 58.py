numeros = [10, 20, 30, 100, 40, 50, 5]
# Filtrar valores fuera de un rango (ej. > 80 o < 10)
numeros_filtrados = [num for num in numeros if 10 <= num <= 80]
suma_total = sum(numeros_filtrados)
promedio = suma_total / len(numeros_filtrados) if numeros_filtrados else 0
print(f"Promedio de números filtrados ({numeros_filtrados}): {promedio:.2f}")