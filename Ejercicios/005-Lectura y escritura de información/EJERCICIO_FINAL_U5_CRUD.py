import pickle

class Cliente ():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


clientes = []

try: #### Ojo q igual no existe el archivo ####
    archivo = open("clientes.bin",'rb')
    clientes = pickle.load(archivo)
    archivo.close()

except:
    print("No existe archivo de datos")


while True:
    archivo = open("clientes.bin","wb")
    pickle.dump(clientes,archivo)
    archivo.close()

    print("Escoge una opción :")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")

    opcion = int(input("Escoge una opcion: "))
    
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")

        clientes.append(Cliente(nombre,apellidos,email))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
         print("Este es el cliente con ID: ",identificador)
         print(cliente.nombre,cliente.apellidos,cliente.email)
         identificador += 1