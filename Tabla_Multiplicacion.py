
print (f"\n--- Tabla del 1 al 12---")
for num in range(1, 13):
 for i in range(1, 13):
    resultado = num * i
    print (f"{num} x {i:2d} = {resultado:3d}")