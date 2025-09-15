print("\n1Bucle while para temporizador:")
import time
segundos = 3
while segundos > 0:
    print(f"   Tiempo restante: {segundos}")
    time.sleep(1)
    segundos -= 1
print("   ¡Tiempo terminado!")