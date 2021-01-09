# File:     Interfaz
# License:  Released under MIT License
# Notice:   Copyright (c) 2020 TytusDB Team

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from storage import storageManager as f
class PP:
    
#------------------------------ PANTALLA INICIAL----------------------------------#

    def __init__(self):
        self.PP = Tk()
        self.PP.resizable(True,False)
        self.PP.title("Tytus 2020")
        self.PP.geometry("1000x500")
        self.PP.configure(bg="#102027")
        self.isPantalla1 = 0
        self.isSeguridad = False
        self.isGrafos = 0
        self.safe = False
        self.isAcerca = False
        self.dell = False
        self.pantalla1()
    
    def pantalla1(self):
        if self.isSeguridad:
            self.ndb.destroy()
        if self.isAcerca:
            self.Acerca.destroy()
            self.isAcerca = False
        self.isPantalla1 = 0
        self.FrameInicial = Frame(height=500, width=800)
        self.FrameInicial.config(bg="#37474f")
        self.FrameInicial.pack(padx=25, pady=25)
        self.image = PhotoImage(file='storage/b/docs/img/usac.png')
        Label(self.FrameInicial,image=self.image, bg="#37474f").place(x=230,y=70)
        Label(self.FrameInicial,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Button(self.FrameInicial, text="Seguridad",command=self.Seguridad,font=("Times New Roman",15),fg="#000000", bg="#ff6f00",width=10).place(x=330,y=125)
        Button(self.FrameInicial, text="Grafos",command=self.Grafos,font=("Times New Roman",15),fg="#000000",bg="#ff6f00",width=10).place(x=330,y=200)
        Button(self.FrameInicial, text="Acerca De", command=self.AcercaDe,font=("Times New Roman",15),fg="#000000",bg="#ff6f00",width=10).place(x=330,y=275)
        Button(self.FrameInicial, text="Salir", command=self.Salir,font=("Times New Roman",15),fg="#ffffff",bg="#ff3d00",width=5).place(x=10,y=400)
        Label(self.FrameInicial,text="USAC",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=315,y=375)
        self.FrameInicial.mainloop()

    def AcercaDe(self):
        self.FrameInicial.destroy()
        self.isAcerca = True
        self.isPantFunciones = 0
        self.Acerca = Frame(height=500, width=800)
        self.Acerca.config(bg="#37474f")
        self.Acerca.pack(padx=15, pady=15)
        self.t3 = PhotoImage(file="storage/b/docs/img/t3.png")
        Label(self.Acerca, image = self.t3, bg="#37474f").place(x=575,y=300)
        Label(self.Acerca,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.Acerca,text="Acerca De",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.Acerca,text="Universidad San Carlos de Guatemala",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=100)
        Label(self.Acerca,text="Facultad de Ingeniera",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=125)
        Label(self.Acerca,text="Escuela de Ciencias y Sistemas",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=150)
        Label(self.Acerca,text="Estructuras de Datos",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=175)
        Label(self.Acerca,text="Ing. Luis Espino",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=200)
        Label(self.Acerca,text="Aux. Andree Avalos",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=225)

        Label(self.Acerca,text="Programadadores: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=260)
        Label(self.Acerca,text="Adrian Samuel Molina Cabrera",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=300,y=295)
        Label(self.Acerca,text="Diego Andrés Obín Rosales",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=300,y=320)
        Label(self.Acerca,text="German José Paz Cordón",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=300,y=345)
        Label(self.Acerca,text="Pablo Josué Ayapán Vargas",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=300,y=370)
        Button(self.Acerca,text="Atras",font=("Times New Roman",15),fg="black",bg="white",command=self.pantalla1, width=10).place(x=325,y=400)

#-----------------------------------SEGURIDAD----------------------------------#

    def Seguridad(self):
        if self.safe:
            self.safe.destroy()
        self.FrameInicial.destroy()
        self.isSeguridad = True
        self.isPantFunciones = 0
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Seguridad",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Button(self.ndb, text="SafeModeOff",command=self.SafeModeOff,font=("Times New Roman",15),fg="#000000",bg="#ff6f00",width=10).place(x=230,y=210)

        Button(self.ndb, text="BlockChain",command=self.BlockChain,font=("Times New Roman",15),fg="#000000",bg="#ff6f00",width=10).place(x=430,y=210)

        Button(self.ndb, text="Atras", command=self.pantalla1,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=330,y=350)

    def SafeModeOff(self):
        self.ndb.destroy()
        self.isSafeOn = True
        self.isPantFunciones = 0
        self.safe = Frame(height=500, width=800)
        self.safe.config(bg="#37474f")
        self.safe.pack(padx=15, pady=15)
        self.database = StringVar()
        self.table = StringVar()
        Label(self.safe,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.safe,text="Safe Mode Off",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.safe,text="Base de Datos:",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=150,y=200)
        Label(self.safe,text="Tabla:",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=200,y=250)

        Entry(self.safe,textvariable=self.database,font=("Times New Roman",15),fg="black").place(x=300,y=200)
        Entry(self.safe,textvariable=self.table,font=("Times New Roman",15),fg="black").place(x=300,y=250)

        Button(self.safe, text="Atras", command=self.Seguridad,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=260,y=350)
        Button(self.safe, text="Aceptar", command=self._SafeModeOff,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=390,y=350)

    def _SafeModeOff(self):
        if str(self.database.get()) != "" and str(self.table.get()) != "":
            r = str(self.database.get())
            s = str(self.table.get())
            c = f.f.safeModeOff(r,s)
            if c == 0:
                messagebox.showinfo(message="Operacion Realizada con Exito\n",
                            title="Succes")
            elif c == 1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                            title="Error")
            elif c == 2:
                messagebox.showinfo(message="La base de Datos no Existe\n",
                            title="Data Base does not exist")
            elif c == 3:
                messagebox.showinfo(message="La Tabla no existe\n",
                            title="Table does not exist")
            elif c == 4:
                messagebox.showinfo(message="El modo seguro esta ya apagado\n",
                            title="SafeModeOff")
        else:
            messagebox.showinfo(message="Por favor ingrese todos los campos\n",
                        title="Sin datos")

    def BlockChain(self):
        self.ndb.destroy()
        self.isSafeOn = True
        self.isPantFunciones = 0
        self.safe = Frame(height=500, width=800)
        self.safe.config(bg="#37474f")
        self.safe.pack(padx=15, pady=15)
        self.database = StringVar()
        self.table = StringVar()
        Label(self.safe,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.safe,text="Safe Mode On",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.safe,text="Base de Datos:",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=150,y=200)
        Label(self.safe,text="Tabla:",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=200,y=250)

        Entry(self.safe,textvariable=self.database,font=("Times New Roman",15),fg="black").place(x=300,y=200)
        Entry(self.safe,textvariable=self.table,font=("Times New Roman",15),fg="black").place(x=300,y=250)

        Button(self.safe, text="Atras", command=self.Seguridad,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=260,y=350)
        Button(self.safe, text="Aceptar", command=self._BlockChain,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=390,y=350)

    def _BlockChain(self):
        if self.database.get() != "" and self.table.get() != "":
            a = str(self.database.get())
            b = str(self.table.get())
            c = f.f.showBlockChain(a,b)
            if c == None:
                messagebox.showinfo(message="No existen datos para graficar\n",
                        title="Sin datos")
    
#--------------------------------GRAFOS----------------------------------------#
    def Grafos(self):
        if self.safe:
            self.safe.destroy()
        self.FrameInicial.destroy()
        self.isSeguridad = True
        self.isPantFunciones = 0
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Seguridad",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Button(self.ndb, text="Base de Datos",command=self.Dsd,font=("Times New Roman",15),fg="#000000", bg="#ff6f00",width=10).place(x=200,y=200)
        Button(self.ndb, text="Tabla",command=self.Tb1,font=("Times New Roman",15),fg="#000000",bg="#ff6f00",width=10).place(x=475,y=200)

        Button(self.ndb, text="Atras", command=self.pantalla1,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=330,y=350)

    def Dsd(self):
        self.ndb.destroy()
        self.isSafeOn = True
        self.isPantFunciones = 0
        self.safe = Frame(height=500, width=800)
        self.safe.config(bg="#37474f")
        self.safe.pack(padx=15, pady=15)
        self.database = StringVar()
        self.table = StringVar()
        Label(self.safe,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.safe,text="Bases",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.safe,text="Base de Datos:",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=150,y=200)

        Entry(self.safe,textvariable=self.database,font=("Times New Roman",15),fg="black").place(x=300,y=200)

        Button(self.safe, text="Atras", command=self.Grafos,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=260,y=350)
        Button(self.safe, text="Aceptar", command=self._Dsd,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=390,y=350)

    def _Dsd(self):
        if str(self.database.get()) != "":
            r = str(self.database.get())
            c = f.f.graphDSD(r)
            if c == None:
                messagebox.showinfo(message="No existen datos para graficar\n",
                        title="Sin datos")
        else:
            messagebox.showinfo(message="Por favor ingrese todos los campos\n",
                        title="Sin datos")
    
    def Tb1(self):
        self.ndb.destroy()
        self.isSafeOn = True
        self.isPantFunciones = 0
        self.safe = Frame(height=500, width=800)
        self.safe.config(bg="#37474f")
        self.safe.pack(padx=15, pady=15)
        self.database = StringVar()
        self.table = StringVar()
        Label(self.safe,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.safe,text="Tablas",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.safe,text="Base de Datos:",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=150,y=200)
        Label(self.safe,text="Tabla:",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=200,y=250)

        Entry(self.safe,textvariable=self.database,font=("Times New Roman",15),fg="black").place(x=300,y=200)
        Entry(self.safe,textvariable=self.table,font=("Times New Roman",15),fg="black").place(x=300,y=250)

        Button(self.safe, text="Atras", command=self.Grafos,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=260,y=350)
        Button(self.safe, text="Aceptar", command=self._Tbl,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=390,y=350)

    def _Tbl(self):
        if str(self.database.get()) != "" and str(self.table.get()) != "":
            r = str(self.database.get())
            s = str(self.table.get())
            c = f.f.graphDF(r,s)
            if c == None:
                messagebox.showinfo(message="No existen datos para graficar\n",
                        title="Sin datos")

        else:
            messagebox.showinfo(message="Por favor ingrese todos los campos\n",
                        title="Sin datos")

#--------------------------------SALIR----------------------------------------#
    def Salir(self):
        self.PP.destroy()

def runInterface():
    i = PP()
