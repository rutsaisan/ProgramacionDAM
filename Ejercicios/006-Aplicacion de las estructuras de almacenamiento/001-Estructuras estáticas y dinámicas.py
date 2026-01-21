def main():
    # Lista dinámica para almacenar las coordenadas de los enemigos
    enemigos = []

    # Añadimos tres enemigos con sus coordenadas
    enemigos.append({"x": 10, "y": 5})
    enemigos.append({"x": 20, "y": 15})
    enemigos.append({"x": 30, "y": 25})

    # Verificamos que los enemigos se han añadido correctamente
    print("Lista de enemigos con sus coordenadas:")
    print(enemigos)

# Llamada a la función principal
main()