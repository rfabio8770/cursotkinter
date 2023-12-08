# Clase 9 Spinbox y ventanas emergentes
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejemplo de spinbox y ventanas emergentes")
ventana.geometry("400x300")
menuBar = Menu(ventana)
ventana.config(menu=menuBar, bd=20, bg="sky blue")


def cerrar():
    messagebox.askquestion("Cerrar", message="Estás seguro?")


def version():
    messagebox.showinfo("Versión", message="Versión 1.0\nAutor: Prof. Ricardo Fabio")

def error():
    messagebox.showerror("ERROR CRÍTICO", "Error fatal en la aplicación")


def atencion():
    messagebox.showwarning("Atención", message="Se borrará el archivo actual")
archivoMenu = Menu(menuBar, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=atencion)
archivoMenu.add_command(label="Guardar", command=error)
archivoMenu.add_command(label="Cerrar", command=cerrar)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventana.quit)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

ayudaMenu = Menu(menuBar, tearoff=0)
ayudaMenu.add_command(label="Acerca de...", command=version)
ayudaMenu.add_separator()

menuBar.add_cascade(label="Archivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)
menuBar.add_cascade(label="Ayuda", menu=ayudaMenu)



w = Spinbox(ventana, values=("C", "Python", "HTML5", "Java"))
w.pack()
e = Spinbox(ventana, values=("Carne", "Verdura", "Pasta", "Ensalada"))
e.pack()





ventana.mainloop()