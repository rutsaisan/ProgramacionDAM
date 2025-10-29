import zipfile
import os

carpeta = "archivos" #Nombre de la carpeta q quieras comprimir

for directorio,carpetas,archivos in os.walk(carpeta):
 for nombre_archivo in archivos:
    origen = os.path.join(directorio, nombre_archivo)
    destino = os.path.join(directorio, nombre_archivo + ".zip")
    archivo = zipfile.ZipFile(destino,'w',compresion=zipfile.ZIP_DEFLATED)
    archivo.write(origen, arcname=nombre_archivo)


