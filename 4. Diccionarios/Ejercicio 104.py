dic_validar = {'nombre': 'Pedro', 'edad': 40}
claves_requeridas = ['nombre', 'edad', 'email']
estructura_valida = all(clave in dic_validar for clave in claves_requeridas)
print(f"\n¿La estructura del diccionario es válida? (faltan claves): {estructura_valida}")
dic_validar_correcto = {'nombre': 'Pedro', 'edad': 40, 'email': 'pedro@example.com'}
estructura_valida_correcta = all(clave in dic_validar_correcto for clave in claves_requeridas)
print(f"    ¿La estructura del diccionario es válida? (correcta): {estructura_valida_correcta}")