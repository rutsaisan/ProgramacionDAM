import pickle

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Ruth","rutsaisan@gmail.com"))
clientes.append(Cliente("Juan","juan@gmail.com"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()