import ast
from Manager import Manager
import tkinter as Tkinter
import webbrowser
from tkinter import *
from tkinter import Menu 
from tkinter import filedialog 
from tkinter import messagebox  
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk

contenidoCSV = ""
class GUI: 
    def __init__(self):
        self.control = Manager()
        self.window = tk.Tk()
        self.window.title("Proyecto EDD Grupo 11")
        self.window.geometry('1250x650') 
        self.window.configure(bg='#000000')

        self.pestañas_notebook = ttk.Notebook(self.window)
        self.pestañas_notebook.grid(column=0, row=0, padx=15, pady=15)
        self.pestañas_notebook.config(width=1330, height=620)
        
        self.Grupo()

        #1
        self.canvas2_bd=tk.Canvas(self.pestaña2, width=1010, height=700, background="#2EFE2E",scrollregion=(0,0,500,500))        
        self.canvas2_bd.place(x=353,y=10)
        #2
        self.canvas2_tabla=tk.Canvas(self.pestaña3, width=1010, height=700, background="#F7D358",scrollregion=(0,0,500,500))        
        self.canvas2_tabla.place(x=353,y=10)
        #3
        self.canvas2_tupla=tk.Canvas(self.pestaña4, width=1010, height=700, background="#2EFEF7",scrollregion=(0,0,500,500))        
        self.canvas2_tupla.place(x=353,y=10)


        barraMenu = tk.Menu(self.window)
        self.window.config(menu=barraMenu, width=900, height=700)
        archivoMenu = tk.Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Abrir", command=self.abrirFile)
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir", command=self.salir)
        barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
        #self.window.config(menu=barraMenu)

  #########################   MENU  ###########################

        opciones2 = tk.Menu(barraMenu)
        opciones2.add_command(label="def createDatabase(database: str) -> int:",command=self.dialogo_createDatabase)
        opciones2.add_separator()
        opciones2.add_command(label="def showDatabases() -> list:",command=self.dialogo_showDatabase)
        opciones2.add_separator()
        opciones2.add_command(label="def alterDatabase(databaseOld, databaseNew) -> int:",command=self.dialogo_alterDatabase)
        opciones2.add_separator()
        opciones2.add_command(label="def dropDatabase(database: str) -> int: ",command=self.dialogo_dropDatabase)
        opciones2.add_separator()
        barraMenu.add_cascade(label='Comandos BD', menu=opciones2)


        opciones3 = tk.Menu(barraMenu)
        opciones3.add_command(label="def createTable(database: str, table: str, numberColumns: int) -> int:",command=self.dialogo_createTable)
        opciones3.add_separator()
        opciones3.add_command(label="def showTables(database: str) -> list:",command=self.dialogo_showTables)
        opciones3.add_separator()
        opciones3.add_command(label="def extractTable(database: str, table: str) -> list:",command=self.dialogo_extracTable)
        opciones3.add_separator()
        opciones3.add_command(label="def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:",command=self.dialogo_extractRange)
        opciones3.add_separator()
        opciones3.add_command(label="def alterAddPK(database: str, table: str, columns: list) -> int:",command=self.dialogo_alterAddPk)
        opciones3.add_separator()
        opciones3.add_command(label="def alterDropPK(database: str, table: str) -> int:",command=self.dialogo_alterDropPk)
        opciones3.add_separator()
        opciones3.add_command(label="def alterAddFK(database: str, table: str, references: dict) -> int:",command=self.dialogo_alterAddFk)
        opciones3.add_separator()
        opciones3.add_command(label="def alterAddIndex(database: str, table: str, references: dict) -> int:",command=self.dialogo_alterAddIndex)
        opciones3.add_separator()
        opciones3.add_command(label="def alterTable(database: str, tableOld: str, tableNew: str) -> int:",command=self.dialogo_alterTable)
        opciones3.add_separator()
        opciones3.add_command(label="def alterAddColumn(database: str, table: str, default: any) -> int:",command=self.dialogo_alterAddColumn)
        opciones3.add_separator()
        opciones3.add_command(label="def alterDropColumn(database: str, table: str, columnNumber: int) -> int:",command=self.dialogo_alterDropColumn)
        opciones3.add_separator()
        opciones3.add_command(label="def dropTable(database: str, table: str) -> int:",command=self.dialogo_dropTable)
        barraMenu.add_cascade(label='Comandos Tables', menu=opciones3)


        opciones4 = tk.Menu(barraMenu)
        opciones4.add_command(label="def insert(database: str, table: str, register: list) -> int:",command=self.dialogo_insert)
        opciones4.add_separator()
        opciones4.add_command(label="def loadCSV(file: str, database: str, table: str) -> list:",command=self.dialogo_loadCSV)
        opciones4.add_separator()
        opciones4.add_command(label="def extractRow(database: str, table: str, columns: list) -> list:",command=self.dialogo_extractRow)
        opciones4.add_separator()
        opciones4.add_command(label="def update(database: str, table: str, register: dict, columns: list) -> int:",command=self.dialogo_update)
        opciones4.add_separator()
        opciones4.add_command(label="def delete(database: str, table: str, columns: list) -> int:",command=self.dialogo_delete)
        opciones4.add_separator()
        opciones4.add_command(label="def truncate(database: str, table: str) -> int:",command=self.dialogo_truncate)
        barraMenu.add_cascade(label='Comandos Tuplas', menu=opciones4)

    def Grupo(self):

        # Crear el contenido de cada una de las pestañas.
        self.pestaña1 = ttk.Frame(self.pestañas_notebook)
        self.pestaña2 = ttk.Frame(self.pestañas_notebook)
        self.pestaña3 = ttk.Frame(self.pestañas_notebook)
        self.pestaña4 = ttk.Frame(self.pestañas_notebook)
        self.pestaña5 = tk.Frame(self.pestañas_notebook,background="#BED6D2")
        self.pestaña6 = tk.Frame(self.pestañas_notebook,background="#BED6D2")

        self.Grupos = tk.PhotoImage(file="./image/Grupo11.png")
        self.imgDB = tk.PhotoImage(file="./image/db.png")
        self.Team = tk.PhotoImage(file="./image/Equipo.png")
        self.Table = tk.PhotoImage(file="./image/Tablas.png")
        self.Tuple = tk.PhotoImage(file="./image/Tupla.png")
        self.Integrantes = tk.PhotoImage(file="./image/Integrantes.png")
        
        # Añadirlas al panel con su respectivo texto.
        self.pestañas_notebook.add(self.pestaña1, text="    GRUPO 11    ",image=self.Team,underline=4,compound=tk.LEFT, padding=20)
        self.pestañas_notebook.add(self.pestaña2, text="    DB-TREE AVL    ",image=self.imgDB,underline=4,compound=tk.LEFT, padding=20)
        self.pestañas_notebook.add(self.pestaña3, text="    TABLA-TREE AVL    ",image=self.Table,underline=4,compound=tk.LEFT, padding=20)
        self.pestañas_notebook.add(self.pestaña4, text="    TUPLA-TREE AVL    ",image=self.Tuple,underline=4,compound=tk.LEFT, padding=20)
        self.pestañas_notebook.add(self.pestaña5, text="    Manual ténico    ",underline=4,compound=tk.LEFT, padding=20)
        self.pestañas_notebook.add(self.pestaña6, text="    Manual usuario    ",underline=4,compound=tk.LEFT, padding=20)

        
        self.labelframe1=ttk.LabelFrame(self.pestaña1, text="Grupo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=5)
        self.label1=ttk.Label(self.labelframe1,image=self.Grupos)
        self.label1.grid(column=0, row=0, padx=4, pady=4)


        self.labelframeInt=ttk.LabelFrame(self.pestaña1, text="INTEGRANTES:")        
        self.labelframeInt.grid(column=1, row=0, padx=5, pady=5)
        self.labelInt=ttk.Label(self.labelframe1,image=self.Integrantes)
        self.labelInt.grid(column=1, row=0, padx=4, pady=4)


        #PANEL DE CONTROL DE BASES
        self.labelframe3=tk.LabelFrame(self.pestaña2, text="Control DB-TreeAVL:",background="#2EFE2E")        
        self.labelframe3.grid(column=1, row=0, padx=5, pady=10)
        self.Label1b=tk.Label(self.labelframe3, text="Selecciona La base de datos De la lista:",background="#2EFE2E")
        self.Label1b.grid(column=1, row=0, padx=5, pady=4)
        self.Label2b=tk.Label(self.labelframe3, text="Graficar: Visualiza Arbol de Bases de Datos.",background="#2EFE2E")
        self.Label2b.grid(column=1, row=1, padx=5, pady=4)
        self.lista1b = ttk.Combobox(self.labelframe3,width=35)
        self.lista1b.grid(column=1, row=2, padx=10, pady=4)
        self.boton0b=ttk.Button(self.labelframe3, text="Refresh",command=self.actualizardbs)#
        self.boton0b.grid(column=2, row=0, padx=4, pady=4)
        self.boton1b=ttk.Button(self.labelframe3, text="Revisar",command=self.tabla_bases)#
        self.boton1b.grid(column=2, row=2, padx=4, pady=4)

        self.lista1b['values']=self.control.showDatabases()
        self.boton2b=ttk.Button(self.pestaña2, text="Explorar Árbol",width=35,command=self.shown1)
        self.boton2b.grid(column=1, row=1, padx=4, pady=4)
        self.boton3b=tk.Button(self.pestaña2, text="Archivo de Entrada",width=35,background="#2EFE2E")
        self.boton3b.grid(column=1, row=2, padx=4, pady=4)


        #PANEL DE CONTROL DE LA TABLAS
        #BASES
        self.labelframe6=tk.LabelFrame(self.pestaña3, text="Control DB-TreeAVL:",background="#2EFE2E")        
        self.labelframe6.grid(column=1, row=0, padx=5, pady=10)
        #
        self.label1c=tk.Label(self.labelframe6, text="Selecciona La base de datos De la lista:",background="#2EFE2E")
        self.label1c.grid(column=1, row=0, padx=5, pady=4)
        self.label2c=tk.Label(self.labelframe6, text="Cargar: Carga las tablas de una base de datos",background="#2EFE2E")
        self.label2c.grid(column=1, row=1, padx=5, pady=4)
        self.datobd1c = tk.StringVar()
        self.lista1c = ttk.Combobox(self.labelframe6,width=35,textvariable=self.datobd1c)
        self.lista1c.grid(column=1, row=2, padx=10, pady=4)

        self.lista1c['values']=self.control.showDatabases()
        self.boton1c=ttk.Button(self.labelframe6, text="Refresh",command=self.actualizardbs2)#,command=self.tabla_bases
        self.boton1c.grid(column=2, row=0, padx=4, pady=4)
        self.boton2c=ttk.Button(self.labelframe6, text="Cargar",command=self.obtener_tablasc)#,command=self.tabla_bases
        self.boton2c.grid(column=2, row=2, padx=4, pady=4)

        #Tablas
        self.labelframe4=tk.LabelFrame(self.pestaña3, text="Control Table-TreeAVL:",background="#F7D358")        
        self.labelframe4.grid(column=1, row=1, padx=5, pady=10)
        #
        self.label3c=tk.Label(self.labelframe4, text="Selecciona Una Tabla.",background="#F7D358")
        self.label3c.grid(column=1, row=0, padx=5, pady=4)
        self.label4c=tk.Label(self.labelframe4, text="Cargar:Carga las tuplas de tabla seleccionada",background="#F7D358")
        self.label4c.grid(column=1, row=1, padx=5, pady=4)
        self.lista2c = ttk.Combobox(self.labelframe4,width=35)
        self.lista2c.grid(column=1, row=2, padx=10, pady=4)
        #
        self.boton3c=ttk.Button(self.labelframe4, text="Ver",command=self.tabla_tablas)#,command=self.tabla_tablas
        self.boton3c.grid(column=2, row=2, padx=4, pady=4)
        self.boton4c=ttk.Button(self.pestaña3, text="Explorar Árbol",width=35,command=self.shown2)
        self.boton4c.grid(column=1, row=2, padx=4, pady=4)


        ## PANEL DE CONTROL DE TUPLAS##
        #DBS
        self.labelframe6=tk.LabelFrame(self.pestaña4, text="Control DB-TreeAVL:",background="#2EFE2E")        
        self.labelframe6.grid(column=1, row=0, padx=5, pady=10)
        #
        self.label1d=tk.Label(self.labelframe6, text="Selecciona La base de datos De la lista:",background="#2EFE2E")
        self.label1d.grid(column=1, row=0, padx=5, pady=4)
        self.label2d=tk.Label(self.labelframe6, text="Cargar: Carga las tablas de una base de datos",background="#2EFE2E")
        self.label2d.grid(column=1, row=1, padx=5, pady=4)
        self.datobd2d = tk.StringVar()
        self.lista1d = ttk.Combobox(self.labelframe6,width=35,textvariable=self.datobd2d)
        self.lista1d.grid(column=1, row=2, padx=10, pady=4)
        
        self.lista1d['values']= self.control.showDatabases()
        self.boton1d=ttk.Button(self.labelframe6, text="Refresh",command=self.actualizardbs3)#,command=self.tabla_bases
        self.boton1d.grid(column=2, row=0, padx=4, pady=4)
        self.boton2d=ttk.Button(self.labelframe6, text="Cargar",command=self.obtener_tablasd)#,command=self.tabla_bases
        self.boton2d.grid(column=2, row=2, padx=4, pady=4)

        #Tabla
        self.labelframe4=tk.LabelFrame(self.pestaña4, text="Control Table-TreeAVL:",background="#F7D358")        
        self.labelframe4.grid(column=1, row=1, padx=5, pady=10)
        #
        self.label3d=tk.Label(self.labelframe4, text="Selecciona Una Tabla.",background="#F7D358")
        self.label3d.grid(column=1, row=0, padx=5, pady=4)
        self.label4d=tk.Label(self.labelframe4, text="Cargar:Carga las tuplas de tabla seleccionada",background="#F7D358")
        self.label4d.grid(column=1, row=1, padx=5, pady=4)
        self.datotablad = StringVar()
        self.lista2d = ttk.Combobox(self.labelframe4,width=35,textvariable=self.datotablad)
        self.lista2d.grid(column=1, row=2, padx=10, pady=4)

        self.boton3d=ttk.Button(self.labelframe4, text="Cargar",command=self.obtener_tuplasd)#,command=self.tabla_tablas
        self.boton3d.grid(column=2, row=2, padx=4, pady=4)
        

        #Tupla
        self.labelframe5=tk.LabelFrame(self.pestaña4, text="Control Tupla-TreeAVL:",background="#2EFEF7")        
        self.labelframe5.grid(column=1, row=2, padx=5, pady=10)
        #
        self.label5d=tk.Label(self.labelframe5, text="Selecciona La base de datos De la lista:",background="#2EFEF7")
        self.label5d.grid(column=1, row=0, padx=5, pady=4)
        self.label6d=tk.Label(self.labelframe5, text="Graficar: Visualiza las tuplas de una Tabla.",background="#2EFEF7")
        self.label6d.grid(column=1, row=1, padx=5, pady=4)
        self.lista3d = ttk.Combobox(self.labelframe5,width=35)
        self.lista3d.grid(column=1, row=2, padx=10, pady=4)

        self.boton4d=ttk.Button(self.labelframe5, text="Ver",command=self.tabla_tuplas)
        self.boton4d.grid(column=2, row=2, padx=4, pady=4)


        #EXPLORAR Y AGREGAR CSV
        self.boton4= ttk.Button(self.pestaña4, text="Explorar Arbol",width=30,command=self.shown3)
        self.boton4.grid(column=1, row=3, padx=4, pady=4)
        self.boton5= ttk.Button(self.pestaña4, text="Agregar por CSV",width=30,command=self.abrirFile)
        self.boton5.grid(column=1, row=4, padx=4, pady=4)

     # SE ACTUALIZAN LOS VALORES DE LAS LISTAS
    def actualizardbs(self):
        self.lista1b['values']=self.control.showDatabases()

    def actualizardbs2(self):
        self.lista1c['values']=self.control.showDatabases()
    
    def obtener_tablasc(self):
        self.lista2c['values']=self.control.showTables(str(self.datobd1c.get()))
    
    def actualizardbs3(self):
        self.lista1d['values']=self.control.showDatabases()

    def obtener_tablasd(self):
        self.lista2d['values']=self.control.showTables(str(self.datobd2d.get()))
    
    def obtener_tuplasd(self):
        self.lista3d['values']=self.control.extractTable(str(self.datobd2d.get()),str(self.datotablad.get()))


## MUESTRA LAS TABLAS
    def tabla_bases(self):
        self.generar_arbol_bd()
        self.dialogo1 = vdialogo(self.window,"modo1",None,None)
        
    def tabla_tablas(self):
        self.generar_arbol_tb()
        self.dialogo1 = vdialogo(self.window,"modo2",self.datobd1c.get(),None)

    def tabla_tuplas(self):
        self.generar_arbol_tp()
        self.dialogo1 = vdialogo(self.window,"modo3",str(self.datobd2d.get()),str(self.datotablad.get()))


## GENERA LOS TRES ARBOLES AVL
    def generar_arbol_bd(self):
        nombre = 'arboldb'
        file = open(nombre+".dot", "w",encoding="utf-8")
        file. write(str(self.control.graficarDB()))
        file.close()
        from graphviz import render                             
        render('dot', 'png', f'{nombre}.dot')                     
        f'{nombre}.dot.png'
        render('dot', 'svg', f'{nombre}.dot')                     
        f'{nombre}.dot.svg'
        import time
        time.sleep(2.0)
        self.archi1=tk.PhotoImage(file=f'{nombre}.dot.png')
        self.canvas2_bd.create_image(5, 5,image=self.archi1,anchor="nw")

    def generar_arbol_tb(self):
        nombre = 'arboltb'
        file = open(nombre+".dot", "w",encoding="utf-8")
        file. write(str(self.control.graficarTabla(str(self.datobd1c.get()))))
        file.close()
        from graphviz import render                             
        render('dot', 'png', f'{nombre}.dot')                     
        f'{nombre}.dot.png'
        render('dot', 'svg', f'{nombre}.dot')                     
        f'{nombre}.dot.svg'
        import time
        time.sleep(2.0)
        self.archi2=tk.PhotoImage(file=f'{nombre}.dot.png')
        self.canvas2_tabla.create_image(5, 5,image=self.archi2,anchor="nw")

    def generar_arbol_tp(self):
        nombre = 'arboltpl'
        file = open(nombre+".dot", "w",encoding="utf-8")
        file. write(str(self.control.graficarRegistros(str(self.datobd2d.get()),str(self.datotablad.get()))))
        file.close()
        from graphviz import render                             
        render('dot', 'png', f'{nombre}.dot')                     
        f'{nombre}.dot.png'
        render('dot', 'svg', f'{nombre}.dot')                     
        f'{nombre}.dot.svg'
        import time
        time.sleep(2.0)
        self.archi3=tk.PhotoImage(file=f'{nombre}.dot.png')
        self.canvas2_tupla.create_image(5, 5,image=self.archi3,anchor="nw")

## SHOW DE SVG EN NAVEGADOR
    def shown1(self):
        webbrowser.open("arboldb.dot.svg")
        #self.f = Image.open('arbol.dot.svg')
        #self.f.show()
    
    def shown2(self):
        webbrowser.open("arboltb.dot.svg")

    def shown3(self):
        webbrowser.open("arboltpl.dot.svg")
        
    def database(self):    
        #treeFill(self.treeview)
        self.treeview.place(x=950, y=50)
        img = Image.open('C:/Users/HP/Desktop/MIT2.png')
        # print('GGGG')
        pimg = ImageTk.PhotoImage(img)
        size = img.size 
        frame=Frame(self.window,width=300,height=300)
        frame.pack(fill=BOTH) #.grid(row=0,column=0)
        frame.place(x=25,y=25)   
        canvaX=Canvas(frame,bg='#FFFFFF',scrollregion=(0,0,size[0],size[1]))
        self.canva = canvaX
        hbar=Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command= self.canva.xview)
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command= self.canva.yview)

        self.canva.config(width=850,height=450)
        self.canva.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
            
        self.canva.create_image(0,0,anchor='nw',image=pimg)
        self.canva.pack(side=LEFT)    
        self.treeview.bind("<Double-1>", self.OnDoubleClick)
       #self.window.mainloop()
    
    def OnDoubleClick(self,event):
       
        item = self.treeview.selection()[0]                
        img = Image.open('C:/Users/HP/Desktop/MIT2'+str(self.treeview.item(item,"text"))+'.png')
        pimg = ImageTk.PhotoImage(img)
        size = img.size
        
        frame=Frame(self.window,width=300,height=300)
        frame.pack(fill=BOTH)
        frame.place(x=25,y=25)
        canvaX=Canvas(frame,bg='#FFFFFF',scrollregion=(0,0,size[0],size[1]))
        self.canva=canvaX
        hbar=Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command= self.canva.xview)
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command= self.canva.yview)
        
        self.canva.config(width=850,height=450)
        self.canva.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canva.pack(side=LEFT)       
        self.canva.create_image(0,0,anchor='nw',image=pimg)     
        #self.canva.mainloop()

        #CULMINA LA VENTANA DIALOGO
    def salir(self):
        value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if value:
            self.window.destroy()
            
        # RECUPERA UNA RUTA PARA CSV
    def abrirFile(self):
        global contenidoCSV
        nameFile = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[(
            ("Archivo CSV", ".csv"))])
        if nameFile != '':
            self.control.loadCSV(nameFile,str(self.datobd2d.get()),str(self.datotablad.get()))

            ############################### COMANDOS #############################################

    def dialogo_createDatabase(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def createDatabase (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.createDatabase)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def createDatabase(self):
        s=self.control.createDatabase(str(self.datos.get()))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def dialogo_showDatabase(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def showDatabase ()", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=0, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)

        self.lis = ttk.Combobox(self.labelframeInt,width=35)
        self.lis.grid(column=1, row=0, padx=10, pady=4)
        self.lis['values'] = self.control.showDatabases()

        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def showDatabase(self):
        None
        
    def dialogo_alterDatabase(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def alterDatabase (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.alterDatabase)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def alterDatabase(self):
        nombres = self.datos.get().split(",")
        s=self.control.alterDatabase(str(nombres[0]),str(nombres[1]))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def dialogo_dropDatabase(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def dropDatabase (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.dropDatabase)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def dropDatabase(self):
        s=self.control.dropDatabase(str(self.datos.get()))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)



    def dialogo_createTable(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def createTable (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.crearTable)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def crearTable(self):
        cadena = self.datos.get().split(",")
        s= self.control.createTable(str(cadena[0]),str(cadena[1]),int(cadena[2]))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorno: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    
    def dialogo_showTables(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def showTables (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.showTables)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def showTables(self):
        self.lis = ttk.Combobox(self.labelframeInt,width=35)
        self.lis.grid(column=1, row=0, padx=10, pady=4)
        self.lis['values'] = self.control.showTables(str(self.datos.get()))


    def dialogo_extracTable(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def extractTable (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.extracTable)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def extracTable(self):
        cadena = self.datos.get().split(",")
        self.lis = ttk.Combobox(self.labelframeInt,width=35)
        self.lis.grid(column=1, row=0, padx=10, pady=4)
        self.lis['values'] = self.control.extractTable(str(cadena[0]),str(cadena[1]))
            
    
    def dialogo_extractRange(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def extracRangeTable (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.extractRange)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def extractRange(self):
        cadena = self.datos.get().split(",")
        self.lis = ttk.Combobox(self.labelframeInt,width=35)
        self.lis.grid(column=1, row=0, padx=10, pady=4)
        extract = cadena[3]
        range = cadena[4]
        self.lis['values'] = self.control.extractRangeTable(str(cadena[0]),str(cadena[1]),int(cadena[2]),ast.literal_eval(f'{extract}'),ast.literal_eval(f'{range}'))
        

    def dialogo_alterAddPk(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def alterAddPk (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.alterAddPk)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def alterAddPk(self):
        cadena = self.datos.get().split(",",2)
        alter = cadena[2]
        s= self.control.alterAddPK(str(cadena[0]),str(cadena[1]),ast.literal_eval(f'{alter}'))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)
    
    def dialogo_alterDropPk(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def alterDropPk (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.alterDropPk)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def alterDropPk(self):
        cadena= self.datos.get().split(",")
        s=self.control.alterDropPK(str(cadena[0]),str(cadena[1]))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def dialogo_alterAddFk(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def alterAddFk (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.alterAddFk)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def alterAddFk(self): # pendiente
        cadena = self.datos.get().split(",",2)
        alterA = cadena[2]
        s=self.control.alterAddPK(str(cadena[0]),str(cadena[1]),ast.literal_eval(f'{alterA}'))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def dialogo_alterAddIndex(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def alterAddIndex (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.alterAddIndex)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def alterAddIndex(self): #pendiente
        None
        #cadena = self.datos.get().split(",")
        #s=self.control.alterAddIndex(str(cadena[0]),str(cadena[1]),str(cadena[2]))
        #self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        #self.labelInt.grid(column=1, row=0, padx=8, pady=8)
    
    def dialogo_alterTable(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def añterTable (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.alterTable)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def alterTable(self):
        cadena = self.datos.get().split(",")
        s=self.control.alterTable(str(cadena[0]),str(cadena[1]),str(cadena[2]))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def dialogo_alterAddColumn(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def alterAddColumn (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.alterAddColumn)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def alterAddColumn(self):
        cadena = self.datos.get().split(",",2)
        parametro = cadena[2]
        s = self.control.alterAddColumn(str(cadena[0]),str(cadena[1]),ast.literal_eval(f'{parametro}'))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def dialogo_alterDropColumn(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def alterDropColumn (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.alterDropColumn)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def alterDropColumn(self):
        cadena = self.datos.get().split(",")
        s=self.control.alterDropColumn(str(cadena[0]),str(cadena[1]),int(cadena[2]))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)
        

    def dialogo_dropTable(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def dropTable (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.dropTable)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def dropTable(self):
        cadena=self.datos.get().split(",")
        s=self.control.dropTable(str(cadena[0]),str(cadena[1]))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)


    def dialogo_insert(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def insert (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.insert)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def insert(self):
        cadena = self.datos.get().split(",",2)
        insert = cadena[2]
        s= self.control.insert(str(cadena[0]),str(cadena[1]),ast.literal_eval(f'{insert}'))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def dialogo_loadCSV(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def loadCSV (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.loadCSV)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def loadCSV(self):
        cadena = self.datos.get().split(",")
        self.lis = ttk.Combobox(self.labelframeInt,width=35)
        self.lis.grid(column=1, row=0, padx=10, pady=4)
        self.lis['values'] = self.control.loadCSV(str(cadena[0]),str(cadena[1]),str(cadena[2]))

    def dialogo_extractRow(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def extractRow (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.extractRow)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def extractRow(self):
        cadena = self.datos.get().split(",",2)
        self.lis = ttk.Combobox(self.labelframeInt,width=35)
        self.lis.grid(column=1, row=0, padx=10, pady=4)
        extract = cadena[2]
        self.lis['values'] = self.control.extractRow(str(cadena[0]),str(cadena[1]),ast.literal_eval(f'{extract}'))

    def dialogo_update(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def update (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.update)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def update(self):
        cadena = self.datos.get().split(",",2)
        cadena2 = cadena[2].split("},")
        update = cadena2[0]+"}"
        update2 = cadena2[1]
        s= self.control.update(str(cadena[0]),str(cadena[1]),ast.literal_eval(f'{update}'),ast.literal_eval(f'{update2}'))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def dialogo_delete(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def delete (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.delete)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def delete(self):
        cadena = self.datos.get().split(",",2)
        delete = cadena[2]
        s= self.control.delete(str(cadena[0]),str(cadena[1]),ast.literal_eval(f'{delete}'))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)
        

    def dialogo_truncate(self):
        self.dialogo=tk.Toplevel(self.window)
        self.label1=ttk.Label(self.dialogo, text="def truncate (", font=("Arial Black", 12))
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.dialogo, text=")", font=("Arial Black", 12))
        self.label2.grid(column=2, row=0, padx=5, pady=5)
        self.datos=tk.StringVar()
        self.entrada1=ttk.Entry(self.dialogo, textvariable=self.datos)
        self.entrada1.grid(column=1, row=0, padx=8, pady=8)
        self.entrada1.focus()
        self.boton1=ttk.Button(self.dialogo, text="Confirmar",command=self.truncate)#
        self.boton1.grid(column=1, row=2, padx=8, pady=8)
        self.boton2=ttk.Button(self.dialogo, text="Salir",command=self.cerrar)#
        self.boton2.grid(column=1, row=3, padx=8, pady=8)
        self.labelframeInt=ttk.LabelFrame(self.dialogo, text="Mensaje:")        
        self.labelframeInt.grid(column=0, row=2, padx=8, pady=8)
        self.dialogo.resizable(0,0)
        self.dialogo.grab_set()

    def truncate(self):
        cadena = self.datos.get().split(",")
        s=self.control.truncate(str(cadena[0]),str(cadena[1]))
        self.labelInt=ttk.Label(self.labelframeInt,text=f" retorna: {s}",width=35)
        self.labelInt.grid(column=1, row=0, padx=8, pady=8)

    def cerrar(self):
        self.dialogo.destroy()

# CREA LA VENTANA  CON LAS TABLAS  
class vdialogo:    
    def __init__(self, ventanaprincipal,modo,nombredb,nombretabla):
        self.mostrar = Manager()
        columnas=None
        c=None
        if modo == "modo1":
            columnas =  self.mostrar.showDatabases()
            c="#2EFE2E"
        elif modo == "modo2":
            columnas =  self.mostrar.showTables(str(nombredb))
            c="#F7D358"
        elif modo == "modo3":
            columnas =  self.mostrar.extractTable(str(nombredb),str(nombretabla))
            c="#2EFEF7"
        else:
            None
        
        root = Tkinter.Tk()
        frame = Tkinter.Frame(root, background=f"{c}", borderwidth = 5)
        frame.pack(side=Tkinter.TOP, expand=1, fill=Tkinter.BOTH)
        self.generar_treeview(frame, columnas) 

        root.geometry("600x300")
        root.wm_title("Tabla")
        root.mainloop()

    def generar_treeview(self,frame, tuplas):
        tree=ttk.Treeview(frame, style="Treeview",height=10)
        vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
        vsb.configure(command=tree.yview)
        vsb.pack(side='right', fill='y')
        tree.configure(yscrollcommand=vsb.set)
        hsb = ttk.Scrollbar(tree, orient="horizontal", command=tree.xview)
        hsb.configure(command=tree.xview)
        hsb.pack(side='bottom', fill='x')
        tree.configure(xscrollcommand=hsb.set)
        tree["columns"]=tuplas[0]

        ii=1
        for i in tuplas:
            tree.insert("", ii, ii, text=str(ii), values=i)
            ii+=1
        
        tree["show"] = ["headings"]        
        tree.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=TRUE)

    def mostrar(self):
        None
        #self.dialogo.wait_window()

    def confirmar(self):
        None

x=GUI()
x.window.mainloop()
