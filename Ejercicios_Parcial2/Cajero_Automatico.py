def calcular_billetes(cantidad):
    billetes = [200, 100, 50, 20, 10, 5]
    resultado = {}
    
    for billete in billetes:
        if cantidad >= billete:
            resultado[billete] = cantidad // billete
            cantidad = cantidad % billete
    return resultado

bucle = True
while bucle:
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        if cantidad <= 5 or cantidad % 5 != 0:
            print("Cantidad ingresada no es válida. Por favor, ingrese una cantidad mayor a Q5 y que sea multipo de 5.")
            salir = input("\n¿Desea realizar otro retiro? (s/n): ")
            if salir.lower() == "n":
             bucle = False
             print("Gracias por usar el cajero automático")
             print("Hasta luego!")   


        elif cantidad > 5 and cantidad % 5 == 0:    
            billetes_a_entregar = calcular_billetes(cantidad)
            print("Billetes a entregar:") 
            for billete, cantidad in billetes_a_entregar.items():
             print(f"{cantidad} billetes de Q{billete}")
            salir = input("\n¿Desea realizar otro retiro? (s/n): ")
            if salir.lower() == "n":
             bucle = False
             print("Gracias por usar el cajero automático")
             print("Hasta luego!") 
           




