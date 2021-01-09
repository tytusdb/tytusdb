from storage import storage as j
from tkinter import *
from tkinter import ttk
from storage.BPlusMode import Serializable as BPlusM
from storage.BMode import BMode as BM
from storage.ISAMMode import ISAMMode as ISAMM
from storage.HashMode import HashMode as HashM
from storage.AVLMode.DataAccessLayer.reports import graphAVL
from storage import Blockchain as BC
import os


class PantallaBD():
    def __init__(self, vectorBases):
        self.ventana = Tk()
        self.ventana.geometry('350x480')
        self.vectorBases = vectorBases
        self.ventana.title("Bases De Datos")
        self.contenedor = Frame(self.ventana, width=110, height=200, bg='#CBE86B')
        self.contenedor.pack(fill="both", expand=True)
        self.titulo = Label(self.contenedor, text="Bases de Datos", font=("TkFixedFont", 18, 'bold'), bg='#CBE86B').place(x=75, y=20)

        # botones crear eliminar y editar bases de datos
        self.BtnTablas = Button(self.contenedor, text="Ver Tablas", command=self.Tablas, width=20,
                                font=('TkFixedFont', 10, 'bold')).place(x=75, y=400)
        self.BtnDSD = Button(self.contenedor, text="Graficar DSD", command=self.DSD, width=20,
                                font=('TkFixedFont', 10, 'bold')).place(x=75, y=430)
        self.listboxBases = Listbox(self.contenedor, bg='#F2E9E1',  font=('TkFixedFont', 10, 'bold'),
                                    width=40, height=18, selectbackground='#FF9C5B')
        self.CargarBases()
        self.listboxBases.place(x=30, y=80)

        self.ventana.mainloop()

    # cargar los elementos del arreglo de bases de datos
    def CargarBases(self):
        for i in range(0, len(self.vectorBases)):
            self.listboxBases.insert(i, self.vectorBases[i])

    # para visualizar las tablas
    def Tablas(self):
        if len(self.listboxBases.curselection()) != 0:
            nombreBD = self.listboxBases.get(self.listboxBases.curselection()[0])
            self.ventana.destroy()
            # hay que mandar el vector de tablas
            PantallaTablas(nombreBD)

    def DSD(self):
        if len(self.listboxBases.curselection()) != 0:
            nombreDB = self.listboxBases.get(self.listboxBases.curselection()[0])
            self.ventana.destroy()
            PantallaGraficoBases(nombreDB)


# --------------------------------------------------------opciones de las tablas-----------------------------------------------


