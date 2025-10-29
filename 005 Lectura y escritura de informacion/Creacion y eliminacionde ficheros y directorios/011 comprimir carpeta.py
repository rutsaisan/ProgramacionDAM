import zipfile
import os


origen = "archivos"
destino = "archivos.zip"

archivozip = zipfile.ZipFile(destino,'w',zipfile.ZIP_DEFLATED)
for directorio,carpetas,archivos in os.walk(origen):
  for archivo in archivos:
    rutaarchivo = os.path.join(directorio,archivo)
    rutalternativa = os.path.relpath(rutaarchivo,origen)
    archivozip.write(rutaarchivo,rutalternativa)

archivozip.close()