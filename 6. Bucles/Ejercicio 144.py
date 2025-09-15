print("\nBucle while con múltiples condiciones y banderas:")
tarea_exitosa = False
intentos_max = 3
intentos_actuales = 0
while not tarea_exitosa and intentos_actuales < intentos_max:
    print(f"   Intento {intentos_actuales + 1} de {intentos_max}...")
    # Simular si la tarea fue exitosa (ej. 1 de cada 2 intentos)
    if random.random() < 0.5:
        tarea_exitosa = True
        print("   Tarea completada con éxito!")
    else:
        print("   Tarea fallida.")
        intentos_actuales += 1
if not tarea_exitosa:
    print("   Tarea fallida después de varios intentos.")