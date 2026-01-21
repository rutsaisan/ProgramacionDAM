import random

# Conjunto objetivo con los números del 1 al 9
objetivo = {1, 2, 3, 4, 5, 6, 7, 8, 9}

encontrado = False
intentos = 0

while not encontrado:
    intentos += 1

    # 1. Generar una lista de 9 números aleatorios entre 1 y 9
    fila = []
    for _ in range(9):
        numero = random.randint(1, 9)
        fila.append(numero)

    # 2. Convertir la lista en conjunto para eliminar repeticiones
    conjunto_fila = set(fila)

    # 3. Comprobar si el conjunto coincide exactamente con {1,...,9}
    if conjunto_fila == objetivo:
        encontrado = True
        print("Fila válida encontrada:", fila)
        print("Número de intentos:", intentos)