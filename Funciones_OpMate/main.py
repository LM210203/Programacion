import Fibonacci as fib
numero = 10
print(f"El {numero}º número de Fibonacci es: {fib.fibonacci(numero)}")
numero = 0
print(f"El {numero}º número de Fibonacci es: {fib.fibonacci(numero)}")
numero = -5        
print(f"El {numero}º número de Fibonacci es: {fib.fibonacci(numero)}")   

import Area_Circulo as AC
radio = 5
print(f"El área de un círculo con radio {radio} es: {AC.area_circulo(radio)}")
radio = 10          
print(f"El área de un círculo con radio {radio} es: {AC.area_circulo(radio)}")
radio = 2.5
print(f"El área de un círculo con radio {radio} es: {AC.area_circulo(radio)}")

import Es_primo as EP
numero = 17
if EP.es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
numero = 20
if EP.es_primo(numero):
    print(f"{numero} es un número primo.")
else:    print(f"{numero} no es un número primo.")
numero = 9      
if EP.es_primo(numero):
    print(f"{numero} es un número primo.")
else:    print(f"{numero} no es un número primo.")  

import Factorial as F
numero = 5 
print(f"El factorial de {numero} es: {F.factorial(numero)}")
numero = 0
print(f"El factorial de {numero} es: {F.factorial(numero)}")
numero = -3
print(f"El factorial de {numero} es: {F.factorial(numero)}")

import Celcius_A_F as CF
celsius = 25
print(f"{celsius} grados Celsius son {CF.celsius_a_fahrenheit(celsius)} grados Fahrenheit.")
celsius = 0
print(f"{celsius} grados Celsius son {CF.celsius_a_fahrenheit(celsius)} grados Fahrenheit.")
celsius = -10
print(f"{celsius} grados Celsius son {CF.celsius_a_fahrenheit(celsius)} grados Fahrenheit.")

import Maximo as M
numeros = [3, 7, 2, 9, 5]
print(f"El número máximo en la lista {numeros} es: {M.maximo(numeros)}")
numeros = [-1, -5, -3, -4]
print(f"El número máximo en la lista {numeros} es: {M.maximo(numeros)}")
numeros = [45, 23, 67, 12, 89]
print(f"El número máximo en la lista {numeros} es: {M.maximo(numeros)}")