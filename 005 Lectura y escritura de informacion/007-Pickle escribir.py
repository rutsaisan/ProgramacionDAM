#pip install pypickle (Windows)
#pip3 installl pickle (Linux)
import pickle

archivo = open("datos.bin",'wb')
cadena = "Ruth"

pickle.dump(cadena,archivo)

archivo.close()
    