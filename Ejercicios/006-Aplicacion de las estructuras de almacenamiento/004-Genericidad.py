def calculaDoble(numeros):
    for elemento in numeros:
        try:
            numero = int(elemento)
            doble = numero * 2
            print("El doble de", numero, "es", doble)
        except ValueError:
            print("Valor no válido para convertir a entero:", elemento)


# Ejemplo práctico
numeros = [10, "20", "hola", 5, "30puntos", "40", -3]

calculaDoble(numeros)