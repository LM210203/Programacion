print("Coloque Temperatura en Celsius para convertir a Fahrenheit")
Temp = int(input("Ingrese la temperatura en Celsius: "))
Fahrenheit = (Temp * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {Fahrenheit}°F")
if Temp < 15:
    print("Hace frío")  
elif Temp >= 15 and Temp <= 25:
    print("Hace fresco")
else:
    print("Hace calor")