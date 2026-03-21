Diccionario = {
    'nombre': 'Luis',
    'edad' : '23',
    'ciudad':'Escuintla',
    'lenguaje_favorito':'Python'
}

Diccionario['edad'] = 24
for k, v in Diccionario.items():
    print(f'{k}: {v}')
print('email' in Diccionario)
print(Diccionario.get('telefono', 'No se encontró'))

import agregar as ag
ag.agregar('telefono', '12345678', Diccionario)
print(Diccionario)