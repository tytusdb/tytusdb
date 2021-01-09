import tkinter as tk
import os
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from storageManager import unified_mode as bp
#bp.deserializar()

#---------------VENTANAS-------------------
#ventana1----------------------------------
def ventanaBD():

    def ventanaMostrarTabla():
        if my_listbox.get(ANCHOR)!= "":
            my_listbox2.delete(0,tk.END)
            lista2=[]
            lista2=bp.showTables(my_listbox.get(ANCHOR))

 
            for item in lista2:
                my_listbox2.insert(END, item)
         
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
    lista=bp.showDatabases()

 
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
    ventanaFun.geometry("1000x300")
    ventanaFun.title="Funciones de Base de datos"

            
    def createDatabase():

        if texto.get()=="" or textoModo.get()=="":
            informacion.set("Llenar todos los campos de la base de datos...")
            
        else:
            salidaModo=textoModo.get()
            if textoEncoding.get()=="":
                x=bp.createDatabase(str(texto.get()), salidaModo.lower() )
                if x==0:
                    informacion.set("BD creada, Encoding por defecto...")        
                elif x==1:
                    informacion.set("Ocurrio un error al crear la Base de datos")
                elif x==2:
                    informacion.set("Base de Datos existente")
            else:
                salidaEncoding=textoEncoding.get()
                x=bp.createDatabase(str(texto.get()), salidaModo.lower(), salidaEncoding.lower())
                if x==0:
                    informacion.set("BD creada correctamente")        
                elif x==1:
                    informacion.set("Ocurrio un error al crear la Base de datos")
                elif x==2:
                    informacion.set("Base de Datos existente")


            texto.set("")
            textoModo.set("")
            textoEncoding.set("")
    def showDatabase():
        ventanashowDatabase=Toplevel()
        ventanashowDatabase.geometry("400x600")
        ventanashowDatabase.title="BASES DE DATOS EXISTENTES"
        Label(ventanashowDatabase, text="LISTA DE BASES DE DATOS:", fg="blue").place(x=50,y=20)
        my_listbox=Listbox(ventanashowDatabase , width="50", height="30")
        my_listbox.place(x=50, y =50)
        lista=[]
        x=lista=bp.showDatabases()
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
    boton1=Button(ventanaFun, text="CREAR BD:", command=createDatabase, bg="green" , fg="white", width="20").place(x=50, y=100)
    texto = StringVar()
    Label(ventanaFun, text="Nombre de BD").place(x=250, y=80)
    CajaTextoBD= Entry(ventanaFun, textvariable=texto, width="40" ).place(x=250, y=100 + 5)

    textoModo = StringVar()
    Label(ventanaFun, text="Modo:").place(x=500, y=80)
    CajaTextoModo= Entry(ventanaFun, textvariable=textoModo, width="30" ).place(x=500, y=100 + 5)

    textoEncoding = StringVar()
    Label(ventanaFun, text="Encoding:").place(x=700, y=80)
    CajaTextoEncoding= Entry(ventanaFun, textvariable=textoEncoding, width="30" ).place(x=700, y=100 + 5)
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
                x=bp.createTable(textoNombreBD.get(), textoNombreTabla.get(), int(textoColumnas.get()))
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
    

    
#ventana5----------------------------------
def ventanaTupla():
    ventanaTup=Toplevel()
    ventanaTup.geometry("900x500")
    ventanaTup.title="Funciones de Tuplas"
    informacion=StringVar()
    Label(ventanaTup, text="...", fg="red", textvariable=informacion).pack()
    def modificarURL(url):
        i=0
        nuevaCadena=""
        for i in range (0, len(url),1):
            if url[i]=="/":
                nuevaCadena+="\\"
            else:
                nuevaCadena+=url[i]
       
        return nuevaCadena

    def urlCSV():

        if textoBDSCV.get()!="" and textoTablaSCV.get()!="":
            f = open (filedialog.askopenfilename(title="Seleccione el archivo", filetypes=(("Archivos CSV", "*.csv"),("Todos", "*.*"))),'r', encoding="utf8", errors='ignore')
            print(modificarURL(f.name))
            informacion.set("")
            salida=bp.loadCSV(modificarURL(f.name), textoBDSCV.get(),textoTablaSCV.get())
            if salida==[]:
                informacion.set("Ocurrio un error o Lista Vacia")
            else:
                informacion.set("CSV cargado correctamente")

        else:
            informacion.set("Colocar BD y tabla antes de cargar el CSV")
            
    def insertTupla():
        ventanaTup=Toplevel()
        ventanaTup.geometry("425x600")
        ventanaTup.title="INSERTAR TUPLA"
        def eliminarElemento():
            my_listbox.delete(ANCHOR)

        def agregarTupla():

            if textoBaseDatos.get()!="" and textoTabla.get()!="":
                listaTupla=[]
                for cont in range (0,my_listbox.size(),1):
                    listaTupla+=[my_listbox.get(cont)]
                x=bp.insert(textoBaseDatos.get(),textoTabla.get(), listaTupla)
                if x==0:
                    textoInfo.set("Tupla agregada correctamente")

                    my_listbox.delete(0,tk.END)
                elif x==1:
                    textoInfo.set("Error al agregar Tupla")
                elif x==2:
                    textoInfo.set("La Base de datos no Existe")
                elif x==3:
                    textoInfo.set("La Tabla no existe")
                elif x==4:
                    textoInfo.set("Llave primaria Duplicada")
                elif x==5:
                    textoInfo.set("Columnas fuera de los limites")
            else:
                textoInfo.set("Debe colocar una BD y una tabla")


        def agregarListBox():
            if textoItem.get()!="":
                my_listbox.insert(END, textoItem.get())
                textoItem.set("")
            else:
                None

        textoBaseDatos = StringVar()
        Label(ventanaTup, text="Nombre de BD").place(x=10, y=10)
        cajaBasedatos= Entry(ventanaTup, textvariable=textoBaseDatos, width="30" ).place(x=10, y=30)

        textoTabla = StringVar()
        Label(ventanaTup, text="Nombre de TABLA").place(x=215, y=10)
        cajaBasedatos= Entry(ventanaTup, textvariable=textoTabla, width="30" ).place(x=215, y=30)

        botonAgregarLista=Button(ventanaTup, text="AGREGAR A LA LISTA", command=agregarListBox, bg="green", fg="white", width="55").place(x=10,  y=50+40)
        botonEliminarElemento=Button(ventanaTup, text="ELIMINAR ELEMENTO", command=eliminarElemento, bg="red", fg="white", width="55").place(x=10, y=280+40)
        botonAgregarTupla=Button(ventanaTup, text="AGREGAR TUPLA", command=agregarTupla, bg="yellow", width="55").place(x=10, y=305+40) 

        textoItem = StringVar()
        Label(ventanaTup, text="ITEM: ").place(x=10,y=10+55)
        cajaItem= Entry(ventanaTup, textvariable=textoItem, width="58" ).place(x=50, y=10+55)


        my_listbox=Listbox(ventanaTup, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaTup, fg="blue", textvariable=textoInfo).place(x=10,y=400)
        
    def extractRow():
        ventanaExtractRow=Toplevel()
        ventanaExtractRow.geometry("600x600")
        ventanaExtractRow.title="EXTRACT ROW"
        def eliminarElemento():
            my_listbox.delete(ANCHOR)

        def agregarListBox():
            if textoItem.get()!="":
                my_listbox.insert(END, textoItem.get())
                textoItem.set("")
            else:
                None

        def ejecutarExtractRow():

            if textoBaseDatosExtractRow.get()!="" and textoTablaExtractRow.get()!="":
                listaKey=[]
                for cont in range (0,my_listbox.size(),1):
                    listaKey+=[my_listbox.get(cont)]
                
                salidaExtractRow=bp.extractRow(textoBaseDatosExtractRow.get(),textoTablaExtractRow.get(), listaKey)
                print(textoBaseDatosExtractRow.get())
                print(textoTablaExtractRow.get())
                print(listaKey)
                
                print (salidaExtractRow)
                if salidaExtractRow==[]:
                    textoInfo.set("Ocurrio un Error o no hay registros que mostrar...")

                else:
                    my_listbox.delete(0,tk.END)
                    textoInfo.set("Extract Row ejecutado correctamente")
                    informacion.set("")
                    ventanaExtract=Toplevel()
                    ventanaExtract.geometry("800x300")
                    ventanaExtract.title="EXTRACT TABLE"

                    #Frame para acoplarlo con el dataGrid
                    miFrame3=Frame(ventanaExtract)
                    miFrame3.pack()
                    miFrame3.config(width="300", height="200")

                    Label(miFrame3, text="BD: " + textoBaseDatosExtractRow.get() + " TABLA: " + textoTablaExtractRow.get(), fg="blue").pack()
                    #Lista de Listas
                    arreglo=salidaExtractRow
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
                textoInfo.set("Debe colocar una BD y una tabla")

        textoBaseDatosExtractRow = StringVar()
        Label(ventanaExtractRow, text="Nombre de BD").place(x=10, y=10)
        cajaBasedatos= Entry(ventanaExtractRow, textvariable=textoBaseDatosExtractRow, width="30" ).place(x=10, y=30)

        textoTablaExtractRow = StringVar()
        Label(ventanaExtractRow, text="Nombre de TABLA").place(x=215, y=10)
        cajaBasedatosExtractRow= Entry(ventanaExtractRow, textvariable=textoTablaExtractRow, width="30" ).place(x=215, y=30)

        botonAgregarLlave=Button(ventanaExtractRow, text="AGREGAR LLAVE", command=agregarListBox, bg="green", fg="white", width="55").place(x=10,  y=50+40)
        botonEliminarLlave=Button(ventanaExtractRow, text="ELIMINAR LLAVE", command=eliminarElemento, bg="red", fg="white", width="55").place(x=10, y=280+40)
        botonAgregarKey=Button(ventanaExtractRow, text="ExtractRow", command=ejecutarExtractRow, bg="yellow", width="55").place(x=10, y=305+40) 

        textoItem = StringVar()
        Label(ventanaExtractRow, text="Llave: ").place(x=10,y=10+55)
        cajaItem= Entry(ventanaExtractRow, textvariable=textoItem, width="58" ).place(x=50, y=10+55)


        my_listbox=Listbox(ventanaExtractRow, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaExtractRow, fg="blue", textvariable=textoInfo).place(x=10,y=400)
    
    def update():
        ventanaUpdate=Toplevel()
        ventanaUpdate.geometry("875x450")
        ventanaUpdate.title="UPDATE"

        #variables mas globales
        diccionario={}
        lista=[]

        def eliminarDiccionario():
            my_listbox.delete(0,tk.END)
            diccionario.clear()
            print(diccionario)

        def eliminarColumna():
            my_listbox2.delete(ANCHOR)
            lista.clear()
            for cont in range (0,my_listbox2.size(),1):
                lista.append(my_listbox2.get(cont))
            print(lista)    
            
        def agregarAlDiccionario():
            if textoClave.get()!="" and textoValor.get()!="":
                try:
                    
                    my_listbox.delete(0,tk.END)
                    numero=int(textoClave.get())
                    dicAux={numero:textoValor.get()}
                    diccionario.update(dicAux)
                    #
                    for clave, valor in diccionario.items():
                        my_listbox.insert(END, str(clave) +":"+ valor)

                    print(diccionario)
                    textoInfo.set("")
                    textoClave.set("")
                    textoValor.set("")
                except:
                    textoInfo.set("Debe ingresar un numero en la CLAVE!")

            else:
                textoInfo.set("Debe ingresar una clave y valor primero")

        def agregarListBox():
            if textoColumna.get()!="":
                my_listbox2.insert(END, textoColumna.get())
                textoColumna.set("")
                lista.clear()
                for cont in range (0,my_listbox2.size(),1):
                    lista.append(my_listbox2.get(cont))
                print(lista)    
            else:
                None

        def ejecutarUpdate():
            if textoBaseDatos.get()!="" and textoTabla.get()!="":
                if diccionario!={}:
                    if lista!=[]:
                        print(textoBaseDatos.get())
                        print(textoTabla.get())
                        print(diccionario)
                        print(lista)
                        salidaUpdate=bp.update(textoBaseDatos.get(),textoTabla.get(), diccionario, lista)
                        if salidaUpdate==0:
                            textoInfo.set("Update ejecutado correctamente")
                            my_listbox2.delete(0,tk.END)
                            lista.clear()
                            eliminarDiccionario()
                        elif salidaUpdate==1:
                            textoInfo.set("Error al realizar el Update")
                        elif salidaUpdate==2:
                            textoInfo.set("La Base de datos NO existe")
                        elif salidaUpdate==3:
                            textoInfo.set("La Tabla NO existe")
                        elif salidaUpdate==4:
                            textoInfo.set("La llave primaria no existe")
                        print(salidaUpdate)
                    else:
                        textoInfo.set("Lista vacia, colocar valores")
                        print(lista)
                        print(diccionario)
                else:
                    textoInfo.set("Diccionario vacio, colocar valores")
            else:
                textoInfo.set("No dejar vacio el Campo de BD y Tabla")
        #COLUMNA 1-----------------------------------------------------------------------------------------------------------------

        textoBaseDatos = StringVar()
        Label(ventanaUpdate, text="Nombre de BD").place(x=10, y=10)
        cajaBasedatos= Entry(ventanaUpdate, textvariable=textoBaseDatos, width="30" ).place(x=10, y=30)

        textoTabla = StringVar()
        Label(ventanaUpdate, text="Nombre de TABLA").place(x=215, y=10)
        cajaBasedatos= Entry(ventanaUpdate, textvariable=textoTabla, width="30" ).place(x=215, y=30)

        botonAgregarDiccionario=Button(ventanaUpdate, text="AGREGAR AL DICCIONARIO", command=agregarAlDiccionario, bg="yellow", width="55").place(x=10,  y=50+40)
        botonEliminarDiccionario=Button(ventanaUpdate, text="Borrar todo el Diccionario", command=eliminarDiccionario, bg="red", fg="white", width="55").place(x=10, y=280+40)


        textoClave = StringVar()
        Label(ventanaUpdate, text="CLAVE: ").place(x=10,y=10+55)
        cajaClave= Entry(ventanaUpdate, textvariable=textoClave, width="23" ).place(x=50, y=10+55)

        textoValor = StringVar()
        Label(ventanaUpdate, text="VALOR: ").place(x=215,y=10+55)
        cajaValor= Entry(ventanaUpdate, textvariable=textoValor, width="23" ).place(x=260, y=10+55)


        my_listbox=Listbox(ventanaUpdate, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaUpdate, fg="blue", textvariable=textoInfo).place(x=10,y=400)
        #COLUMNA 2-----------------------------------------------------------------------------------------------------------------




        botonAgregarColumna=Button(ventanaUpdate, text="AGREGAR COLUMNA", command=agregarListBox, bg="yellow", width="55").place(x=10+450,  y=50+40)
        botonEliminarColumna=Button(ventanaUpdate, text="ELIMINAR COLUMNA", command=eliminarColumna, bg="red", fg="white", width="55").place(x=10+450, y=280+40)

        botonAgregarColumna=Button(ventanaUpdate, text="UPDATE!", command=ejecutarUpdate, bg="green", fg="white", width="120").place(x=10, y=305+45) 

        textoColumna = StringVar()
        Label(ventanaUpdate, text="Columna: ").place(x=10+450,y=10+55)
        cajaColumna= Entry(ventanaUpdate, textvariable=textoColumna, width="55" ).place(x=50+470, y=10+55)

        my_listbox2=Listbox(ventanaUpdate, width=64)
        my_listbox2.place(x=15+450, y =100+40)


    def delete():
        ventanaDelete=Toplevel()
        ventanaDelete.geometry("600x600")
        ventanaDelete.title="DELETE"
        def eliminarElemento():
            my_listbox.delete(ANCHOR)

        def agregarListBox():
            if textoItem.get()!="":
                my_listbox.insert(END, textoItem.get())
                textoItem.set("")
            else:
                None

        def ejecutarDelete():

            if textoBaseDatosDelete.get()!="" and textoTablaDelete.get()!="":
                listaKey=[]
                for cont in range (0,my_listbox.size(),1):
                    listaKey+=[my_listbox.get(cont)]
                
                salidaDelete=bp.delete(textoBaseDatosDelete.get(),textoTablaDelete.get(), listaKey)
                print(salidaDelete)
                #print(textoBaseDatosDelete.get())
                #print(textoTablaDelete.get())
                #print(listaKey)
                #print (salidaDelete)

                if salidaDelete==0:
                    textoInfo.set("Registro eliminado correctamente")
                    my_listbox.delete(0,tk.END)

                elif salidaDelete==1:
                    textoInfo.set("Error al eliminar el registro")
                elif salidaDelete==2:
                    textoInfo.set("La Base de datos NO existe")
                elif salidaDelete==3:
                    textoInfo.set("La tabla NO existe")
                    

                   
            else:
                textoInfo.set("Debe colocar una BD y una tabla")

        textoBaseDatosDelete = StringVar()
        Label(ventanaDelete, text="Nombre de BD").place(x=10, y=10)
        cajaBasedatosDelete= Entry(ventanaDelete, textvariable=textoBaseDatosDelete, width="30" ).place(x=10, y=30)

        textoTablaDelete = StringVar()
        Label(ventanaDelete, text="Nombre de TABLA").place(x=215, y=10)
        cajaBasedatosDelete= Entry(ventanaDelete, textvariable=textoTablaDelete, width="30" ).place(x=215, y=30)

        botonAgregarLlave=Button(ventanaDelete, text="AGREGAR LLAVE", command=agregarListBox, bg="green", fg="white", width="55").place(x=10,  y=50+40)
        botonEliminarLlave=Button(ventanaDelete, text="ELIMINAR LLAVE", command=eliminarElemento, bg="red", fg="white", width="55").place(x=10, y=280+40)
        botonAgregarKey=Button(ventanaDelete, text="DELETE!", command=ejecutarDelete, bg="yellow", width="55").place(x=10, y=305+40) 

        textoItem = StringVar()
        Label(ventanaDelete, text="Llave: ").place(x=10,y=10+55)
        cajaItem= Entry(ventanaDelete, textvariable=textoItem, width="58" ).place(x=50, y=10+55)


        my_listbox=Listbox(ventanaDelete, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaDelete, fg="blue", textvariable=textoInfo).place(x=10,y=400)

    def truncate():
        if textoNombreBDTruncate.get()!="" and textoTablaTruncate.get()!="":

            salidaTruncate=bp.truncate(textoNombreBDTruncate.get(), textoTablaTruncate.get())
            if salidaTruncate==0:
                informacion.set("Operacion Exitosa")
                textoNombreBDTruncate.set("")
                textoTablaTruncate.set("")

            elif salidaTruncate==1:
                informacion.set("Error al ejecutar el Truncate")
            elif salidaTruncate==2:
                informacion.set("La Base de datos NO existe")
            elif salidaTruncate==3:
                informacion.set("La tabla NO existe")
        else:
            informacion.set("No dejar campos vacios, BD y tabla..")
    
        #label informacion
    informacion=StringVar()
    Label(ventanaTup, text="...", fg="red", textvariable=informacion).pack()

    #BOTONES PARA LA VENTANA DE TUPLAS---------------------------------------------------------------------------
    botonInsertTupla=Button(ventanaTup, text="INSERTAR TUPLA", command=insertTupla,bg="#3300FF", fg="white", width="20").place(x=10, y=100)

    #SEPARADOR_____________________________________________________________________________________________
    separador1 = ttk.Separator(ventanaTup, orient='horizontal').place(y=140, relwidth=1.2, relheight=1)

    #CARGAR ARCHIVO-------------------------------------
    BotonSeleccionarArchivo=Button(ventanaTup, text="Cargar CSV", bg="#3300CC", fg="white",command=urlCSV, width="20").place(x=10, y=160)

          #textbox NOMBRE BASE
    textoBDSCV = StringVar()
    Label(ventanaTup, text="Nombre BD: ").place(x=250, y=160-15)
    cajaBDSCV= Entry(ventanaTup, textvariable=textoBDSCV, width="35" ).place(x=250, y=5 + 160)

    textoTablaSCV = StringVar()
    Label(ventanaTup, text="Tabla ya creada: ").place(x=500, y=160-15)
    cajaTablaSCV= Entry(ventanaTup, textvariable=textoTablaSCV, width="35" ).place(x=500, y=5 + 160)

          # _________________________________________separador ________________________________________________________
    separador2 = ttk.Separator(ventanaTup, orient='horizontal').place(y=200, relwidth=1.2, relheight=1)
    botonExtractTable=Button(ventanaTup, text="EXTRACT ROW", command=extractRow,bg="#330099", fg="white", width="20").place(x=10, y=220)
    

    
     # _________________________________________separador ________________________________________________________
    separador7 = ttk.Separator(ventanaTup, orient='horizontal').place(y=260, relwidth=1.2, relheight=1)
            #EXTRACT RANGE TABLE
    botonUpdate=Button(ventanaTup, text="UPDATE", command=update,bg="#330066", fg="white", width="20").place(x=10, y=280)
    
    
        # _________________________________________separador ________________________________________________________
    separador8 = ttk.Separator(ventanaTup, orient='horizontal').place(y=330, relwidth=1.2, relheight=1)


    botonDelete=Button(ventanaTup, text="DELETE", command=delete,bg="#330033", fg="white", width="20").place(x=10, y=360)
    
     # _________________________________________separador ________________________________________________________
    separador9 = ttk.Separator(ventanaTup, orient='horizontal').place(y=410, relwidth=1.2, relheight=1)

    botonalterAddColumn=Button(ventanaTup, text="TRUNCATE", command=truncate,bg="#330000", fg="white", width="20").place(x=10, y=440)
    
    textoNombreBDTruncate = StringVar()
    Label(ventanaTup, text="Nombre BD: ").place(x=250, y=440-20)
    cajaNombreBDTruncate= Entry(ventanaTup, textvariable=textoNombreBDTruncate, width="35" ).place(x=250, y= 440)

    
    textoTablaTruncate= StringVar()
    Label(ventanaTup, text="Tabla: ").place(x=500, y=440-20)
    cajaTablaTruncate= Entry(ventanaTup, textvariable=textoTablaTruncate, width="35" ).place(x=500, y=440)

