from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from crud_bd import CRUD_DataBase

def mostrarTablas(text):
    crud = CRUD_DataBase()
    objeto = crud.searchDatabase(text)
    # print("objeto: {}".format(objeto.name))
    window = Tk()
    # Centrado de la Ventana
    ancho_ventana = 700
    alto_ventana = 450
    x_ventana = window.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = window.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    window.geometry(posicion)

    # Edicion de la Ventana
    window.resizable(0,0)
    window.title("Tablas")
    window.geometry('700x450')    

    window.mainloop()

def iniciar():
    crud = CRUD_DataBase()
    list_words = crud.showDatabases()
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
        btn = Button(second_frame, text=word, width=58, height=2, bg="#DBE2FC", font=var_font, command=lambda txt=word:mostrarTablas(txt))
        btn.grid(row=var, column=0, pady=1)
        var += 1

    ventana_principal.mainloop()