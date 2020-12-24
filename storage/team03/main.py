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


