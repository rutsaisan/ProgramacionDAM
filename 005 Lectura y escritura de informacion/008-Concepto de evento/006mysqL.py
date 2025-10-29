# pip3 install mysql-connector-python --break-system-packages
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="EmpresaDAM2526$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    1,
    "12345678Z"
    "Ruth",
    "Sainz Santos-Olmo",
    "rutsaisan@gmail.com"
  );
''')

conexion.commit()

cursor.close()
conexion.close()