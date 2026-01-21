# Creación del diccionario personaje
personaje = {
    "Nombre": "Mario",
    "Edad": 30,
    "Habilidades": ["saltar", "correr", "esquivar"],
    "Armas": {"espada": "Fuego", "escudo": "Metal"}
}

# El nombre del personaje
print("Nombre del personaje:", personaje["Nombre"])

# La edad del personaje
print("Edad del personaje:", personaje["Edad"])

# La primera habilidad del personaje
print("Habilidad del personaje:", personaje["Habilidades"][0])

# El tipo de arma
print("Arma: escudo - ", personaje["Armas"]["escudo"])