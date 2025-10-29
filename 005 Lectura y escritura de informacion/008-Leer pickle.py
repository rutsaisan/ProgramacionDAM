#pip install pickle (Windows)
#pip3 installl pickle (Linux)
import pickle

archivo = open("datos.bin","rb")
cadena = pickle.load(archivo)

print(cadena)

archivo.close()
    