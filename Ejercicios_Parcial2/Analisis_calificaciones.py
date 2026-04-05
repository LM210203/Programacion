def promedio(notas):
    return sum(notas) / len(notas)

def mayor(notas):
    maximo = notas[0]
    for n in notas:
        if n > maximo:
            maximo = n
    return maximo

def menor(notas):
    minimo = notas[0]
    for n in notas:
        if n < minimo:
            minimo = n
    return minimo

def contar_aprobados(notas, minimo=61):
    contador = 0
    for n in notas:
        if n >= minimo:
            contador += 1
    return contador

def reporte(notas):
    print("=== REPORTE DE NOTAS ===")
    print(f"Promedio: {promedio(notas):.2f}")
    print(f"Mayor nota: {mayor(notas)}")
    print(f"Menor nota: {menor(notas)}")
    print(f"Aprobados (mínimo 61): {contar_aprobados(notas)}")
    print("\nHistograma de notas:")
    histograma(notas)

def histograma(notas):
    for n in notas:
        barras = "*" * (n // 10)  # cada 10 puntos = una barra
        print(f"{n}: {barras}")

# Prueba con la lista de notas
notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
reporte(notas)

