class Cliente:
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion

  #Método seter
  def set_email(self,nuevo_eamil):
    self.email = nuevo_eamil

  #Método getter
  def get_email(self):
    return "El email del cliente es: " + self.email

cliente1 = Cliente("María", "Gonzalvo Serrano", "mariagon@gmail.com", "La calle de María")
cliente2 = Cliente("Jorge", "Fajarí Saez", "jorgefajari@gmail.com", "La calle de Jorge")
cliente3 = Cliente("Arantxa", "Mundina Mengual", "arantxamundina@gmail.com", "La calle de Arantxa")

# Mostrar email original
print("Email original de cliente1:", cliente1.get_email())

# Cambiar email
cliente1.set_email("mariaa@gmail.com")

# Mostrar email actualizado
print("Email actualizado de cliente1:", cliente1.get_email())

# Repetimos para cliente2
print("Email original de cliente2:", cliente2.get_email())
cliente2.set_email("jorgefajarisaez@gmail.com")
print("Email actualizado de cliente2:", cliente2.get_email())

#Por ultimo cliente3
print("Email original de cliente3:", cliente3.get_email())
cliente3.set_email("arantxa21@gmail.com")
print("Email actualizado de cliente3:", cliente3.get_email())
