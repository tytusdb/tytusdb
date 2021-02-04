# Package:      BPlusMode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from Funciones import *
from PIL import Image
from team16.DataAccessLayer import reports as reportsTeam16



def graphStructure(j, mode, structure, database, table):
    # structure = [ database, table, tuple ]
    if mode == 'bplus':

        if structure == 'database':
            databaseTree_ = j.serializable.Read('./Data/BPlusMode/', 'Databases')
            databaseTree_.graph("Databases")
            return './Data/BPlusMode/DataBases.png'

        elif structure == 'table':
            table_ = j.serializable.Read(f"./Data/BPlusMode/{database}/", f'{database}')
            table_.graph(database)
            return f'./Data/BPlusMode/{database}/{database}.png'

        elif structure == 'tuple':
            tuple_ = j.serializable.Read(f"./Data/BPlusMode/{database}/{table}/", f'{table}')
            tuple_.graficar(database, table)
            return f'./Data/BPlusMode/{database}/{table}/{table}.png'

    elif mode == 'hash':

        if structure == 'database':
            j._storage.graficar()
            return './dbs.png'

        elif structure == 'table':
            tmp = j._storage.Buscar(database)
            tmp.graficar()
            return './tablas.png'

        elif structure == 'tuple':
            tmp = j._storage.Cargar(database, table)
            tmp.Grafico()
            return './hash.png'

    elif mode == 'isam':

        if structure == 'database':
            j.checkDirs()
            j.chartList(j.showDatabases())
            return './list.png'

        elif structure == 'table':
            j.checkDirs()
            j.chartList(j.showTables(database))
            return './list.png'

        elif structure == 'tuple':
            j.checkDirs()
            tab = j.rollback('tables/' + database + table)
            tab.chart()
            return './isam.png'

    elif mode == 'avl':

        if structure == 'database':
            reportsTeam16.graphicDatabases()
            return './tmp/databases.png'

        elif structure == 'table':
            reportsTeam16.graphicTables(database)
            return './tmp/db-tables.png'

        elif structure == 'tuple':
            reportsTeam16.graphAVL(database, table)
            return './tmp/grafo-avl.png'

    elif mode == 'b':

        if structure == 'database':
            databases_ = j.showDatabases()
            listGraph(databases_)
            return './List.png'

        elif structure == 'table':
            tables_ = j.showTables(database)
            listGraph(tables_)
            return './List.png'

        elif structure == 'tuple':
            j.serializar.rollback(str(database) + "-" + str(table) + "-B").graficar()
            return './salida.png'

    elif mode == 'json':

        if structure == 'database':
            databases_ = j.showDatabases()
            listGraph(databases_)
            return './List.png'

        if structure == 'table':
            tables_ = j.showTables(database)
            print(tables_)
            listGraph(tables_)
            return './List.png'

        if structure == 'tuple':
            tuples_ = j.extractTable(database, table)
            tupleGraph(tuples_)
            return './List.png'

    elif mode == 'dict':

        if structure == 'database':
            databases_ = j.showDatabases()
            listGraph(databases_)
            return './List.png'

        if structure == 'table':
            tables_ = j.showTables(database)
            listGraph(tables_)
            return './List.png'

        if structure == 'tuple':
            tuples_ = j.extractTable(database, table)
            tupleGraph(tuples_)
            return './List.png'


def centrar_ventana(app, ancho, alto):
    app.config(width=ancho, height=alto)  # linen - light cyan - ghost white WhiteSmoke
    # Centrar ventana
    x_ventana = app.winfo_screenwidth() // 2 - ancho // 2
    y_ventana = app.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x_ventana) + "+" + str(y_ventana)
    app.geometry(posicion)
    app.configure(bg='#F0FFFF')


def configuracion_defecto(app):
    app.title("    TYTUS")
    app.resizable(0, 0)
    app.iconbitmap('./images/blockchain_.ico')


def ventana_imagen(path):
    try:
        app = Toplevel()
        configuracion_defecto(app)
        app.state('zoomed')

        img = PhotoImage(file=path)
        label = Label(app, image=img)
        label.image = img
        label.grid(row=0, column=0)
        label.pack(side="bottom", fill="both", expand="yes")

    except:
        print('Imagen no existe')


def fondo(app):
    img = PhotoImage(file='./images/fondo.png')
    label = Label(app, image=img, bg="#F0FFFF")
    label.image = img
    label.grid(row=0, column=0)


