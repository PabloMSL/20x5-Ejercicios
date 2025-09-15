print("\nBucle while para stream de datos simulado:")
datos_stream = [10, 5, 12, -3, 8, -1, 20]
indice_stream = 0
while indice_stream < len(datos_stream) and datos_stream[indice_stream] >= 0:
    dato_actual = datos_stream[indice_stream]
    print(f"   Procesando dato positivo: {dato_actual}")
    indice_stream += 1
if indice_stream < len(datos_stream):
    print(f"   Stream detenido en dato negativo: {datos_stream[indice_stream]}")
else:
    print("   Fin del stream.")