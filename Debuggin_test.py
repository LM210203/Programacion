password = input("Clave: ")

print(f"DEBUG tipo: {type(password)}")

print(f"DEBUG valor: [{password}]")

print(f"DEBUG len: {len(password)}")

if password == 1234: # Bug aquí!
 print("Acceso concedido")
else:
 print("Acceso denegado")