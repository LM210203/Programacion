
def conversor(temp, unidad_origen, unidad_destino):
    if unidad_origen == "C" and unidad_destino == "F":
        return temp * 9/5 + 32
    elif unidad_origen == "C" and unidad_destino == "K":
        return temp + 273.15
    elif unidad_origen == "C" and unidad_destino == "R":
        return temp * 9/5 + 491.67
    elif unidad_origen == "F" and unidad_destino == "C":
        return (temp - 32) * 5/9
    elif unidad_origen == "F" and unidad_destino == "K":
        return (temp - 32) * 5/9 + 273.15
    elif unidad_origen == "F" and unidad_destino == "R":
        return temp + 459.67
    elif unidad_origen == "K" and unidad_destino == "C":
        return temp - 273.15
    elif unidad_origen == "K" and unidad_destino == "F":
        return (temp - 273.15) * 9/5 + 32
    elif unidad_origen == "K" and unidad_destino == "R":
        return temp * 9/5
    elif unidad_origen == "R" and unidad_destino == "C":
        return (temp - 491.67) * 5/9
    elif unidad_origen == "R" and unidad_destino == "F":
        return temp - 459.67
    elif unidad_origen == "R" and unidad_destino == "K":
        return temp * 5/9
    else:
        raise ValueError("Unidades no válidas. Use 'C', 'F', 'K' o 'R'.")
    
input_temp = float(input("Ingrese la temperatura a convertir: "))
input_unidad_origen = input("Ingrese la unidad de origen (C, F, K, R): ").upper()
input_unidad_destino = input("Ingrese la unidad de destino (C, F, K, R): ").upper()
try:
    resultado = conversor(input_temp, input_unidad_origen, input_unidad_destino)
    print(f"{input_temp} {input_unidad_origen} son {resultado:.2f} {input_unidad_destino}.")
except ValueError as e:
    print(e)
        