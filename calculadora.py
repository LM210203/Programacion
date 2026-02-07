print("Bienvenido a la calculadora")

activa = True
while activa:
    numero1 = int(input("Ingrese la primera cantidad: "))
    numero2 = int(input("Ingrese la segunda cantidad: "))

    print("seleccione una operacion a realizar")
    print("Sus opciones son: ")
    print("1)Suma")
    print("2)Resta")
    print("3)Multiplicacion")
    print("4)Division")
    operacion = input("Ingrese la opcion que desee realizar: ")

    if operacion =="1":
        print(f"Resultado: {numero1 + numero2} ")
    elif operacion =="2":
        print(f"Resultado: {numero1 - numero2} ")
    elif operacion =="3":
        print(f"Resultado: {numero1 * numero2} ")
    elif operacion =="4":
        while numero2 == 0:
            print("No se puede dividir entre 0")
            numero1 = int(input("Ingrese la primera cantidad: "))
            numero2 = int(input("Ingrese la segunda cantidad: "))
        print(f"Resultado: {numero1 / numero2} ")
    else:
        print("La opcion ingresada no es valida")
    
    salir = input("\n¿Desea realizar otra operacion? (s/n): ")
    if salir.lower() == "n":
        activa = False
        print("Gracias por usar la calculadora")
        print("Hasta luego!")
