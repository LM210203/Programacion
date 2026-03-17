def fibonacci(n):
    """
    Devuelve el n-ésimo número de Fibonacci.
    Parámetros:
      n (int): índice en la serie de Fibonacci (0 basado).
    Retorna:
      int o str: número de Fibonacci o mensaje de error para n negativo.
    """
    if n < 0:
        return "No se puede calcular la serie de Fibonacci para un número negativo."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b