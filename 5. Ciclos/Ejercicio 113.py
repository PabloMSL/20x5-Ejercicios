print("\nBucle while con condición compleja y break/continue:")
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue # Saltar a la siguiente iteración si es par
    if contador > 7:
        break # Salir del bucle si es mayor que 7
    print(f"   Contador impar: {contador}")