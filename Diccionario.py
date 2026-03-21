def actualizar_edad(dic, nueva_edad):
    """Actualiza el valor de la clave 'edad' en el diccionario."""
    dic['edad'] = nueva_edad
    return dic


Diccionario = {
    'nombre': 'Luis',
    'edad' : 23,
    'ciudad':'Escuintla',
    'lenguaje_favorito':'Python'
}
Diccionario.update({'universidad':'USPG'})

# Actualizar la edad usando la función
actualizar_edad(Diccionario, 24)

for k, v in Diccionario.items():
    print(f'{k}: {v}')
print('email' in Diccionario)
print(Diccionario.get('telefono', 'No se encontró'))