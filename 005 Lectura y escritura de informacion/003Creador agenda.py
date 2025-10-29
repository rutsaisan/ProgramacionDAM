while True:
 print("Dime lo que quieres hacer: ")
 print("1.- Introducir un nuevo contacto")
 print("2.- Leer todos los contactos")
 opcion = int(input("Escoge tu opcion:"))
 
 if opcion == 1:
  nombre = input("Introduce el nombre d ela persona: ")
  email = input("Introduce el email de la persona: ")
  archivo = open("agenda.txt",'a') # a = Añadir, si monemos w machaca lo que habia antes
  archivo.write(nombre+ ","+email+ "\n")
  archivo.close()
 elif opcion == 2:
  archivo = open("agenda.txt",'r')
  lineas = archivo.readlines()
  for linea in lineas:
   print(linea)
   archivo.close()