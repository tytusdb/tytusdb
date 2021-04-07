from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import json
import Table
from tkinter import filedialog
import ISAMMode as Storage
from DataBase import DataBase
from Table import Table
import os
import pickle
#--------------------------------------------------opciones de las bases de datos-------------------------------------------------
class PantallaBD():
    def __init__(self,vectorBases):
        self.ventana = Tk()
        self.vectorBases=vectorBases
        self.ventana.title("Opciones Bases de Datos")
        self.contenedor = Frame(self.ventana, width=500, height=400)
        self.contenedor.pack(fill="both", expand=True)
        self.titulo=Label(self.contenedor, text="Bases de Datos", font=("Comic Sans MS", 18)).place(x=150, y=20)
        # botones crear eliminar y editar bases de datos
        self.BtnCrearBase = Button(self.contenedor, text="Crear Base de Datos", command=self.crear, width=20).place(x=300, y=100)
        self.BtnEliminarBase = Button(self.contenedor, text="Eliminar Base de Datos", command=self.EliminarBase, width=20).place(x=300, y=160)
        self.BtnEditarBase = Button(self.contenedor, text="Editar Nombre de BD", command=self.EditarBase, width=20).place(x=300, y=220)
        self.BtnTablas = Button(self.contenedor, text="Ver Tablas", command=self.Tablas,width=20).place(x=300, y=280)
        self.BtnGraficar = Button(self.contenedor, text="Graficar Tablas", command=self.graficar, width=20).place(x=300, y=340)

        self.listboxBases = Listbox(self.contenedor, width=40, height=18)
        self.CargarBases()
        self.listboxBases.place(x=35, y=80)

        self.ventana.mainloop()


#eliminar elemento del listbox y de el arreglo de bases de datos
    def EliminarBase(self):
        if len(self.listboxBases.curselection()) != 0:
            elemento=self.listboxBases.get(self.listboxBases.curselection()[0])
            a=messagebox.askquestion("Eliminar","Quieres eliminar La base de datos \n\t"+elemento)
            if a=="yes":
                self.listboxBases.delete(self.listboxBases.curselection())
                indice=0
                for i in range(0,len(self.vectorBases)):
                    if self.vectorBases[i]==elemento:
                        indice=i
                print(Storage.dropDatabase(elemento))

#cambiar nombre de la base de datos
    def EditarBase(self):
        if len(self.listboxBases.curselection()) != 0:
            elemento=self.listboxBases.get(self.listboxBases.curselection()[0])
            self.ventana.destroy()
            PantallaEditarBD(elemento)


#cargar los elementos del arreglo de bases de datos
    def CargarBases(self):
        for i in range(0,len(self.vectorBases)):
            self.listboxBases.insert(i,self.vectorBases[i])
#llamando crear
    def crear(self):
        self.ventana.destroy()
        PantallaCrearBD()
#para visualizar las tablas
    def Tablas(self):
        if len(self.listboxBases.curselection()) != 0:
            nombreBD = self.listboxBases.get(self.listboxBases.curselection()[0])
            self.ventana.destroy()
            #hay que mandar el vector de tablas
            PantallaTablas(nombreBD)
    def graficar(self):
        if len(self.listboxBases.curselection()) != 0:
            nombreBD = self.listboxBases.get(self.listboxBases.curselection()[0])
            self.ventana.destroy()
            PantallaGraficoTablas(nombreBD)

class PantallaCrearBD:
    def __init__(self):
        self.ventana = Tk()
        self.val = StringVar()
        self.ventana.geometry('300x130')
        self.ventana.title('Crear BD')
        self.titulo = Label(self.ventana, text="Ingrese el nombre de la BD", font=("Comic Sans MS", 15)).place(x=20, y=5)
        self.Entrada = Entry(self.ventana, textvariable=self.val, width=40).place(x=20, y=40)
        self.Boton = Button(self.ventana, text='CREAR', command=self.llamar(), width=15).place(x=80, y=70)
        self.ventana.mainloop()

    def llamar(self):
        return lambda: self._llamar()

    def _llamar(self):
        # para crear la base de datos valv es el nombre
        valv = str(self.val.get())
        print(Storage.createDatabase(valv))
        self.ventana.destroy()
        PantallaBD(Storage.showDatabases())

