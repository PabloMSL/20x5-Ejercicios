print("\nBucle for con listas anidadas y desempaquetado:")
datos_productos = [["Laptop", 1200], ["Teclado", 75], ["Mouse", 25]]
for nombre_producto, precio in datos_productos:
    print(f"   {nombre_producto}: ${precio}")