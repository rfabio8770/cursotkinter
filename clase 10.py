# Clase 10 ListBox
from tkinter import *

ventana = Tk()
ventana.geometry("400x300")
ventana.title("Ejemplo de Listbox")


def agregar():
    listaProductos.insert(END, nuevoProducto.get())
productos = Label(ventana, text="Productos")
productos.pack()

listaProductos = Listbox(ventana, width=50)
listaProductos.insert(0, "Carne")
listaProductos.insert(1, "Pollo")
listaProductos.insert(2, "Cerdo")
listaProductos.insert(3, "Verdura")
listaProductos.pack()

#  eliminar un producto por su índice
listaProductos.delete(0)

nuevoProducto  = Entry(ventana, bd=10)
nuevoProducto.pack()
botonAgregar = Button(ventana, text="Agregar producto", bd=10, command=agregar)
botonAgregar.pack()


ventana.mainloop()