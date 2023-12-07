# Clase 8 Menús
from tkinter import *


ventana = Tk()
ventana.title("Ejemplo con menús")
ventana.geometry("400x300")

menuBar = Menu(ventana)
ventana.config(menu=menuBar)#, bd=20, bg="sky blue")

archivoMenu = Menu(menuBar, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventana.quit)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

ayudaMenu = Menu(menuBar, tearoff=0)
ayudaMenu.add_command(label="Acerca de...")
ayudaMenu.add_separator()

menuBar.add_cascade(label="Archivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)
menuBar.add_cascade(label="Ayuda", menu=ayudaMenu)

ventana.mainloop()