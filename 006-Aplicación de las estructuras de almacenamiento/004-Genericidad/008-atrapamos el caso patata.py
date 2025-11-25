numeros =[1,2,"3",4,"cinco","patata"]

print(numeros)
numeros_etiquetas=["cero","uno","dos","tres","cuatro","cinco"]

def calculaDoble ():
    for numero in numeros:
        try:
            numero=int(numero) #Primero intenta convertir
            print(numero*2)
        except: 
            centinela = False                      #Si no puedes
            #Intenta buscar el valor en la lista de numeros
            for i in range(0,len(numeros_etiquetas)): 
                if numero == numeros_etiquetas[i]:
                    print(i*2)
                    centinela = True
                if centinela == False:
                    print("Mira tio, lo he intentado pero no he podido")
      

calculaDoble()