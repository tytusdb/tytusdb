import tkinter as tk
from tkinter import *
from tkinter import ttk
import functions as ft

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("1450x650+100+100")
        s = ttk.Style()

        s.configure('Red.TLabelframe.Label', font=('Roboto Condensed', 12))
        s.configure('Red.TLabelframe.Label', foreground ='green')


        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Base de Datos :", style = "Red.TLabelframe")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.AgregarH()

        self.labelframe2=ttk.LabelFrame(self.ventana1, text="Modo: ", style = "Red.TLabelframe")
        self.labelframe2.grid(column=1, row=0, padx=5, pady=10)
        self.avl()

        self.labelframe3 = ttk.LabelFrame(self.ventana1, text="Tablas: ", style="Red.TLabelframe")
        self.labelframe3.grid(column=2, row=0, padx=5, pady=10)
        self.Tablas()

        self.labelframe4 = ttk.LabelFrame(self.ventana1, text="Reportes: ", style="Red.TLabelframe")
        self.labelframe4.grid(column=0, row=1, padx=0, pady=10)
        self.Reportes()
        #self.operaciones()

        self.ventana1.mainloop()

    # Implementamos el método login:x
    # El algoritmo del método login tiene por objetivo crear las 2 Label, 2 Entry y Button
    # y añadirlos dentro del LabelFrame:
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
        self.entry1 = ttk.Entry(self.labelframe1, width=30, textvariable=self.EliminarrHash)
        self.entry1.grid(column=1, row=3, padx=4, pady=4)


        self.ModificarHash = StringVar()
        self.ModificarHash1 = StringVar()

        self.label1 = ttk.Label(self.labelframe1, text="AlterDatabase:")
        self.label1.grid(column=0, row=4, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe1, text="Nombre Viejo:")
        self.label1.grid(column=0, row=5, padx=4, pady=4, sticky="w")

        self.entry1 = ttk.Entry(self.labelframe1, width=30, textvariable=self.ModificarHash)
        self.entry1.grid(column=1, row=5, padx=4, pady=4)


        self.label1 = ttk.Label(self.labelframe1, text="Nombre Nuevo:")
        self.label1.grid(column=0, row=6, padx=4, pady=4, sticky="w")

        self.entry1 = ttk.Entry(self.labelframe1, width=30, textvariable=self.ModificarHash1)
        self.entry1.grid(column=1, row=6, padx=4, pady=4)






        self.boton1 = ttk.Button(self.labelframe1, text="CreateDataBase", command=ft.createDatabase(self.AgregarHash))
        self.boton1.grid(column=0, row=7, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe1, text="DropDatabase", command=ft.dropDatabase(self.EliminarrHash))
        self.boton2.grid(column=1 , row=7, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe1, text="AlterDatabase" ,command=ft.alterDatabase(self.ModificarHash,self.ModificarHash1))
        self.boton3.grid(column=2, row=7, padx=4, pady=4)
        self.boton4 = ttk.Button(self.labelframe1, text="ShowDatabases", command=ft.showDatabases())
        self.boton4.grid(column=3, row=7, padx=4, pady=4)

    def avl(self):
        self.label1 = ttk.Label(self.labelframe2, text="Create Table:")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe2, text="Base de Datos:")
        self.label1.grid(column=0, row=1, padx=4, pady=4, sticky="w")

        self.AgregarAvl = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.AgregarAvl)
        self.entry1.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Nombre:")
        self.label1.grid(column=0, row=2, padx=4, pady=4, sticky="w")

        self.AgregarAvl1 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.AgregarAvl1)
        self.entry1.grid(column=1, row=2, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Numero Columnas:")
        self.label1.grid(column=0, row=3, padx=4, pady=4, sticky="w")

        self.AgregarAvl2 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.AgregarAvl2)
        self.entry1.grid(column=1, row=3, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe2, text="ShowTables:")
        self.label2.grid(column=0, row=4, padx=4, pady=4, sticky="w")

        self.label2 = ttk.Label(self.labelframe2, text="Nombre a buscar:")
        self.label2.grid(column=0, row=5, padx=4, pady=4, sticky="w")
        self.BuscarAvl = StringVar()
        self.entry2 = ttk.Entry(self.labelframe2, width=30, textvariable=self.BuscarAvl)
        self.entry2.grid(column=1, row=5, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe2, text="DropTable:")
        self.label1.grid(column=0, row=6, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe2, text="Base de datos:")
        self.label1.grid(column=0, row=7, padx=4, pady=4, sticky="w")

        self.EliminarAvl = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.EliminarAvl)
        self.entry1.grid(column=1, row=7, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Tabla a eliminar:")
        self.label1.grid(column=0, row=8, padx=4, pady=4, sticky="w")

        self.EliminarAvl1 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.EliminarAvl1)
        self.entry1.grid(column=1, row=8, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="AlterTable:")
        self.label1.grid(column=0, row=9, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe2, text="Base de datos:")
        self.label1.grid(column=0, row=10, padx=4, pady=4, sticky="w")
        self.ModificarAvl = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.ModificarAvl)
        self.entry1.grid(column=1, row=10, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Nombre tabla nueva:")
        self.label1.grid(column=0, row=11, padx=4, pady=4, sticky="w")
        self.ModificarAvl1 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.ModificarAvl)
        self.entry1.grid(column=1, row=11, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Nombre tabla vieja:")
        self.label1.grid(column=0, row=12, padx=4, pady=4, sticky="w")
        self.ModificarAvl2 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.ModificarAvl)
        self.entry1.grid(column=1, row=12, padx=4, pady=4)



        self.boton1 = ttk.Button(self.labelframe2, text="CreateTable", command=ft.createTable(self.AgregarAvl,self.AgregarAvl1,self.AgregarAvl2))
        self.boton1.grid(column=0, row=26, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe2, text="DropTable", command=ft.dropTable(self.EliminarAvl,self.EliminarAvl1))
        self.boton2.grid(column=1, row=26, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe2, text="AlterTable", command=ft.alterTable(self.ModificarAvl, self.ModificarAvl1, self.ModificarAvl2))
        self.boton3.grid(column=2, row=26, padx=4, pady=4)
        self.boton4 = ttk.Button(self.labelframe2, text="ShowTables", command=ft.showTables(self.BuscarAvl))
        self.boton4.grid(column=3, row=26, padx=4, pady=4)

    def Tablas(self):
        self.label1 = ttk.Label(self.labelframe3, text="Insert:")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="w")
        self.AgregarHash = StringVar()
        self.label1 = ttk.Label(self.labelframe3, text="Base de datos:")
        self.label1.grid(column=0, row=1, padx=4, pady=4, sticky="w")
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.AgregarHash)
        self.entry1.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Tabla:")
        self.label1.grid(column=0, row=2, padx=4, pady=4, sticky="w")
        self.AgregarHash1 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.AgregarHash1)
        self.entry1.grid(column=1, row=2, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Registro:")
        self.label1.grid(column=0, row=3, padx=4, pady=4, sticky="w")
        self.AgregarHash2 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.AgregarHash2)
        self.entry1.grid(column=1, row=3, padx=4, pady=4)

        # alterAddPK  database, table, columns
        self.label1 = ttk.Label(self.labelframe3, text="AlterAddPK:")
        self.label1.grid(column=0, row=4, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe3, text="Base de datos:")
        self.label1.grid(column=0, row=5, padx=4, pady=4, sticky="w")
        self.ModificarHash = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ModificarHash)
        self.entry1.grid(column=1, row=5, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Tabla:")
        self.label1.grid(column=0, row=6, padx=4, pady=4, sticky="w")
        self.ModificarHash1 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ModificarHash1)
        self.entry1.grid(column=1, row=6, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Columna:")
        self.label1.grid(column=0, row=7, padx=4, pady=4, sticky="w")
        self.ModificarHash2 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ModificarHash2)
        self.entry1.grid(column=1, row=7, padx=4, pady=4)

        #extractTable  database, table
        self.label1 = ttk.Label(self.labelframe3, text="ExtractTable:")
        self.label1.grid(column=0, row=8, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe3, text="Base de datos:")
        self.label1.grid(column=0, row=9, padx=4, pady=4, sticky="w")
        self.ExtraerTabla = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ExtraerTabla)
        self.entry1.grid(column=1, row=9, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Tabla:")
        self.label1.grid(column=0, row=10, padx=4, pady=4, sticky="w")
        self.ExtraerTabla1 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ExtraerTabla1)
        self.entry1.grid(column=1, row=10, padx=4, pady=4)


        #truncate  database, table
        self.label1 = ttk.Label(self.labelframe3, text="Truncate:")
        self.label1.grid(column=0, row=11, padx=4, pady=4, sticky="w")

        self.label1 = ttk.Label(self.labelframe3, text="Base de datos:")
        self.label1.grid(column=0, row=12, padx=4, pady=4, sticky="w")
        self.Truncar = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.Truncar)
        self.entry1.grid(column=1, row=12, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Tabla:")
        self.label1.grid(column=0, row=13, padx=4, pady=4, sticky="w")
        self.Truncar1 = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.Truncar1)
        self.entry1.grid(column=1, row=13, padx=4, pady=4)

