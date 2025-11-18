import pickle

menu = []

while True:
    print("Opciones:")
    print("1.- Introducir nueva comida en el menu")
    print("2.- Listar comidas del menu")
    print("3.- Guardar en archivo")
    print("4.- cargar datos de archivo")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
     comida = input("Introduce el nombre de la comida: ")
     menu.append(comida)
    elif opcion == 2:
     print("Tu comida hasta el momento es:")
     for elemento in menu:
        print(elemento)
    elif opcion == 3:
      archivo = open("datos.txt","wb") #Write Binary
      pickle.dump(menu,archivo)
      archivo.close()
      print("Se ha guardado con exito✅")
    elif opcion == 4:
      archivo = open("datos.txt","rb") #Read Binary
      menu = pickle.load(archivo) #Volcamos el archivpo en la lista
      archivo.close()
      print("Se ha cargado con exito✅")