#ventana6----------------------------------
def ventana1Fase2():
    def alterDatabaseMode():

        if (textoBD.get()=="") or (textoModo.get()=="") :
            informacion.set("Completar todos los campos...")
            
        else:
            
            x=bp.alterDatabaseMode(textoBD.get(), textoModo.get())
            if x==0:
                informacion.set("AlterDatabaseMode correctamente...")
                textoBD.set("")
                textoModo.set("")
            elif x==1:
                informacion.set("Error en la Operacion...")
            elif x==2:
                informacion.set("La base de datos no existe...")
            elif x==4:
                informacion.set("Modo Incorrecto")
            print(x)

    def alterTableMode():

        if (textoAlterTableModeBD.get()=="" or textoAlterTableModeTabla.get()=="" or textoAlterTableModeMode.get()==""):
            informacion.set( "No deje campos vacios.")
            
        else:
            try:
                salida=textoAlterTableModeMode.get()
                x=bp.alterTableMode(textoAlterTableModeBD.get(),textoAlterTableModeTabla.get(),salida.lower() )
               
                if x==0:
                    informacion.set("AlterTableMode Exitoso")

                    textoAlterTableModeBD.set("")
                    textoAlterTableModeTabla.set("")
                    textoAlterTableModeMode.set("")
                elif x==1:
                    informacion.set("Error al ejecutar el AlterTableMode")
                elif x==2:
                    informacion.set("Base de datos NO existente")
                elif x==3:
                    informacion.set("Tabla NO existente")
                elif x==4:
                    informacion.set("Modo Incorrecto")              
                else:
                    informacion.set("Error desconocido ")
            except:
                informacion.set("Error desconocido ")
            
    def alterTableAddFK():
        ventanaAlterTableAddFK=Toplevel()
        ventanaAlterTableAddFK.geometry("875x450")
        ventanaAlterTableAddFK.title="alterTableAddFK"

        #variables mas globales
        listaCol=[]
        listaColRef=[]

        def eliminarListBox1():
            my_listbox.delete(0,tk.END)
            my_listbox.clear()
            
        def eliminarListBox2():
            my_listbox2.delete(ANCHOR)
            listaColRef.clear()
            for cont in range (0,my_listbox2.size(),1):
                listaColRef.append(my_listbox2.get(cont))
            print(listaColRef)    
            
        def agregarListBox1():
            if textoClave.get()!="":
                try:
                    my_listbox.insert(END, int(textoClave.get()))
                    textoClave.set("")
                    listaCol.clear()
                    for cont in range (0,my_listbox.size(),1):
                        listaCol.append(my_listbox.get(cont))
                    print(listaCol)
                except:
                    textoInfo.set("Columnas solo acepta Enteros")
            else:
                None

        def agregarListBox2():
            if textoColumna.get()!="":
                try:
                    my_listbox2.insert(END, int(textoColumna.get()))
                    textoColumna.set("")
                    listaColRef.clear()
                    for cont in range (0,my_listbox2.size(),1):
                        listaColRef.append(my_listbox2.get(cont))
                    print(listaColRef)    
                except:
                    textoInfo.set("ColumnasRef solo acepta Enteros")
            else:
                None

        def ejecutarAlterTableAddFK():
            if textoBaseDatos.get()!="" and textoTabla.get()!="" or textoIndexName.get()!="" or  textoTableRef.get()!="":
                if listaCol!=[]:
                    if listaColRef!=[]:
                        print(textoBaseDatos.get())
                        print(textoTabla.get())
                        print(listaCol)
                        print(listaColRef)

                        x=bp.alterTableAddFK(textoBaseDatos.get(),textoTabla.get(),textoIndexName.get(), listaCol, textoTableRef.get(),listaColRef)
                        
                        if x==0:
                            textoInfo.set("AlterTableAddFK ejecutado correctamente")
                            my_listbox2.delete(0,tk.END)
                            my_listbox.delete(0,tk.END)
                            listaColRef.clear()
                            listaCol.clear()
                            textoBaseDatos.set("")
                            textoTabla.set("")
                            textoIndexName.set("")
                            textoTableRef.set("")

                        elif x==1:
                            textoInfo.set("Error al realizar el AlterTableAddFK")
                        elif x==2:
                            textoInfo.set("La Base de datos NO existe")
                        elif x==3:
                            textoInfo.set("Table o TableRef NO existe")
                        elif x==4:
                            textoInfo.set("Cantidad NO exacta entre columns y columnsRef")
                        elif x==5:
                            textoInfo.set("No se cumple la integridad referencial")
                        print(x)
                    else:
                        textoInfo.set("ColumnsRef, colocar valores")
                else:
                    textoInfo.set("Columns vacio, colocar valores")
            else:
                textoInfo.set("No dejar campos vacios: BD, tabla, indexName, tableRef")
        #COLUMNA 1-----------------------------------------------------------------------------------------------------------------

        #def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
        textoBaseDatos = StringVar()
        Label(ventanaAlterTableAddFK, text="Base de Datos").place(x=10, y=10)
        cajaBasedatos= Entry(ventanaAlterTableAddFK, textvariable=textoBaseDatos, width="30" ).place(x=10, y=30)

        textoTabla = StringVar()
        Label(ventanaAlterTableAddFK, text="Tabla").place(x=215, y=10)
        cajaBasedatos= Entry(ventanaAlterTableAddFK, textvariable=textoTabla, width="30" ).place(x=215, y=30)

        textoIndexName = StringVar()
        Label(ventanaAlterTableAddFK, text="IndexName").place(x=465, y=10)
        cajaIndexName= Entry(ventanaAlterTableAddFK, textvariable=textoIndexName, width="30" ).place(x=465, y=30)

        textoTableRef = StringVar()
        Label(ventanaAlterTableAddFK, text="TableRef").place(x=665, y=10)
        cajatableRef= Entry(ventanaAlterTableAddFK, textvariable=textoTableRef, width="30" ).place(x=665, y=30)

        botonAgregarDiccionario=Button(ventanaAlterTableAddFK, text="Agregar Columna", command=agregarListBox1, bg="yellow", width="55").place(x=10,  y=50+40)
        botonEliminarDiccionario=Button(ventanaAlterTableAddFK, text="Borrar Columnas", command=eliminarListBox1, bg="red", fg="white", width="55").place(x=10, y=280+40)


        textoClave = StringVar()
        Label(ventanaAlterTableAddFK, text="Columna: ").place(x=10,y=10+55)
        cajaClave= Entry(ventanaAlterTableAddFK, textvariable=textoClave, width="15" ).place(x=70, y=10+55)


        my_listbox=Listbox(ventanaAlterTableAddFK, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaAlterTableAddFK, fg="blue", textvariable=textoInfo).place(x=10,y=400)



        #COLUMNA 2-----------------------------------------------------------------------------------------------------------------
        botonAgregarColumna=Button(ventanaAlterTableAddFK, text="Agregar ColumnRef", command=agregarListBox2, bg="yellow", width="55").place(x=10+450,  y=50+40)
        botonEliminarColumna=Button(ventanaAlterTableAddFK, text="Borrar ColumnRef", command=eliminarListBox2, bg="red", fg="white", width="55").place(x=10+450, y=280+40)

        botonAgregarColumna=Button(ventanaAlterTableAddFK, text="Alter Table Add FK!", command=ejecutarAlterTableAddFK, bg="green", fg="white", width="120").place(x=10, y=305+45) 

        textoColumna = StringVar()
        Label(ventanaAlterTableAddFK, text="ColumnaRef: ").place(x=10+450,y=10+55)
        cajaColumna= Entry(ventanaAlterTableAddFK, textvariable=textoColumna, width="50" ).place(x=50+495, y=10+55)

        my_listbox2=Listbox(ventanaAlterTableAddFK, width=64)
        my_listbox2.place(x=15+450, y =100+40)

    def AlterTableDropFK():
                #def alterTableDropFK(database: str, table: str, indexName: str) -> int:
        if (textoAlterTableDropFKBD.get()!="" and textoAlterTableDropFKTable.get()!="" and textoAlterTableDropFKIndexName.get()!=""):
            informacion.set("")
            salida=bp.alterTableDropFK(textoAlterTableDropFKBD.get(),textoAlterTableDropFKTable.get(),  textoAlterTableDropFKIndexName.get())
            if salida==0:
                informacion.set("AlterTableDropFK ejecutado correctamente")
            elif salida==1:
                informacion.set("Error al realizar el AlterTableDropFK")
            elif salida==2:
                informacion.set("Base de datos NO existente")
            elif salida==3:
                informacion.set("Tabla NO existente")
            elif salida==4:
                informacion.set("Nombre de indice no existente")

        else:
            informacion.set("Debe llenar BD, Tabla e indexName")

    def alterTableAddUnique():
        ventanaAlterTableAddUnique=Toplevel()
        ventanaAlterTableAddUnique.geometry("425x450")
        ventanaAlterTableAddUnique.title="ventanaAlterTableAddUnique"
        def eliminarElemento():
            my_listbox.delete(ANCHOR)

        def ejecutaraAterTableAddUnique():

            if textoBaseDatos.get()!="" or textoTabla.get()!="" or textoIndexName.get()!="":
                listaColumna=[]
                for cont in range (0,my_listbox.size(),1):  
                    listaColumna+=[int(my_listbox.get(cont))]

                x=bp.alterTableAddUnique(textoBaseDatos.get(), textoTabla.get(), textoIndexName.get(), listaColumna)
                
                print(textoBaseDatos.get())
                print(textoTabla.get())
                print(listaColumna)
                if x==0:
                    textoInfo.set("AlterTableAddUnique realizado correctamente")
                    my_listbox.delete(0,tk.END)
                    textoBaseDatos.set("")
                    textoTabla.set("")
                    textoIndexName.set("")

                elif x==1:
                    textoInfo.set("Error al realizar el AlterTableAddUnique")
                elif x==2:
                    textoInfo.set("La base de Datos NO existe")
                elif x==3:
                    textoInfo.set("Table o tableRef no existente")
                elif x==4:
                    textoInfo.set("Cantidad no exacta entre columns y columnsRef")
                elif x==5:
                    textoInfo.set("No se cumple la integridad de unicidad")
            else:
                textoInfo.set("Debe colocar BD, tabla, index, y columnas")


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
        Label(ventanaAlterTableAddUnique, text="Base de Datos").place(x=10, y=10)
        cajaBasedatos= Entry(ventanaAlterTableAddUnique, textvariable=textoBaseDatos, width="30" ).place(x=10, y=30)

        textoTabla = StringVar()
        Label(ventanaAlterTableAddUnique, text="Tabla").place(x=215, y=10)
        cajaBasedatos= Entry(ventanaAlterTableAddUnique, textvariable=textoTabla, width="30" ).place(x=215, y=30)

        botonAgregarLista=Button(ventanaAlterTableAddUnique, text="Agregar Columna", command=agregarListBox, bg="green", fg="white", width="55").place(x=10,  y=50+40)
        botonEliminarElemento=Button(ventanaAlterTableAddUnique, text="Quitar Columna", command=eliminarElemento, bg="red", fg="white", width="55").place(x=10, y=280+40)
        botonAgregarTupla=Button(ventanaAlterTableAddUnique, text="AlterTableAddUnique", command=ejecutaraAterTableAddUnique, bg="yellow", width="55").place(x=10, y=305+40) 

        textoItem = StringVar()
        Label(ventanaAlterTableAddUnique, text="Columna: ").place(x=10,y=10+55)
        cajaItem= Entry(ventanaAlterTableAddUnique, textvariable=textoItem, width="15" ).place(x=70, y=10+55)

        textoIndexName = StringVar()
        Label(ventanaAlterTableAddUnique, text="IndexName: ").place(x=10+200,y=10+55)
        cajaIIndexName= Entry(ventanaAlterTableAddUnique, textvariable=textoIndexName, width="15" ).place(x=70+230, y=10+55)


        my_listbox=Listbox(ventanaAlterTableAddUnique, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaAlterTableAddUnique, fg="blue", textvariable=textoInfo).place(x=10,y=400)
        textoInfo.set("FUNCION AlterTableAddUnique")


    def AlterTableDropUnique():
        if (textoAlterTableDropUniqueBD.get()!="" and textoAlterTableDropUniqueTabla.get()!="" and textoAlterTableDropUniqueIndexName.get()!=""):
            informacion.set("")
            salidaAlter=bp.alterTableDropUnique(textoAlterTableDropUniqueBD.get(), textoAlterTableDropUniqueTabla.get(),textoAlterTableDropUniqueIndexName.get())
            if salidaAlter==0:
                informacion.set("AlterTableDropUnique ejecutado correctamente")
                textoAlterTableDropUniqueBD.set("")
                textoAlterTableDropUniqueTabla.set("")
                textoAlterTableDropUniqueIndexName.set("")

            elif salidaAlter==1:
                informacion.set("Error al ejecutar el AlterTableDropUnique")
            elif salidaAlter==2:
                informacion.set("La base de datos No existe")
            elif salidaAlter==3:
                informacion.set("La Tabla no existe")
            elif salidaAlter==4:
                informacion.set("Nombre de índice NO existente")
        else:
            informacion.set("No deje campos vacios...")

    def alterTableAddIndex():
        ventanaAlterTableAddUnique=Toplevel()
        ventanaAlterTableAddUnique.geometry("425x450")
        ventanaAlterTableAddUnique.title="alterTableAddIndex"
        def eliminarElemento():
            my_listbox.delete(ANCHOR)

        def ejecutaraAterTableAddUnique():

            if textoBaseDatos.get()!="" or textoTabla.get()!="" or textoIndexName.get()!="":
                listaColumna=[]
                for cont in range (0,my_listbox.size(),1):  
                    listaColumna+=[int(my_listbox.get(cont))]

                x=bp.alterTableAddUnique(textoBaseDatos.get(), textoTabla.get(), textoIndexName.get(), listaColumna)
                print(textoBaseDatos.get())
                print(textoTabla.get())
                print(listaColumna)
                if x==0:
                    textoInfo.set("alterTableAddIndex realizado correctamente")
                    my_listbox.delete(0,tk.END)
                    textoBaseDatos.set("")
                    textoTabla.set("")
                    textoIndexName.set("")

                elif x==1:
                    textoInfo.set("Error al realizar el alterTableAddIndex")
                elif x==2:
                    textoInfo.set("La base de Datos NO existe")
                elif x==3:
                    textoInfo.set("Table o tableRef no existente")
                elif x==4:
                    textoInfo.set("Cantidad no exacta entre columns y columnsRef")
         
            else:
                textoInfo.set("Debe colocar BD, tabla, index, y columnas")


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
        Label(ventanaAlterTableAddUnique, text="Base de Datos").place(x=10, y=10)
        cajaBasedatos= Entry(ventanaAlterTableAddUnique, textvariable=textoBaseDatos, width="30" ).place(x=10, y=30)

        textoTabla = StringVar()
        Label(ventanaAlterTableAddUnique, text="Tabla").place(x=215, y=10)
        cajaBasedatos= Entry(ventanaAlterTableAddUnique, textvariable=textoTabla, width="30" ).place(x=215, y=30)

        botonAgregarLista=Button(ventanaAlterTableAddUnique, text="Agregar Columna", command=agregarListBox, bg="green", fg="white", width="55").place(x=10,  y=50+40)
        botonEliminarElemento=Button(ventanaAlterTableAddUnique, text="Quitar Columna", command=eliminarElemento, bg="red", fg="white", width="55").place(x=10, y=280+40)
        botonAgregarTupla=Button(ventanaAlterTableAddUnique, text="alterTableAddIndex", command=ejecutaraAterTableAddUnique, bg="yellow", width="55").place(x=10, y=305+40) 

        textoItem = StringVar()
        Label(ventanaAlterTableAddUnique, text="Columna: ").place(x=10,y=10+55)
        cajaItem= Entry(ventanaAlterTableAddUnique, textvariable=textoItem, width="15" ).place(x=70, y=10+55)

        textoIndexName = StringVar()
        Label(ventanaAlterTableAddUnique, text="IndexName: ").place(x=10+200,y=10+55)
        cajaIIndexName= Entry(ventanaAlterTableAddUnique, textvariable=textoIndexName, width="15" ).place(x=70+230, y=10+55)


        my_listbox=Listbox(ventanaAlterTableAddUnique, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaAlterTableAddUnique, fg="blue", textvariable=textoInfo).place(x=10,y=400)
        textoInfo.set("FUNCION alterTableAddIndex")

    def alterTableDropIndex():
        
        if (textoAlterTableDropIndexBD.get()!="" and textoAlterTableDropIndexTabla.get()!="" and textoAlterTableDropIndexIndexName.get()!=""):
            informacion.set("")
            salidaAlter=bp.alterTableDropIndex(textoAlterTableDropIndexBD.get(), textoAlterTableDropIndexTabla.get(),textoAlterTableDropIndexIndexName.get())
            
            if salidaAlter==0:
                informacion.set("AlterTableDropIndex ejecutado correctamente")
                textoAlterTableDropIndexBD.set("")
                textoAlterTableDropIndexTabla.set("")
                textoAlterTableDropIndexIndexName.set("")

            elif salidaAlter==1:
                informacion.set("Error al ejecutar el AlterTableDropIndex")
            elif salidaAlter==2:
                informacion.set("La base de datos No existe")
            elif salidaAlter==3:
                informacion.set("La Tabla no existe")
            elif salidaAlter==4:
                informacion.set("Nombre de índice NO existente")
        else:
            informacion.set("No deje campos vacios...")

    def AlterDatabaseEncoding():
        if (textoAlterDatabaseEncodingBD.get()!="" and textoAlterDatabaseEncodingEncoding.get()!=""):
            informacion.set("")
   
            salidaAlter=bp.alterDatabaseEncoding(textoAlterDatabaseEncodingBD.get(), textoAlterDatabaseEncodingEncoding.get())
            
            if salidaAlter==0:
                informacion.set(" ejecutado correctamente")
                textoAlterDatabaseEncodingBD.set("")
                textoAlterDatabaseEncodingEncoding.set("")
            elif salidaAlter==1:
                informacion.set("Error al ejecutar el AlterDatabaseEncoding")
            elif salidaAlter==2:
                informacion.set("La base de datos No existe")
            elif salidaAlter==3:
                informacion.set("nombre de codificación no existente")
        else:
            informacion.set("No deje campos vacios...")

    ventanaTab=Toplevel()
    ventanaTab.geometry("1100x700")
    ventanaTab.title="Funciones de Tablas"

    #label informacion
    informacion=StringVar()
    Label(ventanaTab, text="...", fg="red", textvariable=informacion).pack()

    #CREAR TABLA-------------------------------------
    boton1=Button(ventanaTab, text="ALTER DATABASE MODE", bg="#5D6D7E", fg="white",command=alterDatabaseMode, width="20").place(x=10, y=100)
        
        #textbox BD
    textoBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=85)
    cajaNombreBD= Entry(ventanaTab, textvariable=textoBD, width="35" ).place(x=250, y=5 + 100)

            #textbox MODO
    textoModo = StringVar()
    Label(ventanaTab, text="Modo ").place(x=500, y=85)
    cajaNombreTabla= Entry(ventanaTab, textvariable=textoModo, width="35" ).place(x=500, y=5 + 100)

        # _________________________________________separador ________________________________________________________
    separador1 = ttk.Separator(ventanaTab, orient='horizontal').place(y=140, relwidth=1.2, relheight=1)

    #def alterTableMode(database: str, table: str, mode: str) -> int:-------------------------------------
    botonalterTableMode=Button(ventanaTab, text="ALTER TABLE MODE", bg="#34495E", fg="white",command=alterTableMode, width="20").place(x=10, y=160)
        
        #textbox BD
    textoAlterTableModeBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=160-15)
    cajaAlterTableModeBD= Entry(ventanaTab, textvariable=textoAlterTableModeBD, width="35" ).place(x=250, y=5 + 160)

        #textbox Tabla
    textoAlterTableModeTabla = StringVar()
    Label(ventanaTab, text="Tabla:").place(x=500, y=160-15)
    cajaAlterTableModeTabla= Entry(ventanaTab, textvariable=textoAlterTableModeTabla, width="35" ).place(x=500, y=5 + 160)

        #textbox MODE
    textoAlterTableModeMode = StringVar()
    Label(ventanaTab, text="Mode:").place(x=750, y=160-15)
    cajaAlterTableModeMode= Entry(ventanaTab, textvariable=textoAlterTableModeMode, width="35" ).place(x=750, y=5 + 160)

            # _________________________________________separador ________________________________________________________
    separador2 = ttk.Separator(ventanaTab, orient='horizontal').place(y=200, relwidth=1.2, relheight=1)
    botonalterTableAddFK=Button(ventanaTab, text="Alter Table Add FK", command=alterTableAddFK,bg="#2E4053", fg="white", width="20").place(x=10, y=220)
    

        # _________________________________________separador ________________________________________________________
    separador7 = ttk.Separator(ventanaTab, orient='horizontal').place(y=260, relwidth=1.2, relheight=1)
    
    botonAlterTableDrop=Button(ventanaTab, text="Alter Table Drop FK", command=AlterTableDropFK,bg="#283747", fg="white", width="20").place(x=10, y=280)
    
    textoAlterTableDropFKBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=270)
    cajaAlterTableDropBD= Entry(ventanaTab, textvariable=textoAlterTableDropFKBD, width="35" ).place(x=250, y= 290)


    textoAlterTableDropFKTable = StringVar()
    Label(ventanaTab, text="Nombre de Tabla: ").place(x=500, y=270)
    cajaAlterTableDropFKTable= Entry(ventanaTab, textvariable=textoAlterTableDropFKTable, width="35" ).place(x=500, y=290)

    textoAlterTableDropFKIndexName = StringVar()
    Label(ventanaTab, text="Index Name: ").place(x=750, y=270)
    cajaAlterTableDropFKIndexName= Entry(ventanaTab, textvariable=textoAlterTableDropFKIndexName, width="15" ).place(x=750, y=290)

    
        # _________________________________________separador ________________________________________________________
    separador8 = ttk.Separator(ventanaTab, orient='horizontal').place(y=330, relwidth=1.2, relheight=1)


    botonalterTableAddUnique=Button(ventanaTab, text="Alter Table Add Unique", command=alterTableAddUnique,bg="#212F3C", fg="white", width="20").place(x=10, y=360)
    

    #def AlterTableDropUnique(database: str, table: str, indexName: str) -> int:
            # _________________________________________separador ________________________________________________________
    separador9 = ttk.Separator(ventanaTab, orient='horizontal').place(y=410, relwidth=1.2, relheight=1)

    botonAlterTableDropUnique=Button(ventanaTab, text="Alter Table Drop Unique", command=AlterTableDropUnique, bg="#1B2631", fg="white",width="28").place(x=10, y=440)
    
    textoAlterTableDropUniqueBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=440-20)
    cajaAlterTableDropUniqueBD= Entry(ventanaTab, textvariable=textoAlterTableDropUniqueBD, width="35" ).place(x=250, y= 440)

    
    textoAlterTableDropUniqueTabla = StringVar()
    Label(ventanaTab, text="Tabla: ").place(x=500, y=440-20)
    cajaAlterTableDropUniqueTabla= Entry(ventanaTab, textvariable=textoAlterTableDropUniqueTabla, width="35" ).place(x=500, y=440)

    textoAlterTableDropUniqueIndexName = StringVar()
    Label(ventanaTab, text="indexName: ").place(x=750, y=440-20)
    cajaAlterTableDropUniqueIndexName= Entry(ventanaTab, textvariable=textoAlterTableDropUniqueIndexName, width="35" ).place(x=750, y=440)
   

               # _________________________________________separador ________________________________________________________
    separador10 = ttk.Separator(ventanaTab, orient='horizontal').place(y=480, relwidth=1.2, relheight=1)

    botonalterTableAddIndex=Button(ventanaTab, text="Alter Table Add Index", command=alterTableAddIndex, bg="#1B2631", fg="white",width="28").place(x=10, y=500)
    
                  # _________________________________________separador ________________________________________________________
    separador11 = ttk.Separator(ventanaTab, orient='horizontal').place(y=550, relwidth=1.2, relheight=1)
   
    botonAlterTableDropIndex=Button(ventanaTab, text="AlterTableDropIndex", command=alterTableDropIndex, bg="#1B2631", fg="white",width="28").place(x=10, y=440+130)
    
    textoAlterTableDropIndexBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=440-20+140)
    cajaAlterTableDropIndexBD= Entry(ventanaTab, textvariable=textoAlterTableDropIndexBD, width="35" ).place(x=250, y= 440+140)

    textoAlterTableDropIndexTabla = StringVar()
    Label(ventanaTab, text="Tabla: ").place(x=500, y=440-20+140)
    cajaAlterTableDropIndexTabla= Entry(ventanaTab, textvariable=textoAlterTableDropIndexTabla, width="35" ).place(x=500, y=440+140)

    textoAlterTableDropIndexIndexName = StringVar()
    Label(ventanaTab, text="indexName: ").place(x=750, y=440-20+140)
    cajaAlterTableDropIndexIndexName= Entry(ventanaTab, textvariable=textoAlterTableDropIndexIndexName, width="35" ).place(x=750, y=440+140)
   
    # _________________________________________separador ________________________________________________________
    separador11 = ttk.Separator(ventanaTab, orient='horizontal').place(y=620, relwidth=1.2, relheight=1)

    botonAlterDatabaseEncoding=Button(ventanaTab, text="AlterDatabaseEncoding", command=AlterDatabaseEncoding, bg="#1B2631", fg="white",width="28").place(x=10, y=570+80)
    
    textoAlterDatabaseEncodingBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=570-20+80)
    cajaAlterDatabaseEncodingBD= Entry(ventanaTab, textvariable=textoAlterDatabaseEncodingBD, width="35" ).place(x=250, y= 570+80)

    textoAlterDatabaseEncodingEncoding = StringVar()
    Label(ventanaTab, text="Encoding: ").place(x=500, y=570-20+80)
    cajaAlterDatabaseEncodingTabla= Entry(ventanaTab, textvariable=textoAlterDatabaseEncodingEncoding, width="35" ).place(x=500, y=570+80)
   

