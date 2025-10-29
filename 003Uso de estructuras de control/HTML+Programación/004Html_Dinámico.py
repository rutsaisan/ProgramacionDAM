#sudo apt intall python3-pip - sí no teneis PIP en Ubuntu
#pip intall flask - Windows/Linux/macOs (depende de el SI q uses)
#pip3 intall flask --break-system-packages - Windows

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
     <!doctype html>
     <html>
      <head>
       <tittle></tittle>
       <style>
        h1{colo:purple;}
       </style>
      </head>
      <body>
       <h1>Esto es HTML a tope de power</h1>
       '''
    for dia in range(1,31):
      cadena += '<div>'+str(dia)+'<div>'
      cadena+= '''
      </body>
     </html>
     '''
if __name__ == "__main__":
    aplicacion.run(debug=True)

