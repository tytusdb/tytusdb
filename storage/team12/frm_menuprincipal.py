from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from crud_bd import CRUD_DataBase
from frm_tablas import mostrarTablas

def view_createDatabase():

    def guardar():
        name_database = txt.get()
        if name_database:
            txt.delete(0, END)
            crud = CRUD_DataBase()
            value = crud.createDatabase(name_database)
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
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
    list_words = CRUD_DataBase().showDatabases()
    var = 0
    # Esta es la ventana principal
    ventana_principal = Tk()
    ventana_principal.title('show Databases')
    ventana_principal.geometry("550x500")

    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    # Edicion de la Ventana
    ancho_ventana = 550
    alto_ventana = 500
    x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana_principal.geometry(posicion)

    # Edicion de la Ventana
    ventana_principal.resizable(0,0)
    dimension = str(ancho_ventana)+'x'+str(alto_ventana)
    ventana_principal.geometry(dimension)
    ventana_principal.configure(bg="white")
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------

    # Se crea un marco principal
    marco_principal = Frame(ventana_principal)
    marco_principal.pack(fill=BOTH, expand=1)

    # Se crea un canvas
    var_canvas = Canvas(marco_principal)
    var_canvas.config(bg="red")
    var_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Se agrega un scrollbar al canvas
    var_scrollbar = Scrollbar(marco_principal, orient=VERTICAL, command=var_canvas.yview)
    var_scrollbar.pack(side=RIGHT, fill=Y)

    # Se configura el canvas
    var_canvas.configure(yscrollcommand=var_scrollbar.set)
    var_canvas.bind('<Configure>', lambda e: var_canvas.configure(scrollregion = var_canvas.bbox("all")))

    # Se crea otro marco dentro del canvas
    second_frame = Frame(var_canvas)

    # Se agrega ese nuevo marco a la ventana en el canvas
    var_canvas.create_window((0,0), window=second_frame, anchor="nw")
    var_font = tkFont.Font(size=13, weight="bold", family="Arial")

    for word in list_words:
        btn = Button(second_frame, text=word, width=58, height=2, bg="#DBE2FC", font=var_font, command=lambda txt=word:mostrarTablas(txt, ventana_principal))
        btn.grid(row=var, column=0, pady=1)
        var += 1

    ventana_principal.mainloop()

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
                window.destroy()
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
                window.destroy()
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

def view_showGraphivz():
    CRUD_DataBase().showGraphviz()

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

edicionPantalla(window,"Base de Datos","white",  830, 525)

var_width = 25
separacion = 3
var_height = int(var_width//2.5)
var_font = tkFont.Font(size=12, weight="bold", family="Arial")

btnGraficarArbol = Button(window, text="Graficar Arbol", bg="#AAAFBF", fg="white", font=var_font, width=60, command=view_showGraphivz)
btnGraficarArbol.grid(padx=separacion, pady=separacion, row=0, column=1, columnspan = 3)

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