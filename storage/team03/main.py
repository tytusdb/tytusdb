import tkinter as tk
import os
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from principalManager import BPlusMode as bp
bp.server.deserializar()

#---------------VENTANAS-------------------
#ventana1----------------------------------
def ventanaBD():

    def ventanaMostrarTabla():
        if my_listbox.get(ANCHOR)!= "":
            ventana5=Toplevel()
            ventana5.geometry("800x500")
            ventana5.title="GRAFICA DE BASES DE DATOS"


            cTableContainer = tk.Canvas(ventana5)
            fTable = tk.Frame(cTableContainer)
            sbHorizontalScrollBar = tk.Scrollbar(ventana5)
            sbVerticalScrollBar = tk.Scrollbar(ventana5)

            # Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
            def updateScrollRegion():
                cTableContainer.update_idletasks()
                cTableContainer.config(scrollregion=fTable.bbox())

            # Sets up the Canvas, Frame, and scrollbars for scrolling
            def createScrollableContainer():
                cTableContainer.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
                sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
                sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

                sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
                sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
                cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
                cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)

            # Adds labels diagonally across the screen to demonstrate the scrollbar adapting to the increasing size

            createScrollableContainer()
            print("Tabla seleccionada: "+ my_listbox.get(ANCHOR))
            bp.server.generarReporteTabla(my_listbox.get(ANCHOR))
            if os.path.isfile('Tablas.png')==True:
                imagen =PhotoImage(file="Tablas.png")
                fondo=Label(fTable, image=imagen, ).grid(column=0, row=1)
                updateScrollRegion()
            else:
                messagebox.showerror("Error", "No se encontro la imagen")
            my_listbox2.delete(0,tk.END)
            lista2=[]
            lista2=bp.showTables(my_listbox.get(ANCHOR))

 
            for item in lista2:
                my_listbox2.insert(END, item)
            ventana5.mainloop()
        else:
            messagebox.showerror("Error", "Seleccione primero una Base de Datos")
        

    def abrirImagenDB():
            #exist path ..
        if os.path.isfile('DB.png')==True:
            #open File
            os.system('DB.png')
        else:
            messagebox.showerror("Error", "No se encontro la imagen")
    
    def graficaBD():
        ventana4=Toplevel()
        ventana4.geometry("800x500")
        ventana4.title="GRAFICA DE BASES DE DATOS"


        cTableContainer = tk.Canvas(ventana4)
        fTable = tk.Frame(cTableContainer)
        sbHorizontalScrollBar = tk.Scrollbar(ventana4)
        sbVerticalScrollBar = tk.Scrollbar(ventana4)

        # Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
        def updateScrollRegion():
            cTableContainer.update_idletasks()
            cTableContainer.config(scrollregion=fTable.bbox())

        # Sets up the Canvas, Frame, and scrollbars for scrolling
        def createScrollableContainer():
            cTableContainer.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
            sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
            sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

            sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
            sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
            cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
            cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)

        # Adds labels diagonally across the screen to demonstrate the scrollbar adapting to the increasing size

        createScrollableContainer()


        imagen =PhotoImage(file="DB.png")
        fondo=Label(fTable, image=imagen, ).grid(column=0, row=1)
        updateScrollRegion()

        ventana4.mainloop()

    def ventanaGraficaTuplas():
        if my_listbox2.get(ANCHOR)!= "":
            ventanaGraficaTupla=Toplevel()
            ventanaGraficaTupla.geometry("800x500")
            ventanaGraficaTupla.title="GRAFICA DE BASES DE DATOS"

            bp.server.generarReporteBMasPlus(my_listbox.get(ANCHOR), my_listbox2.get(ANCHOR))




            cTableContainer = tk.Canvas(ventanaGraficaTupla)
            fTable = tk.Frame(cTableContainer)
            sbHorizontalScrollBar = tk.Scrollbar(ventanaGraficaTupla)
            sbVerticalScrollBar = tk.Scrollbar(ventanaGraficaTupla)

            # Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
            def updateScrollRegion():
                cTableContainer.update_idletasks()
                cTableContainer.config(scrollregion=fTable.bbox())

            # Sets up the Canvas, Frame, and scrollbars for scrolling
            def createScrollableContainer():
                cTableContainer.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
                sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
                sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

                sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
                sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
                cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
                cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)

            # Adds labels diagonally across the screen to demonstrate the scrollbar adapting to the increasing size

            createScrollableContainer()


            imagen =PhotoImage(file="salida.png")
            fondo=Label(fTable, image=imagen, ).grid(column=0, row=1)
            updateScrollRegion()



            ventanaGraficaTupla.mainloop()
        else:
            messagebox.showerror("Error", "Seleccione primero una Tabla")
  


    ventana2=Toplevel()
    ventana2.geometry("1000x225")
    ventana2.title="Gestor de Bases de Datos"


    boton2=Button(ventana2, text="GRAFICA BD, HERRAMIENTA EXTERNA", command=abrirImagenDB,bg="yellow", width = 62).place(x=50, y=70)
    boton4=Button(ventana2, text="GRAFICA BD TYTUS", command=graficaBD,bg="yellow", width = 62).place(x=50, y=100)
    
    # separador
    separador = ttk.Separator(ventana2, orient='vertical').place(x=550, relwidth=0.2, relheight=1)
    #Listbox para Bases de Datos
    my_listbox=Listbox(ventana2 )
    my_listbox.place(x=625, y =5)
    lista=[]
    lista=bp.server.generarReporteDB()

 
    for item in lista:
        my_listbox.insert(END, item)

    botonTablas=Button(ventana2, text="Mostrar grafica de tablas", command=ventanaMostrarTabla,bg="green", fg="white").place(x=625-10,  y=175)      

    #ListBox para mostrar Tablas
    my_listbox2=Listbox(ventana2 )
    my_listbox2.place(x=800, y =5)

        
    botonTablas=Button(ventana2, text="Mostrar grafica de Tuplas", command=ventanaGraficaTuplas,bg="green", fg="white").place(x=800-10,  y=175)      




