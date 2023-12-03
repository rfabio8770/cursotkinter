# Clase 6 RadioButtons
from tkinter import *

ventana = Tk()
ventana.title("Ejemplo con Radiobuttons")
ventana.geometry("300x300")
ventana.config(bg="goldenrod3")
ventana.resizable(0,0)

opcion = IntVar()
num = IntVar()

def operacion():
    numero = num.get()
    op = opcion.get()
    total = 0
    if op == 1:
        total = numero * 5
    elif op == 2:
        total = numero * 10
    elif op == 3:
        total = numero * 20
    elif op == 4:
        total = numero * 30
    elif op == 5:
        total = numero * 40
    else:
        total = numero ** 2
    print("El total es", total)



etiqueta1 = Label(ventana, text="Escriba su número", bg="goldenrod3", bd=5)
etiqueta1.place(x=20, y=20)

entrada1 = Entry(ventana, font="Helvetica 12", textvariable=num)
entrada1.place(x =150, y = 20)

etiqueta2 = Label(ventana, text="Elija la cantidad", bg="goldenrod3", bd=5)
etiqueta2.place(x=20, y = 50)

# Creación de los radiobuttons
x5 = Radiobutton(ventana, text="x5", value=1, bg="goldenrod3", bd=5, variable=opcion)
x5.place(x=20, y=80)

x10 = Radiobutton(ventana, text="x10",value=2, bg="goldenrod3", bd=5, variable=opcion)
x10.place(x=70, y=80)

x20 = Radiobutton(ventana, text="x20", value=3, bg="goldenrod3", bd=5, variable=opcion)
x20.place(x=120, y=80)

x30 = Radiobutton(ventana, text="30", value=4, bg="goldenrod3", bd=5, variable=opcion)
x30.place(x=20, y=110)

x40 = Radiobutton(ventana, text="x40", value=5, bg="goldenrod3", bd=5, variable=opcion)
x40.place(x=70, y=110)


# Creación del botón
boton1 = Button(ventana, text="Calcular", bg="goldenrod3", bd=5, command=operacion)
boton1.place(x=20, y=140)

ventana.mainloop()
