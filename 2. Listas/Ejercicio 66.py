colas = {
    "alta": ["tarea_a1", "tarea_a2"],
    "baja": ["tarea_b1", "tarea_b2", "tarea_b3"]
}
orden_procesamiento = ["alta", "baja", "alta", "baja", "baja"]
tareas_procesadas = []
for prioridad in orden_procesamiento:
    if colas[prioridad]:
        # Simulando popleft()
        tareas_procesadas.append(colas[prioridad].pop(0))
print(f"Tareas procesadas en orden de prioridades (usando lista y dict): {tareas_procesadas}, Colas restantes: {colas}") 