import pickle

# Definimos la estructura de datos: una lista multidimensional
agenda = []

# Inserción de registros
while True:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    telefono = input("Introduce el teléfono: ")

    # Cada contacto es una lista con 4 elementos
    contacto = [nombre, apellidos, email, telefono]
    agenda.append(contacto)

    continuar = input("¿Quieres añadir otro contacto? (s/n): ")
    if continuar.lower() != 's':
        break

# Guardar la agenda de forma persistente
with open("agenda.pkl", "wb") as archivo:
    pickle.dump(agenda, archivo)

print("Agenda guardada correctamente.")

# Leer y mostrar los registros guardados
with open("agenda.pkl", "rb") as archivo:
    agenda_cargada = pickle.load(archivo)

print("📌 Contactos almacenados en la agenda:")
for contacto in agenda_cargada:
    print(f"Nombre: {contacto[0]}, Apellidos: {contacto[1]}, Email: {contacto[2]}, Teléfono: {contacto[3]}")

'''# Función extra inspirada en hobbies: búsqueda de contactos
def buscar_contacto(agenda, criterio):
    print("🔎 Resultados de búsqueda para:" +  criterio)
    encontrado = False
    for contacto in agenda:
        if criterio in contacto:
            print("Nombre: " +contacto[0]+", Apellidos: "+contacto[1]+", Email:" +contacto[2]+", Teléfono:"+ contacto[3])
            encontrado = True
    if not encontrado:
        print("No se encontró ningún contacto con ese criterio.")

# Ejemplo de uso de la búsqueda
criterio = input("Introduce un nombre o email para buscar: ")
buscar_contacto(agenda_cargada, criterio)'''