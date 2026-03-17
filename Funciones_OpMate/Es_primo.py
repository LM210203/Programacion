def es_primo(n):
    """
    Determina si un número es primo.
    Parámetros:
      n (int): número a evaluar.
    Retorna:
      bool: True si n es primo, False en caso contrario.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True