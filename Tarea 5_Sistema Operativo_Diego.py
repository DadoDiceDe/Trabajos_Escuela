print("¡Bienvenido! Este programa le ayudara a mantener un registro contstante de sus tareas.")
print("El funcionamiento del programa es asi, A cada\n")
print("tarea se le puede asignar un valor, o 1 o 0.\n")
print("El numero 0 indica que la tarea aun no se ha realizado.\n")
print("El numero 100 indica que la tarea se ha terminado.\n")
def menu():
    print("[1] Ver todas las tareas")
    print("[2] Escoger una tarea")
    print("[3] Cambiar valor")
    print("[4] Salir")
            
menu()
n = ''
opc = int(input("Seleccione alguna opción: "))
            
grupo_Tareas = {
    'Tarea 1': "0/100",
    'Tarea 2': "0/100",
    'Tarea 3': "0/100",
    'Tarea 4': "0/100",
    'Tarea 5': "0/100",
    'Tarea 6': "0/100",
    'Tarea 7': "0/100",
    'Tarea 8': "0/100",
    'Tarea 9': "0/100",
    'Tarea 10': "0/100",
}
while opc != 4:
    if (opc == 1):
        for x, y in grupo_Tareas.items():
            print(x, y)
        input("Presione cualquier boton para continuar.")
        print()
        menu()
        opc = int(input("Seleccione alguna opción: "))
    elif (opc == 2):
        n = input("¿Que tarea quieres ver? ")
        print(n)
        print(grupo_Tareas.get(n))
        input("Presione cualquier boton para continuar.")
        print()
        menu()
        opc = int(input("Seleccione alguna opción: "))
    elif (opc ==3):
        n = input("¿Que tarea quieres cambiar? ")
        c = input("Si completaste la tarea pon 100, sino pon 0: ")
        grupo_Tareas[n] = c+"/100"
        print(n)
        print(grupo_Tareas.get(n))
        input("Presione cualquier boton para continuar.")
        print()
        menu()
        opc = int(input("Seleccione alguna opción: "))
    else:
        print("La opción no es valida")
        print()
        menu()
        opc = int(input("Seleccione alguna opción: "))
while opc==4:
    print("Apagando...")
    break
