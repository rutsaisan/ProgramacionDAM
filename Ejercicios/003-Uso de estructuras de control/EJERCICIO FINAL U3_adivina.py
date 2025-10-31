'''
Programa elige numero secreto del 1 al 50 ( import random, random.randint(1,50))
EL usuario tiene solo 6 intentos para acertarlo.
El contador de intetntos no puede ser negativo.
Pide un número por input. Si no es convertible a int, muestra aviso y no gasta intento (usa continue).
Si está fuera de rango (<1 o >50), avisa y no gasta intento.
Indicar al usuario si es demasiado alto o demasiado bajo.

'''

import random
numero_maquina = random.randint(1,50)
intentos_consumidos = 0

print("Hola!, bienvenido a adivina el número. En este programa tendras que adivinar un numero aleatorio del 1 al 50 que escogerá la máquina!")
print("Vamos a empezar!")


while intentos_consumidos < 7:
    numero_jugador =input("Dime tu número: ")
 
    #Convierto la respuesta el usuario a  entero
    try: 
        numero_jugador_convertido = int(numero_jugador)
    except:
        print("No puedo convertir tu respuesta a un numero, porfavor, dime un número")
        continue
    
    #Me aseguro que esta en el rango
    if numero_jugador_convertido < 1 or numero_jugador_convertido > 50:
        print("Tu numero esta fuera de rango, intriduce un numero de 1 a 50")
        continue
    else: 
        # Sumar intento
     intentos_consumidos += 1
     assert intentos_consumidos >= 0, "El contador de intentos no puede ser negativo."
        
     if numero_jugador_convertido < numero_maquina:
            print("El numero es mayor")
     elif numero_jugador_convertido > numero_maquina:
            print("El numero es menor")
    
    if numero_maquina == numero_jugador_convertido:
        print("Enohorabuen has gando! Has adivinado el número!")
        break

    if intentos_consumidos == 6:
        print("O no, te has quedado sin intentas, has perdido...")
        break
    


 


