import tkinter as tk
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="EmpresaDAM2526$",
    database="empresadam"
)

cursor = conexion.cursor()
cursor.execute('''
  SELECT * FROM clientes;     
 ''')
    
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.commit()
cursor.close()
conexion.close()