#sudo apt intall python3-pip - sí no teneis PIP en Ubuntu
#pip intall flask - Windows/Linux/macOs (depende de el SI q uses)
#pip3 intall flask --break-system-packages - Windows

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return "Esto es HTML desde Flask"
if __name__ == "__main__":
    aplicacion.run(debug=True)

