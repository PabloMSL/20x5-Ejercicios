tupla_anidada = ((1, 2, 3), ('a', 'b', 'c'), (True, False, None))
print("\nIterar sobre tuplas anidadas:")
for sub_tupla in tupla_anidada:
    for elemento in sub_tupla:
        print(f"   {elemento}", end=" ")
    print()