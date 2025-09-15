dic1_update = {'a': 1, 'b': 2}
dic2_update = {'b': 20, 'c': 3}
# Esto sobrescribe 'b'. Para preservar, se necesita lógica adicional.
# Ejemplo: copiar solo las claves que no existen en dic1_update
for key, value in dic2_update.items():
    if key not in dic1_update:
        dic1_update[key] = value
print(f"\nDiccionario actualizado (sin sobrescribir): {dic1_update}")