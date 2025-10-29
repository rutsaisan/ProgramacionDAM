import zipfile

origen = 'miarchivo.txt'

destino = 'comprimido.zip'

archivo = zipfile.ZipFile(destino,'w',compresion=zipfile.ZIP_DEFLATED)
archivo.write(origen)
