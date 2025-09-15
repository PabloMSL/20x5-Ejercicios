lista_elementos = ['rojo', 'azul', 'rojo', 'verde', 'azul', 'rojo']
frecuencia_elementos = {}
for elemento in lista_elementos:
    frecuencia_elementos[elemento] = frecuencia_elementos.get(elemento, 0) + 1
print(f"\nFrecuencia de elementos en una lista: {frecuencia_elementos}")