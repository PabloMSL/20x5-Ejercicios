print("\nBucle while con estado cambiante:")
energia = 50
comida = 20
while energia < 100 and comida > 0:
    energia += 10
    comida -= 5
    print(f"   Energía: {energia}, Comida restante: {comida}")
print("   Proceso terminado.")