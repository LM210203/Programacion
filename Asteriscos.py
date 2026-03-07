n = 12
if n % 2 == 0:
    n += 1
mitad = n // 2


for i in range(mitad + 1):
    espacios = mitad - i
    estrellas = 2 * i + 1
    print(" " * espacios + "*" * estrellas)

for i in range(mitad - 1, -1, -1):
    espacios = mitad - i
    estrellas = 2 * i + 1
    print(" " * espacios + "*" * estrellas)

