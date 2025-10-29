
class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
    def setNombreCompeto(self,nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return  self.nombrecompleto
    def getEmail(self):
        return self.email
    
clientes = []
    
print("Gestor de clientes v0.1 Ruth SainzSantos-Olmo")
while True: 
    print("Selecciona una opción: ")
    print("1.- Insertar un nuevo Cliente")
    print("2.-Obtener listado de clientes")
    opcion = int(input("Escoja su opcion (1,2): "))

    if opcion ==1 :
        print("voy a insertar un cliente")
        nuevocliente = Cliente()
        nombrecliente = input("Introduce el nombre del cliente")#Tomo el dato
        nuevocliente.setNombreCompeto(nombrecliente) #Uso el metodo set para meter  el dato en el objeto
        emailcliente = input("Introduce el email del cliente") #Tomo el dato

    elif opcion ==2 : #Los GETTERS se usan en las operaciones de listado
        print("Saco el listado de clientes")

    for cliente in clientes:
        print("------------------------------------------")
        print("Nombre: ",cliente.getNombreCompleto())
        print("Email: ",cliente.getEmail())
        print("------------------------------------------")