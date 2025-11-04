class Cliente:
  def __init__(self):
    self.email = ""
    self.direccion = "" 
    self.nombre = ""
    self.apellidos = ""
  def mostrar_info(self):
    print("Información del Cliente:")
    print("Nombre: ",self.nombre)
    print("Apellido: ",self.apellidos)
    print("Email: ",self.email)
    print("Dirección: ",self.direccion)


cliente1 = Cliente()
cliente1.email = "carmenmoliner@gmail.com"
cliente1.direccion = "La direccion de Carmen"
cliente1.nombre = "Carmen"
cliente1.apellidos = "Moliner Fernandez"

cliente2 = Cliente()
cliente2.email = "iriaordovas@gmail.com"
cliente2.direccion = "La direccion de Iria"
cliente2.nombre = "Iria"
cliente2.apellidos = "Ordovas"

cliente1.mostrar_info()
cliente2.mostrar_info()