#ventana2----------------------------------
def ventanaFuncionesBD():
    ventanaFun=Toplevel()
    ventanaFun.geometry("550x300")
    ventanaFun.title="Funciones de Base de datos"

            
    def createDatabase():

        if texto.get()=="":
            informacion.set("Debe colocarle un nombre a  la base de datos...")
            
        else:
            x=bp.createDatabase(str(texto.get()))
            if x==0:
                informacion.set("Base de datos creada correctamente")
            elif x==1:
                informacion.set("Ocurrio un error al crear la Base de datos")
            elif x==2:
                informacion.set("Base de Datos existente")
            bp.server.generarReporteDB()
            


            texto.set("")
    def showDatabase():
        ventanashowDatabase=Toplevel()
        ventanashowDatabase.geometry("400x600")
        ventanashowDatabase.title="BASES DE DATOS EXISTENTES"
        Label(ventanashowDatabase, text="LISTA DE BASES DE DATOS:", fg="blue").place(x=50,y=20)
        my_listbox=Listbox(ventanashowDatabase , width="50", height="30")
        my_listbox.place(x=50, y =50)
        lista=[]
        x=lista=bp.server.generarReporteDB()
        informacion.set("Lista de BD cargada exitosamente")
        for item in lista:
            my_listbox.insert(END, item) 

    def alterDatabase():
        x=bp.alterDatabase(textoOld.get(), textoNew.get())
        if x==0:
            informacion.set("Alter Database ejecutado correctamente")
        elif x==1:
            informacion.set("Error en la Operacion")
        elif x==2:
            informacion.set("DataBase Old no existe")
        elif x==3:
            informacion.set("DataBase new existente")

        textoOld.set("")
        textoNew.set("")
    
    def dropDatabase():
        x=bp.dropDatabase(textoEliminarBD.get())
        if x==0:
            informacion.set("Base de Datos eliminada correctamente...")
        elif x==1:
            informacion.set("Error al eliminar Base de Datos..")
        elif x==2:
            informacion.set("Base de datos no Existente")

        
        textoEliminarBD.set("")


        #label informacion
    informacion=StringVar()
    Label(ventanaFun, text="...", fg="red", textvariable=informacion).pack()

    
    #CREAR BASE DE DATOS-------------------------------------
    boton1=Button(ventanaFun, text="CREAR BD", command=createDatabase, bg="green" , fg="white", width="20").place(x=50, y=100)
    texto = StringVar()
    Label(ventanaFun, text="Nombre de BD").place(x=250, y=80)
    textoBD= Entry(ventanaFun, textvariable=texto, width="40" ).place(x=250, y=100 + 5)
    # separador
    separador1 = ttk.Separator(ventanaFun, orient='horizontal').place(y=135, relwidth=1.2, relheight=1)
    #MOSTRAR BASE DE DATOS-------------------------------------
    botonMostrarBD=Button(ventanaFun, text="MOSTRAR BD's", command=showDatabase, width="62", bg="yellow").place(x=50, y=150)
        # separador
    separador2 = ttk.Separator(ventanaFun, orient='horizontal').place(y=185, relwidth=1.2, relheight=1)
    #ALTER BASE DE DATOS-------------------------------------
    botonModificar=Button(ventanaFun, text="ALTER BD", command=alterDatabase,  bg="blue" , fg="white", width="20").place(x=50, y=200)
    
    textoOld = StringVar()
    Label(ventanaFun, text="Old:").place(x=250, y=200 -10)
    cajaOld= Entry(ventanaFun, textvariable=textoOld, width="20" ).place(x=220, y=200+10)

    textoNew = StringVar()
    Label(ventanaFun, text="New:").place(x=250 + 150, y=200 -10)
    cajaNew= Entry(ventanaFun, textvariable=textoNew, width="20" ).place(x=220+ 150, y=200+10)

            # separador
    separador2 = ttk.Separator(ventanaFun, orient='horizontal').place(y=240, relwidth=1.2, relheight=1)

        #ELIMINAR BASE DE DATOS-------------------------------------
    botonEliminarBD=Button(ventanaFun, text="ELIMINAR BD", command=dropDatabase , bg="red" , fg="white", width="20").place(x=50, y=260)
    textoEliminarBD = StringVar()
    Label(ventanaFun, text="Nombre de BD").place(x=250, y=245)
    textoBD= Entry(ventanaFun, textvariable=textoEliminarBD, width="40" ).place(x=250, y=260+5)




