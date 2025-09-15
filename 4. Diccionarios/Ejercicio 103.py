datos_con_categoria = [
    {'item': 'manzana', 'categoria': 'fruta'},
    {'item': 'zanahoria', 'categoria': 'verdura'},
    {'item': 'banana', 'categoria': 'fruta'},
    {'item': 'brocoli', 'categoria': 'verdura'}
]
agrupado_por_categoria = {}
for item in datos_con_categoria:
    categoria = item['categoria']
    if categoria not in agrupado_por_categoria:
        agrupado_por_categoria[categoria] = []
    agrupado_por_categoria[categoria].append(item['item'])
print(f"\nElementos agrupados por categoría: {agrupado_por_categoria}")