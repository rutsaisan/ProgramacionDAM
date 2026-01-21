import random
import json
from flask import Flask, render_template
import math
import pygame  # Asegúrate de tener pygame instalado

class Npc():
    def __init__(self, x, y, radio, direccion):
        self.posx = x
        self.posy = y
        self.radio = radio
        self.direccion = direccion

    def to_dict(self):
        return {
            "posx": self.posx,
            "posy": self.posy,
            "radio": self.radio,
            "direccion": self.direccion
        }

    def mover(self):
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)

# Preparo los personajes
personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    xaleatoria = random.randint(0, 500)
    yaleatoria = random.randint(0, 500)
    radioaleatorio = random.randint(10, 30)
    direccionaleatoria = random.random() * math.pi * 2
    personajes.append(
        Npc(xaleatoria, yaleatoria, radioaleatorio, direccionaleatoria)
    )

# Inicializo pygame para reproducir música
pygame.init()
pygame.mixer.music.load("musica.ogg")
pygame.mixer.music.play(-1)  # Reproduce en bucle

# Lanzo una web
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("juego.html")

@app.route("/api")
def api():
    # Primero muevo todos los personajes
    for personaje in personajes:
        personaje.mover()
    personajes_json = [p.to_dict() for p in personajes]
    return json.dumps(personajes_json, indent=2)

if __name__ == "__main__":
    app.run(debug=True)
