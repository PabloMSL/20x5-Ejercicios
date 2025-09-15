print("\nBucle while para validar entrada:")
while True:
     try:
         edad = int(input("   Introduce tu edad (número): "))
         if edad > 0:
            print(f"   Edad válida: {edad}")
            break
         else:
            print("   La edad debe ser un número positivo.")
     except ValueError:
         print("   Entrada inválida. Por favor, introduce un número.")