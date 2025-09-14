# Lista de compras inteligente
compras = ["pan", "leche", "queso"]
print("Lista inicial:")
print(compras)
# Agregar elementos
compras.append("papel higienico") # append() agrega al final
compras.append("jamon")
print("\nDespués de agregar papel higienico y jamon:")
print(compras)
# Insertar en posición específica
compras.insert(1, "pasta de tomate") # insert(posición, elemento)
print("\nDespués de insertar pasta de tomate en posición 1:")
print(compras)
# Eliminar elementos
compras.remove("queso") # remove() elimina la primera aparición
print("\nDespués de eliminar queso:")
print(compras)
# Eliminar por posición
elemento_eliminado = compras.pop(0) # pop() elimina y devuelve el elemento
print("\nEliminamos el primer elemento:", elemento_eliminado)
print("Lista final:", compras)