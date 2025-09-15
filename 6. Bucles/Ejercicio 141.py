print("\nBucle for con iter() y next():")
iterador_colores = iter(["rojo", "verde", "azul"])
try:
    print(f"   {next(iterador_colores)}")
    print(f"   {next(iterador_colores)}")
    print(f"   {next(iterador_colores)}")
    # Esto generará StopIteration si se llama de nuevo
    # print(f" {next(iterador_colores)}")
except StopIteration:
    print("   Fin de la iteración.")