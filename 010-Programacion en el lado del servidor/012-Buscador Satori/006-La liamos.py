import requests
from lxml import html
import mysql.connector
import time

URLS = ["https://elpais.com"]

DB_HOST = "172.24.103.203"
DB_USER = "satori"
DB_PASSWORD = "Satori123$"
DB_NAME = "satori"

def busca(URLS):
    for URL in URLS:
        time.sleep(5)  # DORMIMOS 5 SEGUNDOS
        
        # El try debe estar alineado dentro del for
        try:
            print("uf")

            response = requests.get(
                URL,
                timeout=10,
                headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
                }
            )
            response.raise_for_status()

            tree = html.fromstring(response.content)

            title_list = tree.xpath("//title/text()")
            web_title = title_list[0].strip() if title_list else None

            html_content = response.text[:255]

            print("WEB TITLE:")
            print(web_title or "No title found")

            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                charset="utf8mb4",
                use_unicode=True
            )

            try:
                cur = conn.cursor()
                sql = """
                    INSERT INTO paginas (titulo, url, contenido)
                    VALUES (%s, %s, %s)
                """
                cur.execute(sql, (web_title, URL, html_content))
                conn.commit()
                print(f"\nOK: guardado en MySQL. ID insertado: {cur.lastrowid}")

            finally:
                try:
                    cur.close()
                except Exception:
                    pass
                conn.close()

            # Extraemos enlaces y llamamos recursivamente
            enlaces = tree.xpath("//a/@href")
            
            # CUIDADO: Aquí comienza la recursividad infinita
            busca(enlaces)

        except Exception as e:
            # Es útil imprimir el error para saber qué pasó, aunque luego continúes
            print(f"Error en {URL}: {e}")
            print("error pero continuamos")

# Llamada inicial
busca(URLS)