claves_nuevas = ['status', 'fecha_creacion']
valor_defecto = 'pendiente'
dic_con_defectos = dict.fromkeys(claves_nuevas, valor_defecto)
print(f"\nDiccionario con valores predeterminados: {dic_con_defectos}")