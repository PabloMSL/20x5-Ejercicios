numeros = list(range(20)) # [0, 1, ..., 19]
# Obtener elementos pares usando slicing con paso
pares = numeros[::2]
# Obtener elementos impares en orden inverso
impares_inverso = numeros[::-2]
print(f"Números pares: {pares}")
print(f"Números impares en orden inverso: {impares_inverso}")