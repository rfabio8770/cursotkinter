# Clase 5 Aspectos gráficos de una interfaz gráfica
from tkinter import *

ventana = Tk()
texto1 = StringVar()
texto2 = StringVar()
mensaje = StringVar()

texto1.set("Escriba su nombre aqui")
texto2.set("Escriba su apellido aqui")

def saludar():
    mensaje.set("Hola " + texto1.get() + " " + texto2.get())

ventana.title("Uso de propiedades gráficas de los controles")
ventana.geometry("400x300")
ventana.resizable(0,0)
etiqueta1 = Label(ventana,text="Escriba su nombre", bd=4, bg="red", font="arial")
etiqueta1.place(x=10, y=10)
entrada1 = Entry(ventana, textvariable=texto1, bd=5)
entrada1.place(x=170, y=10)

etiqueta2= Label(ventana,text="Escriba su apellido", bd=4, bg="red", font="arial")
etiqueta2.place(x=10, y=40)
entrada2 = Entry(ventana,textvariable=texto2, bd=5)
entrada2.place(x=170, y=40)

boton = Button(ventana, text="Saludar",command=saludar ,bd=5, bg="red")
boton.place(x=112, y=123)
# state es para evitar que el entry sea editable.
entrada3 = Entry(ventana, text=mensaje, bd=20, font="arial", state="disable")
entrada3.place(x=70, y= 221)


ventana.mainloop()