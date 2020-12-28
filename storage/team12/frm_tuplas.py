from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
#from crud_tabla import CRUD_Tabla

nombre_BaseDatos = ""

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

def view_insert():
    
    def guardar():
        v_register = txtRegister.get()
        if v_register:
            txtRegister.delete(0, END)
            #value = CRUD_Tabla().createTable(nombre_BaseDatos, name_table, column_table)
            value = 0
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos Inexistente')
            elif value == 3:
                messagebox.showinfo('', 'Tabla No Existente')
            elif value == 4:
                messagebox.showinfo('', 'Llave Primaria Duplicada')
            elif value == 5:
                messagebox.showinfo('', 'Columnas Fuera de Limites')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Insert","#FCFCFB", 500, 350)
    lblRegister = Label(window, text= 'Ingrese su Registro', bg="#FCFCFB")
    lblRegister.place(x = 125, y = 75)
    txtRegister = Entry(window, width = 35)
    txtRegister.place(x = 100, y = 115)

    btn = Button(window, text='Guardar', command=guardar)
    btn.place(x = 350, y = 160)

def view_loadCSV():
    #list_words = CRUD_Tabla().shownTables(nombre_BaseDatos)
    list_words = []
    var = 0
    # Esta es la ventana principal
    ventana_principal = Tk()
    ventana_principal.title('Load CSV')
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
        #btn = Button(second_frame, text=word, width=58, height=2, bg="#DBE2FC", font=var_font, command=lambda txt=word:mostrarTablas(txt))
        btn = Button(second_frame, text=word, width=58, height=2, bg="#DBE2FC", font=var_font)
        btn.grid(row=var, column=0, pady=1)
        var += 1

    ventana_principal.mainloop()

def view_extractRow():
    
    def guardar():
        v_columns = txtColumns.get()
        if v_columns:
            txtColumns.delete(0, END)
            #value = CRUD_Tabla().createTable(nombre_BaseDatos, name_table, column_table)
            value = None
            if value:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            else:
                messagebox.showinfo('', 'No Hay Registro')

    window = Tk()
    edicionPantalla(window,  "Extract Row","#FCFCFB", 500, 350)
    lblColumns = Label(window, text= 'Ingrese su Registro', bg="#FCFCFB")
    lblColumns.place(x = 125, y = 75)
    txtColumns = Entry(window, width = 35)
    txtColumns.place(x = 100, y = 115)

    btn = Button(window, text='Obtener', command=guardar)
    btn.place(x = 350, y = 160)

def view_update():

    def actualizar():
        var_register = txtRegister.get()
        var_columnas = txtColumnas.get()
        if var_register and var_columnas:
            txtRegister.delete(0, END)
            txtColumnas.delete(0, END)
            #value = CRUD_Tabla().dropTable(nombre_BaseDatos, name_database)
            value = 0
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            elif value == 3:
                messagebox.showinfo('', 'Tabla No Existente')
            elif value == 4:
                messagebox.showinfo('', 'Llave Primaria No Existe')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Update","#FCFCFB", 500, 350)
    lblRegister = Label(window, text= 'Ingrese el Register', bg="#FCFCFB")
    lblRegister.place(x = 125, y = 75)
    txtRegister = Entry(window, width = 35)
    txtRegister.place(x = 100, y = 110)
    lblColumnas = Label(window, text= 'Ingrese las Columnas', bg="#FCFCFB")
    lblColumnas.place(x = 125, y = 150)
    txtColumnas = Entry(window, width = 35)
    txtColumnas.place(x = 100, y = 185)
    btn = Button(window, text='Actualizar', command=actualizar)
    btn.place(x = 350, y = 250)

def view_delete():
    
    def ejecutar():
        var_columnas = txtColumnas.get()
        if var_columnas:
            txtColumnas.delete(0, END)
            #value = CRUD_Tabla().extractTable(nombre_BaseDatos, name_table)
            value = 0
            if value:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            elif value == 3:
                messagebox.showinfo('', 'Tabla No Existente')
            elif value == 4:
                messagebox.showinfo('', 'Llave Primaria No Existe')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Delete","#FCFCFB", 500, 350)
    lblColumnas = Label(window, text= 'Ingrese sus Columnas', bg="#FCFCFB")
    lblColumnas.place(x = 125, y = 75)
    txtColumnas = Entry(window, width = 35)
    txtColumnas.place(x = 100, y = 115)

    btn = Button(window, text='Eliminar', command=ejecutar)
    btn.place(x = 350, y = 190)

def view_truncate():
    #value = CRUD_Tabla().alterTable(nombre_BaseDatos, v_table, v_default)
    value = 0
    if value == 0:
        messagebox.showinfo('', 'Operacion Exitosa')
    elif value == 2:
        messagebox.showinfo('', 'Base de Datos No Existente')
    elif value == 3:
        messagebox.showinfo('', 'Nombre de Tabla No Existente')
    else:
        messagebox.showinfo('', 'Error en la Operacion')

def mostrarTuplas(nombre_BD, nombre_TB, f_window):
    f_window.destroy() 
    window = Tk()
    ancho_ventana = 1000
    alto_ventana = 300
    edicionPantalla(window,"Tuplas","white",  ancho_ventana, alto_ventana)

    var_width = 25
    separacion = 3
    var_height = int(var_width//5)
    var_font = tkFont.Font(size=12, weight="bold", family="Arial")

    encabezado = Label(window, text="", bg="white",width=25)
    encabezado.grid(padx=separacion, pady=separacion, row=0, column=0, columnspan=3)

    izquierda = Label(window, text="", bg="white",width=16)
    izquierda.grid(padx=separacion, pady=separacion, row=1, column=0, rowspan=5)

    ###############################################################################
    ###############################################################################

    btnInsert = Button(window, text="INSERT", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_insert)
    btnInsert.grid(padx=separacion, pady=separacion, row=1, column=1)

    btnLoadCSV = Button(window, text="LOAD CSV", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_loadCSV)
    btnLoadCSV.grid(padx=separacion, pady=separacion, row=1, column=2)    

    btnExtractRow = Button(window, text="EXTRACT ROW", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_extractRow)
    btnExtractRow.grid(padx=separacion, pady=separacion, row=1, column=3)

    ###############################################################################
    ###############################################################################

    btnUpdate = Button(window, text="UPDATE", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command=view_update)
    btnUpdate.grid(padx=separacion, pady=separacion, row=2, column=1)
    
    btnDelete = Button(window, text="DELETE", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command=view_delete)
    btnDelete.grid(padx=separacion, pady=separacion, row=2, column=2)

    btnTruncate = Button(window, text="TRUNCATE", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command=view_truncate)
    btnTruncate.grid(padx=separacion, pady=separacion, row=2, column=3)

    ###############################################################################
    ###############################################################################

    global nombre_BaseDatos
    nombre_BaseDatos = nombre_BD
    window.mainloop()
