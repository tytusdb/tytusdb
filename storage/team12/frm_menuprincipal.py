from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from crud_bd import CRUD_DataBase
from frm_tablas import iniciar

def view_createDatabase():

    def guardar():
        name_database = txt.get()
        if name_database:
            txt.delete(0, END)
            crud = CRUD_DataBase()
            value = crud.createDatabase(name_database)
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Create Database","#FCFCFB", 500, 350)
    lbl = Label(window, text= 'Ingrese el Nombre de la Base de Datos', bg="#FCFCFB")
    lbl.place(x = 125, y = 125)
    txt = Entry(window, width = 35)
    txt.place(x = 100, y = 160)
    btn = Button(window, text='Guardar', command=guardar)
    btn.place(x = 350, y = 200)

def view_showDatabase():
    iniciar()

def view_alterDatabase():

    def modificar():
        nombre_anterior = txtAnterior.get()
        nombre_nuevo= txtNueva.get()
        if nombre_anterior and nombre_nuevo:
            txtAnterior.delete(0, END)
            txtNueva.delete(0, END)
            crud = CRUD_DataBase()
            value = crud.alterDatabase(nombre_anterior, nombre_nuevo)
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
            elif value == 2:
                messagebox.showinfo('', 'databaseOld No Existente')
            elif value == 3:
                messagebox.showinfo('', 'databaseNew Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Alter Database","#FCFCFB", 500, 350)
    lblAnterior = Label(window, text= 'Nombre de la Base de Datos Anterior', bg="#FCFCFB")
    lblAnterior.place(x = 125, y = 75)
    txtAnterior = Entry(window, width = 35)
    txtAnterior.place(x = 100, y = 115)
    lblNueva = Label(window, text= 'Nombre de la Base de Datos Nueva', bg="#FCFCFB")
    lblNueva.place(x = 125, y = 150)
    txtNueva = Entry(window, width = 35)
    txtNueva.place(x = 100, y = 190)
    btnModificar = Button(window, text='Modificar', command = modificar)
    btnModificar.place(x = 345, y = 240)

def view_dropDatabase():

    def eliminar():
        name_database = txt.get()
        if name_database:
            txt.delete(0, END)
            crud = CRUD_DataBase()
            value = crud.dropDatabase(name_database)
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Drop Database","#FCFCFB", 500, 350)
    lbl = Label(window, text= 'Ingrese el Nombre de la Base de Datos', bg="#FCFCFB")
    lbl.place(x = 125, y = 125)
    txt = Entry(window, width = 35)
    txt.place(x = 100, y = 160)
    btn = Button(window, text='Eliminar', command=eliminar)
    btn.place(x = 350, y = 200)

def edicionPantalla(window, titulo, color, ancho_ventana, alto_ventana):
    x_ventana = window.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = window.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    window.geometry(posicion)

    # Edicion de la Ventana
    window.resizable(0,0)
    window.title(titulo)
    dimension = str(ancho_ventana)+'x'+str(alto_ventana)
    window.geometry(dimension)
    window.configure(bg=str(color))

window = Tk()

edicionPantalla(window,"Menu Principal","white",  830, 525)

var_width = 25
separacion = 3
var_height = int(var_width//2.5)
var_font = tkFont.Font(size=12, weight="bold", family="Arial")

encabezado = Label(window, text="", bg="white",width=25)
encabezado.grid(padx=separacion, pady=separacion, row=0, column=0, columnspan = 3)

izquierda = Label(window, text="", bg="white",width=16)
izquierda.grid(padx=separacion, pady=separacion, row=1, column=0, rowspan =2)

btncreateDatabase = Button(window, text="CREATE NEW DATABASE", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_createDatabase)
btncreateDatabase.grid(padx=separacion, pady=separacion, row=1, column=1)

btnshowDatabases = Button(window, text="SHOW DATABASE", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command = view_showDatabase)
btnshowDatabases.grid(padx=separacion, pady=separacion, row=2, column=1)

btnalterDatabase = Button(window, text="ALTER DATABASE", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command = view_alterDatabase)
btnalterDatabase.grid(padx=separacion, pady=separacion, row=1, column=2)

btndropDatabase = Button(window, text="DROP DATABASE", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command = view_dropDatabase)
btndropDatabase.grid(padx=separacion, pady=separacion, row=2, column=2)

window.mainloop()