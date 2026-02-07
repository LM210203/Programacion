nombre = input(" ¿Como te llamas? ")
edad = input(" ¿Que edad tienes? ")
while True:
    edad = input(" ¿Que edad tienes? ")
    if edad.isdigit():
        edad = int(edad)
        break
    else:
        print("Por favor, ingresa solo números.")

ciudad = input(" ¿De que ciudad eres? ")
hobby = input(" ¿Cual es tu Hobby? ")
print()
print()
print(f"Un momento, Generando tu tarjeta de presentacion...")
print()
print(f"Hola soy, {nombre}")
print(f"Y tengo {edad} años de edad,")
print(f"Vivo en {ciudad}")
print(f"Y mi Hobby es {hobby}")
print("Es un gusto conocerte!")
#En este codigo investigue acerca de como hacer que el valor en edad sea solamente numero y creo entender como funciona todo
#excepto el int(edad) le envio esrte como extra pero el primero lo hice unicamente yo, en este si use ia