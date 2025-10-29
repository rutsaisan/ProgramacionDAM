class Gato():
    def __init__(self):
        self.color = "" #Esto es una propiedad

    def maulla(self): #Esto e sun método (es una accion)
        return "miau"
    
    def setColor(self,nuevocolor): #Defino un setter-el método es el responsable de cambiar la propiedad
        #Por ejemplo aquí podia validar si elcolor es válido para el gato o no
        self.color =   nuevocolor     #Y cambio la propiedad

gato1 = Gato()
gato1.color = "naranja" #Aquí seteamos una propiedad directamente (no es buena practica)

gato1.setColor("naranja") #Esto es una práctica mucho mejor

print(gato1.color) #Acceso directo,se puede pero no se recomienda

print(gato1.getColor()) #Acceso mediante método, se recomienda

