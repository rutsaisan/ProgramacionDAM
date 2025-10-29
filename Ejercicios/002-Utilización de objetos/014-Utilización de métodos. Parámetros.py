class MiHobby():
    def __init__(self):
        self.nombre = ""
        self.tiempo_dedicado = ""
    def mostrar_hobbie(self):
       return( "EL hobbie es: "+ self.nombre + " y le dedico: "+ self.tiempo_dedicado + " minutos")

hobbie1 = MiHobby()
hobbie1.nombre = "Jugar Videjuegos" 
hobbie1.tiempo_dedicado = "90"
print (hobbie1.mostrar_hobbie())

hobbie2 = MiHobby()
hobbie2.nombre = "Ver series y películas" 
hobbie2.tiempo_dedicado = "120"
print (hobbie2.mostrar_hobbie())