#-----------------------------------------------------------------------------------------------------------------------

        self.boton1 = ttk.Button(self.labelframe3, text="Insert", command=ft.insert(self.AgregarHash, self.AgregarHash1, self.AgregarHash2))
        self.boton1.grid(column=0, row=20, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe3, text="AlterAddPk", command=ft.alterAddPK(self.ModificarHash, self.ModificarHash1, self.ModificarHash2))
        self.boton2.grid(column=1, row=20, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe3, text="ExtractTable", command=ft.extractTable(self.ExtraerTabla, self.ExtraerTabla1))
        self.boton3.grid(column=2, row=20, padx=4, pady=4)
        self.boton4 = ttk.Button(self.labelframe3, text="Truncate", command=ft.truncate(self.Truncar, self.Truncar1))
        self.boton4.grid(column=3, row=20, padx=4, pady=4)

    def Reportes(self):


        self.boton1 = ttk.Button(self.labelframe4, text="Bases de Datos", command=self.metodo)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe4, text="Conjunto de Tablas", command=self.metodo)
        self.boton2.grid(column=1, row=0, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe4, text="Tabla", command=self.metodo)
        self.boton3.grid(column=2, row=0, padx=4, pady=4)
        self.boton4 = ttk.Button(self.labelframe4, text="Tupla", command=self.metodo)
        self.boton4.grid(column=3, row=0, padx=4, pady=4)



    def metodo(self):
        print("metodo prueba")

aplicacion1=Aplicacion()

