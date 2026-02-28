import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

while intentos < max_intentos:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1

    if intento < numero_secreto:
        print("Más alto.")
    elif intento > numero_secreto:
        print("Más bajo.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        break
else:
    print(f"Lo siento, se alcanzó el límite de {max_intentos} intentos. El número era {numero_secreto}.")