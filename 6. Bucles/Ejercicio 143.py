print("\nBucle for con dict comprehension y condicional:")
productos_stock = {"manzanas": 50, "pan": 10, "leche": 5, "huevos": 25}
stock_bajo = {producto: stock for producto, stock in productos_stock.items() if stock < 15}
print(f"   Productos con stock bajo: {stock_bajo}")