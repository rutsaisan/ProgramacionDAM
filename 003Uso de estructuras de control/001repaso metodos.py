class Gato():
    def __init__(self):
        self.color = "" #Esto es una propiedad

    def maulla(self): #Esto e sun método (es una accion)
        return "miau"
   

gato1 = Gato()
gato1.color = "naranja" #Aquí seteamos una propiedad directamente (no es buena practica)
print(gato1.maulla()) #Aqui llamamos a un método

