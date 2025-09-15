print("\nIterar sobre múltiples listas con zip:")
nombres = ["Ana", "Luis", "Sofía"]
edades = [25, 30, 22]
ciudades = ["Madrid", "Barcelona", "Valencia"]
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"   {nombre} tiene {edad} años y vive en {ciudad}.")