from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


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
    app = Toplevel()
    configuracion_defecto(app)
    app.state('zoomed')

    img = PhotoImage(file='./images/'+imagen+'')
    label = Label(app, image=img)
    label.image = img
    label.grid(row=0, column=0)


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
    db = Button(text="Cargar", bg="#FFFFFF", image=img_subir, compound="top", font=("Georgia", 16), command=abrir_archivo)
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
        ventana_lista_tablas(app2, combo.get())

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(app2, font=fuente)
    combo.place(x=150, y=330)

    Label(app2, text="Seleccionar DB",  bg="#F0FFFF", font=("Georgia", 13)).place(x=180, y=300)
    combo["values"] = ["DB1"]
    combo.bind("<<ComboboxSelected>>", selection_changed)

    # Obtener imagen de la lista de db
    img = 'Alien.png'
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

    Label(app, text="Tuplas de DB:\n"+db, bg="#F0FFFF", font=("Georgia", 13)).place(x=190, y=300)
    combo["values"] = ["lista de tablas"]
    combo.bind("<<ComboboxSelected>>", selection_changed)

    # Obtener imagen de la lista de db
    img = 'fondo.png'
    boton_estructura = Button(app, text="Ver estructura", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_imagen(img))
    boton_estructura.place(x=380, y=5)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_db(app))
    boton_regresar.place(x=10, y=5)

    # ---------------------------------------------------- FUNCIONES ---------------------------------------------------
    def cargar_tablas(combo_box):
        # Cargar datos de prueba
        array = []
        for i in range(0, 100):
            array.append(i)
        combo_box['values'] = array

    cargar_tablas(combo)


def ventana_tupla(ventana, tupla, db):
    if ventana != '':
        ventana.withdraw()
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 700)

    img = PhotoImage(file='./images/B+.png')
    label = Label(app, image=img, bg="#F0FFFF")
    label.image = img
    label.place(x=95, y=25)

    # Combobox
    def selection_changed(event):
        mensaje = combo.get()+'\nnombre: Kevin\n'+'Apellido: Sandoval'
        messagebox.showinfo(tupla, mensaje)
        ventana_tupla('', tupla, db)

    combo = ttk.Combobox(app, font=("Georgia", 10))
    combo.place(x=150, y=300)

    Label(app, text="Registro de la tupla:\n" + tupla, bg="#F0FFFF", font=("Georgia", 13)).place(x=180, y=250)
    combo["values"] = ['Registro1', 'Registro2', 'Registro3']
    combo.bind("<<ComboboxSelected>>", selection_changed)

    img = 'B+.png'
    boton_estructura = Button(app, text="Ver estructura", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_imagen(img))
    boton_estructura.place(x=380, y=5)
    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_lista_tablas(app, db))
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
        seleccion = combo_db.get()
        if seleccion == 'createDatabase':
            ventana_create_database(app)
        if seleccion == 'showDatabases':
            ventana_show_database()
            ventana_funciones(app)
        if seleccion == 'alterDatabase':
            ventana_alter_database(app)
        if seleccion == 'dropDatabase':
            ventana_drop_database(app)
        print(combo_db.get())

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
        if seleccion == 'definePK':
            ventana_define_pk(app)
        if seleccion == 'showTables':
            ventana_show_tables()
            ventana_funciones(app)
        if seleccion == 'alterTable':
            ventana_alter_table(app)
        if seleccion == 'dropTable':
            ventana_drop_table(app)
        if seleccion == 'alterAddColumn':
            ventana_alter_addcolumn(app)
        if seleccion == 'alterDropColumn':
            ventana_alter_dropcolumn(app)
        if seleccion == 'extractTable':
            ventana_extract_table(app)
        if seleccion == 'extractRangeTable':
            ventana_extract_rangetable(app)
        print(combo_tabla.get())

    combo_tabla = ttk.Combobox(app, font=("Georgia", 10))
    combo_tabla.place(x=150, y=330)
    Label(app, text='Tablas', bg="#F0FFFF", font=("Georgia", 13)).place(x=210, y=300)
    combo_tabla["values"] = ['createTable', 'definePK', 'defineFK', 'showTables', 'alterTable', 'dropTable',
                             'alterAddColumn', 'alterDropColumn', 'extractTable', 'extractRangeTable']
    combo_tabla.bind("<<ComboboxSelected>>", selection_changed_tablas)

    # Combobox tuplas
    def selection_changed_tuplas(event):
        seleccion = combo_tuplas.get()
        if seleccion == 'insert':
            ventana_tupla_insert(app)
        if seleccion == 'update':
            ventana_tupla_update(app)
        if seleccion == 'deleteTable':
            ventana_deletetable(app)
        if seleccion == 'truncate':
            ventana_tupla_truncate(app)
        if seleccion == 'extractRow':
            ventana_extract_row(app)
        print(combo_tuplas.get())

    combo_tuplas = ttk.Combobox(app, font=("Georgia", 10))
    combo_tuplas.place(x=150, y=430)
    Label(app, text='Tuplas', bg="#F0FFFF", font=("Georgia", 13)).place(x=210, y=400)
    combo_tuplas["values"] = ['insert', 'update', 'deleteTable', 'truncate', 'extractRow']
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

    bt = Button(app, text="Guardar", font='Georgia 10', bg='#98FB98')
    bt.place(x=220, y=260)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_show_database():
    bases_datos = '--------------------\nDB1\nDB2\nDB2\n--------------------'
    messagebox.showinfo('BASES DE DATOS', bases_datos)


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

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado exitosamente')
        ventana_funciones(app)

    bt = Button(app, text="Guardar", font='Georgia 10', bg='#98FB98', command=mensaje)
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

    def mensaje_drop_database():
        messagebox.showinfo('', 'DB eliminada correctamente')

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje_drop_database)
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

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado exitosamente')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
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
    lista_columnas = Text(app, height=6, width=30)
    lista_columnas.place(x=215, y=260)

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado exitosamente')
        print(lista_columnas.get("1.0", END), end='')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
    bt.place(x=215, y=380)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


