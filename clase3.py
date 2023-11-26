from tkinter import *

root = Tk()

# colocando el título a la ventana
root.title("Ventana con título")

# definiendo el tamaño a la ventana
root.geometry("500x300")

boton1 = Button(root, text="Minimizar", command=root.iconify, bg="green")
boton1.pack(side=LEFT)


def imprimir():
    label1 = Label(root, text="imprimiendo")
    label1.pack()


boton2 = Button(root, text="imprimir", command=imprimir, bg="yellow")
boton2.pack(side=RIGHT)
# evitar que se redimensione la ventana
root.resizable(0,0)

# configuraciones de la ventana
root.config(bg="blue", cursor="mouse")

root.mainloop()