#ventana3----------------------------------
def ventanaTabla1():
    def createTable():

        if (textoNombreBD.get()=="") or (textoNombreTabla.get()=="") or (textoColumnas.get()==""):
            informacion.set("Completar todos los campos...")
            
        else:
            try:
                x=bp.createTable(textoNombreBD.get(),textoNombreTabla.get(), int(textoColumnas.get()))
                if x==0:
                    informacion.set("Tabla creada correctamente...")
                elif x==1:
                    informacion.set("Error en la Operacion...")
                elif x==2:
                    informacion.set("La base de datos no existe...")
                elif x==2:
                    informacion.set("La tabla existe...")
            except:
                informacion.set("Debe colocar un numero en las Columnas... ")
            
            

          
            textoNombreBD.set("")
            textoNombreTabla.set("")
            textoColumnas.set("")
    
    def showTables():

        if (    textoShowTables.get()==""):
            informacion.set( "Colocar el nombre de la base de datos..")
            
        else:
            try:
                x=bp.showTables(textoShowTables.get())
               
                if x==[]:
                    informacion.set("Base de datos sin tablas...")
                elif x==None:
                    informacion.set("No existe la base de datos...")
                else:
                    informacion.set("Lista de tablas cargada exitosamente")
                    def ventanaMostrarTablas():
                        ventanashowTable=Toplevel()
                        ventanashowTable.geometry("400x600")
                        ventanashowTable.title="LISTA DE TABLAS"
                        Label(ventanashowTable, text="LISTA DE TABLAS DE: " + textoShowTables.get(), fg="blue").place(x=50,y=20)
                        my_listbox2=Listbox(ventanashowTable , width="50", height="30")
                        my_listbox2.place(x=50, y =50)
                        lista=[]
                        x=lista=bp.showTables(textoShowTables.get())

                        for item in lista:
                            my_listbox2.insert(END, item) 
                    ventanaMostrarTablas()
                    textoShowTables.set("")
            except:
                informacion.set("Error desconocido ")
            
            

          
            textoNombreBD.set("")
            textoNombreTabla.set("")
            textoColumnas.set("")

    def extractTable():
        if textoNombreExtract.get()!="" and textoNombreTablaExtract.get()!="":
            x=bp.extractTable(textoNombreExtract.get(), textoNombreTablaExtract.get())
        
            print(x)
            if x==[]:
                informacion.set("Tabla Vacia...")
            elif x==None:
                informacion.set("Ha ocurrido un error, verificar BD y tabla")
            else:
                informacion.set("")
                ventanaExtract=Toplevel()
                ventanaExtract.geometry("800x300")
                ventanaExtract.title="EXTRACT TABLE"

                #Frame para acoplarlo con el dataGrid
                miFrame3=Frame(ventanaExtract)
                miFrame3.pack()
                miFrame3.config(width="300", height="200")

                Label(miFrame3, text="BD: " + textoNombreExtract.get() + " TABLA: " + textoNombreTablaExtract.get(), fg="blue").pack()
                #Lista de Listas
                arreglo=x
                #Averiguando cuantas columnas tiene la primera Lista(el resto tiene las mismas)
                listaCol=[]
                for x in range(0, len(arreglo[0]), 1):
                    listaCol += [x+1]

                #creando el DataGrid y agregandolo al Frame
                datagrid=ttk.Treeview(miFrame3, columns=(listaCol), show="headings")
                datagrid.pack()

                #Scrollbar horizontal y agregandolo a la ventana
                scrollbar_horizontal = ttk.Scrollbar(ventanaExtract, orient='horizontal', command = datagrid.xview)
                scrollbar_horizontal.pack(side='bottom', fill=X)
                datagrid.configure(xscrollcommand=scrollbar_horizontal.set)
                
                #Agregando las cabeceras
                for i in listaCol:
                    datagrid.heading(i, text="Columna"+ str(i))

                #insertando todos los registros de la lista de listas
                for x in arreglo:
                    datagrid.insert('', 'end', values=x)
        else:
            informacion.set("Debe llenar los datos de BD y Tabla")
                            

    def extractRangeTable():
        if (textoNombreExtractRange.get()!="" and textoNombreTablaExtractRange.get()!="" and textoNoColumna.get()!=""
        and textoRangeLower.get()!="" and textoRangeUpper.get()!=""):
            try:
                int(textoNoColumna.get())
                int(textoRangeLower.get())
                int(textoRangeUpper.get())
                informacion.set("")
                salida=bp.extractRangeTable(textoNombreExtractRange.get(), textoNombreTablaExtractRange.get(), int(textoNoColumna.get()), int(textoRangeLower.get()), int(textoRangeUpper.get()))
                if salida==[]:
                    informacion.set("BD y Tabla existe pero sin registros...")
                elif salida==None:
                    informacion.set("Ha ocurrido un error. Sino la BD o Tabla no existen")
                else:
                    ventanaExtractRange=Toplevel()
                    ventanaExtractRange.geometry("400x300")
                    ventanaExtractRange.title="EXTRACT RANGE TABLE"

                    #Frame para acoplarlo con el dataGrid
                    miFrame3=Frame(ventanaExtractRange)
                    miFrame3.pack()
                    miFrame3.config(width="300", height="200")

                    Label(miFrame3, text="BD:" + textoNombreExtractRange.get() +" TABLA: " + textoNombreTablaExtractRange.get(), fg="blue").pack()
                    #Lista de Listas
                    arreglo=salida
                    #Averiguando cuantas columnas tiene la primera Lista(el resto tiene las mismas)
            

                    #creando el DataGrid y agregandolo al Frame
                    datagrid=ttk.Treeview(miFrame3, columns=(1), show="headings")
                    datagrid.pack()

                    #Agregando las cabeceras
                    datagrid.heading(1, text="Extract Range Table")

                    #insertando todos los registros de la lista de listas
                    for x in arreglo:
                        datagrid.insert('', 'end', values=x)

            except:
                informacion.set("Debe ingresar numeros en Columna, Lower y Upper")
        else:
            informacion.set("Debe llenar BD, Tabla, Columna, Lower y Upper")
                            
    def alterTable():
        if textoAlterTable.get()!="" and textoOldTable.get()!="" and textoNewTable.get()!="":
            salida=bp.alterTable(textoAlterTable.get(),textoOldTable.get(), textoNewTable.get())
            if salida==0:
                informacion.set("Cambio de nombre a la Tabla exitoso...")
                textoAlterTable.set("")
                textoOldTable.set("")
                textoNewTable.set("")
            elif salida==1:
                informacion.set("Error al intentar cambiar de nombre a la Tabla")
            elif salida==2:
                informacion.set("La Base de Datos no Existe")
            elif salida==3:
                informacion.set("La Tabla no existe")
            elif salida==4:
                informacion.set("La Tabla nueva ya existe, cambiar de nombre")
        else:
            informacion.set("No deje campos vacios, BD, tabla vieja, tabla nueva...")

    def alterAddColumn():
        if (textoNombreBDAlterAddColumn.get()!="" and textoTablaAlterAddColumn.get()!="" and textoDefectoAlterAddColumn.get()!=""):
            None 
            informacion.set("")
            salidaAlter=bp.alterAddColumn(textoNombreBDAlterAddColumn.get(), textoTablaAlterAddColumn.get(), textoDefectoAlterAddColumn.get())
            if salidaAlter==0:
                informacion.set("Columna agregada correctamente")
                textoNombreBDAlterAddColumn.set("")
                textoTablaAlterAddColumn.set("")
                textoDefectoAlterAddColumn.set("")
            elif salidaAlter==1:
                informacion.set("Error al agregar la columna")
            elif salidaAlter==2:
                informacion.set("La base de datos No existe")
            elif salidaAlter==3:
                informacion.set("La Tabla no existe")
        else:
            informacion.set("No deje campos vacios. BD, Tabla o Valor por Defecto")


    ventanaTab=Toplevel()
    ventanaTab.geometry("1100x500")
    ventanaTab.title="Funciones de Tablas"

    #label informacion
    informacion=StringVar()
    Label(ventanaTab, text="...", fg="red", textvariable=informacion).pack()

    #CREAR TABLA-------------------------------------
    boton1=Button(ventanaTab, text="CREATE TABLE", bg="#5D6D7E", fg="white",command=createTable, width="20").place(x=10, y=100)
        
        #textbox nombre BD existente
    textoNombreBD = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=85)
    cajaNombreBD= Entry(ventanaTab, textvariable=textoNombreBD, width="35" ).place(x=250, y=5 + 100)

            #textbox nombre nueva Tabla
    textoNombreTabla = StringVar()
    Label(ventanaTab, text="Nombre NUEVA tabla: ").place(x=500, y=85)
    cajaNombreTabla= Entry(ventanaTab, textvariable=textoNombreTabla, width="35" ).place(x=500, y=5 + 100)

                #textbox numeroColumnas
    textoColumnas = StringVar()
    Label(ventanaTab, text="Numero de Columnas: ").place(x=750, y=85)
    cajaNombreColumnas= Entry(ventanaTab, textvariable=textoColumnas, width="35" ).place(x=750, y=5 + 100)

        # _________________________________________separador ________________________________________________________
    separador1 = ttk.Separator(ventanaTab, orient='horizontal').place(y=140, relwidth=1.2, relheight=1)

    #SHOW TABLES-------------------------------------
    botonShowTables=Button(ventanaTab, text="SHOW TABLES", bg="#34495E", fg="white",command=showTables, width="20").place(x=10, y=160)
        
        #textbox NOMBRE BASES
    textoShowTables = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=160-15)
    cajaShowTables= Entry(ventanaTab, textvariable=textoShowTables, width="35" ).place(x=250, y=5 + 160)

            # _________________________________________separador ________________________________________________________
    separador2 = ttk.Separator(ventanaTab, orient='horizontal').place(y=200, relwidth=1.2, relheight=1)
    botonExtractTable=Button(ventanaTab, text="EXTRACT TABLE", command=extractTable,bg="#2E4053", fg="white", width="20").place(x=10, y=220)
    

    textoNombreExtract = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=210)
    cajaNombreExtract= Entry(ventanaTab, textvariable=textoNombreExtract, width="35" ).place(x=250, y= 230)

            #textbox nombre nueva Tabla
    textoNombreTablaExtract = StringVar()
    Label(ventanaTab, text="Nombre de Tabla: ").place(x=500, y=210)
    cajaNombreTablaExtract= Entry(ventanaTab, textvariable=textoNombreTablaExtract, width="35" ).place(x=500, y=230)

        # _________________________________________separador ________________________________________________________
    separador7 = ttk.Separator(ventanaTab, orient='horizontal').place(y=260, relwidth=1.2, relheight=1)
            #EXTRACT RANGE TABLE
    botonExtracRangetTable=Button(ventanaTab, text="EXTRACT RANGE TABLE", command=extractRangeTable,bg="#283747", fg="white", width="20").place(x=10, y=280)
    
    textoNombreExtractRange = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=270)
    cajaNombreExtractRange= Entry(ventanaTab, textvariable=textoNombreExtractRange, width="35" ).place(x=250, y= 290)


    textoNombreTablaExtractRange = StringVar()
    Label(ventanaTab, text="Nombre de Tabla: ").place(x=500, y=270)
    cajaNombreTablaExtractRange= Entry(ventanaTab, textvariable=textoNombreTablaExtractRange, width="35" ).place(x=500, y=290)

    textoNoColumna = StringVar()
    Label(ventanaTab, text="# Columna: ").place(x=750, y=270)
    cajaNoColumna= Entry(ventanaTab, textvariable=textoNoColumna, width="15" ).place(x=750, y=290)

    textoRangeLower = StringVar()
    Label(ventanaTab, text="Lower: ").place(x=850, y=270)
    cajaRangeLower= Entry(ventanaTab, textvariable=textoRangeLower, width="15" ).place(x=850, y=290)

    textoRangeUpper = StringVar()
    Label(ventanaTab, text="Upper: ").place(x=950, y=270)
    cajaRangeUpper= Entry(ventanaTab, textvariable=textoRangeUpper, width="15" ).place(x=950, y=290)

        # _________________________________________separador ________________________________________________________
    separador8 = ttk.Separator(ventanaTab, orient='horizontal').place(y=330, relwidth=1.2, relheight=1)


    botonAlterTable=Button(ventanaTab, text="ALTER TABLE", command=alterTable,bg="#212F3C", fg="white", width="20").place(x=10, y=360)
    
    textoAlterTable = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=360-20)
    cajaNombreBDAlterTable= Entry(ventanaTab, textvariable=textoAlterTable, width="35" ).place(x=250, y= 360)

    
    textoOldTable = StringVar()
    Label(ventanaTab, text="Tabla Vieja: ").place(x=500, y=360-20)
    cajaOldTable= Entry(ventanaTab, textvariable=textoOldTable, width="35" ).place(x=500, y=360)

    textoNewTable = StringVar()
    Label(ventanaTab, text="Tabla Nueva: ").place(x=750, y=360-20)
    cajaNewTable= Entry(ventanaTab, textvariable=textoNewTable, width="35" ).place(x=750, y=360)

            # _________________________________________separador ________________________________________________________
    separador9 = ttk.Separator(ventanaTab, orient='horizontal').place(y=410, relwidth=1.2, relheight=1)

    botonalterAddColumn=Button(ventanaTab, text="ALTER ADD COLUMN", command=alterAddColumn, bg="#1B2631", fg="white",width="20").place(x=10, y=440)
    
    textoNombreBDAlterAddColumn = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=440-20)
    cajaNombreBDAlterAddColumn= Entry(ventanaTab, textvariable=textoNombreBDAlterAddColumn, width="35" ).place(x=250, y= 440)

    
    textoTablaAlterAddColumn = StringVar()
    Label(ventanaTab, text="Tabla: ").place(x=500, y=440-20)
    cajaTablaAlterAddColumn= Entry(ventanaTab, textvariable=textoTablaAlterAddColumn, width="35" ).place(x=500, y=440)

    textoDefectoAlterAddColumn = StringVar()
    Label(ventanaTab, text="Valor por Defecto: ").place(x=750, y=440-20)
    cajaDefectoAlterAddColumn= Entry(ventanaTab, textvariable=textoDefectoAlterAddColumn, width="35" ).place(x=750, y=440)




