print("\nBucle while para crecimiento exponencial:")
poblacion = 100
tasa_crecimiento = 0.1
limite_poblacion = 500
años = 0
while poblacion < limite_poblacion:
    poblacion *= (1 + tasa_crecimiento)
    años += 1
    print(f"   Año {años}: Población ~{int(poblacion)}")
print(f"   Se alcanzó la población límite ({limite_poblacion}) en {años} años.")