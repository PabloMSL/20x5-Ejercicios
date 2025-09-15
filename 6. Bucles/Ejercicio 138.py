print("\nBucle while para validar entrada numérica:")
edad = -1
while edad <= 0:
     try:
         edad_str = input("   Introduce tu edad (debe ser positiva): ")
         edad = int(edad_str)
         if edad <= 0:
             print("   La edad debe ser un número positivo.")
     except ValueError:
         print("   Entrada inválida. Por favor, introduce un número entero.")
print(f"   Edad válida ingresada: {edad}")