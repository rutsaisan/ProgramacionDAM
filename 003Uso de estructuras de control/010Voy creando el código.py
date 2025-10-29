'''
 Aplicacion de gestión de productos
 (c) 2025 Ruth Sainz Santos-Olmo
 Esta aplicación gestiona productos
'''

#Ene sta aplicacion no aplica importar librerias

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0

#Creamos las variables globales

productos = []

#Primero lanzamos un mensaje de bienvenida
print("Gestión de productos v0.1 Ruth Sainz Santos-Olmo")
#Metemos al usuario en un bloque infinito
while True:
#En funcion de la opción que coja el uruario
 print("Selecciona una opción: ")
 print("1.-Crear un  nuevo producto")
 print("2.-Listar productos")
 print("3.-Actualizar productos")
 print("4.-Eliminar productos")
 opcion = int(input("Escoge tu opción: "))
 # O bien creamos un nuevo producto
 if opcion == 1:
    print("Creamos un nuevo producto")
    producto = Producto()
    producto.nombre = input("Introduce el nombre del producto: ")
    producto.precio = input("Introduce el precio del producto: ")
    productos.append(producto)

 # O bien listamos los productos

 elif opcion == 2:
  print("Vamos a listar los productos")

 # O bien actualizamos los productos
 elif opcion == 3:
   print("Vamos a actualizar los productos")
 # O bien eliminamos los productos
 elif opcion == 4:
   print("Vamos a liminar productos")
#Y volvemos a repetir