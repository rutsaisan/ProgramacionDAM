archivo = open("clientes.csv")

lineas = archivo.readlines()

for linea in lineas:
    partido = linea.split(",")
    print(partido)