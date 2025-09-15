dic_precios = {'manzana': 1.0, 'banana': 0.5, 'naranja': 0.8}
dic_precios_con_iva = {k: round(v * 1.21, 2) for k, v in dic_precios.items()}
print(f"\nDiccionario con precios + IVA: {dic_precios_con_iva}")