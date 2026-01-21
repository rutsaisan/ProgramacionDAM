# Defino la superclase Alumno
class Alumno:
    def __init__(self, nombre, apellido, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion

def dameDatos(self):
    return self.nombre + " " + self.apellido + " - " + self.email + " - " + self.direccion


# Subclase AlumnoOnline que hereda de Alumno
class AlumnoOnline(Alumno):
    pass


# Subclase AlumnoPresencial que hereda de Alumno
class AlumnoPresencial(Alumno):
    pass


# Instancio un alumno online
alumno_online = AlumnoOnline(
    "Jose Vicente",
    "Carratala",
    "info@jocarsa.com",
    "Direccion"
)

# Instancio un alumno presencial
alumno_presencial = AlumnoPresencial(
    "Jose Vicente",
    "Carratala",
    "info@jocarsa.com",
    "Direccion"
)

# Imprimo los datos usando el método heredado dameDatos
print("Alumno online:", alumno_online.dameDatos())
print("Alumno presencial:", alumno_presencial.dameDatos())