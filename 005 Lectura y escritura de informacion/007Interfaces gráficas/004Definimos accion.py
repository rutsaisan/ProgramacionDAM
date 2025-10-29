import tkinter as tk

ventana= tk.Tk()

def accion():
    print("Has pulsado el boton...")

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

ventana.mainloop() #No te salgas