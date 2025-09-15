print("\nBucle while para procesar una cola:")
cola_tareas = ["Tarea A", "Tarea B", "Tarea C"]
while cola_tareas:
    tarea_actual = cola_tareas.pop(0) # Simula sacar del inicio
    print(f"   Procesando: {tarea_actual}")