dic_completo = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
claves_a_eliminar = ['b', 'd']
for clave in claves_a_eliminar:
    dic_completo.pop(clave, None) # Usar pop con None por defecto para evitar errores si la clave no existe
print(f"\nDiccionario después de eliminar elementos: {dic_completo}")