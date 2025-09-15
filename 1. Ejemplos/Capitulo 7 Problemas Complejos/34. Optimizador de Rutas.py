import random
import math
from itertools import permutations
def calcular_distancia(ciudad1, ciudad2):
    """
    Calcula la distancia euclidiana entre dos ciudades
    Cada ciudad tiene coordenadas (x, y)
    """
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distancia, 2)
def calcular_distancia_total_ruta(ciudades, ruta):
    """
    Calcula la distancia total de una ruta completa
    La ruta es una lista de índices de ciudades
    """
    distancia_total = 0
    # Calcular distancia entre ciudades consecutivas
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]
        siguiente_ciudad = ciudades[ruta[(i + 1) % len(ruta)]] # % para volver al inicio
        distancia = calcular_distancia(ciudad_actual, siguiente_ciudad)
        distancia_total += distancia
    return round(distancia_total, 2)
def metodo_fuerza_bruta(ciudades):
    """
    Encuentra la ruta óptima probando todas las combinaciones posibles
    ¡ADVERTENCIA: Solo usar con pocas ciudades (f8) por complejidad computacional!
    """
    num_ciudades = len(ciudades)
    print(f"Resolviendo TSP con fuerza bruta para {num_ciudades} ciudades.")
    print(f"Generando {math.factorial(num_ciudades)} permutaciones...") # Número de permutaciones

    mejor_ruta = None
    menor_distancia = float('inf') # Inicializar con infinito

    # Generar todas las posibles rutas (permutaciones de índices de ciudades)
    # Excluimos la primera ciudad de la permutación porque el punto de inicio es fijo
    for i, ruta_parcial in enumerate(permutations(range(1, num_ciudades))):
        # Construir la ruta completa: empezar en la ciudad 0, seguir la permutación
        # y volver a la ciudad 0 al final
        ruta_completa = [0] + list(ruta_parcial)
        distancia_actual = calcular_distancia_total_ruta(ciudades, ruta_completa)

        # Imprimir progreso opcional
        # if i % 1000 == 0: # Imprimir cada 1000 permutaciones
        #     print(f"  Probando permutación {i+1}/{math.factorial(num_ciudades)}")

        if distancia_actual < menor_distancia:
            menor_distancia = distancia_actual
            mejor_ruta = ruta_completa
            print(f"\nNuevo mejor ruta encontrada: {mejor_ruta} con distancia {menor_distancia}")

    # Mapear índices de ruta a nombres de ciudades si es necesario
    # (asumiendo que las ciudades son solo coordenadas aquí)
    # mejor_ruta_nombres = [nombres_ciudades[i] for i in mejor_ruta]

    return mejor_ruta, menor_distancia

# Ejemplo de uso: Ciudades representadas por coordenadas (x, y)
ciudades_ejemplo = [(0, 0), (1, 5), (6, 2), (8, 8)]

print("PROBLEMA DEL VIAJANTE DE COMERCIO (TSP)")
print("=" * 40)

# Mostrar ciudades
print("Ciudades:")
for i, (x, y) in enumerate(ciudades_ejemplo):
    print(f" Ciudad {i}: ({x}, {y})")

# Calcular y mostrar la ruta óptima usando fuerza bruta
ruta_optima, distancia_minima = metodo_fuerza_bruta(ciudades_ejemplo)

print("\n" + "=" * 40)
print("RESULTADO ÓPTIMO (FUERZA BRUTA)")
print("=" * 40)
print(f"Ruta óptima (índices de ciudad): {ruta_optima}")
print(f"Distancia mínima: {distancia_minima}")