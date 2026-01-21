from PIL import Image

imagen = Image.open("tatoo dragon.jpg")

anchura,altura = imagen.size		

for x in range(0,anchura):			
  for y in range(0,altura):			
    pixel = imagen.getpixel((x, y))	
    # Primero leo los componentes de color
    rojo = pixel[0]
    verde = pixel[1]
    azul = pixel[2]
    rojo += 20
    verde += 20
    azul += 20
    # Y sobreeescribo el valor
    imagen.putpixel((x, y), (rojo, verde, azul)) # ESTO ES CORRECTO

imagen.save("modificado.jpg")