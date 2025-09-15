from ast import While
lunes = ["correr", "programar"]
while True :
     print("Este es un programa para insertar y remover tareas para el dia lunes")
     print("1. Insertar tareas")
     print("2. Remover Tareas")
     print("3. Salir")
     rta = int(input())
     if rta == 1 :
         print("Inserte la tarea a alistar")
         tarea = input()
         lunes.append(tarea)
         print("Tarea Insertada")
         print(lunes)
     elif rta == 2 :
         print("Inserte la tarea a remover")
         tarea = input()
         if tarea in lunes:
             lunes.remove(tarea)
             print("Tarea Removida")
             print(lunes)
         else:
             print("La tarea no se encuentra en la lista")
     elif rta == 3 :
         print("Gracias por usar el programa")
         break
     else:
         print("Opción inválida. Intente de nuevo.")