# Clase 7 Checkbox
from tkinter import *


ventana = Tk()
ventana.title("Ejemplo con Checkbox Hamburguesería")
ventana.geometry("400x300")
ventana.config(bd=20, bg="sky blue")

#imagen = PhotoImage(file="hamburguesa.gif")
queso = IntVar()
jamon = IntVar()
#Label(ventana, image=imagen).pack(side=LEFT)
def orden():
    lista = ""
    if queso.get():
        lista += " Con queso"
    else:
        lista += " Sin queso"
    if jamon.get():
        lista += " y con jamón"
    else:
        lista += " y sin jamón"
    imprimir.config(text=lista)

frame= Frame(ventana)
frame.pack(side=RIGHT)
frame.config(bg="sky blue")
Label(frame, text="¿Como quieres tu hamburguesa?", bg="sky blue", font="Curier 15").pack(anchor="w")
Checkbutton(frame, text="Con queso", variable=queso, onvalue=1, offvalue=0, command=orden, bg="sky blue", font="Curier 10").pack(anchor="w")
Checkbutton(frame, text="Con jamón", variable=jamon, onvalue=1, offvalue=0, command=orden, bg="sky blue", font="Curier 10").pack(anchor="w")
imprimir = Label(frame, bg="sky blue")
imprimir.config(font="Curier 20")
imprimir.pack()
ventana.mainloop()
