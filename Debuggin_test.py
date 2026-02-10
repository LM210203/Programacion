def validar_contraseña(password):
    """
    Valida una contraseña según los siguientes criterios:
    - Mínimo 8 caracteres
    - No pueden ser solo números
    - No pueden ser solo letras
    - No pueden contener espacios
    """
    errores = []
    
    if len(password) < 8:
        errores.append("❌ La contraseña debe tener al menos 8 caracteres")
    
    if " " in password:
        errores.append("❌ la contraseña no puede contener espacios")
    
    if password.isdigit():
        errores.append("❌ La contraseña no puede ser solo números")
    
    if password.isalpha():
        errores.append("❌ La contraseña no puede ser solo letras")
    
    return errores

# Programa principal
print("=" * 50)
print("VALIDADOR DE CONTRASEÑAS")
print("=" * 50)

while True:
    password = input("\nIngrese una contraseña: ")
    errores = validar_contraseña(password)

    if not errores:
        print("\n✅ ¡Contraseña válida! Acceso concedido")
        break
    else:
        print("\n❌ Contraseña inválida. Errores encontrados:")
        for error in errores:
            print(f"  {error}")
        print("\nIntentando de nuevo...\n")