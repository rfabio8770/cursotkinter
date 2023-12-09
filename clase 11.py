from tkinter import *
from tkinter import messagebox

# variables y funciones
lista = []

def guardar():
    n = nombre.get()
    ap = apellido.get()
    cor = correo.get()
    tel = telefono.get()
    lista.append(n+"$"+ap+"$"+cor+"$"+tel)
    escribirContacto()
    n = nombre.set("")
    ap = apellido.set("")
    cor = correo.set("")
    tel = telefono.set("")
    consultar()




def eliminar():
    eliminarCont.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$")
        if eliminarCont.get()==arreglo[3]:
            lista.remove(elemento)
            removido=True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado"+ " "+ eliminarCont.get())


def consultar():
    r = Text(ventana, width=80, height=15)
    lista.sort()
    valores = []
    r.insert(INSERT, "Nombre\tApellido\t\tTelefono\t\tCorreo\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        r.insert(INSERT,arreglo[0]+"\t"+arreglo[1]+"\t"+arreglo[2]+"\t"+arreglo[3])
        r.place(x=20, y=230)
        spinTelefono = Spinbox(ventana, value=(valores), textvariable=eliminarCont)
        spinTelefono.place(x=450, y=50)
    if lista == []:
         spinTelefono=Spinbox(ventana, value=(valores))
         spinTelefono.place(x=450, y=50)
    r.config(state=DISABLED)         
      
    

def iniciarArchivo():
    archivo=open("ag.txt","a")
    archivo.close()

def cargar():
    archivo = open("ag.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1]=="\n":
                linea=linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def escribirContacto():
    archivo = open("ag.txt", "w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()


ventana = Tk()
ventana.title("Agenda con Archivos")
ventana.geometry("700x500")
ventana.resizable(0,0)
colorFondo = "#006"
colorLetra = "#FFF"

# variables de intercambio con la interfaz.
nombre = StringVar()
apellido = StringVar()
correo = StringVar()
telefono = StringVar()
eliminarCont = StringVar()

iniciarArchivo()
cargar()
consultar()
ventana.config(bg=colorFondo)


tituloEtiqueta = Label(ventana, text="Mi Agenda de Contactos", fg=colorLetra, bg=colorFondo)
tituloEtiqueta.place(x=270, y=10)

nombreEtiqueta = Label(ventana, text="Nombre",fg=colorLetra, bg=colorFondo)
nombreEtiqueta.place(x=50, y=50)

nombreEntrada = Entry(ventana, textvariable=nombre)
nombreEntrada.place(x=150,y=50)


apellidoEtiqueta = Label(ventana, text="Apellido",fg=colorLetra, bg=colorFondo)
apellidoEtiqueta.place(x=50, y=80)

apellidoEntrada = Entry(ventana, textvariable=apellido)
apellidoEntrada.place(x=150,y=80)

telefonoEtiqueta = Label(ventana, text="Teléfono",fg=colorLetra, bg=colorFondo)
telefonoEtiqueta.place(x=50, y=140)

telefonoEntrada = Entry(ventana, textvariable=telefono)
telefonoEntrada.place(x=150,y=140)

correoEtiqueta = Label(ventana, text="Correo",fg=colorLetra, bg=colorFondo)
correoEtiqueta.place(x=50, y=170)

correoEntrada = Entry(ventana, textvariable=correo)
correoEntrada.place(x=150,y=170)

eliminarEtiqueta = Label(ventana, text="Teléfono",fg=colorLetra, bg=colorFondo)
eliminarEtiqueta.place(x=370, y=50)

spinTelefono = Spinbox(ventana, text=eliminarCont)
spinTelefono.place(x=450, y=50)

botonGuardar = Button(ventana, text="Guardar", fg=colorFondo, bg=colorLetra, command=guardar)
botonGuardar.place(x=180, y=200)

botonEliminar = Button(ventana, text="Eliminar", fg=colorFondo, bg=colorLetra, command=eliminar)
botonEliminar.place(x=490, y=80)
ventana.mainloop()