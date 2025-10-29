import random

nombre_jugador = input("Introduce tu nombre: ")
nivel_actual = 1
puntos_acumulados = 0

print("Nombre: ",nombre_jugador,"Nivel: ",nivel_actual,"Puntos Acumulados: ",puntos_acumulados)

for partidas in range (1000):
 continuar = input("Deseas continuar jugando: ")
 if continuar == "Sí" or continuar == "sí":
        nivel_actual = nivel_actual +1

        aleatorio = random.randint(10, 50)  # genera un número entre 10 y 50
        puntos_acumulados = puntos_acumulados + aleatorio
        print("Nombre: ",nombre_jugador,"Nivel: ",nivel_actual,"Puntos Acumulados: ",puntos_acumulados)
 else: 
     print("Adiós: ",nombre_jugador,", Gracias por jugar. Has temrinado con nivel: ",nivel_actual)
     break






