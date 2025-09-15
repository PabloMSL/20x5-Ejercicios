texto = "Este es un texto de ejemplo. Este texto tiene palabras repetidas."
# Limpiar el texto (quitar puntuación y convertir a minúsculas) y dividir en palabras
import re
palabras = re.findall(r'\b\w+\b', texto.lower())
# Contar frecuencia manualmente (simulando Counter)
frecuencia_palabras = {}
for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
print(f"Frecuencia de palabras (usando lista y dict): {frecuencia_palabras}") 