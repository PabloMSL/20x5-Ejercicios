materiales = ["lapiz", "papel", "borrador"]
while True :
    print("Programa para insertar materiales")
    print("1 Insertar Materiales")
    print("2 Terminar programa")
    rta = int(input())
    if rta == 1 :
        print("Inserte el material a alistar")
        material = input()
        materiales.append(material)
        print("Material Insertado")
        print(materiales)
    elif rta == 2 :
        print("Gracias por usar el programa")
        break