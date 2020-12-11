from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def ventana_principal():
    # Raíz de la aplicación
    app = Tk()
    app.title("    TYTUS")
    app.resizable(0, 0)
    app.iconbitmap('./images/blockchain_.ico')
    ancho_ventana = 900
    alto_ventana = 700
    app.config(bg="linen", width=ancho_ventana, height=alto_ventana)  # linen - light cyan - ghost white WhiteSmoke
    # Centrar ventana
    x_ventana = app.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = app.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    app.geometry(posicion)

    # Fondo
    bg_image = PhotoImage(file="./images/fondo.png")
    x = Label(image=bg_image, bg="linen")
    x.place(x=0, y=0)
    x.pack()

    # Botones
    img_db = PhotoImage(file="./images/base-de-datos.png")
    db = Button(text="Bases de datos", image=img_db, compound="top", font=("Georgia", 16), command=ventana_db)
    db.place(x=500, y=200)

    img_subir = PhotoImage(file="./images/subir.png")
    db = Button(text="Cargar", image=img_subir, compound="top", font=("Georgia", 16), command=abrir_archivo)
    db.place(x=600, y=400)

    # Selección del combobox
    def selection_changed( event):
        combo_bases_db(combo.get())

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(font=fuente)
    combo.place(x=680, y=200)

    combo["values"] = ["createDatabase", "showDatabases", "alterDatabase", "dropDatabase"]
    combo.bind("<<ComboboxSelected>>", selection_changed)
    etiqueta = Label(text="Funciones", bg="linen", font=("Georgia", 16)).place(x=720, y=225)

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


def ventana_db():
    app2 = Tk()
    app2.title("    TYTUS")
    app2.resizable(0, 0)
    app2.iconbitmap('./images/blockchain_.ico')

    ancho_ventana = 500
    alto_ventana = 700
    app2.config(bg="linen", width=ancho_ventana, height=alto_ventana)  # linen - light cyan - ghost white WhiteSmoke
    # Centrar ventana
    x_ventana = app2.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = app2.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    app2.geometry(posicion)

    # Fondo
    bg_image = PhotoImage(file="./images/notas.png")
    x = Label(image=bg_image, bg="linen")
    x.place(x=200, y=200)
    x.pack()


# CARGAR ARCHIVO
def abrir_archivo():
    nombre_archivo = filedialog.askopenfilename(title='Seleccione archivo')
    if nombre_archivo != '':
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = archivo.read()
        archivo.close()
        print(contenido)


ventana_principal()
