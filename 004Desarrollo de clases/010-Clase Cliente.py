#Poco escalable - uso de muchas variables
cliente1_email = "info@jocarsa.com"
cliente1_direccion = "La calle de Jose Vicente"
cliente1_nombre = "Jose Vicente"
cliente1_apellidos ="Carratala Sanchis"

cliente2_email = "info@jumaech.com"
cliente2_direccion = "La calle del Juan José"
cliente2_nombre = "Juan José"
cliente2_apellidos ="Maya Echeverri"

#Mucho mejor: uso de clases
class Cliente:
    def __init__(self):
        self.email = ""
        self.direccion = "" 
        self.nombre = ""
        self.apellidos = ""

cliente1 = Cliente()
cliente1.email = "info@jumaech.com"
cliente1.direccion = "La calle de Jose Vicente"
cliente1.nombre = "Jose Vicente"
cliente1.apellidos ="Carratala Sanchis"

cliente2 = Cliente()
cliente2.email = "info@cliente2.com"
cliente2.direccion = "La calle del Juan José"
cliente2.nombre = "Juan José"
cliente2.apellidos ="Maya Echeverri"
