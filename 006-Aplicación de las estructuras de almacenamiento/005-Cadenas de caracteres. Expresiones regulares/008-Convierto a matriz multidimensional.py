archivo = open("clientes.csv")

lineas = archivo.readlines()

conjunto_datos = []

for linea in lineas:
    partido = linea.split(",")
    conjunto_datos.append(partido)

print(conjunto_datos)