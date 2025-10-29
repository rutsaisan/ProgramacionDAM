#Abre una terminal e instala flask:
#pip install flask
#Flask es un microservidorweb que nos permitre generar HTML desde Python

from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return '''
        <!DOCTYPE html>
     <html lang="es">
        <head>
        <title>RUTHSAINZblog</title>
        <meta charset="utf-8">
        <style>
            body{background: steelblue;color:steelblue;font-family:sans-serif;}
            header,main,footer{background: white;padding: 20px;margin: auto;width: 600px;}
            header,footer{text-align: center;}
            main{color: black;}
        </style>
        </head>
        <body>
            <header> <h1>RUTHSAINZblog</h1></header>
            <main>
            '''
    archivo = open("blog.json",'r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
         <article>
                    <h3> '''+linea['titulo']+'''</h3>
                    <time>'''+linea['fecha']+'''</time>
                    <p>'''+linea['autor']+'''</p>
                    <p>'''+linea['contenido']+'''</p>
                </article>
         '''
    
    cadena += '''
            </main>
            <footer> (c)2025 Ruth Sainz Santos-Olmo</footer>
        </body>
     </html>
    '''
    return cadena

#Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)
    