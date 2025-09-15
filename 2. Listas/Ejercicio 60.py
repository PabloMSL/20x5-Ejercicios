estudiantes = [
    ["Ana", 85],
    ["Luis", 92],
    ["Sofía", 78],
    ["Pedro", 95]
] # [nombre, puntuacion]
# Ordenar por puntuación (índice 1) de mayor a menor
estudiantes.sort(key=lambda x: x[1], reverse=True)
print(f"Estudiantes ordenados por puntuación: {estudiantes}")