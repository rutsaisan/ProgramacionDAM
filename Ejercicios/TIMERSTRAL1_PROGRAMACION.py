
import mysql.connector
 
# Conexión a la base de datos con usuario seguro
db = mysql.connector.connect(
    host="localhost",
    user="usuario_portafolioexamen",  # Usuario creado previamente
    password="P0rtaF0li0*ExAm3n",
    database="portafolioexamen"
)
 
cursor = db.cursor()
 
# Mensaje de bienvenida
print("===================================")
print("  Bienvenido a tu Portafolio  ")
print("===================================\n")
 
# Bucle principal infinito
while True:
    print("Opciones disponibles:")
    print("1 - Crear nueva pieza")
    print("2 - Ver todas las piezas")
    print("3 - Actualizar una pieza")
    print("4 - Borrar una pieza")
    print("5 - Salir")
 
    opcion = input("Selecciona una opción (1-5): ")
 
    #Crear nueva pieza
    if opcion == "1":
        titulo = input("Título de la pieza: ")
        descripcion = input("Descripción de la pieza: ")
        fecha = input("Fecha en la que estas creando esta pieza: ")
        id_categoria = input("ID de la categoría a la que pertenece la pieza: ")
 
        # Insert usando parámetros para seguridad
        sql = "INSERT INTO piezasportafolio (titulo, descripcion, fecha, id_categoria) VALUES (%s, %s, %s, %s, %s)"
        valores = (titulo, descripcion, fecha, id_categoria)
        cursor.execute(sql, valores)
        db.commit()
        print("Pieza creada correctamente.")
 
    # Ver todas las piezas
    elif opcion == "2":
        sql = """
        SELECT piezasportafolio.Identificador, piezasportafolio.titulo, piezasportafolio.descripcion, piezasportafolio.fecha, categoriasportafolio.nombre
        FROM piezasportafolio
        LEFT JOIN categoriasportafolio ON piezasportafolio.id_categoria = categoriasportafolio.Identificador
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print("--- Lista de piezas ---")
        for fila in resultados:
            print("ID:", fila[0], "| Título:", fila[1], "| Descripción:", fila[2], "| Fecha:", fila[3], "| Categoría:", fila[4])
 
    # Actualizar una pieza
    elif opcion == "3":
        id_pieza = input("Ingresa el ID de la pieza a actualizar: ")
        nuevo_titulo = input("Nuevo título: ")
        nueva_descripcion = input("Nueva descripción: ")
        sql = "UPDATE piezasportafolio SET titulo = %s, descripcion = %s WHERE Identificador = %s"
        valores = (nuevo_titulo, nueva_descripcion, id_pieza)
        cursor.execute(sql, valores)
        db.commit()
        print("Pieza actualizada correctamente.")
 
    # Borrar una pieza
    elif opcion == "4":
        id_pieza = input("Ingresa el ID de la pieza a borrar: ")
        sql = "DELETE FROM piezasportafolio WHERE Identificador = %s"
        cursor.execute(sql, (id_pieza,))
        db.commit()
        print("Pieza eliminada correctamente.")
 
    # Salir de la aplicación
    elif opcion == "5":
        print("Saliendo de la aplicación. ¡Hasta luego!")
        break
 
    # Opción inválida
    else:
        print("Opción no válida, intenta nuevamente.")
 
# Cerrar conexión
cursor.close()
db.close()
 
 