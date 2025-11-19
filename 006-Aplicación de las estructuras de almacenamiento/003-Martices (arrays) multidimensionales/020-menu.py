import pickle
agenda = []

# Intentar cargar la agenda si existe
try:
    with open("agenda.bin", "rb") as archivo:
        agenda = pickle.load(archivo)
except FileNotFoundError:
    print("⚠ No hay archivo guardado, se creará uno nuevo.")

while True:
    print("Selecciona una opción:")
    print("1.-Insertar registros")
    print("2.-Leer registros")
    print("3.-Guardar registros")
    print("4.-Borrar registros")
    print("5.-Salir del programa")
    opcion = int(input("Opción escogida: "))

    if opcion == 1:
        #Insertar
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tus apellidos: ")
        email = input("Dime tu email: ")
        telefono = input("Dime tu teléfono: ")
        #Añado a la agenda
        agenda.append([nombre,apellidos,email,telefono])
    if opcion == 2:
        #Imprimir
        print(agenda)

    if opcion == 3:
        #Guardar
        archivo = open("agenda.bin","wb")
        pickle.dump(agenda,archivo)
        archivo.close
        print("Los archivos se han guardado correctamente✅")
    if opcion == 4:
        print(agenda)
        eliminar = int(input("Numero del elemento que quieres eliminar: "))
        agenda.pop(eliminar)
        print(agenda)
    if opcion == 5:
        break