def ventana_show_tables():
    tablas = '--------------------\nT1\nT2\nT3\n--------------------'
    messagebox.showinfo('showTables', tablas)


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

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado exitosamente')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
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
    nombre_actual = Entry(app, font=("Georgia", 10))
    nombre_actual.place(x=190, y=230, width=200)

    def mensaje():
        messagebox.showinfo('', 'Tabla eliminanda\n  exitosamente')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
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

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado\n  exitosamente')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
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

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado\n  exitosamente')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
    bt.place(x=220, y=290)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


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

    def mensaje():
        registros = '--------------------\nTABLA: Estudiante\nRegistro1\nRegistro2\nRegistro3\n--------------------'
        messagebox.showinfo('extractTable', registros)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
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

    Label(app, text='Límite inferior:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    limite_inferior = Entry(app, font=("Georgia", 10))
    limite_inferior.place(x=190, y=260, width=200)

    Label(app, text='Límite superior:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=290)
    limite_superior = Entry(app, font=("Georgia", 10))
    limite_superior.place(x=190, y=290, width=200)

    def mensaje():
        registros_rango = '--------------------\nRegistros de una tabla\nen un rango especifico\n--------------------'
        messagebox.showinfo('extractTable', registros_rango)
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
    bt.place(x=220, y=310)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


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
    lista_campos = Text(app, height=6, width=30)
    lista_campos.place(x=215, y=260)

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado exitosamente')
        print(lista_campos.get("1.0", END), end='')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
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

    Label(app, text='ID:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=260)
    id_tabla = Entry(app, font=("Georgia", 10))
    id_tabla.place(x=210, y=260, width=200)

    Label(app, text='Número de columna:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=290)
    numero_columna = Entry(app, font=("Georgia", 10))
    numero_columna.place(x=210, y=290, width=200)

    Label(app, text='Valor:', bg="#F0FFFF", font=("Georgia", 10)).place(x=70, y=320)
    valor = Entry(app, font=("Georgia", 10))
    valor.place(x=210, y=320, width=200)

    def mensaje():
        mensaje = 'Proceso realizado\n  exitosamente'
        messagebox.showinfo('extractTable', mensaje)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
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

    def mensaje():
        messagebox.showinfo('', 'Proceso realizado exitosamente')
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
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
    id_registro = Entry(app, font=("Georgia", 10))
    id_registro.place(x=215, y=260, width=245)

    def mensaje():
        tupla = 'devuelve una tupla especificada'
        messagebox.showinfo('', tupla)
        ventana_funciones(app)

    bt = Button(app, text="Confirmar", font='Georgia 10', bg='#98FB98', command=mensaje)
    bt.place(x=215, y=300)

    boton_regresar = Button(app, text="Regresar", bg="#FFFFFF", compound="top", font=("Georgia", 10), command=lambda: ventana_funciones(app))
    boton_regresar.place(x=10, y=5)


# CARGAR ARCHIVO
def abrir_archivo():
    nombre_archivo = filedialog.askopenfilename(title='Seleccione archivo')
    if nombre_archivo != '':
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = archivo.read()
        archivo.close()
        print(contenido)


ventana_principal()

