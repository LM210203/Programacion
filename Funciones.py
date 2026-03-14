def area_circulo(radio):
    """
    Calcula el área de un círculo a partir de su radio.
    Parámetros:
      radio (float): radio del círculo.
    Retorna:
      float: área del círculo.
    """
    pi = 3.1416
    area = pi * (radio ** 2)
    return area
area1 = area_circulo(20)
print("El área del círculo con radio 20 es:", area1)
area2 = area_circulo(10)
print("El área del círculo con radio 10 es:", area2)
area3 = area_circulo(2.5)
print("El área del círculo con radio 2.5 es:", area3)

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
numero = 17
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:    print(f"{numero} no es un número primo.")
numero = 20                 
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")                           
numero = 9                                                 
if es_primo(numero):                                                
    print(f"{numero} es un número primo.")
else:    print(f"{numero} no es un número primo.")  

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
    
numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")  
numero = 0
print(f"El factorial de {numero} es: {factorial(numero)}")
numero = -3 
print(f"El factorial de {numero} es: {factorial(numero)}")

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
    
numero = 10
print(f"El {numero}º número de Fibonacci es: {fibonacci(numero)}")
numero = 0
print(f"El {numero}º número de Fibonacci es: {fibonacci(numero)}")  
numero = -5
print(f"El {numero}º número de Fibonacci es: {fibonacci(numero)}")

def celsius_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit.
    Parámetros:
      celsius (float): temperatura en Celsius.
    Retorna:
      float: temperatura en Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
temp_celsius = 25
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius} grados Celsius son {temp_fahrenheit} grados Fahrenheit.")        
temp_celsius = 0
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius} grados Celsius son {temp_fahrenheit} grados Fahrenheit.")
temp_celsius = -10
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius} grados Celsius son {temp_fahrenheit} grados Fahrenheit.")

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
numeros = [3, 7, 2, 9, 5]
print(f"El número máximo en la lista {numeros} es: {maximo(numeros)}")
numeros = [-1, -5, -3, -4]
print(f"El número máximo en la lista {numeros} es: {maximo(numeros)}")
numeros = [45, 23, 67, 12, 89]
print(f"El número máximo en la lista {numeros} es: {maximo(numeros)}")



