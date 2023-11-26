from tkinter import *

root = Tk()

# colocando el título a la ventana
root.title("Ventana con título")

# definiendo el tamaño a la ventana
root.geometry("500x300")

# cambiamos el ícono
root.iconbitmap("/home/rfabio/Programas/tkinter/piton.ico")

# evitar que se redimensione la ventana
root.resizable(0,0)

# configuraciones de la ventana
root.config(bg="blue", cursor="mouse")

root.mainloop()