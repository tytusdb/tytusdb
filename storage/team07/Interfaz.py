import tkinter as tk
from tkinter import *
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("1400x300+100+100")
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
        self.label1 = ttk.Label(self.labelframe1, text="Agregar:")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="w")
        self.AgregarHash = StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, width=30, textvariable=self.AgregarHash)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="Eliminar:")
        self.label1.grid(column=0, row=1, padx=4, pady=4, sticky="w")
        self.EliminarrHash = StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, width=30, textvariable=self.EliminarrHash)
        self.entry1.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe1, text="Modificar:")
        self.label1.grid(column=0, row=2, padx=4, pady=4, sticky="w")
        self.ModificarHash = StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, width=30, textvariable=self.ModificarHash)
        self.entry1.grid(column=1, row=2, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Buscar:")
        self.label2.grid(column=0, row=3, padx=4, pady=4, sticky="w")
        self.BuscarHash = StringVar()
        self.entry2 = ttk.Entry(self.labelframe1,  width=30, textvariable=self.BuscarHash)
        self.entry2.grid(column=1, row=3, padx=4, pady=4, sticky="w")

        self.boton1 = ttk.Button(self.labelframe1, text="Agregar", command=self.metodo)
        self.boton1.grid(column=0, row=4, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe1, text="Eliminar", command=self.metodo)
        self.boton2.grid(column=1 , row=4, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe1, text="Modificar" ,command=self.metodo)
        self.boton3.grid(column=2, row=4, padx=4, pady=4)
        self.boton4 = ttk.Button(self.labelframe1, text="Buscar", command=self.metodo)
        self.boton4.grid(column=3, row=4, padx=4, pady=4)

    def avl(self):
        self.label1 = ttk.Label(self.labelframe2, text="Agregar:")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="w")
        self.AgregarAvl = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.AgregarAvl)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Eliminar:")
        self.label1.grid(column=0, row=1, padx=4, pady=4, sticky="w")
        self.EliminarAvl = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.EliminarAvl)
        self.entry1.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe2, text="Modificar:")
        self.label1.grid(column=0, row=2, padx=4, pady=4, sticky="w")
        self.ModificarAvl = StringVar()
        self.entry1 = ttk.Entry(self.labelframe2, width=30, textvariable=self.ModificarAvl)
        self.entry1.grid(column=1, row=2, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe2, text="Buscar:")
        self.label2.grid(column=0, row=3, padx=4, pady=4, sticky="w")
        self.BuscarAvl = StringVar()
        self.entry2 = ttk.Entry(self.labelframe2, width=30, textvariable=self.BuscarAvl)
        self.entry2.grid(column=1, row=3, padx=4, pady=4, sticky="w")

        self.boton1 = ttk.Button(self.labelframe2, text="Agregar", command=self.metodo)
        self.boton1.grid(column=0, row=4, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe2, text="Eliminar", command=self.metodo)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe2, text="Modificar", command=self.metodo)
        self.boton3.grid(column=2, row=4, padx=4, pady=4)
        self.boton4 = ttk.Button(self.labelframe2, text="Buscar", command=self.metodo)
        self.boton4.grid(column=3, row=4, padx=4, pady=4)

    def Tablas(self):
        self.label1 = ttk.Label(self.labelframe3, text="Agregar:")
        self.label1.grid(column=0, row=0, padx=4, pady=4, sticky="w")
        self.AgregarHash = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.AgregarHash)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Eliminar:")
        self.label1.grid(column=0, row=1, padx=4, pady=4, sticky="w")
        self.EliminarrHash = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.EliminarrHash)
        self.entry1.grid(column=1, row=1, padx=4, pady=4)

        self.label1 = ttk.Label(self.labelframe3, text="Modificar:")
        self.label1.grid(column=0, row=2, padx=4, pady=4, sticky="w")
        self.ModificarHash = StringVar()
        self.entry1 = ttk.Entry(self.labelframe3, width=30, textvariable=self.ModificarHash)
        self.entry1.grid(column=1, row=2, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe3, text="Buscar:")
        self.label2.grid(column=0, row=3, padx=4, pady=4, sticky="w")
        self.BuscarHash = StringVar()
        self.entry2 = ttk.Entry(self.labelframe3, width=30, textvariable=self.BuscarHash)
        self.entry2.grid(column=1, row=3, padx=4, pady=4, sticky="w")

        self.boton1 = ttk.Button(self.labelframe3, text="Agregar", command=self.metodo)
        self.boton1.grid(column=0, row=4, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe3, text="Eliminar", command=self.metodo)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)
        self.boton3 = ttk.Button(self.labelframe3, text="Modificar", command=self.metodo)
        self.boton3.grid(column=2, row=4, padx=4, pady=4)
        self.boton4 = ttk.Button(self.labelframe3, text="Buscar", command=self.metodo)
        self.boton4.grid(column=3, row=4, padx=4, pady=4)

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
        print(self.AgregarHash.get())

aplicacion1=Aplicacion()

