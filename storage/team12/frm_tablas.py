from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from crud_tabla import CRUD_Tabla
from frm_tuplas import mostrarTuplas

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

def view_createTable():
    
    def guardar():
        name_table = txtNombre.get()
        column_table = txtColumnas.get()
        if name_table:
            txtNombre.delete(0, END)
            txtColumnas.delete(0, END)
            value = CRUD_Tabla().createTable(nombre_BaseDatos, name_table, column_table)
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos Inexistente')
            elif value == 3:
                messagebox.showinfo('', 'Tabla Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Create Table","#FCFCFB", 500, 350)
    lblNombre = Label(window, text= 'Ingrese el Nombre de la Tabla', bg="#FCFCFB")
    lblNombre.place(x = 125, y = 75)
    txtNombre = Entry(window, width = 35)
    txtNombre.place(x = 100, y = 115)

    lblColumnas = Label(window, text= 'Ingrese la Cantidad de Columnas', bg="#FCFCFB")
    lblColumnas.place(x = 125, y = 150)
    txtColumnas = Entry(window, width = 35)
    txtColumnas.place(x = 100, y = 190)
    btn = Button(window, text='Guardar', command=guardar)
    btn.place(x = 350, y = 230)

def view_showTable():
    list_words = CRUD_Tabla().shownTables(nombre_BaseDatos)
    var = 0
    # Esta es la ventana principal
    ventana_principal = Tk()
    ventana_principal.title('show Table')
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
        btn = Button(second_frame, text=word, width=58, height=2, bg="#DBE2FC", font=var_font, command=lambda txt=word:mostrarTuplas(nombre_BaseDatos, txt, ventana_principal))
        btn.grid(row=var, column=0, pady=1)
        var += 1

    ventana_principal.mainloop()

def view_alterTable():

    def modificar():
        nombre_anterior = txtAnterior.get()
        nombre_nuevo= txtNueva.get()
        if nombre_anterior and nombre_nuevo:
            txtAnterior.delete(0, END)
            txtNueva.delete(0, END)
            value = CRUD_Tabla().alterTable(nombre_BaseDatos, nombre_anterior, nombre_nuevo)
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            elif value == 3:
                messagebox.showinfo('', 'Nombre de Tabla Anterior No Existente')
            elif value == 4:
                messagebox.showinfo('', 'Nombre de Tabla Nueva Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Alter Table","#FCFCFB", 500, 350)
    lblAnterior = Label(window, text= 'Nombre de la Tabla Anterior', bg="#FCFCFB")
    lblAnterior.place(x = 125, y = 75)
    txtAnterior = Entry(window, width = 35)
    txtAnterior.place(x = 100, y = 115)
    lblNueva = Label(window, text= 'Nombre de la Tabla Nueva', bg="#FCFCFB")
    lblNueva.place(x = 125, y = 150)
    txtNueva = Entry(window, width = 35)
    txtNueva.place(x = 100, y = 190)
    btnModificar = Button(window, text='Modificar', command = modificar)
    btnModificar.place(x = 345, y = 240)

def view_dropTable():

    def eliminar():
        name_database = txt.get()
        if name_database:
            txt.delete(0, END)
            value = CRUD_Tabla().dropTable(nombre_BaseDatos, name_database)
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            elif value == 3:
                messagebox.showinfo('', 'Tabla No Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Drop Table","#FCFCFB", 500, 350)
    lbl = Label(window, text= 'Ingrese el Nombre de la Base de Datos', bg="#FCFCFB")
    lbl.place(x = 125, y = 125)
    txt = Entry(window, width = 35)
    txt.place(x = 100, y = 160)
    btn = Button(window, text='Eliminar', command=eliminar)
    btn.place(x = 350, y = 200)

def view_extractTable():
    
    def ejecutar():
        name_table = txtNombre.get()
        if name_table:
            txtNombre.delete(0, END)
            value = CRUD_Tabla().extractTable(nombre_BaseDatos, name_table)
            if value:
                messagebox.showinfo('', 'Si Existe')
                window.destroy()
            else:
                messagebox.showinfo('', 'No Existe')

    window = Tk()
    edicionPantalla(window,  "Extract Table","#FCFCFB", 500, 350)
    lblNombre = Label(window, text= 'Ingrese el Nombre de la Tabla', bg="#FCFCFB")
    lblNombre.place(x = 125, y = 75)
    txtNombre = Entry(window, width = 35)
    txtNombre.place(x = 100, y = 115)

    btn = Button(window, text='Obtener', command=ejecutar)
    btn.place(x = 350, y = 190)

########################################
def view_extractRangeTable():
    def ejecutar():
        name_table = txtNombre.get()
        num_column = txtColumnas.get()
        s_pequenio = txtPequenio.get()
        s_grande = txtGrande.get()
        if name_table:
            txtNombre.delete(0, END)
            txtColumnas.delete(0, END)
            txtPequenio.delete(0, END)
            txtGrande.delete(0, END)
            value = CRUD_Tabla().extractRangeTable(nombre_BaseDatos, name_table, num_column, s_pequenio, s_grande)
            #value = 0
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos Inexistente')
            elif value == 3:
                messagebox.showinfo('', 'Tabla Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Extract Range Table","#FCFCFB", 500, 450)
    lblNombre = Label(window, text= 'Ingrese el Nombre de la Tabla', bg="#FCFCFB")
    lblNombre.place(x = 125, y = 50)
    txtNombre = Entry(window, width = 35)
    txtNombre.place(x = 100, y = 80)

    lblColumnas = Label(window, text= 'Ingrese el Numero de Columnas', bg="#FCFCFB")
    lblColumnas.place(x = 125, y = 125)
    txtColumnas = Entry(window, width = 35)
    txtColumnas.place(x = 100, y = 155)

    lblPequenio = Label(window, text= 'Ingrese el String mas Pequeño', bg="#FCFCFB")
    lblPequenio.place(x = 125, y = 200)
    txtPequenio = Entry(window, width = 35)
    txtPequenio.place(x = 100, y = 230)

    lblGrande = Label(window, text= 'Ingrese el String mas Grande', bg="#FCFCFB")
    lblGrande.place(x = 125, y = 275)
    txtGrande = Entry(window, width = 35)
    txtGrande.place(x = 100, y = 305)

    btn = Button(window, text='Guardar', command=ejecutar)
    btn.place(x = 350, y = 350)
########################################

def view_alterAddPk():
    def modificar():
        v_table = txtTabla.get()
        v_columnas = txtColumnas.get()
        if v_table and v_columnas:
            txtTabla.delete(0, END)
            txtColumnas.delete(0, END)
            lista = v_columnas.split(",")
            value = CRUD_Tabla().alterAddPK(nombre_BaseDatos, v_table,lista)
            #value = 0
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            elif value == 3:
                messagebox.showinfo('', 'Nombre de Tabla No Existente')
            elif value == 4:
                messagebox.showinfo('', 'Llave Primaria Existente')
            elif value == 5:
                messagebox.showinfo('', 'Columna Fuera de Limites')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Alter Add PK","#FCFCFB", 500, 350)
    lblTabla = Label(window, text= 'Nombre de la Tabla', bg="#FCFCFB")
    lblTabla.place(x = 125, y = 75)
    txtTabla = Entry(window, width = 35)
    txtTabla.place(x = 100, y = 115)
    lblColumnas = Label(window, text= 'Columnas', bg="#FCFCFB")
    lblColumnas.place(x = 125, y = 150)
    txtColumnas = Entry(window, width = 35)
    txtColumnas.place(x = 100, y = 190)
    btnModificar = Button(window, text='Modificar', command = modificar)
    btnModificar.place(x = 345, y = 240)

def view_alterDropPk():
    def eliminar():
        v_table = txtTabla.get()
        if v_table:
            txtTabla.delete(0, END)
            value = CRUD_Tabla().alterDropPK(nombre_BaseDatos, v_table)
            #value = 0
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            elif value == 3:
                messagebox.showinfo('', 'Nombre de Tabla No Existente')
            elif value == 4:
                messagebox.showinfo('', 'PK No Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Alter Drop PK","#FCFCFB", 500, 350)
    lblTabla = Label(window, text= 'Nombre de la Tabla', bg="#FCFCFB")
    lblTabla.place(x = 125, y = 75)
    txtTabla = Entry(window, width = 35)
    txtTabla.place(x = 100, y = 115)
    btnEliminar = Button(window, text='Eliminar', command = eliminar)
    btnEliminar.place(x = 345, y = 240)

def view_alterAddColumn():
    def modificar():
        v_table = txtTabla.get()
        v_default = txtDefault.get()
        if v_table and v_default:
            txtTabla.delete(0, END)
            txtDefault.delete(0, END)
            lista = v_default.split(",")
            value = 4
            if len(lista) == 1:
                value = CRUD_Tabla().alterAddColumn(nombre_BaseDatos, v_table, v_default)
            else:
                value = CRUD_Tabla().alterAddColumn(nombre_BaseDatos, v_table, lista)
            #value = 0
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            elif value == 3:
                messagebox.showinfo('', 'Nombre de Tabla No Existente')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Alter Add Column","#FCFCFB", 500, 350)
    lblTabla = Label(window, text= 'Nombre de la Tabla', bg="#FCFCFB")
    lblTabla.place(x = 125, y = 75)
    txtTabla = Entry(window, width = 35)
    txtTabla.place(x = 100, y = 115)
    lblDefault = Label(window, text= 'Default', bg="#FCFCFB")
    lblDefault.place(x = 125, y = 150)
    txtDefault = Entry(window, width = 35)
    txtDefault.place(x = 100, y = 190)
    btnModificar = Button(window, text='Modificar', command = modificar)
    btnModificar.place(x = 345, y = 240)

def view_alterDropColumn():
    def modificar():
        v_table = txtTabla.get()
        num_column = txtColumna.get()
        if v_table and num_column:
            txtTabla.delete(0, END)
            txtColumna.delete(0, END)
            value = CRUD_Tabla().alterDropColumn(nombre_BaseDatos, v_table,num_column)
            #value = 0
            if value == 0:
                messagebox.showinfo('', 'Operacion Exitosa')
                window.destroy()
            elif value == 2:
                messagebox.showinfo('', 'Base de Datos No Existente')
            elif value == 3:
                messagebox.showinfo('', 'Nombre de Tabla No Existente')
            elif value == 4:
                messagebox.showinfo('', 'Llave No Puede Eliminarse')
            elif value == 5:
                messagebox.showinfo('', 'Columna Fuera de Limites')
            else:
                messagebox.showinfo('', 'Error en la Operacion')

    window = Tk()
    edicionPantalla(window,  "Alter Drop Column","#FCFCFB", 500, 350)
    lblTabla = Label(window, text= 'Nombre de la Tabla', bg="#FCFCFB")
    lblTabla.place(x = 125, y = 75)
    txtTabla = Entry(window, width = 35)
    txtTabla.place(x = 100, y = 115)
    lblColumna = Label(window, text= 'Numero de Columna', bg="#FCFCFB")
    lblColumna.place(x = 125, y = 150)
    txtColumna = Entry(window, width = 35)
    txtColumna.place(x = 100, y = 190)
    btnModificar = Button(window, text='Modificar', command = modificar)
    btnModificar.place(x = 345, y = 240)

def mostrarTablas(nombre_BD, f_window):
    f_window.destroy() 
    window = Tk()
    ancho_ventana = 1000
    alto_ventana = 550
    edicionPantalla(window,"Tablas","white",  ancho_ventana, alto_ventana)

    var_width = 25
    separacion = 3
    var_height = int(var_width//5)
    var_font = tkFont.Font(size=12, weight="bold", family="Arial")

    encabezado = Label(window, text="", bg="white",width=25)
    encabezado.grid(padx=separacion, pady=separacion, row=0, column=0, columnspan=4)

    izquierda = Label(window, text="", bg="white",width=16)
    izquierda.grid(padx=separacion, pady=separacion, row=1, column=0, rowspan=5)

    ###############################################################################
    ###############################################################################

    btncreateTable = Button(window, text="CREATE TABLE", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_createTable)
    btncreateTable.grid(padx=separacion, pady=separacion, row=1, column=1)

    btnshowTable = Button(window, text="SHOW TABLES", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_showTable)
    btnshowTable.grid(padx=separacion, pady=separacion, row=1, column=2)    

    ###############################################################################
    ###############################################################################

    btndropTable = Button(window, text="DROP TABLE", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_dropTable)
    btndropTable.grid(padx=separacion, pady=separacion, row=2, column=1)

    btnExtractTable = Button(window, text="EXTRACT TABLE", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_extractTable)
    btnExtractTable.grid(padx=separacion, pady=separacion, row=2, column=2)
    
    btnalterTable = Button(window, text="ALTER TABLE", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command=view_alterTable)
    btnalterTable.grid(padx=separacion, pady=separacion, row=2, column=3)

    ###############################################################################
    ###############################################################################
    
    btnalterAddPk = Button(window, text="ALTER ADD PK", bg='#4484BC', fg='white', font=var_font, height= var_height, width=var_width, command=view_alterAddPk)
    btnalterAddPk.grid(padx=separacion, pady=separacion, row=3, column=1)

    btnAlterDropPk = Button(window, text="ALTER DROP PK", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command=view_alterDropPk)
    btnAlterDropPk.grid(padx=separacion, pady=separacion, row=3, column=2)

    btnExtractRangeTable = Button(window, text="EXTRACT RANGE TABLE", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command=view_extractRangeTable)
    btnExtractRangeTable.grid(padx=separacion, pady=separacion, row=3, column=3)

    ###############################################################################
    ###############################################################################

    btnAlterAddColumn = Button(window, text="ALTER ADD COLUMN", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command=view_alterAddColumn)
    btnAlterAddColumn.grid(padx=separacion, pady=separacion, row=4, column=3)

    btnAlterDropColumn = Button(window, text="ALTER DROP COLUMN", bg='#FCE433', fg='black', font=var_font, height= var_height, width=var_width, command=view_alterDropColumn)
    btnAlterDropColumn.grid(padx=separacion, pady=separacion, row=4, column=2)
    global nombre_BaseDatos
    nombre_BaseDatos = nombre_BD
    window.mainloop()
