import pymysql

conn = pymysql.connect(
    host="172.24.103.203",
    user="empresa2026",
    password="Empresa2026$",
    database="empresa2026",
    charset="utf8mb4"
)

with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM clientes")
    for row in cursor.fetchall():
        print(row)

conn.close()
