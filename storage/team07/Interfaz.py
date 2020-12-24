import tkinter as tk
from tkinter import *
from tkinter import ttk
from storage.team07.storageManagement import functions


class Aplicacion:

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.geometry("1450x650+100+100")
        s = ttk.Style()

        s.configure('Red.TLabelframe.Label', font=('Roboto Condensed', 12))
        s.configure('Red.TLabelframe.Label', foreground='green')

        self.labelframe1 = ttk.LabelFrame(self.ventana1, text="Base de Datos :", style="Red.TLabelframe")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.AgregarH()

        self.labelframe2 = ttk.LabelFrame(self.ventana1, text="Modo: ", style="Red.TLabelframe")
        self.labelframe2.grid(column=1, row=0, padx=5, pady=10)
        self.avl()

        self.labelframe3 = ttk.LabelFrame(self.ventana1, text="Tablas: ", style="Red.TLabelframe")
        self.labelframe3.grid(column=2, row=0, padx=5, pady=10)
        self.Tablas()

        self.labelframe4 = ttk.LabelFrame(self.ventana1, text="Reportes: ", style="Red.TLabelframe")
        self.labelframe4.grid(column=0, row=1, padx=0, pady=10)
        self.Reportes()
        # self.operaciones()

        self.ventana1.mainloop()

    # Implementamos el método login:x
    # El algoritmo del método login tiene por objetivo crear las 2 Label, 2 Entry y Button
    # y añadirlos dentro del LabelFrame:

    def createDataBase(self):
        newDataBase = self.AgregarHash.get()

        print(functions.createDatabase(newDataBase))
        # print(functions.showDatabases())

    def showDataBases(self):
        print(functions.showDatabases())

    def AgregarH(self):
        self.label1 = ttk.Label(self.labelframe1, text="CreateDataBase:")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="w")

        self.AgregarHash = StringVar()
        self.label1 = ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=1, padx=4, pady=4, sticky="w")
        self.entry1 = ttk.Entry(self.labelframe1, width=30, textvariable=self.AgregarHash)
        self.entry1.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="DropDataBase:")
        self.label1.grid(column=0, row=2, padx=4, pady=4, sticky="w")
        self.label1 = ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=3, padx=4, pady=4, sticky="w")
        self.EliminarrHash = StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, width=30, textvariable=self.EliminarrHash)
        self.entry2.grid(column=1, row=3, padx=4, pady=4)

        self.ModificarHash = StringVar()
        self.ModificarHash1 = StringVar()

        self.label1 = ttk.Label(self.labelframe1, text="AlterDatabase:")
        self.label1.grid(column=0, row=4, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe1, text="Nombre Viejo:")
        self.label1.grid(column=0, row=5, padx=4, pady=4, sticky="w")

        self.entry3 = ttk.Entry(self.labelframe1, width=30, textvariable=self.ModificarHash)
        self.entry3.grid(column=1, row=5, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="Nombre Nuevo:")
        self.label1.grid(column=0, row=6, padx=4, pady=4, sticky="w")

        self.entry4 = ttk.Entry(self.labelframe1, width=30, textvariable=self.ModificarHash1)
        self.entry4.grid(column=1, row=6, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe1, text="CreateDataBase",command= lambda: functions.createDatabase(self.AgregarHash.get()))
        self.boton1.grid(column=0, row=7, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe1, text="DropDatabase", command= lambda: functions.dropDatabase(self.EliminarrHash.get()))
        self.boton2.grid(column=1, row=7, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe1, text="AlterDatabase", command= lambda: functions.alterDatabase(self.ModificarHash.get(),self.ModificarHash1.get()))
        self.boton3.grid(column=2, row=7, padx=4, pady=4)
        self.boton4 = ttk.Button(self.labelframe1, text="ShowDatabases", command= lambda: functions.showDatabases())
        self.boton4.grid(column=3, row=7, padx=4, pady=4)

    def avl(self):
        self.label1 = ttk.Label(self.labelframe2, text="Create Table:")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe2, text="Base de Datos:")
        self.label1.grid(column=0, row=1, padx=4, pady=4, sticky="w")

        self.AgregarAvl = StringVar()
        self.entry5 = ttk.Entry(self.labelframe2, width=30, textvariable=self.AgregarAvl)
        self.entry5.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Nombre:")
        self.label1.grid(column=0, row=2, padx=4, pady=4, sticky="w")

        self.AgregarAvl1 = StringVar()
        self.entry6 = ttk.Entry(self.labelframe2, width=30, textvariable=self.AgregarAvl1)
        self.entry6.grid(column=1, row=2, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Numero Columnas:")
        self.label1.grid(column=0, row=3, padx=4, pady=4, sticky="w")

        self.AgregarAvl2 = StringVar()
        self.entry7 = ttk.Entry(self.labelframe2, width=30, textvariable=self.AgregarAvl2)
        self.entry7.grid(column=1, row=3, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe2, text="ShowTables:")
        self.label2.grid(column=0, row=4, padx=4, pady=4, sticky="w")

        self.label2 = ttk.Label(self.labelframe2, text="Nombre a buscar:")
        self.label2.grid(column=0, row=5, padx=4, pady=4, sticky="w")
        self.BuscarAvl = StringVar()
        self.entry8 = ttk.Entry(self.labelframe2, width=30, textvariable=self.BuscarAvl)
        self.entry8.grid(column=1, row=5, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe2, text="DropTable:")
        self.label1.grid(column=0, row=6, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe2, text="Base de datos:")
        self.label1.grid(column=0, row=7, padx=4, pady=4, sticky="w")

        self.EliminarAvl = StringVar()
        self.entry9 = ttk.Entry(self.labelframe2, width=30, textvariable=self.EliminarAvl)
        self.entry9.grid(column=1, row=7, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Tabla a eliminar:")
        self.label1.grid(column=0, row=8, padx=4, pady=4, sticky="w")

        self.EliminarAvl1 = StringVar()
        self.entry10 = ttk.Entry(self.labelframe2, width=30, textvariable=self.EliminarAvl1)
        self.entry10.grid(column=1, row=8, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="AlterTable:")
        self.label1.grid(column=0, row=9, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe2, text="Base de datos:")
        self.label1.grid(column=0, row=10, padx=4, pady=4, sticky="w")
        self.ModificarAvl = StringVar()
        self.entry11 = ttk.Entry(self.labelframe2, width=30, textvariable=self.ModificarAvl)
        self.entry11.grid(column=1, row=10, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Nombre tabla nueva:")
        self.label1.grid(column=0, row=11, padx=4, pady=4, sticky="w")
        self.ModificarAvl1 = StringVar()
        self.entry12 = ttk.Entry(self.labelframe2, width=30, textvariable=self.ModificarAvl)
        self.entry12.grid(column=1, row=11, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Nombre tabla vieja:")
        self.label1.grid(column=0, row=12, padx=4, pady=4, sticky="w")
        self.ModificarAvl2 = StringVar()
        self.entry13 = ttk.Entry(self.labelframe2, width=30, textvariable=self.ModificarAvl)
        self.entry13.grid(column=1, row=12, padx=4, pady=4)
        #command= lambda: functions.showDatabases()
        self.boton5 = ttk.Button(self.labelframe2, text="CreateTable", command=lambda: functions.createTable(self.AgregarAvl.get(), self.AgregarAvl1.get(), self.AgregarAvl2.get()))
        self.boton5.grid(column=0, row=26, padx=4, pady=4)
        self.boton6 = ttk.Button(self.labelframe2, text="DropTable", command=lambda: functions.dropTable(self.EliminarAvl.get(), self.EliminarAvl1.get()))
        self.boton6.grid(column=1, row=26, padx=4, pady=4)

        self.boton7 = ttk.Button(self.labelframe2, text="AlterTable",command=lambda: functions.alterTable(self.ModificarAvl.get(), self.ModificarAvl1.get(), self.ModificarAvl2.get()))
        self.boton7.grid(column=2, row=26, padx=4, pady=4)
        self.boton8 = ttk.Button(self.labelframe2, text="ShowTables", command=lambda: functions.showTables(self.BuscarAvl.get()))
        self.boton8.grid(column=3, row=26, padx=4, pady=4)

    def Tablas(self):
        self.label1 = ttk.Label(self.labelframe3, text="Insert:")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="w")
        self.AgregarHash2 = StringVar()
        self.label1 = ttk.Label(self.labelframe3, text="Base de datos:")
        self.label1.grid(column=0, row=1, padx=4, pady=4, sticky="w")
        self.entry14 = ttk.Entry(self.labelframe3, width=30, textvariable=self.AgregarHash2)
        self.entry14.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Tabla:")
        self.label1.grid(column=0, row=2, padx=4, pady=4, sticky="w")
        self.AgregarHash1 = StringVar()
        self.entry15 = ttk.Entry(self.labelframe3, width=30, textvariable=self.AgregarHash1)
        self.entry15.grid(column=1, row=2, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Registro:")
        self.label1.grid(column=0, row=3, padx=4, pady=4, sticky="w")
        self.AgregarHash2 = StringVar()
        self.entry16 = ttk.Entry(self.labelframe3, width=30, textvariable=self.AgregarHash2)
        self.entry16.grid(column=1, row=3, padx=4, pady=4)

        # alterAddPK  database, table, columns
        self.label1 = ttk.Label(self.labelframe3, text="AlterAddPK:")
        self.label1.grid(column=0, row=4, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe3, text="Base de datos:")
        self.label1.grid(column=0, row=5, padx=4, pady=4, sticky="w")
        self.ModificarHash = StringVar()
        self.entry17 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ModificarHash)
        self.entry17.grid(column=1, row=5, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Tabla:")
        self.label1.grid(column=0, row=6, padx=4, pady=4, sticky="w")
        self.ModificarHash1 = StringVar()
        self.entry18 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ModificarHash1)
        self.entry18.grid(column=1, row=6, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Columna:")
        self.label1.grid(column=0, row=7, padx=4, pady=4, sticky="w")
        self.ModificarHash2 = StringVar()
        self.entry19 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ModificarHash2)
        self.entry19.grid(column=1, row=7, padx=4, pady=4)

        # extractTable  database, table
        self.label1 = ttk.Label(self.labelframe3, text="ExtractTable:")
        self.label1.grid(column=0, row=8, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe3, text="Base de datos:")
        self.label1.grid(column=0, row=9, padx=4, pady=4, sticky="w")
        self.ExtraerTabla = StringVar()
        self.entry20 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ExtraerTabla)
        self.entry20.grid(column=1, row=9, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Tabla:")
        self.label1.grid(column=0, row=10, padx=4, pady=4, sticky="w")
        self.ExtraerTabla1 = StringVar()
        self.entry21 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ExtraerTabla1)
        self.entry21.grid(column=1, row=10, padx=4, pady=4)

        # truncate  database, table
        self.label1 = ttk.Label(self.labelframe3, text="Truncate:")
        self.label1.grid(column=0, row=11, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe3, text="Base de datos:")
        self.label1.grid(column=0, row=12, padx=4, pady=4, sticky="w")
        self.Truncar = StringVar()
        self.entry22 = ttk.Entry(self.labelframe3, width=30, textvariable=self.Truncar)
        self.entry22.grid(column=1, row=12, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Tabla:")
        self.label1.grid(column=0, row=13, padx=4, pady=4, sticky="w")
        self.Truncar1 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.Truncar1)
        self.entry1.grid(column=1, row=13, padx=4, pady=4)

        # -----------------------------------------------------------------------------------------------------------------------
        # command= lambda: functions.showDatabases()
        self.boton9 = ttk.Button(self.labelframe3, text="Insert", command=lambda: functions.insert(self.AgregarHash2.get(), self.AgregarHash1.get(), self.AgregarHash2.get()))
        self.boton9.grid(column=0, row=20, padx=4, pady=4)
        self.boton10 = ttk.Button(self.labelframe3, text="AlterAddPk", command=lambda: functions.alterAddPK(self.ModificarHash.get(), self.ModificarHash1.get(), self.ModificarHash2.get()))
        self.boton10.grid(column=1, row=20, padx=4, pady=4)
        self.boton11 = ttk.Button(self.labelframe3, text="ExtractTable", command=lambda: functions.extractTable(self.ExtraerTabla.get(), self.ExtraerTabla1.get()))
        self.boton11.grid(column=2, row=20, padx=4, pady=4)
        self.boton12 = ttk.Button(self.labelframe3, text="Truncate", command=lambda: functions.truncate(self.Truncar.get(), self.Truncar1.get()))
        self.boton12.grid(column=3, row=20, padx=4, pady=4)

    def Reportes(self):
        self.boton13 = ttk.Button(self.labelframe4, text="Bases de Datos", command=self.metodo)
        self.boton13.grid(column=0, row=0, padx=4, pady=4)
        self.boton14 = ttk.Button(self.labelframe4, text="Conjunto de Tablas", command=self.metodo)
        self.boton14.grid(column=1, row=0, padx=4, pady=4)
        self.boton15 = ttk.Button(self.labelframe4, text="Tabla", command=self.metodo)
        self.boton15.grid(column=2, row=0, padx=4, pady=4)
        self.boton16 = ttk.Button(self.labelframe4, text="Tupla", command=self.metodo)
        self.boton16.grid(column=3, row=0, padx=4, pady=4)

    def metodo(self):
        print("metodo prueba")


aplicacion1 = Aplicacion()
