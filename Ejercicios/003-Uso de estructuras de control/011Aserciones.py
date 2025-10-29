
def comprobar_puntuacion(puntos_obtenidos, puntos_totales):
    # (El alumnado debe completar este apartado)
    if puntos_totales == 0:
        return False  # Evita división por cero
    porcentaje = (puntos_obtenidos / puntos_totales) * 100
    return porcentaje > 50


# Prueba la función con aserciones
assert comprobar_puntuacion(60, 100) == True, "La puntuación no es correcta" 
assert comprobar_puntuacion(45, 100) == False, "La puntuación no es correcta"

try:
    assert comprobar_puntuacion(60, 100) == True, "La puntuación no es correcta"
    assert comprobar_puntuacion(45, 100) == False, "La puntuación no es correcta"
    assert comprobar_puntuacion(0, 0) == False, "La puntuación no es correcta"
    print("✅ Las pruebas de comprobar_puntuacion pasaron correctamente.")
except AssertionError as error:
    print(f"❌ Error en comprobar_puntuacion: {error}")
