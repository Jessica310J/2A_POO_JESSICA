# utils.py

def validar_hora(hora):
    """Valida que la hora tenga formato HH:MM y sea válida en 24h."""
    try:
        h, m = map(int, hora.split(":"))  # Separa la hora y minutos y convierte a enteros
        return 0 <= h < 24 and 0 <= m < 60  # Verifica que estén en rango válido
    except:
        return False  # Retorna False si no cumple formato o no se puede convertir