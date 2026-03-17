def maximo(lista):
    """
    Busca el valor máximo en una lista de números.
    Parámetros:
      lista (list): lista de valores numéricos.
    Retorna:
      número o str: valor máximo o mensaje si la lista está vacía.
    """
    if not lista:
        return "La lista está vacía."
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo