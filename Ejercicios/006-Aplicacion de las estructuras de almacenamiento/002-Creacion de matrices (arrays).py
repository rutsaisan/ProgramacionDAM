import pickle

# Lista principal del menú
menu = []

# Empezamos el bucle infinito
while True:
    print("Opciones:")
    print("1.- Introducir nueva comida en el menú")
    print("2.- Listar comidas en el menú")
    print("3.- Guardar en archivo")
    print("4.- Salir")

    opcion = int(input("Selecciona una opción: "))  # Recogemos la opcion que quiere el usuario

    if opcion == 1:
        # Preguntamos la comida al usuario
        comida = input("Introduce el nombre de la comida: ")
        # Añadimos la respuesta del usuario al menu
        menu.append(comida)
        print( comida + "ha sido añadida al menú.\n")

    elif opcion == 2:
          # Si esta vacio se lo indicamos al usuario
          if len(menu) == 0:
           print("El menú está vacío.\n")
          else:
            # Listamos el contenido de menu
            print("Comidas actuales en el menú:")
            for comida in menu:
                print(comida)

    elif opcion == 3:
        archivo = open("datos.bin", "wb")  # Abrimos el archivo en el que vamos a guardar los datos
        pickle.dump(menu, archivo)    # Guardamos los datos
        archivo.close()               #Cerramos el archivo
        print(" Se ha guardado con éxito.\n")

    elif opcion == 4:
        print("Adiós, vuelve cuando tengas mas comida!") # Mostramos un mensaje de despedida
        break                # Rompemos el bucle infinito