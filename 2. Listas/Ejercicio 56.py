cola_impresion = [["doc1.pdf", 3], ["doc2.txt", 1], ["doc3.jpg", 2]] # [nombre, prioridad]
# Ordenar la cola por prioridad (menor número = mayor prioridad)
cola_impresion.sort(key=lambda x: x[1])
# Procesar la tarea de mayor prioridad (simulando popleft)
if cola_impresion:
    tarea_actual = cola_impresion.pop(0)
    print(f"Tarea de impresión procesada: {tarea_actual}, Cola restante: {cola_impresion}")
else:
    print("Cola de impresión vacía.")