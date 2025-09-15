print("\n1Bucle while para consumir lista:")
procesos_pendientes = ["Proceso 1", "Proceso 2", "Proceso 3"]
while procesos_pendientes:
    proceso = procesos_pendientes.pop() # Simula sacar del final (pila)
    print(f"   Completando: {proceso}")
print("   Todos los procesos completados.")