class PantallaEditarBD:
    def __init__(self, nombreViejo):
        self.nombreViejo=nombreViejo
        self.ventana = Tk()
        self.val = StringVar()
        self.ventana.geometry('300x130')
        self.ventana.title('Editar BD')
        self.titulo = Label(self.ventana, text="Ingrese el nuevo nombre de la BD", font=("Comic Sans MS", 15)).place(x=15, y=5)

        self.Entrada = Entry(self.ventana, textvariable=self.val, width=40).place(x=20, y=40)
        self.Boton = Button(self.ventana, text='EDITAR', command=self.llamar(), width=15).place(x=80, y=70)
        self.ventana.mainloop()

    def llamar(self):
        return lambda: self._llamar()

    def _llamar(self):
        nombreNuevo = str(self.val.get())
        print(Storage.alterDatabase(self.nombreViejo,nombreNuevo))

        self.ventana.destroy()
        PantallaBD(Storage.showDatabases())


# ------------------------------------------------------graficas de tablas--------------------------------
class PantallaGraficoTablas:
    def __init__(self, nombreBD):
        self.ventana = Tk()
        self.nombreBD = nombreBD
        # obteniendo grafico de la tabla indicada
        Storage.checkDirs()
        Storage.chartList(Storage.showTables(self.nombreBD))
        self.ventana.title("BD "+self.nombreBD)
        self.ventana.geometry("450x300")

        self.contenedor = Frame(self.ventana)
        self.contenedor.pack(fill="both", expand=True)
        self.canvas = Canvas(self.contenedor)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.scroll = ttk.Scrollbar(self.contenedor, orient=VERTICAL, command=self.canvas.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.segundocontenedor = Frame(self.canvas, width=300, height=300)
        self.canvas.create_window((0, 0), window=self.segundocontenedor, anchor="nw")
        imagen = PhotoImage(file="list.png")
        labelimagen = Label(self.segundocontenedor, image=imagen).pack()

        Button(self.segundocontenedor, text="Salir", command=self.salir, width=20).pack()
        self.ventana.mainloop()

    def salir(self):
        self.ventana.destroy()
        PantallaBD(Storage.showDatabases())

#--------------------------------------------------------opciones de las tablas-----------------------------------------------

class PantallaTablas:
    def __init__(self, nombreBD):
        self.ventana = Tk()
        self.nombreBD=nombreBD
        self.ventana.title("Opciones de las tablas")
        self.contenedor = Frame(self.ventana, width=500, height=400)
        self.contenedor.pack(fill="both", expand=True)
        self.titulo = Label(self.contenedor, text="Tablas de la BD: "+nombreBD, font=("Comic Sans MS", 18)).place(x=110, y=20)
        # boton crear tabla
        Button(self.contenedor, text="Crear Tabla de Datos", command=self.crear, width=20).place(x=300, y=80)
        Button(self.contenedor, text="Borrar Tabla", command=self.borrar, width=20).place(x=300, y=110)
        Button(self.contenedor, text="Cambiar nombre", command=self.renombrar, width=20).place(x=300,y=140)
        Button(self.contenedor, text="Agregar Columna", command=self.agregarC, width=20).place(x=300, y=170)
        Button(self.contenedor, text="Eliminar Columna", command=self.borrarC, width=20).place(x=300, y=200)
        Button(self.contenedor, text="Agregar PK", command=self.agregarPK, width=20).place(x=300, y=230)
        Button(self.contenedor, text="Eliminar PK", command=self.eliminarPK, width=20).place(x=300, y=260)
        Button(self.contenedor, text="Ver Tabla", command=self.extraerTabla, width=20).place(x=300, y=290)
        Button(self.contenedor, text="Graficar", command=self.graficar, width=20).place(x=300, y=320)
        Button(self.contenedor, text="Regresar", command=self.salir, width=20).place(x=300, y=350)

        self.listboxTablas= Listbox(self.contenedor, width=40, height=18)
        self.Cargartablas()
        self.listboxTablas.place(x=35, y=80)

        self.ventana.mainloop()

    # cargar los elementos del arreglo de tablas
    def Cargartablas(self):
        for i in range(0, len(Storage.showTables(self.nombreBD))):
            self.listboxTablas.insert(i, Storage.showTables(self.nombreBD)[i])
    def crear(self):
        try:
            nombretabla=simpledialog.askstring('Crear Tabla Datos','ingrese el nombre de la tabla')
            cantcolumnas=simpledialog.askinteger('Crear Tabla Datos', 'ingrese el numero de columnas que desea')
            print(Storage.createTable(self.nombreBD,nombretabla,cantcolumnas))
            self.listboxTablas.delete(0, END)
            self.Cargartablas()
        except:
            ""

    def borrar(self):
        try:
            if len(self.listboxTablas.curselection()) != 0:
                elemento = self.listboxTablas.get(self.listboxTablas.curselection()[0])
                a = messagebox.askquestion("Eliminar", "Quieres eliminar La tabla \n\t" + elemento)
                if a == "yes":
                    print(Storage.dropTable(self.nombreBD, elemento))
                    self.listboxTablas.delete(0, END)
                    self.Cargartablas()
        except:
            ""
    def renombrar(self):
        try:
            if len(self.listboxTablas.curselection()) != 0:
                nombreviejo = self.listboxTablas.get(self.listboxTablas.curselection()[0])
                nombrenuevo=simpledialog.askstring('Editar Tabla','ingrese el nombre nuevo de la tabla')
                a = messagebox.askquestion("Editar", "Quieres Cambiar el nombre La tabla " + nombreviejo+"\npor "+nombrenuevo)
                if a == "yes":
                    print(Storage.alterTable(self.nombreBD,nombreviejo,nombrenuevo))
                    self.listboxTablas.delete(0, END)
                    self.Cargartablas()
        except:
            ""

    def agregarC(self):
        try:
            if len(self.listboxTablas.curselection()) != 0:
                nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
                valor = simpledialog.askstring('Agregar Columna', 'ingrese el valor por default')
                print(Storage.alterAddColumn(self.nombreBD,nombretabla,valor))
        except:
            ""

    def borrarC(self):
        try:
            if len(self.listboxTablas.curselection()) != 0:
                nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
                columna = simpledialog.askinteger('Borrar Columna', 'ingrese el numero de columna')
                print(Storage.alterDropColumn(self.nombreBD,nombretabla,columna))
        except:
            ""

    def extraerTabla(self):
        if len(self.listboxTablas.curselection()) != 0:
            nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
            self.ventana.destroy()
            PantallaTuplas(self.nombreBD,nombretabla,Storage.extractTable(self.nombreBD, nombretabla))

    def agregarPK(self):
        try:
            if len(self.listboxTablas.curselection()) != 0:
                nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
                entrada = simpledialog.askstring('Listado de # de columnas', 'ingrese el listado separado por , sin espacios')
                lista=entrada.split(",")
                listafinal = []
                for i in lista:
                    listafinal.append(int(i))
                print(Storage.alterAddPK(self.nombreBD,nombretabla,listafinal))
        except:
            ""

    def eliminarPK(self):
        if len(self.listboxTablas.curselection()) != 0:
            nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
            print(Storage.alterDropPK(self.nombreBD,nombretabla))

    def graficar(self):
        if len(self.listboxTablas.curselection()) != 0:
            nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
            self.ventana.destroy()
            PantallaGrafico(self.nombreBD,nombretabla)

    def salir(self):
        self.ventana.destroy()
        PantallaBD(Storage.showDatabases())

#------------------------------------------------------graficas de arboles--------------------------------
class PantallaGrafico:
    def __init__(self,nombreBD, nombreTabla):
        self.ventana = Tk()
        self.nombreBD=nombreBD
        self.nombreTabla=nombreTabla
        #obteniendo grafico de la tabla indicada
        Storage.checkDirs()
        tab=Storage.rollback('tables/' + nombreBD + nombreTabla)
        tab.chart()

        self.ventana.title("Tabla "+self.nombreTabla)
        self.ventana.geometry("450x300")

        self.contenedor = Frame(self.ventana)
        self.contenedor.pack(fill="both", expand=True)
        #self.titulo = Label(self.contenedor, text="Tuplas de la tabla: " + self.nombreTabla, font=("Comic Sans MS", 18)).place(x=150, y=5)
        self.canvas=Canvas(self.contenedor)
        self.canvas.pack(side=LEFT,fill=BOTH,expand=1)
        self.scroll=ttk.Scrollbar(self.contenedor, orient=VERTICAL,command=self.canvas.yview)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.canvas.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.segundocontenedor=Frame(self.canvas,width=300, height=300)
        self.canvas.create_window((0,0),window=self.segundocontenedor,anchor="nw")
        imagen=PhotoImage(file="isam.png")
        labelimagen=Label(self.segundocontenedor,image=imagen).pack()

        Button(self.segundocontenedor, text="Salir", command=self.salir, width=20).pack()
        self.ventana.mainloop()

    def salir(self):
        self.ventana.destroy()
        PantallaTablas(self.nombreBD)

#----------------------------------------------------tuplas extract-------------------------------------------------------------------
class PantallaTuplas:
    def __init__(self, nombreBD, nombreTabla, listaTuplas):
        self.ventana = Tk()
        self.nombreBD = nombreBD
        self.nombreTabla=nombreTabla
        self.listaTuplas=listaTuplas
        self.ventana.title("Opciones de las Tuplas")
        self.contenedor = Frame(self.ventana, width=500, height=380)
        self.contenedor.pack(fill="both", expand=True)
        self.titulo = Label(self.contenedor, text="Tuplas de la tabla: " + self.nombreTabla, font=("Comic Sans MS", 18)).place(x=110, y=10)
        self.titulo = Label(self.contenedor, text="Posee "+str(Storage.rollback('tables/' + self.nombreBD + self.nombreTabla).numberColumns)+" Columnas",font=("Comic Sans MS", 14)).place(x=150, y=40)

        # boton crear tabla
        Button(self.contenedor, text="Extraer Tabla Completa", command=self.extraertabla, width=20).place(x=300, y=80)
        Button(self.contenedor, text="Extraer Por Rangos", command=self.extraerrango, width=20).place(x=300, y=110)
        Button(self.contenedor, text="Extraer Row (tupla)", command=self.extraertupla, width=20).place(x=300, y=140)

        Button(self.contenedor, text="Insertar Registro", command=self.insertar, width=20).place(x=300, y=170)

        Button(self.contenedor, text="Actualizar Registro", command=self.actualizar, width=20).place(x=300, y=200)

        Button(self.contenedor, text="Eliminar Registro", command=self.eliminar, width=20).place(x=300, y=230)
        Button(self.contenedor, text="Eliminar Todo", command=self.eliminartodo, width=20).place(x=300, y=260)
        Button(self.contenedor, text="Cargar CSV", command=self.cargarCSV, width=20).place(x=300, y=290)

        Button(self.contenedor, text="Regresar", command=self.salir, width=20).place(x=300, y=320)

        self.listboxTuplas = Listbox(self.contenedor, width=40, height=16)
        self.Cargartuplas()
        self.listboxTuplas.place(x=35, y=80)

        self.ventana.mainloop()

    def Cargartuplas(self):
        for i in range(0, len(self.listaTuplas)):
            self.listboxTuplas.insert(i, self.listaTuplas[i])

    def extraertabla(self):
        self.listboxTuplas.delete(0, END)
        self.listaTuplas=Storage.extractTable(self.nombreBD, self.nombreTabla)
        self.Cargartuplas()

    def extraerrango(self):
        try:
            columna = simpledialog.askinteger('Rango', 'ingrese el numero de indice de la columna')
            inicio = simpledialog.askstring('Rango', 'ingrese el valor de inicio')
            final = simpledialog.askstring('Rango', 'ingrese el valor del final')
            self.listboxTuplas.delete(0, END)
            self.listaTuplas=Storage.extractRangeTable(self.nombreBD,self.nombreTabla,columna,inicio,final)
            self.Cargartuplas()
        except:
            ""

    def extraertupla(self):
        try:
            lista = simpledialog.askstring('Extraer Registro', 'ingrese el id del registro que desea extraer\n'
                                                               'si tiene llave compuesta separela por ,')
            listafinal=lista.split(",")
            Tupla = Storage.extractRow(self.nombreBD,self.nombreTabla,listafinal)
            self.listboxTuplas.delete(0, END)
            self.listboxTuplas.insert(0, Tupla)
        except:
            ""

    def insertar(self):
        try:
            entrada = simpledialog.askstring('Insertar tuplas', 'ingrese el listado separado por , sin espacios')
            lista=entrada.split(",")
            Storage.insert(self.nombreBD, self.nombreTabla, lista)
            self.listboxTuplas.delete(0, END)
            self.listaTuplas=Storage.extractTable(self.nombreBD, self.nombreTabla)
            self.Cargartuplas()
        except:
            ""
    def actualizar(self):
        try:
            entrada = simpledialog.askstring('Actualizar Registro por un diccionario', 'Ingrese los datos separados por : y ,\n'
                                                                                       'por ejemplo id:valor,id2:valor2\n'
                                                                                       'sin espacios')

            llave= simpledialog.askstring('Ingrese la llave primaria',
                                             'si la llave es compuesta ingresela separada por ,'
                                             'sin espacios')
            entrada2=entrada.split(",")
            entrada3=[]
            for i in entrada2:
                aux=i.split(":")
                for j in aux:
                    try:
                        k=int(j)
                        esnumero=True
                    except:
                        esnumero=False
                    if esnumero:
                        entrada3.append(k)
                    else:
                        entrada3.append(j)
            diccionario={}
            for i in range(0,len(entrada3),2):
                diccionario[entrada3[i]]=entrada3[i+1]
            pk=llave.split(",")
            print(Storage.update(self.nombreBD,self.nombreTabla,diccionario,pk))
            self.listboxTuplas.delete(0, END)
            self.listaTuplas = Storage.extractTable(self.nombreBD, self.nombreTabla)
            self.Cargartuplas()

        except:
            ""

    def eliminar(self):
        try:
            entrada = simpledialog.askstring('Eliminar tuplas', 'ingrese las pk separado por , sin espacios')
            lista = entrada.split(",")
            print(Storage.delete(self.nombreBD,self.nombreTabla,lista))
            self.listboxTuplas.delete(0, END)
            self.listaTuplas = Storage.extractTable(self.nombreBD, self.nombreTabla)
            self.Cargartuplas()
        except:
            ""
    def eliminartodo(self):
        try:
            a = messagebox.askquestion("Eliminar", "Quieres eliminar todos los registros de la tabla \n\t" + self.nombreTabla)
            if a == "yes":
                print(Storage.truncate(self.nombreBD,self.nombreTabla))
                self.listboxTuplas.delete(0, END)
                self.listaTuplas = Storage.extractTable(self.nombreBD, self.nombreTabla)
                self.Cargartuplas()
        except:
            ""
    def cargarCSV(self):
        try:
            archivo=filedialog.askopenfilename(title="Cargar")
            Storage.loadCSV(archivo,self.nombreBD,self.nombreTabla)
            self.listboxTuplas.delete(0, END)
            self.listaTuplas = Storage.extractTable(self.nombreBD, self.nombreTabla)
            self.Cargartuplas()
        except:
            ""
    def salir(self):
        self.ventana.destroy()
        PantallaTablas(self.nombreBD)
