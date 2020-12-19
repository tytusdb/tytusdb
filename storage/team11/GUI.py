import os 
from tkinter import * 
from tkinter import Menu 
from tkinter import filedialog 
from tkinter import scrolledtext 
from tkinter import messagebox  
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk

contenidoCSV = ""
class GUI: 
    def __init__(self):
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

        #lbl = Label(self.window, text="TYTUS DB", font="Verdana 20 bold")
        #lbl.place(x=5, y=5)

        barraMenu = Menu(self.window)
        self.window.config(menu=barraMenu, width=900, height=700)
        archivoMenu = Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Abrir", command=self.abrirFile)
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir", command=self.salir)
            
        barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
        #self.window.config(menu=barraMenu)
        
        opciones2 = tk.Menu(barraMenu)
        opciones2.add_command(label="def createDatabase(database: str) -> int:")
        opciones2.add_separator()
        opciones2.add_command(label="def showDatabases() -> list:")
        opciones2.add_separator()
        opciones2.add_command(label="def alterDatabase(databaseOld, databaseNew) -> int:")
        opciones2.add_separator()
        opciones2.add_command(label="def dropDatabase(database: str) -> int: ")
        opciones2.add_separator()
        barraMenu.add_cascade(label='Comandos BD', menu=opciones2)


        opciones3 = tk.Menu(barraMenu)
        opciones3.add_command(label="def createTable(database: str, table: str, numberColumns: int) -> int:")
        opciones3.add_separator()
        opciones3.add_command(label="def showTables(database: str) -> list:")
        opciones3.add_separator()
        opciones3.add_command(label="def extractTable(database: str, table: str) -> list:")
        opciones3.add_separator()
        opciones3.add_command(label="def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:")
        opciones3.add_separator()
        opciones3.add_command(label="def alterAddPK(database: str, table: str, columns: list) -> int:")
        opciones3.add_separator()
        opciones3.add_command(label="def alterDropPK(database: str, table: str) -> int:")
        opciones3.add_separator()
        opciones3.add_command(label="def alterAddFK(database: str, table: str, references: dict) -> int:")
        opciones3.add_separator()
        opciones3.add_command(label="def alterAddIndex(database: str, table: str, references: dict) -> int:")
        opciones3.add_separator()
        opciones3.add_command(label="def alterTable(database: str, tableOld: str, tableNew: str) -> int:")
        opciones3.add_separator()
        opciones3.add_command(label="def alterAddColumn(database: str, table: str, default: any) -> int:")
        opciones3.add_separator()
        opciones3.add_command(label="def alterDropColumn(database: str, table: str, columnNumber: int) -> int:")
        opciones3.add_separator()
        opciones3.add_command(label="def dropTable(database: str, table: str) -> int:")
        barraMenu.add_cascade(label='Comandos Tables', menu=opciones3)


        opciones4 = tk.Menu(barraMenu)
        opciones4.add_command(label="def insert(database: str, table: str, register: list) -> int:")
        opciones4.add_separator()
        opciones4.add_command(label="def loadCSV(file: str, database: str, table: str) -> list:")
        opciones4.add_separator()
        opciones4.add_command(label="def extractRow(database: str, table: str, columns: list) -> list:")
        opciones4.add_separator()
        opciones4.add_command(label="def update(database: str, table: str, register: dict, columns: list) -> int:")
        opciones4.add_separator()
        opciones4.add_command(label="def delete(database: str, table: str, columns: list) -> int:")
        opciones4.add_separator()
        opciones4.add_command(label="def truncate(database: str, table: str) -> int:")
        barraMenu.add_cascade(label='Comandos Tuplas', menu=opciones4)
        
        '''BDButton = Button(self.window, text="Bases de Datos", width=25,
                  height=5, font="Verdana 14 bold", command=self.database)

        BDButton.place(x=50, y=51)'''
        
    def Grupo(self):
        # Crear el contenido de cada una de las pestañas.
        
        self.pestaña1 = ttk.Frame(self.pestañas_notebook)
        self.pestaña2 = ttk.Frame(self.pestañas_notebook)
        self.pestaña3 = ttk.Frame(self.pestañas_notebook)
        self.pestaña4 = ttk.Frame(self.pestañas_notebook)
        self.pestaña5 = tk.Frame(self.pestañas_notebook,background="#BED6D2")
        self.pestaña6 = tk.Frame(self.pestañas_notebook,background="#BED6D2")


        self.Grupos = tk.PhotoImage(file="Grupo11.png")
        self.imgDB = tk.PhotoImage(file="db.png")
        self.Team = tk.PhotoImage(file="Equipo.png")
        self.Table = tk.PhotoImage(file="Tablas.png")
        self.Tuple = tk.PhotoImage(file="Tupla.png")
        self.Integrantes = tk.PhotoImage(file="Integrantes.png")
        
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


        #PANEL DE CONTROL DE LA BASES
        self.labelframe3=tk.LabelFrame(self.pestaña2, text="Control DB-TreeAVL:",background="#2EFE2E")        
        self.labelframe3.grid(column=1, row=0, padx=5, pady=10)
        self.label6=tk.Label(self.labelframe3, text="Selecciona La base de datos De la lista:",background="#2EFE2E")
        self.label6.grid(column=1, row=0, padx=5, pady=4)
        self.label7=tk.Label(self.labelframe3, text="Graficar: Visualiza Arbol de Bases de Datos.",background="#2EFE2E")
        self.label7.grid(column=1, row=1, padx=5, pady=4)
        self.boton1=ttk.Button(self.labelframe3, text="Cargar")#,command=self.tabla_bases
        self.boton1.grid(column=2, row=2, padx=4, pady=4)
        self.lista1 = ttk.Combobox(self.labelframe3,width=35)
        self.lista1.grid(column=1, row=2, padx=10, pady=4)
        listaDB = ["1","2"]
        self.lista1['values']=listaDB

        self.boton6=tk.Button(self.pestaña2, text="Explorar Árbol",width=35,background="#2EFE2E")
        self.boton6.grid(column=1, row=1, padx=4, pady=4)

        self.boton8=tk.Button(self.pestaña2, text="Archivo de Entrada",width=35,background="#2EFE2E")
        self.boton8.grid(column=1, row=2, padx=4, pady=4)

        #PANEL DE CONTROL DE LA TABLAS
        #BASES
        self.labelframe6=tk.LabelFrame(self.pestaña3, text="Control DB-TreeAVL:",background="#2EFE2E")        
        self.labelframe6.grid(column=1, row=0, padx=5, pady=10)
        #
        self.label6=tk.Label(self.labelframe6, text="Selecciona La base de datos De la lista:",background="#2EFE2E")
        self.label6.grid(column=1, row=0, padx=5, pady=4)
        self.label7=tk.Label(self.labelframe6, text="Cargar: Carga las tablas de una base de datos",background="#2EFE2E")
        self.label7.grid(column=1, row=1, padx=5, pady=4)
        self.boton1=ttk.Button(self.labelframe6, text="Cargar")#,command=self.tabla_bases
        self.boton1.grid(column=2, row=2, padx=4, pady=4)
        self.lista1 = ttk.Combobox(self.labelframe6,width=35)
        self.lista1.grid(column=1, row=2, padx=10, pady=4)
        listaDB = ["1","2"]
        self.lista1['values']=listaDB

        #Table
        self.labelframe4=tk.LabelFrame(self.pestaña3, text="Control Table-TreeAVL:",background="#F7D358")        
        self.labelframe4.grid(column=1, row=1, padx=5, pady=10)
        #
        self.label8=tk.Label(self.labelframe4, text="Selecciona Una Tabla.",background="#F7D358")
        self.label8.grid(column=1, row=0, padx=5, pady=4)
        self.label9=tk.Label(self.labelframe4, text="Cargar:Carga las tuplas de tabla seleccionada",background="#F7D358")
        self.label9.grid(column=1, row=1, padx=5, pady=4)
        self.boton2=ttk.Button(self.labelframe4, text="Cargar")#,command=self.tabla_tablas
        self.boton2.grid(column=2, row=2, padx=4, pady=4)
        self.lista2 = ttk.Combobox(self.labelframe4,width=35)
        self.lista2.grid(column=1, row=2, padx=10, pady=4)
        listaTabla = ["1","2"]
        self.lista2['values']=listaTabla

        self.boton7=ttk.Button(self.pestaña3, text="Explorar Árbol",width=35)
        self.boton7.grid(column=1, row=2, padx=4, pady=4)

        ## TUPLAS PANEL DE CONTROL
        #DBs
        self.labelframe6=tk.LabelFrame(self.pestaña4, text="Control DB-TreeAVL:",background="#2EFE2E")        
        self.labelframe6.grid(column=1, row=0, padx=5, pady=10)
        #
        self.label6=tk.Label(self.labelframe6, text="Selecciona La base de datos De la lista:",background="#2EFE2E")
        self.label6.grid(column=1, row=0, padx=5, pady=4)
        self.label7=tk.Label(self.labelframe6, text="Cargar: Carga las tablas de una base de datos",background="#2EFE2E")
        self.label7.grid(column=1, row=1, padx=5, pady=4)
        self.boton1=ttk.Button(self.labelframe6, text="Cargar")#,command=self.tabla_bases
        self.boton1.grid(column=2, row=2, padx=4, pady=4)
        self.lista1 = ttk.Combobox(self.labelframe6,width=35)
        self.lista1.grid(column=1, row=2, padx=10, pady=4)
        listaDB = ["1","2"]
        self.lista1['values']=listaDB

        #Table
        self.labelframe4=tk.LabelFrame(self.pestaña4, text="Control Table-TreeAVL:",background="#F7D358")        
        self.labelframe4.grid(column=1, row=1, padx=5, pady=10)
        #
        self.label8=tk.Label(self.labelframe4, text="Selecciona Una Tabla.",background="#F7D358")
        self.label8.grid(column=1, row=0, padx=5, pady=4)
        self.label9=tk.Label(self.labelframe4, text="Cargar:Carga las tuplas de tabla seleccionada",background="#F7D358")
        self.label9.grid(column=1, row=1, padx=5, pady=4)
        self.boton2=ttk.Button(self.labelframe4, text="Cargar")#,command=self.tabla_tablas
        self.boton2.grid(column=2, row=2, padx=4, pady=4)
        self.lista2 = ttk.Combobox(self.labelframe4,width=35)
        self.lista2.grid(column=1, row=2, padx=10, pady=4)
        listaTabla = ["1","2"]
        self.lista2['values']=listaTabla
        
        #Tupla
        self.labelframe5=tk.LabelFrame(self.pestaña4, text="Control Tupla-TreeAVL:",background="#2EFEF7")        
        self.labelframe5.grid(column=1, row=2, padx=5, pady=10)
        #
        self.label10=tk.Label(self.labelframe5, text="Selecciona La base de datos De la lista:",background="#2EFEF7")
        self.label10.grid(column=1, row=0, padx=5, pady=4)
        self.label11=tk.Label(self.labelframe5, text="Graficar: Visualiza las tuplas de una Tabla.",background="#2EFEF7")
        self.label11.grid(column=1, row=1, padx=5, pady=4)
        self.boton3=ttk.Button(self.labelframe5, text="Cargar",command=self.generar_arbol_tupla)
        self.boton3.grid(column=2, row=2, padx=4, pady=4)
        self.lista3 = ttk.Combobox(self.labelframe5,width=35)
        self.lista3.grid(column=1, row=2, padx=10, pady=4)
        listaTupla = ["1","2"]
        self.lista3['values']=listaTupla


        #EXPLORAR Y AGREGAR CSV
        self.boton4= ttk.Button(self.pestaña4, text="Explorar Arbol",width=30,command=self.shown)
        self.boton4.grid(column=1, row=3, padx=4, pady=4)
        self.boton5= ttk.Button(self.pestaña4, text="Agregar por CSV",width=30,command=self.abrirFile)
        self.boton5.grid(column=1, row=4, padx=4, pady=4)
        
    def generar_arbol_tupla(self):
        nombre = 'arbol'
        file = open(nombre+".dot", "w",encoding="utf-8")
        file. write("digraph G { \n")
        file. write("A -> B \n")
        file. write("A -> C \n")
        file. write("B -> D \n")
        file. write("D -> M \n")
        file. write("")
        file. write("}\n")
        file.close()
        from graphviz import render                             
        render('dot', 'png', f'{nombre}.dot')                     
        f'{nombre}.dot.png'
        render('dot', 'jpg', f'{nombre}.dot')                     
        f'{nombre}.dot.jpg'
        import time
        time.sleep(2.4)
        self.archi1=tk.PhotoImage(file=f'{nombre}.dot.png')
        self.canvas2_tupla.create_image(5, 5,image=self.archi1,anchor="nw")
    
    def shown(self):
        self.f = Image.open('arbol.dot.jpg')
        self.f.show()

    def database(self):
        
        #treeFill(self.treeview)
        self.treeview.place(x=950, y=50)
        
        img = Image.open('C:/Users/Carlos/Desktop/graphviz210.png')
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
        img = Image.open('C:/Users/Carlos/Desktop/graphviz'+str(self.treeview.item(item,"text"))+'.png')
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

    def salir(self):
        value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if value:
            self.window.destroy()

    def abrirFile(self):
        global contenidoCSV
        nameFile = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[(
            ("Archivo CSV", ".csv"))])
        if nameFile != '':
            archi1 = open(nameFile, "r")
            contenidoCSV = archi1.read()
            archi1.close()

    def treeFill(treeview):
        '''avl=AVLTree()
    avl.add(1)
    avl.add(210)
    avl.add(13)
    nodos =avl.inorder()
    print(nodos)
    treeview["columns"]=("one")
    treeview.heading("#0", text="Numero",anchor=W)
    
    for nodo in nodos:
        treeview.insert("", tk.END,text=nodo)'''

x=GUI()
x.window.mainloop()

