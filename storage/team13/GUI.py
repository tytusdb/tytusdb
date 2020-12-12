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
    db = Button(text="Funciones", bg="#FFFFFF", image=img_func, compound="top", font=("Georgia", 16), command=ventana_funciones)
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
        messagebox.showinfo(tupla, mensaje)  # título, mensaje
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


def ventana_funciones():
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 700)
    Label(app, text='FUNCIONES', bg="#F0FFFF", font=("Georgia", 20)).place(x=170, y=100)

    # Combobox db
    def selection_changed_db(event):
        print(combo_db.get())

    combo_db = ttk.Combobox(app, font=("Georgia", 10))
    combo_db.place(x=150, y=230)
    Label(app, text='Bases de datos', bg="#F0FFFF", font=("Georgia", 13)).place(x=200, y=200)
    combo_db["values"] = ['createDatabase', 'showDatabases', 'alterDatabase', 'dropDatabase']
    combo_db.bind("<<ComboboxSelected>>", selection_changed_db)

    # Combobox tablas
    def selection_changed_tablas(event):
        print(combo_tabla.get())

    combo_tabla = ttk.Combobox(app, font=("Georgia", 10))
    combo_tabla.place(x=150, y=330)
    Label(app, text='Tablas', bg="#F0FFFF", font=("Georgia", 13)).place(x=210, y=300)
    combo_tabla["values"] = ['createTable', 'definePK', 'defineFK', 'showTables', 'alterTable', 'dropTable',
                             'alterAddColumn', 'alterDropColumn', 'extractTable', 'extractRangeTable']
    combo_tabla.bind("<<ComboboxSelected>>", selection_changed_tablas)

    # Combobox tuplas
    def selection_changed_tuplas(event):
        print(combo_tuplas.get())

    combo_tuplas = ttk.Combobox(app, font=("Georgia", 10))
    combo_tuplas.place(x=150, y=430)
    Label(app, text='Tuplas', bg="#F0FFFF", font=("Georgia", 13)).place(x=210, y=400)
    combo_tuplas["values"] = ['insert', 'update', 'deleteTable', 'truncate', 'extractRow']
    combo_tuplas.bind("<<ComboboxSelected>>", selection_changed_tablas)


# CARGAR ARCHIVO
def abrir_archivo():
    nombre_archivo = filedialog.askopenfilename(title='Seleccione archivo')
    if nombre_archivo != '':
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = archivo.read()
        archivo.close()
        print(contenido)


ventana_principal()

