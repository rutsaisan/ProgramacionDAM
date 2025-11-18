print("Lista de videojuegos v0.1")
import json # Para usar la libreria tengo que importarla


lista_de_juegos = []

while True:
    print("Selecciona una opcion")
    print("1.- Añadir un nuevo juego jugado")
    print("2.- Leer la lista de videojuegos")

    opcion = int(input(" Selecciona tu opcion: "))
    
    if opcion == 1 :
        print("Añadimos un nuevo juego")
        nombre =  input("Indica el nombre del juego: ")
        precio = input("Indica el precio del juego: ")
        descripcion = input("Añade una breve descripción del juego: ")
        calificacion = input("Calificalo del 1 al 5: ")


        lista_de_juegos.append({"nombre":nombre,"precio":precio,"descripcion":descripcion,"calificacion":calificacion})
        
        archivo = open("ListaJuegos.json","w")       #Abro un archivo
        json.dump(lista_de_juegos, archivo) #Guardo en json
        archivo.close()                        #Cierro el archivo
    
    elif opcion == 2:
        print("Listamos los elementos de la lista")
        for juego in lista_de_juegos:
            print("##################################")
            print("Juego:", juego['nombre'])
            print("Precio:", juego['precio'])
            print("Descripcion:", juego['descripcion'])
            print("Calificacion del 1 al 5:", juego['calificacion'])
            print("##################################")# Esto es estético, separador