import math
def raizSegura(numero):
    try:
        # Intentamos convertir el valor a tipo float
        numero = float(numero)

        # Si el número es negativo, no se puede calcular la raíz real
        if numero < 0:
            return 0

        # Cálculo la raíz cuadrada
        raiz = math.sqrt(numero)
        return raiz

    except:
        # Si ocurre cualquier error (por ejemplo, no se puede convertir a número), devolvemos 0
        return 0

#Pruebo todos los podibles errores que pueden surgir:

print(raizSegura(25))        # Resultado: 5.0
print(raizSegura("49"))      # Resultado: 7.0
print(raizSegura(-9))        # Resultado: 0
print(raizSegura("holi"))    # Resultado: 0
print(raizSegura(0))         # Resultado: 0.0
