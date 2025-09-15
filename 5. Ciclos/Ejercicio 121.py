print("Bucle while para procesar elementos con condición:")
saldo = 100
retiros = [20, 30, 40, 50, 10]
i = 0
while saldo > 0 and i < len(retiros):
    saldo -= retiros[i]
    print(f"   Retirando {retiros[i]}, Saldo restante: {saldo}")
    i += 1
if saldo <= 0:
    print("   Saldo agotado.")
elif i == len(retiros):
    print("   Todos los retiros procesados.")