# ------------------------------------------------- VENTANAS PRINCIPALES -----------------------------------------------
def ventana_principal():
    # Raíz de la aplicación
    app = Tk()
    color = "#F0FFFF"
    configuracion_defecto(app)
    centrar_ventana(app, 900, 700)

    bg_image = PhotoImage(file="./images/fondo.png")
    x = Label(app, image=bg_image, bg=color)
    x.place(x=0, y=0)
    x.pack()

    img_db = PhotoImage(file="./images/base-de-datos.png")
    db = Button(text="Bases de datos",  bg="#FFFFFF", image=img_db, compound="top", font=("Georgia", 16), command=lambda: ventana_db('', combo.get()))
    db.place(x=500, y=200)

    img_subir = PhotoImage(file="./images/subir.png")
    db = Button(text="Cargar", bg="#FFFFFF", image=img_subir, compound="top", font=("Georgia", 16), command=ventana_loadCSV)
    db.place(x=700, y=200)

    imgGraph = PhotoImage(file="./images/grafosBoton.png")
    buttonGrap = Button(text="Grafos", bg="#FFFFFF", image=imgGraph, compound="top", font=("Georgia", 16), command=lambda: windowReportsGraph())
    buttonGrap.place(x=500, y=400)

    imgBlockchain = PhotoImage(file="./images/blockchainBoton.png")
    buttonBlockchain = Button(text="Blockchain", bg="#FFFFFF", image=imgBlockchain, compound="top", font=("Georgia", 16) ,command=lambda: windowBlockchain())
    buttonBlockchain.place(x=700, y=400)

    # Combobox
    combo = ttk.Combobox(app)
    combo.place(x=90, y=230)

    # Selección del combobox
    def selection_changed(event):
        seleccion = combo.get()

    Label(app, text="Seleccionar modo", bg="#F0FFFF", font=("Arial Black", 18, "bold")).place(x=50, y=180)
    combo["values"] = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
    combo.bind("<<ComboboxSelected>>", selection_changed)

    app.mainloop()


def ventana_db(ventana, mode):
    if mode == '':
        messagebox.showinfo('', 'Debe elegir un modo')
        return
    if ventana != '':
        ventana.withdraw()
    app2 = Toplevel()
    configuracion_defecto(app2)
    centrar_ventana(app2, 500, 700)
    app2.configure(bg="#F0FFFF")

    img = PhotoImage(file='./images/base-de-datos2.png')
    label = Label(app2, image=img, bg="#F0FFFF")
    label.image = img
    label.place(x=120, y=30)

    # Selección del combobox
    def selection_changed(event):
        seleccion = combo.get()
        ventana_lista_tablas(app2, seleccion, mode)

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(app2, font=fuente)
    combo.place(x=150, y=330)

    j = checkMode(mode)
    # GRAPH DATABASES
    path = graphStructure(j, mode, 'database', None, None)

    Label(app2, text="Seleccionar DB",  bg="#F0FFFF", font=("Georgia", 13)).place(x=180, y=300)
    combo["values"] = j.showDatabases()
    combo.bind("<<ComboboxSelected>>", selection_changed)

    boton_estructura = Button(app2, text="Ver estructura", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_imagen(path))
    boton_estructura.place(x=380, y=5)


def ventana_lista_tablas(ventana, db, mode):
    ventana.withdraw()  # Cerrar ventana anterior
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 700)

    img = PhotoImage(file='./images/base-de-datos3.png')
    label = Label(app, image=img, bg="#F0FFFF")
    label.image = img
    label.place(x=120, y=30)

    # Selección del combobox
    def selection_changed(event):
        ventana_tupla(app, combo.get(), db, mode)

    j = checkMode(mode)
    # GRAPH DATABASES
    path = graphStructure(j, mode, 'table', db, None)

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(app, font=fuente)
    combo.place(x=150, y=350)
    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_db(app, mode))
    boton_regresar.place(x=10, y=5)

    Label(app, text="Tablas de DB:\n"+db, bg="#F0FFFF", font=("Georgia", 13)).place(x=190, y=300)

    lista_tablas = j.showTables(db)

    if lista_tablas is None:
        messagebox.showinfo('', 'LA DB "'+db+'" NO TIENE TABLAS')
        ventana_db(app, mode)
    else:
        combo["values"] = lista_tablas
        combo.bind("<<ComboboxSelected>>", selection_changed)

        boton_estructura = Button(app, text="Ver estructura", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_imagen(path))
        boton_estructura.place(x=380, y=5)


def ventana_tupla(ventana, tupla, db, mode):
    print(tupla)
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 700)

    img = PhotoImage(file='./images/B+.png')
    label = Label(app, image=img, bg="#F0FFFF")
    label.image = img
    label.place(x=95, y=25)

    Label(app, text="Registro de la tupla:\n" + tupla, bg="#F0FFFF", font=("Georgia", 13)).place(x=180, y=250)

    j = checkMode(mode)

    def mensaje():
        try:
            lista = j.extractTable(db, tupla)
            if lista is not None:
                path = graphStructure(j, mode, 'tuple', db, tupla)
                boton_estructura = Button(app, text="Ver estructura", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_imagen(path))
                boton_estructura.place(x=380, y=5)

                app2 = Toplevel()
                color = "#F0FFFF"
                configuracion_defecto(app2)
                centrar_ventana(app2, 900, 700)

                tabla = ttk.Treeview(app2, height=32)
                tabla["columns"] = "#0"
                tabla.column("#0", width=650, minwidth=400)
                tabla.heading("#0", text="Registros", anchor="center")
                tabla.place(x=20, y=20)

                mensaje = ''
                contador = 0
                for i in lista:
                    contador += 1
                    for x in i:
                        mensaje += str(x) + "  "
                    tabla.insert('', 'end', text=mensaje)
                    mensaje = ''
        except:
            messagebox.showinfo('', 'LA TABLA NO TIENE REGISTROS')
            ventana_lista_tablas(app, db, mode)

    bt = Button(app, text="Ver registros", font='Georgia 10', bg='#98FB98', command=mensaje)
    bt.place(x=200, y=310)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_lista_tablas(app, db, mode))
    boton_regresar.place(x=10, y=5)


def ventana_loadCSV():
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='loadCSV', bg="#F0FFFF", font=("Georgia", 20)).place(x=200, y=140)

    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=215, y=200, width=245)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=215, y=230, width=245)

    Label(app, text='Ruta:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    ruta = Entry(app, font=("Georgia", 10))
    ruta.place(x=215, y=260, width=245)

    def guardar(ruta_, database, table):
        valor_retorno = loadCSV(ruta_, database, table)
        print('loadCSV: ', valor_retorno)
        messagebox.showinfo('', 'ARCHIVO PROCESADO')

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98',command=lambda:guardar(ruta.get(), nombre_db.get(), nombre_tabla.get()))
    bt.place(x=215, y=300)


# ---------------------------------------------------------- GRAPH -----------------------------------------------------
def windowReportsGraph():
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 700)
    app.configure(bg="#F0FFFF")
    Label(app, text='GRAFOS', bg="#F0FFFF", font=("Georgia", 22)).place(x=180, y=50)
    Label(app, text='Campos requeridos:                                                                          ',
          bg="#FFFFFF", font=("Georgia", 10)).place(x=70, y=100)
    Label(app, text='graphDSD : base de datos                                                                ',
          bg="#FFFFFF", font=("Georgia", 10)).place(x=70, y=120)
    Label(app, text='graphDF : base de datos y tabla                                                    ',
          bg="#FFFFFF", font=("Georgia", 10)).place(x=70, y=140)

    img = PhotoImage(file='./images/grafos2.png')
    label = Label(app, image=img, bg="#F0FFFF")
    label.image = img
    label.place(x=130, y=370)

    font = ("Georgia", 12)
    Label(app, text='Base de datos:', bg="#F0FFFF", font=font).place(x=70, y=200)
    nameDb = Entry(app, font=font)
    nameDb.place(x=215, y=200, width=200)

    Label(app, text='Tabla:', bg="#F0FFFF", font=font).place(x=70, y=230)
    nameTable = Entry(app, font=font)
    nameTable.place(x=215, y=230, width=200)

    def showGraph(database, table):
        try:
            dictionary = load('metadata')
            db = dictionary.get(database)
            if db is None:
                messagebox.showinfo('', 'DB no existe')
                return

            if database != '' and table == '':  # graphDSD
                print('graphDSD')

                graphDSD(database)
                ventana_imagen('./DSD.png')

            elif database != '' and table != '':  # graphDF
                print('graphDF')

                graphDF(database, table)
                ventana_imagen('./DF.png')
            else:
                messagebox.showinfo('', 'Debe rellenar los campos')
                windowReportsGraph()
        except:
            messagebox.showinfo('', 'Error en el método')
            windowReportsGraph()

    confirm = Button(app, text="Confirmar", font=font, bg='#98FB98', command=lambda: showGraph(nameDb.get(), nameTable.get()))
    confirm.place(x=215, y=290)


# ---------------------------------------------------------- BLOCKCHAIN ------------------------------------------------
def windowBlockchain():
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 700)
    app.configure(bg="#F0FFFF")
    Label(app, text='BLOCKCHAIN', bg="#F0FFFF", font=("Georgia", 22)).place(x=180, y=50)

    img = PhotoImage(file='./images/blockchain2.png')
    label = Label(app, image=img, bg="#F0FFFF")
    label.image = img
    label.place(x=130, y=370)

    font = ("Georgia", 12)
    Label(app, text='Base de datos:', bg="#F0FFFF", font=font).place(x=70, y=200)
    nameDb = Entry(app, font=font)
    nameDb.place(x=215, y=200, width=200)

    Label(app, text='Tabla:', bg="#F0FFFF", font=font).place(x=70, y=230)
    nameTable = Entry(app, font=font)
    nameTable.place(x=215, y=230, width=200)

    def showImage(database, table):
        try:
            path = f'./ImageBlockChain/{database}-{table}.png'
            abrir_img = Image.open('../team13/' + path + '')
            abrir_img.show()
        except:
            messagebox.showinfo('', 'Database / Table incorrectos')
            windowBlockchain()

    confirm = Button(app, text="Confirmar", font=font, bg='#98FB98', command=lambda: showImage(nameDb.get(), nameTable.get()))
    confirm.place(x=215, y=290)


ventana_principal()
