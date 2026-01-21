# Clase base Persona
class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def dameDatos(self):
        # Devuelve el nombre completo
        return self.nombre + " " + self.apellidos


# Clase Profesor que hereda de Persona
class Profesor(Persona):
    def dameDatos(self):
        # Sobrescribe el método para añadir el título "Profesor"
        return "Profesor: " + self.nombre + " " + self.apellidos


# Clase Alumno que hereda de Persona
class Alumno(Persona):
    def __init__(self, nombre, apellidos, email):
        # Llamamos al constructor de la superclase Persona
        Persona.__init__(self, nombre, apellidos)
        self.email = email

    def dameDatos(self):
        # Sobrescribe el método para añadir el título "Alumno"
        return "Alumno: " + self.nombre + " " + self.apellidos + " " + self.email


# Pruebas de la jerarquía de clases

# Creo un profesor
profesor = Profesor("Jose Vicente", "Carratala")

# Creo un alumno
alumno = Alumno("Jose Vicente", "Carratala", "info@jocarsa.com")

# Llamo a dameDatos en cada instancia
print(profesor.dameDatos())
print(alumno.dameDatos())