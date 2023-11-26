# Clase 4 uso de Entry
from tkinter import *







ventana = Tk()
texto1 = StringVar()
texto2 = StringVar()

texto1.set("Escriba su nombre aqui")
texto2.set("Escriba su apellido aqui")

def saludar():
    print("Hola " + texto1.get() + " " + texto2.get())

ventana.title("Uso de Entry")
ventana.geometry("500x300")
etiqueta1 = Label(ventana,text="Escriba su nombre")
etiqueta1.place(x=10, y=10)
entrada1 = Entry(ventana, textvariable=texto1)
entrada1.place(x=170, y=10)

etiqueta2= Label(ventana,text="Escriba su apellido")
etiqueta2.place(x=10, y=40)
entrada2 = Entry(ventana,textvariable=texto2)
entrada2.place(x=170, y=40)

boton = Button(ventana, text="Saludar",command=saludar)
boton.place(x=10, y=100)

ventana.mainloop()