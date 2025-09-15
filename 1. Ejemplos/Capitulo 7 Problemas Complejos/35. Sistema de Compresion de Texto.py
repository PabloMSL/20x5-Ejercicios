from collections import Counter
import heapq
class NodoHuffman:
    """Nodo para el árbol de codificación Huffman"""
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq
def comprimir_repeticion_simple(texto):
    """
    Compresión simple: reemplaza secuencias repetidas
    Ejemplo: "aaaa" -> "4a"
    """
    print("Aplicando compresión simple de repetición...")
    comprimido = ""
    i = 0
    while i < len(texto):
        caracter_actual = texto[i]
        contador = 0
        j = i
        while j < len(texto) and texto[j] == caracter_actual:
            contador += 1
            j += 1
        if contador > 1:
            comprimido += str(contador) + caracter_actual
        else:
            comprimido += caracter_actual
        i = j # Mover el índice al final de la secuencia repetida
    return comprimido

def construir_arbol_huffman(texto):
    """Construye el árbol de codificación Huffman"""
    # Contar frecuencias
    frecuencias = Counter(texto)
    # Crear una cola de prioridad de nodos
    cola = [NodoHuffman(char, freq) for char, freq in frecuencias.items()]
    heapq.heapify(cola) # Convertir la lista en una cola de prioridad
    # Construir el árbol
    while len(cola) > 1:
        # Sacar los dos nodos con menor frecuencia
        izquierdo = heapq.heappop(cola)
        derecho = heapq.heappop(cola)
        # Crear un nuevo nodo interno
        nodo_interno = NodoHuffman(None, izquierdo.freq + derecho.freq, izquierdo, derecho)
        # Añadir el nuevo nodo a la cola
        heapq.heappush(cola, nodo_interno)
    return cola[0] # El último nodo es la raíz del árbol

def generar_codigos_huffman(nodo, prefijo="", codigos={}):
    """Genera los códigos de Huffman recorriendo el árbol"""
    if nodo is not None:
        if nodo.char is not None: # Es un nodo hoja (tiene un carácter)
            codigos[nodo.char] = prefijo if prefijo else "0" # Asignar el prefijo como código
        else: # Es un nodo interno
            # Recorrer hacia la izquierda (0) y hacia la derecha (1)
            generar_codigos_huffman(nodo.left, prefijo + "0", codigos)
            generar_codigos_huffman(nodo.right, prefijo + "1", codigos)
    return codigos

def codificar_huffman(texto, codigos):
    """Codifica el texto usando los códigos de Huffman"""
    print("\nCodificando con Huffman...")
    texto_codificado = "".join([codigos[caracter] for caracter in texto])
    return texto_codificado

def decodificar_huffman(texto_codificado, raiz_arbol):
    """Decodifica el texto codificado con Huffman"""
    print("\nDecodificando con Huffman...")
    texto_decodificado = ""
    nodo_actual = raiz_arbol
    for bit in texto_codificado:
        if bit == "0":
            nodo_actual = nodo_actual.left
        else: # bit == "1"
            nodo_actual = nodo_actual.right

        if nodo_actual.char is not None: # Llegamos a un nodo hoja
            texto_decodificado += nodo_actual.char
            nodo_actual = raiz_arbol # Reiniciar para el siguiente carácter

    return texto_decodificado

# Ejemplo de uso
texto_original = "este es un ejemplo de compresion de texto"

print("TEXTO ORIGINAL:", texto_original)
print("Longitud:", len(texto_original), "caracteres")
print("-" * 30)

# Compresión simple de repetición
texto_comprimido_simple = comprimir_repeticion_simple(texto_original)
print("\nTEXTO COMPRIMIDO (simple):", texto_comprimido_simple)
print("Longitud:", len(texto_comprimido_simple), "caracteres")

# Compresión con Huffman
print("\n--- Compresión Huffman ---")
arbol_huffman = construir_arbol_huffman(texto_original)
codigos_huffman = generar_codigos_huffman(arbol_huffman)

print("\nCódigos de Huffman generados:")
for char, code in sorted(codigos_huffman.items()):
    print(f" '{char}': {code}")

texto_codificado_huffman = codificar_huffman(texto_original, codigos_huffman)
print("TEXTO CODIFICADO (Huffman):", texto_codificado_huffman)
print("Longitud:", len(texto_codificado_huffman), "bits")

# Decodificación con Huffman
texto_decodificado_huffman = decodificar_huffman(texto_codificado_huffman, arbol_huffman)
print("\nTEXTO DECODIFICADO (Huffman):", texto_decodificado_huffman)