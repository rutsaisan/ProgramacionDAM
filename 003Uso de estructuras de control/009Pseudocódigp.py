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
#En funcion de la opción que coja el uruario
 # O bien creamos un nuevo producto
 # O bien listamos los productos
 # O bien actualizamos los productos
 # O bien eliminamos los productos
#Y volvemos a repetir