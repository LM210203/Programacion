tareas = []
while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    print ("5. Marcar tarea como completada")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":  
        tarea = input("Ingrese la tarea: ")
        tareas.append(tarea)
        print("Tarea agregada.")
    elif opcion == "2":
        for i, t in enumerate (tareas, 1):
            print(f"{i}. {t}")
    elif opcion == "3":
        idx = int(input("Ingrese el número de la tarea a eliminar: "))
        tareas.pop (idx - 1)
        print("Tarea eliminada.")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    elif opcion == "5":
        idx = int(input("Ingrese el número de la tarea a marcar como completada: "))
        tareas[idx - 1] += " (completada)"
        print("Tarea marcada como completada.")