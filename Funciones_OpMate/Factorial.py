def factorial(n):
    """
    Calcula el factorial de un número entero >= 0.
    Parámetros:
      n (int): número para calcular factorial.
    Retorna:
      int o str: factorial de n o mensaje de error si n es negativo.
    """
    if n < 0:
        return "No se puede calcular el factorial de un número negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado   