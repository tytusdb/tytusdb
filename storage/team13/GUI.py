# Package:      BPlusMode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from BPlusMode import *
from PIL import Image


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


def ventana_imagen(imagen):
    try:
        app = Toplevel()
        configuracion_defecto(app)
        app.state('zoomed')

        img = PhotoImage(file='../team13/'+imagen+'')
        label = Label(app, image=img)
        label.image = img
        label.grid(row=0, column=0)
        label.pack(side="bottom", fill="both", expand="yes")
        
        abrir_img = Image.open('../team13/' + imagen + '')
        abrir_img.show()
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

    # Botones
    img_db = PhotoImage(file="./images/base-de-datos.png")
    db = Button(text="Bases de datos",  bg="#FFFFFF", image=img_db, compound="top", font=("Georgia", 16), command=lambda: ventana_db(''))
    db.place(x=500, y=200)

    img_subir = PhotoImage(file="./images/subir.png")
    db = Button(text="Cargar", bg="#FFFFFF", image=img_subir, compound="top", font=("Georgia", 16), command=ventana_loadCSV)
    db.place(x=600, y=400)

    img_func = PhotoImage(file="./images/codificacion.png")
    db = Button(text="Funciones", bg="#FFFFFF", image=img_func, compound="top", font=("Georgia", 16), command=lambda: ventana_funciones(''))
    db.place(x=700, y=200)

    # ---------------------------------------------------- FUNCIONES ---------------------------------------------------
    # SELECCIÓN COMBOBOX
    def combo_bases_db(seleccion):
        if seleccion == 'createDatabase':
            print('create_database')
        elif seleccion == 'showDatabases':
            print('showDatabases')
        elif seleccion == 'alterDatabase':
            print('alterDatabase')
        elif seleccion == 'dropDatabase':
            print('dropDatabase')

    app.mainloop()


def ventana_db(ventana):
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
        ventana_lista_tablas(app2, seleccion)

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(app2, font=fuente)
    combo.place(x=150, y=330)

    if CheckData():
        DB_archivo = Load("BD")

        Label(app2, text="Seleccionar DB",  bg="#F0FFFF", font=("Georgia", 13)).place(x=180, y=300)
        combo["values"] = DB_archivo.lista_bases()
        combo.bind("<<ComboboxSelected>>", selection_changed)

        # Obtener imagen de la lista de db
        DB_archivo.graficar()
        img = 'AVL_DB.png'
        boton_estructura = Button(app2, text="Ver estructura", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_imagen(img))
        boton_estructura.place(x=380, y=5)


def ventana_lista_tablas(ventana, db):
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
        ventana_tupla(app, combo.get(), db)
        print(combo.get())

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(app, font=fuente)
    combo.place(x=150, y=350)
    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_db(app))
    boton_regresar.place(x=10, y=5)

    Label(app, text="Tablas de DB:\n"+db, bg="#F0FFFF", font=("Georgia", 13)).place(x=190, y=300)

    if CheckData():
        DataBase = Load("BD")
        db = DataBase.buscar(db)
        lista_tablas = db.avlTable.lista_tablas()
        print(db.name + ' ', lista_tablas)

        if lista_tablas is None:
            messagebox.showinfo('', 'LA DB "'+db.name+'" NO TIENE TABLAS')
            ventana_db(app)
        else:
            combo["values"] = lista_tablas
            combo.bind("<<ComboboxSelected>>", selection_changed)

            db.avlTable.graficar()
            img = 'AVL_T.png'
            boton_estructura = Button(app, text="Ver estructura", bg="#FFFFFF", compound="top", font=("Georgia", 10),
                                      command=lambda: ventana_imagen(img))
            boton_estructura.place(x=380, y=5)


