Diccionario = {
    'nombre': 'Luis',
    'edad' : '23',
    'ciudad':'Escuintla',
    'lenguaje_favorito':'Python'
}
Diccionario.update({'universidad':'USPG'})
Diccionario['edad'] = 24
for k, v in Diccionario.items():
    print(f'{k}: {v}')
print('email' in Diccionario)
print(Diccionario.get('telefono', 'No se encontró'))

a=input('Ingrese la clave a agregar: ')
b=input('Ingrese el valor a agregar: ')
Diccionario.update({ a : b })
print(Diccionario)

