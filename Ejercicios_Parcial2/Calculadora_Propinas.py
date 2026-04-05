def calcular_propina(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)

def calcular_total(subtotal, propina):
    return subtotal + propina

def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: el número de personas debe ser mayor que 0."
    return total / personas

def aplicar_descuento(subtotal, descuento_pct):
    return subtotal * (1 - descuento_pct / 100)

def mostrar_menu():
    print("\n=== MENÚ DEL RESTAURANTE ===")
    print("1. Calcular propina")
    print("2. Dividir la cuenta entre personas")
    print("3. Aplicar descuento + propina")
    print("4. Salir")
    print("5. Resumen de operaciones (bonus)")

def main():
    historial = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                subtotal = float(input("Ingresa el subtotal: "))
                print("Sugerencias de propina: 10%, 15%, 20%")
                porcentaje = float(input("Ingresa el porcentaje de propina: "))
                propina = calcular_propina(subtotal, porcentaje)
                total = calcular_total(subtotal, propina)
                print(f"Propina: Q{propina:.2f}")
                print(f"Total a pagar: Q{total:.2f}")
                historial.append(f"Propina {porcentaje}% sobre Q{subtotal:.2f} → Q{propina:.2f}, total Q{total:.2f}")
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")

        elif opcion == "2":
            try:
                total = float(input("Ingresa el total de la cuenta: "))
                personas = int(input("Número de personas: "))
                resultado = dividir_cuenta(total, personas)
                print(f"Cada persona paga: {resultado}" if isinstance(resultado, float) else resultado)
                historial.append(f"División de Q{total:.2f} entre {personas} personas → {resultado}")
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")

        elif opcion == "3":
            try:
                subtotal = float(input("Ingresa el subtotal: "))
                descuento = float(input("Ingresa el porcentaje de descuento: "))
                nuevo_subtotal = aplicar_descuento(subtotal, descuento)
                porcentaje = float(input("Ingresa el porcentaje de propina: "))
                propina = calcular_propina(nuevo_subtotal, porcentaje)
                total = calcular_total(nuevo_subtotal, propina)
                print(f"Subtotal con descuento: Q{nuevo_subtotal:.2f}")
                print(f"Propina: Q{propina:.2f}")
                print(f"Total a pagar: Q{total:.2f}")
                historial.append(f"Descuento {descuento}% sobre Q{subtotal:.2f} → Q{nuevo_subtotal:.2f}, propina {porcentaje}% → Q{propina:.2f}, total Q{total:.2f}")
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")

        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

        elif opcion == "5":
            print("\n=== RESUMEN DE OPERACIONES ===")
            if historial:
                for h in historial:
                    print("-", h)
            else:
                print("No se han realizado operaciones aún.")

        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()