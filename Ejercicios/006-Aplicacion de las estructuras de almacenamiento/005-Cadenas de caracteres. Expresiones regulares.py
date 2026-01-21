# Abrir el archivo clientes.csv en modo lectura
archivo = open("clientes.csv", "r")

# Leer todas las líneas y guardarlas en una lista
lineas = archivo.readlines()

# Cerrar el archivo después de leer
archivo.close()

# Recorrer cada línea de la lista
for linea in lineas:
    # Eliminar el salto de línea final, si lo hay
    linea = linea.strip()
    
    # Dividir la línea por comas y guardar el resultado en 'partido'
    partido = linea.split(",")

    # Imprimir la lista con los detalles del cliente
    print(partido)