def ventana2Fase2():
    def checksumDatabase():

        if (textoBD.get()=="") or (textoModo.get()=="") :
            informacion.set("Completar todos los campos...")
        else:
            
            x=bp.checksumDatabase(textoBD.get(), textoModo.get())
            if x==None:
                informacion.set("Ocurrio un error al calcular el checksum")
            else:
                informacion.set("ChechsumDatabase, Modo: "+ textoModo.get() +", " +x)
                textoBD.set("")
                textoModo.set("")
                print("Checksum Database: " + x)

    def checksumTable():

        if (textoChecksumTableModeBD.get()=="" or textoChecksumTableModeTabla.get()=="" or textoChecksumTableModeMode.get()==""):
            informacion.set( "No deje campos vacios.")
            
        else:
            x=bp.checksumTable(textoChecksumTableModeBD.get(),textoChecksumTableModeTabla.get(),textoChecksumTableModeMode.get() )
            
            if x==None:
                informacion.set("Ocurrio un error al calcular el ChecksumTable")
            else:
                
                informacion.set(x)
                informacion.set("ChechsumTable, Modo: "+ textoModo.get().Upper() +", " +x)
                textoChecksumTableModeBD.set("")
                textoChecksumTableModeTabla.set("")
                textoChecksumTableModeMode.set("")  
      
    def encrypt():
        if (textoEncriptBD.get()!="" and textoEncriptPassword.get()!=""):
   
            salidaEncript=bp.encrypt(textoEncriptBD.get(), textoEncriptPassword.get())
            
            if salidaEncript==None:
                informacion.set("Ocurrio un problema al ejecutar el Encript")

            else:
                informacion.set("Criptograma: " + salidaEncript)
                print("Criptograma: " + salidaEncript)
                textoEncriptBD.set("")
                textoEncriptPassword.set("")
        else:
            informacion.set("No deje campos vacios...")  

    def decrypt():
        if (textoDecriptCipherBackup.get()!="" and textoDecriptPassword.get()!=""):
   
            salidaEncript=bp.decrypt(textoDecriptCipherBackup.get(), textoDecriptPassword.get())
            
            if salidaEncript==None:
                informacion.set("Ocurrio un problema al ejecutar el Decript")

            else:
                informacion.set("Decrypt: " + salidaEncript)
                print("Decrypt: " + salidaEncript)
                textoDecriptCipherBackup.set("")
                textoDecriptPassword.set("")
        else:
            informacion.set("No deje campos vacios...")  

    def safeModeOn():
        if (textoSafeModeOnBD.get()!="" and textoSafeModeOnTable.get()!=""):
            salida=bp.safeModeOn(textoSafeModeOnBD.get(), textoSafeModeOnTable.get())
            
            if salida==0:
                informacion.set("safeModeOn ejecutado correctamente")
                textoSafeModeOnBD.set("")
                textoSafeModeOnTable.set("")

            elif salida==1:
                informacion.set("Error al realizar el safeModeOn")
            elif salida==2:
                informacion.set("Base de datos NO existente")
            elif salida==3:
                informacion.set("Tabla NO existente")
            elif salida==4:
                informacion.set("Modo seguro existente")

        else:
            informacion.set("No dejar campos vacios...")
    
    def safeModeOff():
        if (textoSafeModeOffBD.get()!="" and textoSafeModeOffTabla.get()!=""):
            salida=bp.safeModeOff(textoSafeModeOffBD.get(), textoSafeModeOffTabla.get())
            
            if salida==0:
                informacion.set("safeModeOff ejecutado correctamente")
                textoSafeModeOffBD.set("")
                textoSafeModeOffTabla.set("")
            elif salida==1:
                informacion.set("Error al realizar el safeModeOff")
            elif salida==2:
                informacion.set("Base de datos NO existente")
            elif salida==3:
                informacion.set("Tabla NO existente")
            elif salida==4:
                informacion.set("Modo seguro OFF existente")

        else:
            informacion.set("No dejar campos vacios...")


    def GraphDSDBD():
        if not (textoGraphDSDBD.get()==""):
            x=bp.graphDSD(textoGraphDSDBD.get())
            if x==None:
                informacion.set("Ocurrio un error al Graficar DSD")
            else:
                informacion.set("")
            textoGraphDSDBD.set("")
        else:
            informacion.set("No deje espacios en blanco...")

    def graphDF():
        
        if not (textoGraphDFBD.get()=="") and not(textoGraphDFTabla.get()==""):
            x=bp.graphDF(textoGraphDFBD.get(),textoGraphDFTabla.get() )
            if x==None:
                informacion.set("Ocurrio un error al graficar DF")
            else:
                informacion.set("")
                textoGraphDFBD.set("")
                textoGraphDFTabla.set("")
        else:
            informacion.set("No deje espacios en blanco...")

 

    ventanaTab=Toplevel()
    ventanaTab.geometry("1100x700")
    ventanaTab.title="fase2 parte2"

    #label informacion
    informacion=StringVar()
    Label(ventanaTab, text="...", fg="red", textvariable=informacion).pack()

    #CREAR TABLA-------------------------------------
    boton1=Button(ventanaTab, text="Checksum Database", bg="#5D6D7E", fg="white",command=checksumDatabase, width="20").place(x=10, y=100)
        
        #textbox BD
    textoBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=85)
    cajaNombreBD= Entry(ventanaTab, textvariable=textoBD, width="35" ).place(x=250, y=5 + 100)

            #textbox MODO
    textoModo = StringVar()
    Label(ventanaTab, text="Modo ").place(x=500, y=85)
    cajaNombreTabla= Entry(ventanaTab, textvariable=textoModo, width="35" ).place(x=500, y=5 + 100)

    
        # _________________________________________separador ________________________________________________________
    separador1 = ttk.Separator(ventanaTab, orient='horizontal').place(y=140, relwidth=1.2, relheight=1)

    #def alterTableMode(database: str, table: str, mode: str) -> int:-------------------------------------
    botonChecksumTableMode=Button(ventanaTab, text="Checksum Table", bg="#34495E", fg="white",command=checksumTable, width="20").place(x=10, y=160)
        
        #textbox BD
    textoChecksumTableModeBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=160-15)
    cajaChecksumTableModeBD= Entry(ventanaTab, textvariable=textoChecksumTableModeBD, width="35" ).place(x=250, y=5 + 160)

        #textbox Tabla
    textoChecksumTableModeTabla = StringVar()
    Label(ventanaTab, text="Tabla:").place(x=500, y=160-15)
    cajaChecksumTableModeTabla= Entry(ventanaTab, textvariable=textoChecksumTableModeTabla, width="35" ).place(x=500, y=5 + 160)

        #textbox MODE
    textoChecksumTableModeMode = StringVar()
    Label(ventanaTab, text="Mode:").place(x=750, y=160-15)
    cajaChecksumTableModeMode= Entry(ventanaTab, textvariable=textoChecksumTableModeMode, width="35" ).place(x=750, y=5 + 160)

    #def encrypt(backup: str, password: str) -> str:
    # _________________________________________separador ________________________________________________________
    separador2 = ttk.Separator(ventanaTab, orient='horizontal').place(y=200, relwidth=1.2, relheight=1)
    botonencrypt=Button(ventanaTab, text="Encrypt", command=encrypt,bg="#2E4053", fg="white", width="20").place(x=10, y=220)

            #textbox BD
    textoEncriptBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=220-15)
    cajaEncriptBD= Entry(ventanaTab, textvariable=textoEncriptBD, width="35" ).place(x=250, y=5 + 220)

        #textbox password
    textoEncriptPassword = StringVar()
    Label(ventanaTab, text="Password:").place(x=500, y=220-15)
    cajaEncriptPassword= Entry(ventanaTab, textvariable=textoEncriptPassword, width="35" ).place(x=500, y=5 + 220)

    
    
        # _________________________________________separador ________________________________________________________
    separador7 = ttk.Separator(ventanaTab, orient='horizontal').place(y=260, relwidth=1.2, relheight=1)
    
    botonAlterTableDrop=Button(ventanaTab, text="Decrypt", command=decrypt,bg="#283747", fg="white", width="20").place(x=10, y=280)
    
    textoDecriptCipherBackup = StringVar()
    Label(ventanaTab, text="CipherBackup: ").place(x=250, y=270)
    cajaDecriptCipherBackup= Entry(ventanaTab, textvariable=textoDecriptCipherBackup, width="35" ).place(x=250, y= 290)


    textoDecriptPassword = StringVar()
    Label(ventanaTab, text="Password: ").place(x=500, y=270)
    cajaDecriptPassword= Entry(ventanaTab, textvariable=textoDecriptPassword, width="35" ).place(x=500, y=290)

    
    
        # _________________________________________separador ________________________________________________________
    separador8 = ttk.Separator(ventanaTab, orient='horizontal').place(y=330, relwidth=1.2, relheight=1)


    botonasafeModeOn=Button(ventanaTab, text="Safe Mode On", command=safeModeOn,bg="#212F3C", fg="white", width="20").place(x=10, y=360)
    

    textoSafeModeOnBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=360-20)
    cajasafeModeOnBD= Entry(ventanaTab, textvariable=textoSafeModeOnBD, width="35" ).place(x=250, y= 360)


    textoSafeModeOnTable = StringVar()
    Label(ventanaTab, text="Tabla: ").place(x=500, y=360-20)
    cajaSafeModeOn= Entry(ventanaTab, textvariable=textoSafeModeOnTable, width="35" ).place(x=500, y=360)

    
    

            # _________________________________________separador ________________________________________________________
    separador9 = ttk.Separator(ventanaTab, orient='horizontal').place(y=410, relwidth=1.2, relheight=1)

    botonSafeModeOff=Button(ventanaTab, text="SafeModeOff", command=safeModeOff, bg="#1B2631", fg="white",width="28").place(x=10, y=440)
    
    textoSafeModeOffBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=440-20)
    cajaSafeModeOffBD= Entry(ventanaTab, textvariable=textoSafeModeOffBD, width="35" ).place(x=250, y= 440)

    
    textoSafeModeOffTabla = StringVar()
    Label(ventanaTab, text="Tabla: ").place(x=500, y=440-20)
    cajaSafeModeOffTabla= Entry(ventanaTab, textvariable=textoSafeModeOffTabla, width="35" ).place(x=500, y=440)
    
    

               # _________________________________________separador ________________________________________________________
    separador10 = ttk.Separator(ventanaTab, orient='horizontal').place(y=480, relwidth=1.2, relheight=1)

    botontextoGraphDSD=Button(ventanaTab, text="GraphDSD", command=GraphDSDBD, bg="#1B2631", fg="white",width="28").place(x=10, y=500)
    
    textoGraphDSDBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=505-20)
    cajaGraphDSD= Entry(ventanaTab, textvariable=textoGraphDSDBD, width="35" ).place(x=250, y= 505)

    
                  # _________________________________________separador ________________________________________________________
    separador11 = ttk.Separator(ventanaTab, orient='horizontal').place(y=550, relwidth=1.2, relheight=1)
   
    botonGraphDF=Button(ventanaTab, text="GraphDF", command=graphDF, bg="#1B2631", fg="white",width="28").place(x=10, y=440+130)
    
    textoGraphDFBD = StringVar()
    Label(ventanaTab, text="Base de Datos: ").place(x=250, y=440-20+140)
    cajaGraphDFBD= Entry(ventanaTab, textvariable=textoGraphDFBD, width="35" ).place(x=250, y= 440+140)

    textoGraphDFTabla = StringVar()
    Label(ventanaTab, text="Tabla: ").place(x=500, y=440-20+140)
    cajaGraphDF= Entry(ventanaTab, textvariable=textoGraphDFTabla, width="35" ).place(x=500, y=440+140)


