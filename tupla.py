coordenadas_ciudad = [14.3916, -90.8358]
latitud, longitud = coordenadas_ciudad
print(f'Latitud: {latitud}, Longitud: {longitud}')

lista_prom=(85, 60 ,45, 64, 90)
def data(lista):
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return [promedio, maximo, minimo]

resultado = data(lista_prom)
print(f'Promedio: {resultado[0]}, Máximo: {resultado[1]}, Mínimo: {resultado[2]}')
 
