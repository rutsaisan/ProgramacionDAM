class Cliente:
  def __init__(self):
    self.email = ""
    self.direccion = "" 
    self.nombre = ""

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

# Le permito escoger una opción
opcion = input("Escoge una opción: ")
opcion = int(opcion)   # Convierto a entero

clientes = []   # Creo una lista VACIA

while True: # Esto desata un bucle infinito pero controlado
  if opcion == 1:
    print("Vamos a insertar un cliente")
    cliente1 = Cliente()
    cliente1.email = input("Nombre del cliente: ")
    cliente1.direccion = input("Direccion del cliente: ")
    cliente1.nombre = input("Email del cliente: ")
  elif opcion == 2:
    print("Vamos a ver los clientes")

  elif opcion == 3:
    print("Vamos a actualizar un cliente")
  elif opcion == 4:
    print("Vamos a eliminar un cliente")
  else:
    break

