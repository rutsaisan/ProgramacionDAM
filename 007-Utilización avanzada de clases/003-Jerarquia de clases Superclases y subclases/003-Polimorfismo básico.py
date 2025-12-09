class Profesor():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
  def dameDatos(self):
    return self.nombre+self.apellidos

class Alumno():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
  def dameDatos(self):
    return self.nombre+self.apellidos
    
alumno1 = Alumno("Ruth","Sainz Santos-Olmo","rutsaisan.code@gmail.com")
print(alumno1)

profesor1 = Profesor("Jose Vicente","Carratala","info@jocarsa.com")
print(profesor1)