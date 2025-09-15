print("\nBucle while para juego de adivinanza:")
import random
numero_secreto = random.randint(1, 10)
intentos = 0
while True:
    intentos += 1
    try:
        adivinanza = int(input(f"   Intento {intentos}: Adivina el número (1-10): "))
        if adivinanza == numero_secreto:
            print(f"   ¡Correcto! Adivinaste en {intentos} intentos.")
            break
        elif adivinanza < numero_secreto:
            print("   Demasiado bajo.")
        else:
            print("   Demasiado alto.")
    except ValueError:
        print("   Entrada inválida. Introduce un número.")