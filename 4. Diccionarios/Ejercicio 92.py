def fusionar_diccionarios(dic1, dic2):
    """Fusiona dic2 en dic1, anidando si es necesario."""
    for key, value in dic2.items():
        if key in dic1 and isinstance(dic1[key], dict) and isinstance(value, dict):
            fusionar_diccionarios(dic1[key], value)
        else:
            dic1[key] = value
    return dic1

dic_base = {'a': {'x': 1, 'y': 2}, 'b': 3}
dic_actualizacion = {'a': {'y': 20, 'z': 30}, 'c': 4}
dic_fusionado = fusionar_diccionarios(dic_base.copy(), dic_actualizacion) # Usar copy para no modificar el original
print(f"\nDiccionarios fusionados: {dic_fusionado}")