class PantallaTablas:
    def __init__(self, nombreBD):
        self.ventana = Tk()
        self.nombreBD = nombreBD
        self.ventana.title("Opciones de las tablas")
        self.contenedor = Frame(self.ventana, width=500, height=400, bg='#CBE86B')
        self.contenedor.pack(fill="both", expand=True)
        self.titulo = Label(self.contenedor, text="Tablas de la BD: " + nombreBD, font=("TkFixedFont", 18, 'bold'),
                            bg='#CBE86B').place(x=110, y=20)

        # boton crear tabla
        Button(self.contenedor, text="Ver Tabla", command=self.extraerTabla, width=20, font=('TkFixedFont', 10, 'bold')).place(x=300, y=140)
        Button(self.contenedor, text="Graficar", command=self.graficar, width=20, font=('TkFixedFont', 10, 'bold')).place(x=300, y=170)
        Button(self.contenedor, text="Ver Blockchain", command=self.graficarBlockChain, width=20, font=('TkFixedFont', 10, 'bold')).place(x=300, y=200)
        Button(self.contenedor, text="Graficar DF", command=self.DF, width=20, font=('TkFixedFont', 10, 'bold')).place(x=300, y=230)
        Button(self.contenedor, text="Regresar", command=self.salir, width=20, font=('TkFixedFont', 10, 'bold')).place(x=300, y=345)

        self.listboxTablas = Listbox(self.contenedor, width=32, height=17, bg='#F2E9E1',
                                     font=('TkFixedFont', 10, 'bold'), selectbackground='#FF9C5B')
        self.Cargartablas()
        self.listboxTablas.place(x=35, y=80)

        self.ventana.mainloop()

    # cargar los elementos del arreglo de tablas
    def Cargartablas(self):
        for i in range(0, len(j.showTables(self.nombreBD))):
            self.listboxTablas.insert(i, j.showTables(self.nombreBD)[i])

    def extraerTabla(self):
        if len(self.listboxTablas.curselection()) != 0:
            nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
            self.ventana.destroy()
            PantallaTuplas(self.nombreBD, nombretabla, j.extractTable(self.nombreBD, nombretabla))

    def graficar(self):
        if len(self.listboxTablas.curselection()) != 0:
            nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
            self.ventana.destroy()
            PantallaGrafico(self.nombreBD, nombretabla, 'tabla')

    def graficarBlockChain(self):
        if len(self.listboxTablas.curselection()) != 0:
            nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
            self.ventana.destroy()
            PantallaGrafico(self.nombreBD, nombretabla, 'blockchain')

    def DF(self):
        if len(self.listboxTablas.curselection()) != 0:
            nombretabla = self.listboxTablas.get(self.listboxTablas.curselection()[0])
            self.ventana.destroy()
            PantallaGrafico(self.nombreBD, nombretabla, 'DF')

    def salir(self):
        self.ventana.destroy()
        PantallaBD(j.showDatabases())


