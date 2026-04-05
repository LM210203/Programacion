def cifrar_caracter(c, desplazamiento):
    if 'a' <= c <= 'z':  # solo letras minúsculas
        base = ord('a')
        pos = ord(c) - base
        nueva_pos = (pos + desplazamiento) % 26
        return chr(base + nueva_pos)
    else:
        return c  # deja espacios, números, signos igual

def cifrar_mensaje(mensaje, desplazamiento):
    mensaje = mensaje.lower()  # todo en minúsculas
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)

def fuerza_bruta(mensaje_cifrado):
    print("\n=== Fuerza bruta César ===")
    for d in range(1, 27):
        posible = descifrar_mensaje(mensaje_cifrado, d)
        print(f"Desplazamiento {d}: {posible}")

# Ejemplo de uso:
mensaje = "hola mundo"
cifrado = cifrar_mensaje(mensaje, 3)
print(f"Mensaje original: {mensaje}")
print(f"Cifrado (desplazamiento 3): {cifrado}")

descifrado = descifrar_mensaje(cifrado, 3)
print(f"Descifrado: {descifrado}")

# Bonus: probar fuerza bruta
fuerza_bruta(cifrado)