def ventana3Fase2():

    def alterDatabaseCompress():
        try:
            if textoBD.get()!="" and textoLevel.get()!="":
                x=bp.alterDatabaseCompress(textoBD.get(), int(textoLevel.get()))
                print(textoBD.get())
                print(textoLevel.get())
                if x==0:
                    informacion.set("AlterDatabaseCompress ejecutado correctamente")
                    textoBD.set("")
                    textoLevel.set("")
                elif x==1:
                    informacion.set("Error al ejecutar AlterDatabaseCompress")
                elif x==2:
                    informacion.set("La Base de Datos no existe")
                elif x==3:
                    informacion.set("Level incorrecto")
            else:
                informacion.set("No deje campos vacios")
        except:
            informacion.set("Poner un numero entero en Level")


    def alterDatabaseDecompress():
        if textoAlterDatabaseDecompressBD.get()!="":
            x=bp.alterDatabaseDecompress(textoAlterDatabaseDecompressBD.get())
            if x==0:
                textoAlterDatabaseDecompressBD.set("")
                informacion.set("AlterDatabaseDecompress ejecutado correctamente")
            if x==1:
                informacion.set("Error al ejecutar el AlterDatabaseDecompress")
            if x==2:
                informacion.set("Base de datos no existente")
            if x==3:
                informacion.set("No hay compresion")
        else:
            informacion.set("No dejar campo vacio")


    def alterTableCompress():

        if textoAlterTableCompressBD.get()!="" and textoAlterTableCompressTabla.get()!="" and textoAlterTableCompressLevel.get()!="":
            try:
                x=bp.alterTableCompress(textoAlterTableCompressBD.get(),textoAlterTableCompressTabla.get(), int(textoAlterTableCompressLevel.get()))

                if x==0:
                    informacion.set("AlterTableCompress ejecutado Correctamente")
                    textoAlterTableCompressBD.set("")
                    textoAlterTableCompressTabla.set("")
                    textoAlterTableCompressLevel.set("")
                if x==1:
                    informacion.set("Error al ejecutar AlterTableCompress")
                if x==2:
                    informacion.set("Base de datos no existente")
                if x==3:
                    informacion.set("Tabla no existente")
                if x==4:
                    informacion.set("Level incorrecto")
            except:
                informacion.set("Debe colocar un numero entero en level...")
        else:
            informacion.set("No deje espacios en blanco....")

    def alterTableDecompress():
        if textoAlterTableDecompressBD.get()!="" and textoAlterTableDecompressBD.get()!="":
            x=bp.alterTableDecompress(textoAlterTableDecompressBD.get(), textoAlterTableDecompressBD.get())
            if x==0:
                informacion.set("AlterTableDecompress ejecutado correctamente")
                textoAlterTableDecompressBD.set("")
                textoAlterTableDecompressBD.set("")
            if x==1:
                informacion.set("Error al ejecutar AlterTableDecompress")
            if x==2:
                informacion.set("La base de datos no existe")
            if x==3:
                informacion.set("La tabla no existe")
            if x==4:
                informacion.set("No hay compresion")
        else:
            informacion.set("No deje espacios en blanco...")

    ventana3F2=Toplevel()
    ventana3F2.geometry("1100x700")
    ventana3F2.title="fase2 parte3"

    #label informacion
    informacion=StringVar()
    Label(ventana3F2, text="...", fg="red", textvariable=informacion).pack()

    #CREAR TABLA-------------------------------------
    boton1=Button(ventana3F2, text="Alter Database Compress", bg="#5D6D7E", fg="white",command=alterDatabaseCompress, width="20").place(x=10, y=100)
        
        #textbox BD
    textoBD = StringVar()
    Label(ventana3F2, text="Base de Datos: ").place(x=250, y=85)
    cajaNombreBD= Entry(ventana3F2, textvariable=textoBD, width="35" ).place(x=250, y=5 + 100)

            #textbox MODO
    textoLevel = StringVar()
    Label(ventana3F2, text="Level: ").place(x=500, y=85)
    cajaLevel= Entry(ventana3F2, textvariable=textoLevel, width="35" ).place(x=500, y=5 + 100)

    
        # _________________________________________separador ________________________________________________________
    separador1 = ttk.Separator(ventana3F2, orient='horizontal').place(y=140, relwidth=1.2, relheight=1)

    #def alterTableMode(database: str, table: str, mode: str) -> int:-------------------------------------
    botonAlterDatabaseDecompress=Button(ventana3F2, text="Alter Database Decompress", bg="#34495E", fg="white",command=alterDatabaseDecompress, width="20").place(x=10, y=160)
        
        #textbox BD
    textoAlterDatabaseDecompressBD = StringVar()
    Label(ventana3F2, text="Base de Datos: ").place(x=250, y=160-15)
    cajaAlterDatabaseDecompressBD= Entry(ventana3F2, textvariable=textoAlterDatabaseDecompressBD, width="35" ).place(x=250, y=5 + 160)


    # _________________________________________separador ________________________________________________________
    separador2 = ttk.Separator(ventana3F2, orient='horizontal').place(y=200, relwidth=1.2, relheight=1)
    botonAlterTableCompress=Button(ventana3F2, text="Alter Table Compress", command=alterTableCompress,bg="#2E4053", fg="white", width="20").place(x=10, y=220)

            
    textoAlterTableCompressBD = StringVar()
    Label(ventana3F2, text="Base de Datos: ").place(x=250, y=220-15)
    cajaAlterTableCompressBD= Entry(ventana3F2, textvariable=textoAlterTableCompressBD, width="35" ).place(x=250, y=5 + 220)


    textoAlterTableCompressTabla = StringVar()
    Label(ventana3F2, text="Tabla:").place(x=500, y=220-15)
    cajaAlterTableCompress= Entry(ventana3F2, textvariable=textoAlterTableCompressTabla, width="35" ).place(x=500, y=5 + 220)

    textoAlterTableCompressLevel = StringVar()
    Label(ventana3F2, text="Level:").place(x=750, y=220-15)
    cajaAlterTableCompressLevel= Entry(ventana3F2, textvariable=textoAlterTableCompressLevel, width="35" ).place(x=750, y=5 + 220)

    
    
        # _________________________________________separador ________________________________________________________
    separador7 = ttk.Separator(ventana3F2, orient='horizontal').place(y=260, relwidth=1.2, relheight=1)
    
    botonAlterTableDecompress=Button(ventana3F2, text="Alter Table Decompress", command=alterTableDecompress,bg="#283747", fg="white", width="20").place(x=10, y=280)
    
    textoAlterTableDecompressBD = StringVar()
    Label(ventana3F2, text="Base de Datos: ").place(x=250, y=270)
    cajaAlterTableDecompressBD= Entry(ventana3F2, textvariable=textoAlterTableDecompressBD, width="35" ).place(x=250, y= 290)


    textoAlterTableDecompressTabla = StringVar()
    Label(ventana3F2, text="Tabla: ").place(x=500, y=270)
    cajaAlterTableDecompressTabla= Entry(ventana3F2, textvariable=textoAlterTableDecompressTabla, width="35" ).place(x=500, y=290)

    
    '''
        # _________________________________________separador ________________________________________________________
    separador8 = ttk.Separator(ventana3F2, orient='horizontal').place(y=330, relwidth=1.2, relheight=1)


    botonasafeModeOn=Button(ventana3F2, text="Safe Mode On", command=safeModeOn,bg="#212F3C", fg="white", width="20").place(x=10, y=360)
    

    textoSafeModeOnBD = StringVar()
    Label(ventana3F2, text="Base de Datos: ").place(x=250, y=360-20)
    cajasafeModeOnBD= Entry(ventana3F2, textvariable=textoSafeModeOnBD, width="35" ).place(x=250, y= 360)


    textoSafeModeOnTable = StringVar()
    Label(ventana3F2, text="Tabla: ").place(x=500, y=360-20)
    cajaSafeModeOn= Entry(ventana3F2, textvariable=textoSafeModeOnTable, width="35" ).place(x=500, y=360)

    
    
'''




