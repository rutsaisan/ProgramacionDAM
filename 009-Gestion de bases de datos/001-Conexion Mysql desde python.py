import mysql.connector

conn = mysql.connector.connect(
    host="172.24.103.203",
    user="empresa2026",
    password="Empresa2026$",
    database="empresadam2026"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
