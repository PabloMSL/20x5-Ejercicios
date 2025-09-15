pasos_proceso = ["iniciar", "procesar", "verificar", "finalizar"]
# Revertir el orden y añadir un prefijo
pasos_invertidos_modificados = [f"Paso {i+1}: {paso}" for i, paso in enumerate(reversed(pasos_proceso))]
print(f"Pasos del proceso invertidos y modificados: {pasos_invertidos_modificados}")