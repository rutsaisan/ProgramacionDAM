class Juego():
    def __init__(self):
        self.nombre = ""
        self.categoria = ""
        self.tiempo_jugado = 0
    
    def actualizar_tiempo_juego(self,nuevo_tiempo_jugado):
       self.tiempo_jugado = nuevo_tiempo_jugado

    def mostrar_juego(self):
        return "El nombre del juego es: "+self.nombre+", su categoría es: " +self.categoria+ " y el tiempo de juego es: "+ str(self.tiempo_jugado)


class Serie ():
 def __init__(self):
    self.nombre = ""
    self.numero_temporadas = 0
    self.episodios_vistos= 0
 
 def actualizar_episodios_vistos(self,nuevos_episodios_vistos):
       self.episodios_vistos = nuevos_episodios_vistos

 def mostrar_serie(self):
        return "El nombre de la serie es: " + self.nombre + " , tiene " + str(self.numero_temporadas)+ "  temporadas y he visto "+ str(self.episodios_vistos)+ " episodios"

class ListaDeActividades():
    def __init__(self):
        self.juegos = [Juego]
        self.series = [Serie]

    def AddJuego (self,nuevo_juego):
           self.juegos.append(nuevo_juego)
    
    def AddSerie (self,nueva_serie):
           self.series.append(nueva_serie)

juego1 = Juego()
juego1.nombre = "Tomb Rider"
juego1.categoria = "Accion"
juego1.tiempo_jugado = 75
print(juego1.mostrar_juego())
listamisactividades=ListaDeActividades()
listamisactividades.AddJuego(juego1)
