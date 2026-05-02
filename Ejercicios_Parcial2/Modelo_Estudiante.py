class Estudiante:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota) 

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    def aprobar_materia(self, nota_minima):
        promedio = self.calcular_promedio()
        return promedio >= nota_minima
    

# Ejemplo de uso
nota_minima = 61
estudiante1 = Estudiante("Juan Perez", "20210001", "Ingeniería en Sistemas")    
estudiante1.agregar_nota(100)
estudiante1.agregar_nota(38)
print(f"Promedio de {estudiante1.nombre}: {estudiante1.calcular_promedio()}")

if estudiante1.aprobar_materia(nota_minima):
    print(f"{estudiante1.nombre} ha aprobado la materia.")
else:    print(f"{estudiante1.nombre} no ha aprobado la materia.")
