import os

carpeta = input("Indica una carpeta: ")

suma = 0

for directorio,carpetas,archivos in os.walk(carpeta):
    for archivo in archivos:
     ruta= os.path.join(directorio,archivo)
     try:
      suma += os.path.getsize(ruta)
     except:
       pass #Evita errores si un archivo no se puede

print("La crapeta ocupa: ")
print(suma/(1024*1024),"MB")
   
    
    