print("Lista de la compra v0.1")

lista_de_la_compra = []

while True:
    print("Selecciona una opcion")
    print("1.- Añadir un elemento a la lista")
    print("2.- Leer la lista")

    opcion = int(input(" Sekecciona tu opcion: "))
    
    if opcion == 1 :
        print("Aladimos un elementoa  la lista")
        nombre =  input("Indica el nombre del producto: ")
        cantidad = input("Indica la contidad del producto: ")

        lista_de_la_compra.append({"nombre":nombre,"cantidad":cantidad})
    
    elif opcion == 2:
        print("Listamos los elementos de la lista")
        print(lista_de_la_compra)