#ventana4----------------------------------

def ventanaTabla2():
    def AlterDropColumn():
        if (textoNombreBDAlterDropColumn.get()!="" and textoNombreTablaAlterDropColumn.get()!="" and textoColumnaAlterDropColumn.get()!=""):
            try:
                int(textoColumnaAlterDropColumn.get())
                salida=bp.alterDropColumn(textoNombreBDAlterDropColumn.get(), textoNombreTablaAlterDropColumn.get(), int(textoColumnaAlterDropColumn.get()))

                if salida==0:
                    informacion.set("Columna Eliminada correctamente")
                elif salida==1:
                    informacion.set("Error al Eliminar columna")
                elif salida==2:
                    informacion.set("La base de datos no existe")
                elif salida==3:
                    informacion.set("La tabla no existe")
                elif salida==4:
                    informacion.set("Columna fuera de los limites")
                
            except:
                informacion.set("Debe ingresar un numero en Columna")
        else:
            informacion.set("No dejar campos vacios. Nombre Bd, Tabla, columna a eliminar")
    def dropTable():
        if textoNombreBDDropTable.get()!="" and textoNombreTablaDropTable.get()!="":
            salida=bp.dropTable(textoNombreBDDropTable.get(), textoNombreTablaDropTable.get())
            
            if salida==0:
                informacion.set("Tabla eliminada correctamente...")
                textoNombreBDDropTable.set("")
                textoNombreTablaDropTable.set("")
            elif salida==1:
                informacion.set("Error en la eliminacion de la tabla...")
            elif salida==2:
                informacion.set("La base de datos no existe...")
            elif salida==3:
                informacion.set("La tabla no existe...")
        else:
            informacion.set("No deje campos vacios en BD y Tabla")
    
    def ejecutarAlterDropPK():
        if textoNombreAlterDropPK.get()!="" and textoNombreTablaAlterDropPK.get()!="":
            informacion.set("")
            print(textoNombreAlterDropPK.get())
            print(textoNombreTablaAlterDropPK.get())
            salidaAlterDropPK=bp.alterDropPK(textoNombreAlterDropPK.get(),textoNombreTablaAlterDropPK.get())
            print(salidaAlterDropPK)
            if salidaAlterDropPK==0:
                informacion.set("AlterDropPK ejecutado correctamente")
                textoNombreAlterDropPK.set("")
                textoNombreTablaAlterDropPK.set("")
            elif salidaAlterDropPK==1:
                informacion.set("Error al ejecutar el AlterDropPK")
            elif salidaAlterDropPK==2:
                informacion.set("La Base de Datos NO existe")
            elif salidaAlterDropPK==3:
                informacion.set("La Tabla NO existe")
            elif salidaAlterDropPK==4:
                informacion.set("PK no existente")
            elif salidaAlterDropPK==None:
                informacion.set("None")
        else:
            informacion.set("Llenar los campos BD y Tabla")
    
    def alterAddPK():
        ventanaAlterAddPK=Toplevel()
        ventanaAlterAddPK.geometry("425x450")
        ventanaAlterAddPK.title="ALTER ADD PK"
        def eliminarElemento():
            my_listbox.delete(ANCHOR)

        def agregarColumna():

            if textoBaseDatos.get()!="" and textoTabla.get()!="":
                listaColumna=[]
                for cont in range (0,my_listbox.size(),1):  
                    listaColumna+=[int(my_listbox.get(cont))]

                x=bp.alterAddPK(textoBaseDatos.get(),textoTabla.get(), listaColumna)
                print(textoBaseDatos.get())
                print(textoTabla.get())
                print(listaColumna)
                if x==0:
                    textoInfo.set("AlterAddPK realizado correctamente")
                    my_listbox.delete(0,tk.END)
                elif x==1:
                    textoInfo.set("Error al realizar el AlterAddPK")
                elif x==2:
                    textoInfo.set("La Base de datos no Existe")
                elif x==3:
                    textoInfo.set("La Tabla no existe")
                elif x==4:
                    textoInfo.set("Llave primaria existente")
                elif x==5:
                    textoInfo.set("Columnas fuera de los limites")
            else:
                textoInfo.set("Debe colocar una BD y una tabla")


        def agregarListBox():
            if textoItem.get()!="":
                try:
                    int(textoItem.get())
                    my_listbox.insert(END, textoItem.get())
                    textoItem.set("")
                except:
                    textoInfo.set("DEBE INGRESAR UN NUMERO ENTERO EN COLUMNA...")
            else:
                None

        textoBaseDatos = StringVar()
        Label(ventanaAlterAddPK, text="Nombre de BD").place(x=10, y=10)
        cajaBasedatos= Entry(ventanaAlterAddPK, textvariable=textoBaseDatos, width="30" ).place(x=10, y=30)

        textoTabla = StringVar()
        Label(ventanaAlterAddPK, text="Nombre de TABLA").place(x=215, y=10)
        cajaBasedatos= Entry(ventanaAlterAddPK, textvariable=textoTabla, width="30" ).place(x=215, y=30)

        botonAgregarLista=Button(ventanaAlterAddPK, text="AGREGAR A LA LISTA", command=agregarListBox, bg="green", fg="white", width="55").place(x=10,  y=50+40)
        botonEliminarElemento=Button(ventanaAlterAddPK, text="ELIMINAR ELEMENTO", command=eliminarElemento, bg="red", fg="white", width="55").place(x=10, y=280+40)
        botonAgregarTupla=Button(ventanaAlterAddPK, text="ALTER ADD PK", command=agregarColumna, bg="yellow", width="55").place(x=10, y=305+40) 

        textoItem = StringVar()
        Label(ventanaAlterAddPK, text="Columna: ").place(x=10,y=10+55)
        cajaItem= Entry(ventanaAlterAddPK, textvariable=textoItem, width="54" ).place(x=70, y=10+55)


        my_listbox=Listbox(ventanaAlterAddPK, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaAlterAddPK, fg="blue", textvariable=textoInfo).place(x=10,y=400)
        textoInfo.set("FUNCION AlterAddPK")


    ventanaTab2=Toplevel()
    ventanaTab2.geometry("1000x350")
    ventanaTab2.title="Funciones de Tablas"

    #label informacion
    informacion=StringVar()
    Label(ventanaTab2, text="...", fg="red", textvariable=informacion).pack()

    #Boton -------------------------------------
    botonAlterDropColumn=Button(ventanaTab2, text="ALTER DROP COLUMN", command=AlterDropColumn, bg="#1B4F72", fg="white",width="20").place(x=10, y=100)
        
        #textbox nombre BD existente
    textoNombreBDAlterDropColumn = StringVar()
    Label(ventanaTab2, text="Nombre BD: ").place(x=250, y=85)
    cajaNombreBDAlterDropColumn= Entry(ventanaTab2, textvariable=textoNombreBDAlterDropColumn, width="35" ).place(x=250, y=5 + 100)

            #textbox nombre Tabla
    textoNombreTablaAlterDropColumn = StringVar()
    Label(ventanaTab2, text="Nombre Tabla: ").place(x=500, y=85)
    cajaNombreTablaAlterDropColumn= Entry(ventanaTab2, textvariable=textoNombreTablaAlterDropColumn, width="35" ).place(x=500, y=5 + 100)

                #textbox Columna para eliminar
    textoColumnaAlterDropColumn = StringVar()
    Label(ventanaTab2, text="Columna a Eliminar: ").place(x=750, y=85)
    cajaNombreColumnaAlterDropColumns= Entry(ventanaTab2, textvariable=textoColumnaAlterDropColumn, width="35" ).place(x=750, y=5 + 100)
    
        # _________________________________________separador ________________________________________________________
    separador1 = ttk.Separator(ventanaTab2, orient='horizontal').place(y=140, relwidth=1.2, relheight=1)

    #SHOW TABLES-------------------------------------
    botonDropTable=Button(ventanaTab2, text="DROP TABLE", command=dropTable, bg="#2874A6", fg="white",width="20").place(x=10, y=160)
        
        #textbox NOMBRE BASE DATOS
    textoNombreBDDropTable = StringVar()
    Label(ventanaTab2, text="Nombre BD: ").place(x=250, y=160-15)
    cajaBDDropTable= Entry(ventanaTab2, textvariable=textoNombreBDDropTable, width="35" ).place(x=250, y=5 + 160)

            #textbox NOMBRE TABLA A ELIMINAR
    textoNombreTablaDropTable = StringVar()
    Label(ventanaTab2, text="Tabla a Eliminar: ").place(x=500, y=160-15)
    cajaTablaDropTable= Entry(ventanaTab2, textvariable=textoNombreTablaDropTable, width="35" ).place(x=500, y=5 + 160)

            # _________________________________________separador ________________________________________________________
    separador2 = ttk.Separator(ventanaTab2, orient='horizontal').place(y=200, relwidth=1.2, relheight=1)
    botonExtractTable=Button(ventanaTab2, text="ALTER ADD PK", bg="#2E86C1", fg="white", command=alterAddPK, width="20").place(x=10, y=220)
    

    

        # _________________________________________separador ________________________________________________________
    

    separador7 = ttk.Separator(ventanaTab2, orient='horizontal').place(y=260, relwidth=1.2, relheight=1)
    
            #EXTRACT RANGE TABLE
    botonNombreAlterDropPK=Button(ventanaTab2, text="ALTER DROP PK", command=ejecutarAlterDropPK, bg="#5DADE2", fg="white", width="20").place(x=10, y=280)
    
    textoNombreAlterDropPK = StringVar()
    Label(ventanaTab2, text="Nombre BD: ").place(x=250, y=270)
    cajaNombreAlterDropPK= Entry(ventanaTab2, textvariable=textoNombreAlterDropPK, width="35" ).place(x=250, y= 290)


    textoNombreTablaAlterDropPK = StringVar()
    Label(ventanaTab2, text="Nombre de Tabla: ").place(x=500, y=270)
    cajaNombreTablaAlterDropPK= Entry(ventanaTab2, textvariable=textoNombreTablaAlterDropPK, width="35" ).place(x=500, y=290)
    
