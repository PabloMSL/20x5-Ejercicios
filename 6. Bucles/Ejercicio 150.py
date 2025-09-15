print("\nBucle while con manejo de excepciones:")
reintentos_restantes = 2
while reintentos_restantes >= 0:
    try:
        # Simular una operación que puede fallar
        if random.random() < 0.7: # 70% de probabilidad de fallar
            raise ConnectionError("Error de conexión simulado")
        print("   Operación exitosa.")
        break # Salir si la operación es exitosa
    except ConnectionError as e:
        print(f"   Error: {e}. Reintentando...")
        reintentos_restantes -= 1
        if reintentos_restantes < 0:
            print("   Máximo de reintentos alcanzado.")