class Videojuego():
    def __init__(self):
        self.nombre = ""
        self.plataformas = ['','']
    def mostrar_videojuego(self):
     print("Nombre videojuego: ",self.nombre)
     print("Plataforma en las que esta disponible: ",self.plataformas)

videojuego1 = Videojuego()
videojuego1.nombre = "Cult of the Lamb"
videojuego1.plataformas = ['PC','Nintendo']

videojuego1.mostrar_videojuego()