def ventana_tupla(ventana, tupla, db):
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

    def mensaje():
        if CheckData():
            DataBase = Load("BD")
            base = DataBase.buscar(str(db.name))
            table = base.avlTable.buscar(tupla)
            try:
                lista = table.bPlus.lista_nodos()
                if lista is not None:
                    table.bPlus.graphTree()
                    img = 'ArbolB+.png'
                    boton_estructura = Button(app, text="Ver estructura", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_imagen(img))
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

                    #tabla.place(x=50, y=350)
                    mensaje = ''
                    contador = 0
                    for i in lista:
                        contador += 1
                        for x in i:
                            mensaje += str(x) + "  "
                        print(mensaje)
                        tabla.insert('', 'end', text=mensaje)
                        mensaje = ''
            except:
                messagebox.showinfo('', 'LA TABLA NO TIENE REGISTROS')
                ventana_lista_tablas(app, db.name)

    bt = Button(app, text="Ver registros", font='Georgia 10', bg='#98FB98', command=mensaje)
    bt.place(x=200, y=310)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_lista_tablas(app, db.name))
    boton_regresar.place(x=10, y=5)


def ventana_funciones(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 700)
    Label(app, text='FUNCIONES', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=100)

    # Combobox db
    def selection_changed_db(event):
        try:
            seleccion = combo_db.get()
            if seleccion == 'createDatabase':
                ventana_create_database(app)
            if seleccion == 'showDatabases':
                ventana_show_database()
            if seleccion == 'alterDatabase':
                ventana_alter_database(app)
            if seleccion == 'dropDatabase':
                ventana_drop_database(app)
            print(combo_db.get())
        except:
            print('--')

    combo_db = ttk.Combobox(app, font=("Georgia", 10))
    combo_db.place(x=150, y=230)
    Label(app, text='Bases de datos', bg="#F0FFFF", font=("Georgia", 13)).place(x=200, y=200)
    combo_db["values"] = ['createDatabase', 'showDatabases', 'alterDatabase', 'dropDatabase']
    combo_db.bind("<<ComboboxSelected>>", selection_changed_db)

    # Combobox tablas
    def selection_changed_tablas(event):
        seleccion = combo_tabla.get()
        if seleccion == 'createTable':
            ventana_create_table(app)
        elif seleccion == 'showTables':
            ventana_show_tables(app)
        elif seleccion == 'extractTable':
            ventana_extract_table(app)
        elif seleccion == 'extractRangeTable':
            ventana_extract_rangetable(app)
        elif seleccion == 'alterAddPK':
            ventana_define_pk(app)
        elif seleccion == 'alterDropPK':
            ventana_alterDropPK(app)
        elif seleccion == 'alterTable':
            ventana_alter_table(app)
        elif seleccion == 'alterAddColumn':
            ventana_alter_addcolumn(app)
        elif seleccion == 'alterDropColumn':
            ventana_alter_dropcolumn(app)
        elif seleccion == 'dropTable':
            ventana_drop_table(app)

        print(combo_tabla.get())

    combo_tabla = ttk.Combobox(app, font=("Georgia", 10))
    combo_tabla.place(x=150, y=330)
    Label(app, text='Tablas', bg="#F0FFFF", font=("Georgia", 13)).place(x=210, y=300)
    combo_tabla["values"] = ['createTable', 'showTables', 'extractTable', 'extractRangeTable','alterAddPK', 'alterDropPK',
                             'alterAddFK', 'alterAddIndex', 'alterTable', 'alterAddColumn', 'alterDropColumn', 'dropTable']
    combo_tabla.bind("<<ComboboxSelected>>", selection_changed_tablas)

    # Combobox tuplas
    def selection_changed_tuplas(event):
        seleccion = combo_tuplas.get()
        if seleccion == 'insert':
            ventana_tupla_insert(app)
        elif seleccion == 'loadCSV':
            print('Cargar archivo')
        elif seleccion == 'extractRow':
            ventana_extract_row(app)
        elif seleccion == 'update':
            ventana_tupla_update(app)
        if seleccion == 'delete':
            ventana_deletetable(app)
        if seleccion == 'truncate':
            ventana_tupla_truncate(app)

        print(combo_tuplas.get())

    combo_tuplas = ttk.Combobox(app, font=("Georgia", 10))
    combo_tuplas.place(x=150, y=430)
    Label(app, text='Tuplas', bg="#F0FFFF", font=("Georgia", 13)).place(x=210, y=400)
    combo_tuplas["values"] = ['insert','loadCSV', 'extractRow', 'update', 'delete', 'truncate']
    combo_tuplas.bind("<<ComboboxSelected>>", selection_changed_tuplas)


