sistema_archivos = {
    'root': {
        'home': {
            'usuario1': {'documentos': {}, 'descargas': {'archivo1.txt': 'contenido1'}},
            'usuario2': {'documentos': {'reporte.pdf': 'contenido_pdf'}, 'escritorio': {}}
        },
        'etc': {'config.ini': 'settings'}
    }
}
print(f"Diccionario anidado (sistema de archivos): {sistema_archivos}")
print(f"   Contenido de archivo1.txt: {sistema_archivos['root']['home']['usuario1']['descargas']['archivo1.txt']}")