# ------------------------------------------------------graficas de arboles--------------------------------
class PantallaGrafico:
    def __init__(self, nombreBD, nombreTabla, grafico):
        self.ventana = Tk()
        self.nombreBD = nombreBD
        self.nombreTabla = nombreTabla
        # obteniendo grafico de la tabla indicada
        j.initcheck()

        self.ventana.title("Tabla " + self.nombreTabla)
        self.ventana.geometry("600x430")

        self.contenedor = Frame(self.ventana)
        self.contenedor.pack(fill="both", expand=True)

        self.canvas = Canvas(self.contenedor)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.scrolly = ttk.Scrollbar(self.contenedor, orient=VERTICAL, command=self.canvas.yview)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scrolly.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.segundocontenedor = Frame(self.canvas, width=600, height=400)
        self.canvas.create_window((0, 0), window=self.segundocontenedor, anchor="nw")

        self.scrollx = ttk.Scrollbar(self.canvas, orient=HORIZONTAL, command=self.canvas.xview)
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.canvas.configure(xscrollcommand=self.scrollx.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        Button(self.canvas, text="Salir", command=self.salir, width=20).pack()

        imagen = None
        if grafico == 'tabla':
            imagen = PhotoImage(file=chartTable(nombreBD, nombreTabla))
        elif grafico == 'blockchain':
            imagen = PhotoImage(file=chartBlockchain(nombreBD, nombreTabla))
        elif grafico == 'DF':
            try:
                j.graphDF(nombreBD, nombreTabla)
                imagen = PhotoImage(file=(nombreBD + '-' + nombreTabla + 'DF.png'))
            except:
                imagen = PhotoImage(file=('img/no-DF.png'))
        labelimagen = Label(self.segundocontenedor, image=imagen).pack()


        self.ventana.mainloop()

    def salir(self):
        self.ventana.destroy()
        PantallaTablas(self.nombreBD)

# ------------------------------------------------------graficas de arboles--------------------------------


class PantallaGraficoBases:
    def __init__(self, nombreBD):
        self.ventana = Tk()
        self.nombreBD = nombreBD
        # obteniendo grafico de la tabla indicada
        j.initcheck()

        self.ventana.geometry("600x430")

        self.contenedor = Frame(self.ventana)
        self.contenedor.pack(fill="both", expand=True)

        self.canvas = Canvas(self.contenedor)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.scrolly = ttk.Scrollbar(self.contenedor, orient=VERTICAL, command=self.canvas.yview)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scrolly.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.segundocontenedor = Frame(self.canvas, width=600, height=400)
        self.canvas.create_window((0, 0), window=self.segundocontenedor, anchor="nw")

        self.scrollx = ttk.Scrollbar(self.canvas, orient=HORIZONTAL, command=self.canvas.xview)
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.canvas.configure(xscrollcommand=self.scrollx.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        Button(self.canvas, text="Salir", command=self.salir, width=20).pack()

        imagen = None
        try:
            j.graphDSD(nombreBD)
            imagen = PhotoImage(file=(nombreBD + 'DSD.png'))
        except:
            imagen = PhotoImage(file=('img/no-DSD.png'))
        labelimagen = Label(self.segundocontenedor, image=imagen).pack()

        self.ventana.mainloop()

    def salir(self):
        self.ventana.destroy()
        PantallaBD(j.showDatabases())


# ----------------------------------------------------tuplas extract-------------------------------------------------------------------
class PantallaTuplas:
    def __init__(self, nombreBD, nombreTabla, listaTuplas):
        self.ventana = Tk()
        self.ventana.geometry('800x400')
        self.nombreBD = nombreBD
        self.nombreTabla = nombreTabla
        self.listaTuplas = listaTuplas
        self.ventana.title("Opciones de las Tuplas")
        self.contenedor = Frame(self.ventana, width=490, height=380, bg='#CBE86B')
        self.contenedor.pack(fill="both", expand=True)
        self.titulo = Label(self.contenedor, text="Tuplas de la tabla: " + self.nombreTabla,
                            font=("TkFixedFont", 18, 'bold'), bg='#CBE86B').place(x=235, y=20)

        # boton crear tabla
        Button(self.contenedor, text="Regresar", command=self.salir, width=20, font=('TkFixedFont', 10, 'bold')).place(x=570, y=365)

        self.listboxTuplas = Listbox(self.contenedor, width=100, height=16,  bg='#F2E9E1',  font=('TkFixedFont', 10), selectbackground='#FF9C5B')
        self.Cargartuplas()
        self.listboxTuplas.place(x=35, y=80)

        self.ventana.mainloop()

    def Cargartuplas(self):
        for i in range(0, len(self.listaTuplas)):
            self.listboxTuplas.insert(i, self.listaTuplas[i])

    def extraertabla(self):
        self.listboxTuplas.delete(0, END)
        self.listaTuplas = j.extractTable(self.nombreBD, self.nombreTabla)
        self.Cargartuplas()

    def salir(self):
        self.ventana.destroy()
        PantallaTablas(self.nombreBD)


def chartTable(database, table):
    try:
        if j.databasesinfo[1][database][table]['mode'] == 'avl':
            graphAVL(database, table)
            return 'tmp/grafo-avl.png'
        elif j.databasesinfo[1][database][table]['mode'] == 'b':
            BM.serializar.rollback(database + "-" + table + "-B").graficar()
            os.remove('archivo.dot')
            return 'salida.png'
        elif j.databasesinfo[1][database][table]['mode'] == 'bplus':
            bplus = BPlusM.Read('Data/BPlusMode/' + database + '/' + table + '/', table)
            bplus.graficar(database, table)
            return 'Data/BPlusMode/' + database + '/' + table + '/' + table + '.png'
        elif j.databasesinfo[1][database][table]['mode'] == 'isam':
            ISAMM.chart(database, table)
            os.remove('isam.dot')
            return 'isam.png'
        elif j.databasesinfo[1][database][table]['mode'] == 'hash':
            tmp = HashM._storage.Cargar(database, table)
            tmp.Grafico()
            os.remove('hash.dot')
            return 'hash.png'
        else:
            return 'img/no-graficable.png'
    except:
        return 'img/no-graficable.png'


def chartBlockchain(database, table):
    try:
        BC.chartBlockchain(database, table)
        os.remove('blockchain.dot')
        return 'blockchain.png'
    except:
        return 'img/no-modoseguro.png'


PantallaBD(j.showDatabases())
