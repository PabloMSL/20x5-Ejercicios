dic_config = {'modo': 'debug', 'nivel': 'alto'}
nivel_log = dic_config.get('nivel', 'medio')
timeout = dic_config.get('timeout', 60) # La clave 'timeout' no existe
print(f"\nUsando get() con valor por defecto: Nivel log = {nivel_log}, Timeout = {timeout}")