# --------------------------------------------- FUNCIONES DE BASES DE DATOS --------------------------------------------
def ventana_create_database(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='createDatabase', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre', bg="#F0FFFF", font=("Georgia", 10)).place(x=100, y=200)
    nombre_database = Entry(app, width=25, font=("Georgia", 10))
    nombre_database.grid(row=0, column=0, padx=180, pady=200)

    def guardar(nameDb):
        valor_retorno = str(createDatabase(nameDb))
        print(valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB EXISTENTE')
        ventana_funciones(app)

    bt = Button(app, text="Guardar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_database.get()))
    bt.place(x=220, y=260)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_show_database():
    app = Tk()
    color = "#F0FFFF"
    configuracion_defecto(app)
    centrar_ventana(app, 700, 500)

    tabla = ttk.Treeview(app, height=21)
    tabla["columns"] = "#0"
    tabla.column("#0", width=450, minwidth=450)
    tabla.heading("#0", text="BASES DE DATOS", anchor="center")

    tabla.place(x=20, y=20)
    for i in showDatabases():
        tabla.insert('', 'end', text=i)

    app.mainloop()


def ventana_alter_database(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='alterDatabase', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre actual:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_actual = Entry(app, font=("Georgia", 10))
    nombre_actual.place(x=190, y=200, width=200)

    Label(app, text='Nombre nuevo:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_nuevo = Entry(app, font=("Georgia", 10))
    nombre_nuevo.place(x=190, y=230, width=200)

    def guardar(databaseOld, databaseNew):
        valor_retorno = str(alterDatabase(databaseOld, databaseNew))
        print('alterDatabase: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'databaseOld NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'databaseNew EXISTENTE')
        ventana_funciones(app)

    bt = Button(app, text="Guardar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_actual.get(), nombre_nuevo.get()))
    bt.place(x=220, y=260)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_drop_database(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='dropDatabase', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre', bg="#F0FFFF", font=("Georgia", 10)).place(x=100, y=200)
    nombre_database = Entry(app, font=("Georgia", 10))
    nombre_database.place(x=180, y=200, width=200)

    def guardar(database):
        valor_retorno = str(dropDatabase(database))
        print('dropDatabase: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_database.get()))
    bt.place(x=220, y=260)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


# ------------------------------------------------- FUNCIONES DE TABLAS ------------------------------------------------
def ventana_create_table(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='createTable', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=215, y=200, width=200)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=215, y=230, width=200)

    Label(app, text='Número de columnas:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    numero_columnas = Entry(app, font=("Georgia", 10))
    numero_columnas.place(x=215, y=260, width=200)

    def guardar(database, table, numberColumns):
        valor_retorno = str(createTable(database, table, numberColumns))
        print('createTable: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA EXISTENTE')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), nombre_tabla.get(), int(numero_columnas.get())))
    bt.place(x=220, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_define_pk(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='definePK', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=215, y=200, width=245)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=215, y=230, width=245)

    Label(app, text='Lista de columnas:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    columnas = Entry(app, font=("Georgia", 10))
    columnas.place(x=215, y=260, width=245)


    def guardar(database, table):
        texto = columnas.get()
        lista = texto.split(',')

        lista = list(map(int, lista))

        print('COLUMNAS: ', lista)
        valor_retorno = str(alterAddPK(database, table, lista))
        print('alterAddPK: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA NO EXISTENTE')
        elif valor_retorno == '4':
            messagebox.showinfo('', 'PK EXISTENTE')
        elif valor_retorno == '5':
            messagebox.showinfo('', 'COLUMNAS FUERA DE LÍMITE')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), nombre_tabla.get()))
    bt.place(x=215, y=380)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_alterDropPK(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='alterDropPK', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=190, y=200, width=200)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    tabla = Entry(app, font=("Georgia", 10))
    tabla.place(x=190, y=230, width=200)

    def guardar(database, table):
        valor_retorno = str(alterDropPK(database, table))
        print('alterDropPK: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA NO EXISTENTE')
        elif valor_retorno == '4':
            messagebox.showinfo('', 'PK NO EXISTE')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), tabla.get()))
    bt.place(x=220, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_show_tables(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='showTables', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=215, y=200, width=200)

    def guardar(database):
        valor_retorno = showTables(database)
        if valor_retorno: # No vacia
            ver_tablas(database)
        elif valor_retorno is None:
            messagebox.showinfo('', 'DB NO EXISTE')
            ventana_funciones(app)
        else:
            messagebox.showinfo('', 'NO EXISTEN TABLAS')
            ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get()))
    bt.place(x=220, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ver_tablas(database):
    app = Tk()
    color = "#F0FFFF"
    configuracion_defecto(app)
    centrar_ventana(app, 700, 500)

    tabla = ttk.Treeview(app, height=21)
    tabla["columns"] = "#0"
    tabla.column("#0", width=450, minwidth=450)
    tabla.heading("#0", text="TABLAS DE DB", anchor="center")

    tabla.place(x=20, y=20)
    for i in showTables(database):
        tabla.insert('', 'end', text=i)

    app.mainloop()


def ventana_alter_table(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='alterTable', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=190, y=200, width=200)

    Label(app, text='Nombre actual:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_actual = Entry(app, font=("Georgia", 10))
    nombre_actual.place(x=190, y=230, width=200)

    Label(app, text='Nombre nuevo:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    nombre_nuevo = Entry(app, font=("Georgia", 10))
    nombre_nuevo.place(x=190, y=260, width=200)

    def guardar(database, tableOld, tableNew):
        valor_retorno = str(alterTable(database, tableOld, tableNew))
        print('alterTable: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'tableOld NO EXISTENTE')
        elif valor_retorno == '4':
            messagebox.showinfo('', 'tableNew EXISTENTE')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda:guardar(nombre_db.get(), nombre_actual.get(), nombre_nuevo.get()))
    bt.place(x=220, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_drop_table(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='dropTable', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=190, y=200, width=200)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=190, y=230, width=200)

    def guardar(database, table):
        print('DB:', database, 'TABLA:',table)
        valor_retorno = str(dropTable(database, table))

        print('dropTable: ', valor_retorno)
        print(showTables(database))
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA NO EXISTENTE')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), nombre_tabla.get()))
    bt.place(x=220, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_alter_addcolumn(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='alterAddColumn', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=190, y=200, width=200)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=190, y=230, width=200)

    Label(app, text='Columna:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    columna = Entry(app, font=("Georgia", 10))
    columna.place(x=190, y=260, width=200)

    def guardar(database, table, default):
        valor_retorno = str(alterAddColumn(database, table, default))
        print('alterAddColumn: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA NO EXISTENTE')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), nombre_tabla.get(), columna.get()))
    bt.place(x=220, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_alter_dropcolumn(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='alterDropColumn', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=190, y=200, width=200)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=190, y=230, width=200)

    Label(app, text='Número columna:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    columna = Entry(app, font=("Georgia", 10))
    columna.place(x=190, y=260, width=200)

    def guardar(database, table, columnNumber):
        valor_retorno = str(alterDropColumn(database, table, columnNumber))
        print('alterAddColumn: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA NO EXISTENTE')
        elif valor_retorno == '4':
            messagebox.showinfo('', 'LLAVE NO PUEDE ELIMINARSE\nTABLA NO PUEDE QUEDARSE SIN COLUMNAS')
        elif valor_retorno == '5':
            messagebox.showinfo('', 'COLUMNA FUERA DE LÍMITES')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), nombre_tabla.get(), int(columna.get())))
    bt.place(x=220, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ver_extract_table(lista):
    app = Tk()
    color = "#F0FFFF"
    configuracion_defecto(app)
    centrar_ventana(app, 700, 500)

    tabla = ttk.Treeview(app, height=21)
    tabla["columns"] = "#0"
    tabla.column("#0", width=450, minwidth=450)
    tabla.heading("#0", text="TABLAS DE DB", anchor="center")

    tabla.place(x=20, y=20)
    print(lista)
    for i in lista:
        tabla.insert('', 'end', text=i)

    app.mainloop()


def ventana_extract_table(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='extractTable', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=190, y=200, width=200)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=190, y=230, width=200)

    def guardar(database, table):
        valor_retorno = extractTable(database, table)
        if valor_retorno: # No vacia
            ver_extract_table(valor_retorno)
        elif valor_retorno is None:
            messagebox.showinfo('', 'DB NO EXISTE')
            ventana_funciones(app)
        else:
            messagebox.showinfo('', 'NO EXISTEN TABLAS')
            ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), nombre_tabla.get()))
    bt.place(x=220, y=250)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_extract_rangetable(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='extractRangeTable', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=190, y=200, width=200)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=190, y=230, width=200)

    Label(app, text='Columna:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    numero_columna = Entry(app, font=("Georgia", 10))
    numero_columna.place(x=190, y=260, width=200)

    Label(app, text='Límite inferior:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=290)
    limite_inferior = Entry(app, font=("Georgia", 10))
    limite_inferior.place(x=190, y=290, width=200)

    Label(app, text='Límite superior:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=320)
    limite_superior = Entry(app, font=("Georgia", 10))
    limite_superior.place(x=190, y=320, width=200)

    def guardar(database, table, columnNumber, lower, upper):
        valor_retorno = extractRangeTable(database, table, columnNumber, lower, upper)
        print('extractRangeTable: ', valor_retorno)
        if valor_retorno:  # No vacia
            ver_extractRangeTable(valor_retorno)
        else:
            messagebox.showinfo('', 'LISTA VACIA O CON PROBLEMAS')
            ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda:guardar(nombre_db.get(), nombre_tabla.get(), int(numero_columna.get()), limite_inferior.get(), limite_superior.get()))
    bt.place(x=220, y=370)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ver_extractRangeTable(lista):
    app = Tk()
    color = "#F0FFFF"
    configuracion_defecto(app)
    centrar_ventana(app, 700, 500)

    tabla = ttk.Treeview(app, height=21)
    tabla["columns"] = "#0"
    tabla.column("#0", width=450, minwidth=450)
    tabla.heading("#0", text="extractRangeTable", anchor="center")

    tabla.place(x=20, y=20)
    print(lista)
    for i in lista:
        tabla.insert('', 'end', text=i)

    app.mainloop()

# ------------------------------------------------- FUNCIONES DE TUPLAS ------------------------------------------------
def ventana_tupla_insert(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='insert', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=215, y=200, width=245)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=215, y=230, width=245)

    Label(app, text='Lista de campos:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    lista_campos = Entry(app, font=("Georgia", 10))
    lista_campos.place(x=215, y=260, width=245)


    def guardar(database, table):
        texto = lista_campos.get()
        register = texto.split(',')
        valor_retorno = str(insert(database, table, register))
        print('alterAddColumn: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA NO EXISTENTE')
        elif valor_retorno == '4':
            messagebox.showinfo('', 'LLAVE PRIMARIA DUPLICADA')
        elif valor_retorno == '5':
            messagebox.showinfo('', 'COLUMNA FUERA DE LÍMITES')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), nombre_tabla.get()))
    bt.place(x=215, y=380)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_tupla_update(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='update', bg="#F0FFFF", font=("Georgia", 20)).place(x=200, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=210, y=200, width=200)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=210, y=230, width=200)

    Label(app, text='Llave primaria:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    pk = Entry(app, font=("Georgia", 10))
    pk.place(x=210, y=260, width=200)

    Label(app, text='LLave:Valor :', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=290)
    diccionario = Entry(app, font=("Georgia", 10))
    diccionario.place(x=210, y=290, width=250)

    def guardar(database, table):
        # Diccionarios
        dic = {}
        dic_texto = diccionario.get()
        clave_valor = dic_texto.split(',')
        lista_final = []
        for i in clave_valor:
            lista_final.append(i.split(':'))

        for i in lista_final:
            for x in range(0, len(i)):
                dic[i[0]] = i[1]

        # Llave primaria
        texto = pk.get()
        lista = texto.split(',')
        print('TYPE:', type(dic))
        print('DB: ', database)
        print('TABLE: ', table)
        print('LISTA FINAL: ', dic)
        print('PK: ', lista)

        valor_retorno = str(update(database, table, dic, lista))
        print('update: ', valor_retorno)
        if valor_retorno == '0':

            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA NO EXISTENTE')
        elif valor_retorno == '4':
            messagebox.showinfo('', 'LLAVE PRIMARIA NO EXISTE')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda: guardar(nombre_db.get(), nombre_tabla.get()))
    bt.place(x=220, y=370)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_deletetable(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='deleteTable', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=215, y=200, width=245)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=215, y=230, width=245)

    Label(app, text='ID:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    id_registro = Entry(app, font=("Georgia", 10))
    id_registro.place(x=215, y=260, width=245)

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado exitosamente')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
    bt.place(x=215, y=300)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_tupla_truncate(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='truncate', bg="#F0FFFF", font=("Georgia", 20)).place(x=200, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=215, y=200, width=245)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=215, y=230, width=245)

    def guardar(database, table):
        valor_retorno = str(truncate(database, table))
        print('truncate: ', valor_retorno)
        if valor_retorno == '0':
            messagebox.showinfo('', 'OPERACIÓN EXITOSA')
        elif valor_retorno == '1':
            messagebox.showinfo('', 'ERROR EN LA APLICACIÓN')
        elif valor_retorno == '2':
            messagebox.showinfo('', 'DB NO EXISTENTE')
        elif valor_retorno == '3':
            messagebox.showinfo('', 'TABLA NO EXISTENTE')

        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=lambda:guardar(nombre_db.get(), nombre_tabla.get()))
    bt.place(x=215, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_extract_row(ventana):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 600)
    Label(app, text='extractRow', bg="#F0FFFF", font=("Georgia", 20)).place(x=200, y=140)

    # Cajas de texto
    Label(app, text='Nombre DB:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=200)
    nombre_db = Entry(app, font=("Georgia", 10))
    nombre_db.place(x=215, y=200, width=245)

    Label(app, text='Nombre tabla:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=230)
    nombre_tabla = Entry(app, font=("Georgia", 10))
    nombre_tabla.place(x=215, y=230, width=245)

    Label(app, text='ID:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    lista_registros = Entry(app, font=("Georgia", 10))
    lista_registros.place(x=215, y=260, width=245)

    def guardar(database, table):
        texto = lista_registros.get()
        register = texto.split(',')  #['1','2']
        print(register)

        valor_retorno = extractRow(database, table, register)
        print('extractRow: ', valor_retorno)
        if valor_retorno:  # No vacia
            messagebox.showinfo('', valor_retorno)
        else:
            messagebox.showinfo('', 'LISTA VACIA O CON PROBLEMAS')
            ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98',command=lambda:guardar(nombre_db.get(), nombre_tabla.get()))
    bt.place(x=215, y=300)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
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


ventana_principal()


