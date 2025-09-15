invitados_evento1 = ["Pedro", "María", "Juan", "Luis"]
invitados_evento2 = ["María", "Juan"]
# Verificar si todos los invitados del evento 2 están en el evento 1
todos_presentes = all(nombre in invitados_evento1 for nombre in invitados_evento2)
print(f"¿Están todos los invitados del evento 2 en el evento 1?: {todos_presentes}")