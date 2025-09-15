print("\nBucle for con sorted() para iterar sobre un diccionario ordenado:")
puntuaciones = {"Juan": 85, "Ana": 92, "Pedro": 78}
for nombre in sorted(puntuaciones.keys()):
    print(f"   {nombre}: {puntuaciones[nombre]}")