#-------------FIN VENTANAS-----------------    

#---------------VENTANA PRINCIPAL-------------------
ventana=tk.Tk()
ventana.title("STORAGE MANAGER - GROUP3")
ventana.resizable(0,0) 

#ventana.geometry('1400x780')

#creando el frame para poder colocar cosas dentro
miFrame=Frame()
miFrame.pack()

miFrame.config(width="575", height="400")
miFrame.config(bd=12)
miFrame.config(cursor="plus")

imagen =PhotoImage(file="logoTytus.png")
fondo=Label(miFrame, image=imagen).place(x=100,y=0)


boton1=Button(miFrame, text="BASES DE DATOS", command=ventanaBD,width = 30, bg="#01C3FF", fg="#FFFFFF").place(x=170, y=100+20)
botonFunBD=Button(miFrame, text="FUNCIONES DE BD", command=ventanaFuncionesBD, width = 30, bg="#03A6D7", fg="#FFFFFF").place(x=170, y=125+20)
botonFunTable1=Button(miFrame, text="FUNCIONES DE TABLAS 1", command=ventanaTabla1, width = 30, bg="#0380A6", fg="#FFFFFF").place(x=170, y=150+20)
botonFunTable2=Button(miFrame, text="FUNCIONES DE TABLAS 2", command=ventanaTabla2, width = 30, bg="#005A75", fg="#FFFFFF").place(x=170, y=175+20)
botonFunTuplas=Button(miFrame, text="FUNCIONES DE TUPLAS", command=ventanaTupla, width = 30, bg="#004D64", fg="#FFFFFF").place(x=170, y=200+20)
botonFase21=Button(miFrame, text="FASE 2", command=ventana1Fase2, width = 30, bg="#004D64", fg="#FFFFFF").place(x=170, y=225+20)
botonFase22=Button(miFrame, text="FASE 2+ ", command=ventana2Fase2, width = 30, bg="#004D64", fg="#FFFFFF").place(x=170, y=250+20)
botonFase23=Button(miFrame, text="FASE 2++ ", command=ventana3Fase2, width = 30, bg="#004D64", fg="#FFFFFF").place(x=170, y=275+20)



ventana.mainloop()
#--------------- FIN VENTANA PRINCIPAL-------------------