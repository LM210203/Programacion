def validar_contra(contra):
    if len(contra) < 8:
        return False
    if not any(char.isupper() for char in contra):
        return False
    if not any(char.islower() for char in contra):
        return False
    if not any(char.isdigit() for char in contra):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in contra):
        return False
    if any(contra[i] == contra[i+1] == contra[i+2] for i in range(len(contra) - 2)):
        return False
    return True

def diagnostico_contra(contra):
    errores = []
    if len(contra) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")
    if not any(char.isupper() for char in contra):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")
    if not any(char.islower() for char in contra):
        errores.append("La contraseña debe contener al menos una letra minúscula.")
    if not any(char.isdigit() for char in contra):
        errores.append("La contraseña debe contener al menos un número.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in contra):
        errores.append("La contraseña debe contener al menos un carácter especial.")
    if any(contra[i] == contra[i+1] == contra[i+2] for i in range(len(contra) - 2)):
        errores.append("La contraseña no debe contener tres caracteres iguales consecutivos.")
    if errores:
        return "\n".join(errores)
    return "La contraseña es válida."

contra_usuario = input("Ingrese su contraseña: ")
if validar_contra(contra_usuario):
    print("Contraseña válida.")
else:
    print("Contraseña inválida, Tome en cuenta lo siguiente:")
    print(diagnostico_contra(contra_usuario))   