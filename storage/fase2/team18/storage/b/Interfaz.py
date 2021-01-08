# File:     Interface
# License:  Released under MIT License
# Notice:   Copyright (c) 2020 TytusDB Team

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from . import BMode as B

def runInterface():
        r = PP()

class PP:
#------------------------------ PANTALLA INICIAL----------------------------------#

    def __init__(self):
        self.PP = Tk()
        self.PP.resizable(True,False)
        self.PP.title("Tytus 2020")
        self.PP.geometry("1000x500")
        self.PP.configure(bg="#102027")
        self.isPantalla1 = 0
        self.isPantallaBases = 0
        self.isPantFunciones = 0
        self.isAcerca = False
        self.dell = False
        self.pantalla1()

    


    def pantalla1(self):
        if self.isPantalla1 == 1:
            self.ndb.destroy()
        elif self.isPantalla1 == 2:
            self.Funciones.destroy()
        if self.isAcerca:
            self.Acerca.destroy()
            self.isAcerca = False
        self.isPantalla1 = 0
        self.FrameInicial = Frame(height=500, width=800)
        self.FrameInicial.config(bg="#37474f")
        self.FrameInicial.pack(padx=25, pady=25)
        self.image = PhotoImage(file='team17/docs/img/usac.png')
        Label(self.FrameInicial,image=self.image, bg="#37474f").place(x=230,y=70)
        
        Label(self.FrameInicial,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Button(self.FrameInicial, text="Reportes", command=self.Reportes,font=("Times New Roman",15),fg="#000000", bg="#ff6f00",width=10).place(x=330,y=125)
        Button(self.FrameInicial, text="Funciones", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#000000",bg="#ff6f00",width=10).place(x=330,y=200)
        Button(self.FrameInicial, text="Acerca De", command=self.AcercaDe,font=("Times New Roman",15),fg="#000000",bg="#ff6f00",width=10).place(x=330,y=275)
        Button(self.FrameInicial, text="Salir", command=self.Salir,font=("Times New Roman",15),fg="#ffffff",bg="#ff3d00",width=5).place(x=10,y=400)
        Label(self.FrameInicial,text="USAC",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=315,y=375)
        self.FrameInicial.mainloop()

#---------------------------- REPORTES ---------------------------------------------#
    
    def Reportes(self):
        if self.isPantFunciones ==0:
            self.FrameInicial.destroy()
        self.isPantFunciones = 0
        self.isPantalla1 = 2
        self.Funciones = Frame(height=500, width=800)
        self.Funciones.config(bg="#37474f")
        self.Funciones.pack(padx=25, pady=25)
        Label(self.Funciones,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.Funciones,text="Reportes",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.Funciones,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        Button(self.Funciones, text="Atras", command=self.pantalla1,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=150)
        Button(self.Funciones, text="Aceptar", command=self._Reportes,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

        self.com = ttk.Combobox(self.Funciones,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _Reportes(self):
        if self.com.get() != "Seleccionar":
            self.con = ttk.Combobox(self.Funciones,state="readonly",font=("Times New Roman",15))
            Label(self.Funciones,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Button(self.Funciones, text="Aceptar", command=self.__Reportes,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)
    
    def __Reportes(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar":
            B.serializar.rollback(str(self.com.get())+"-"+str(self.con.get())+"-B").graficar()

            self.nodos = ttk.Combobox(self.Funciones,state="readonly",font=("Times New Roman",15))
            self.nodos.place(x=240,y=250)
            aux = ["Seleccionar"]
            self.o = B.serializar.rollback(str(self.com.get())+"-"+str(self.con.get())+"-B").Keys()
            for i in self.o:
                aux.append(i)
            self.nodos["values"] = aux
            self.nodos.current(0)
            Label(self.Funciones,text="Llaves: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=250)
            Button(self.Funciones, text="Aceptar", command=self.Nodo,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)

            self.win = Toplevel()
            self.win.geometry("600x600")
            self.win.configure(bg="#102027")

            self.image = Image.open('salida.png')
            self.copy = self.image.copy()
            self.foto = ImageTk.PhotoImage(self.image)
            self.label = ttk.Label(self.win, image = self.foto)
            self.label.bind('<Configure>', self.resize_image)
            self.label.pack(fill=BOTH, expand = YES)

    def Nodo(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar" and self.nodos != "Seleccionar":
            c = B.extractRow(str(self.com.get()), str(self.con.get()),self.nodos.get().split("_"))
            if c != []:
                z = ""
                for i in c:
                    z += str(i) + ", "
                z = z[:-2]
                Label(self.Funciones,text= z ,font=("Times New Roman",20),fg="black", bg="white",width=50).place(x=25,y=350)
            else:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                            title="Error")
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Error")
        
    def AccederPestanaFunciones(self):
        if self.isPantFunciones == 0:
            self.FrameInicial.destroy()
        else:
            self.ndb.destroy()
        
        self.isPantFunciones = 0
        self.isPantalla1 = 2
        self.Funciones = Frame(height=500, width=800)
        self.Funciones.config(bg="#37474f")
        self.Funciones.pack(padx=15, pady=15)
        Label(self.Funciones,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.Funciones,text="Funciones",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        #BASES DE DATOS
        Label(self.Funciones,text="Bases de Datos",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=150,y=100)

        Button(self.Funciones, text="Nueva\n BD",font=("Times New Roman",10),command = self.NewDB,fg="#102027", bg="#ff6f00",width=10).place(x=70,y=150)
        Button(self.Funciones, text="Mostrar\n BD",font=("Times New Roman",10),command = self.ShowDB,fg="#102027",bg="#ff6f00",width=10).place(x=170,y=150)
        Button(self.Funciones, text="Cambiar\n Nombre",font=("Times New Roman",10),command = self.ReDB,fg="#102027",bg="#ff6f00",width=10).place(x=270,y=150)
        Button(self.Funciones, text="Eliminar\n BD",font=("Times New Roman",10),command = self.DelBD,fg="#102027", bg="#ff6f00",width=10).place(x=170,y=200)
        
        #TABLAS
        Label(self.Funciones,text="Tablas",font=("Times New Roman",15),fg="#ffffff", bg="#37474f",width=10).place(x=550,y=100)

        Button(self.Funciones, text="Nueva \nTabla",font=("Times New Roman",10),command = self.NewTable,fg="#102027",bg="#ff6f00",width=10).place(x=470,y=150)
        Button(self.Funciones, text="Mostrar \nTablas",font=("Times New Roman",10),command = self.ShowTB,fg="#102027",bg="#ff6f00",width=10).place(x=570,y=150)
        Button(self.Funciones, text="Mostrar \nDatos",font=("Times New Roman",10),command = self.ShowData,fg="#102027",bg="#ff6f00",width=10).place(x=670,y=150)

        Button(self.Funciones, text="Rango\nTabla",font=("Times New Roman",10),command = self.RangleTB,fg="#102027",bg="#ff6f00",width=10).place(x=470,y=200)
        Button(self.Funciones, text="Agregar \nLlave Primaria",font=("Times New Roman",10),command = self.AddPK,fg="#102027",bg="#ff6f00",width=10).place(x=570,y=200)
        Button(self.Funciones, text="Eliminar \nLlave Primaria",font=("Times New Roman",10),command = self.DropPK,fg="#102027",bg="#ff6f00",width=10).place(x=670,y=200)

        Button(self.Funciones, text="Cambiar \nNombre",font=("Times New Roman",10),command = self.AlterTB,fg="#102027",bg="#ff6f00",width=10).place(x=470,y=250)
        Button(self.Funciones, text="Agregar \nColumna",font=("Times New Roman",10),command = self.AddCL,fg="#102027",bg="#ff6f00",width=10).place(x=570,y=250)
        Button(self.Funciones, text="Eliminar \nColumna",font=("Times New Roman",10),command = self.DropCL,fg="#102027",bg="#ff6f00",width=10).place(x=670,y=250)

        Button(self.Funciones, text="Eliminar \nTabla",font=("Times New Roman",10),command = self.DropTB,fg="#102027",bg="#ff6f00",width=10).place(x=570,y=300)

        #TUPLAS
        Label(self.Funciones,text="Tuplas",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=180,y=250)

        Button(self.Funciones, text="Insertar\n Tupla",font=("Times New Roman",10),command = self.insertTP,fg="#102027", bg="#ff6f00",width=10).place(x=70,y=300)
        Button(self.Funciones, text="Cargar\n CSV",font=("Times New Roman",10),command = self.CargarCSV,fg="#102027",bg="#ff6f00",width=10).place(x=170,y=300)
        Button(self.Funciones, text="Extraer\n Tupla",font=("Times New Roman",10),command =self.ExtRow,fg="#102027",bg="#ff6f00",width=10).place(x=270,y=300)

        Button(self.Funciones, text="Update\n Tupla",font=("Times New Roman",10),command =self.Up,fg="#102027", bg="#ff6f00",width=10).place(x=70,y=350)
        Button(self.Funciones, text="Eliminar\n Tupla",font=("Times New Roman",10),command =self.DeleteTP,fg="#102027", bg="#ff6f00",width=10).place(x=170,y=350)
        Button(self.Funciones, text="Truncate\n Tabla",font=("Times New Roman",10),command =self.TruncateTB,fg="#102027", bg="#ff6f00",width=10).place(x=270,y=350)
        
        #REGRESAR A PANTALLA INICIAL
        Button(self.Funciones, text="Atras", command=self.pantalla1,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=350,y=425)

#------------------------FUNCIONES DE BASES DE DATOS -----------------------#
    def NewDB(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Crear Base de Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.ndb,text="Nombre Base de Datos: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=180,y=200)
        Entry(self.ndb,textvariable=self.name,font=("Times New Roman",15),fg="black").place(x=400,y=200)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=250,y=300)
        Button(self.ndb, text="Aceptar", command=self._NewBD,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=400,y=300)

    def _NewBD(self):
        if str(self.name.get()) != "":
            a = B.createDatabase(str(self.name.get()))
            if a == 0:
                messagebox.showinfo(message="Base creada con exito\n",
                                title="BD")
            elif a==1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                                title="BD")
            elif a==2:
                messagebox.showinfo(message="La base de datos\n ya existe",
                                title="BD")
        else:
            messagebox.showinfo(message="No se ha ingresado\nningun nombre",
                                title="Nombre no ingresado")

    def ShowDB(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Mostrar Base de Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=100)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=250,y=400)
        Button(self.ndb, text="Aceptar", command=self._NewBD,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=400,y=400)

        a = B.showDatabases()
        c = 0
        d = 0
        e = 1
        for i in a:
            Label(self.ndb,text=str(e)+")  "+i,font=("Times New Roman",15),fg="white", bg="#37474f").place(x=100+d,y=150+c)
            c += 40
            e += 1
            if c == 200:
                c = 0
                d += 150

    def ReDB(self):
        if self.dell:
            self.ndb.destroy()
            self.dell = False
        else:
            self.Funciones.destroy()
        self.isPantFunciones = 1
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Renombrar Base de Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.ndb,text="Seleccione la Base de Datos: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=50,y=200)
        Label(self.ndb,text="Nuevo Nombre: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=150,y=300)

        Entry(self.ndb,textvariable=self.name,font=("Times New Roman",15),fg="black").place(x=300,y=300)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=250,y=400)
        Button(self.ndb, text="Aceptar", command=self._ReBD,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=400,y=400)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=300,y=200)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _ReBD(self):
        if str(self.com.get()) != "Seleccionar" and str(self.name.get()) != "":
            a = B.alterDatabase(str(self.com.get()),str(self.name.get()))
            if a == 0:
                messagebox.showinfo(message="Operacion realizada\ncon exito",
                                title="BD")
                self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
                self.com.place(x=300,y=200)
                aux = ["Seleccionar"]
                for i in B.showDatabases():
                    aux.append(i)
                self.com["values"] = aux
                self.com.current(0)
            elif a==1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                                title="BD")
                self.com.current(0)
            elif a==3:
                messagebox.showinfo(message="La base de datos\n ya existe",
                                title="BD")
                self.com.current(0)
            self.dell = True
            self.ReDB()
        else:
            messagebox.showinfo(message="Por favor ingrese los campos\n",
                                title="Datos Incompletos")
            self.com.current(0)

    def DelBD(self):
        if self.dell:
            self.ndb.destroy()
            self.dell = False
        else:
            self.Funciones.destroy()
        self.isPantFunciones = 1
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Eliminar Base de Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.ndb,text="Seleccione la Base de Datos: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=80,y=200)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=250,y=300)
        Button(self.ndb, text="Aceptar", command=self._DelBD,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=400,y=300)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=350,y=200)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)
    
    def _DelBD(self):
        if str(self.com.get()) != "Seleccionar":
            a = messagebox.askquestion(message="Seguro que desea eliminar la\n       Base de Datos "+str(self.com.get()+"\nesta accion no puede revertirse"),
                                title="Confirmacion")
            if a != "no":
                z = B.dropDatabase(str(self.com.get()))
                if z == 0:
                    messagebox.showinfo(message="Operacion realizada\n      con exito",
                                    title="BD")
                elif z==1:
                    messagebox.showinfo(message="Ha ocurrido un error\n",
                                    title="BD")
                self.dell = True
                self.DelBD()

            else:
                self.com.current(0)            
        else:
            messagebox.showinfo(message="Por favor ingrese los campos\n",
                                title="Datos Incompletos")
            self.com.current(0)

#-------------------------FUNCIONES DE TABLAS --------------------------------#
    def NewTable(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Crear Nueva Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        self.num = StringVar()
        Label(self.ndb,text="Seleccione la Base de Datos: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=80,y=200)
        Label(self.ndb,text="Ingrese el nombre de la Tabla: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=80,y=250)
        Label(self.ndb,text="Numero de columnas: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=120,y=300)

        Entry(self.ndb,textvariable=self.name,font=("Times New Roman",15),fg="black").place(x=350,y=250)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=250,y=400)
        Button(self.ndb, text="Aceptar", command=self._NewTable,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=400,y=400)

        Spinbox(self.ndb, from_=1,to=10000,font=("Times New Roman",15),fg="black", bg="white",state="readonly",textvariable = self.num).place(x=350,y=300)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=350,y=200)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)
    
    def _NewTable(self):
        if str(self.com.get()) != "Seleccionar" and str(self.name.get()) != "":
            a = B.createTable(str(self.com.get()),str(self.name.get()), int(self.num.get()))
            if a == 0:
                messagebox.showinfo(message="Operacion realizada\ncon exito",
                                title="BD")
            elif a==1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                                title="BD")
            elif a==3:
                messagebox.showinfo(message="La Tabla en la Base de Datos\n       ya existe",
                                title="BD")
        else:
            messagebox.showinfo(message="Por favor ingrese los campos\n",
                                title="Datos Incompletos")

    def ShowTB(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Mostrar Tablas de una Base de Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=100)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=100)
        Button(self.ndb, text="Aceptar", command=self._ShowTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=100)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=105)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _ShowTB(self):
        if str(self.com.get()) != "Seleccionar":
            self.aux = self.com.get()
            self.ndb.destroy()
            self.ndb = Frame(height=500, width=800)
            self.ndb.config(bg="#37474f")
            self.ndb.pack(padx=15, pady=15)
            Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
            Label(self.ndb,text="Mostrar Tablas de una Base de Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
            self.name = StringVar()
            Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=100)
            Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=100)
            Button(self.ndb, text="Aceptar", command=self._ShowTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=100)

            self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.com.place(x=240,y=105)
            aux = ["Seleccionar"]
            for i in B.showDatabases():
                aux.append(i)
            self.com["values"] = aux
            self.com.current(0)
            a = B.showTables(str(self.aux))
            c = 0
            d = 0
            e = 1
            for i in a:
                Label(self.ndb,text=str(e)+")  "+i,font=("Times New Roman",15),fg="white", bg="#37474f").place(x=100+d,y=150+c)
                c += 40
                e += 1
                if c == 240:
                    c = 0
                    d += 150
        else:
            messagebox.showinfo(message="Por favor ingrese los campos\n",
                            title="Datos Incompletos")
            self.com.current(0)   

    def ShowData(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Mostrar Datos de una Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=200)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=200)
        Button(self.ndb, text="Aceptar", command=self._ShowData,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=205)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _ShowData(self):
        if self.com.get() != "Seleccionar":
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=250)
            Button(self.ndb, text="Aceptar", command=self.__ShowData,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)
            self.con.place(x=240,y=250)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)
    
    def __ShowData(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar":
            self.z = B.extractTable(str(self.com.get()),str(self.con.get()))
            if self.z != None and self.z !=[]:
                self.win = Toplevel()
                self.win.geometry("600x400")
                self.win.configure(bg="#102027")
                Label(self.win,text="Tytus 2020",font=("Times New Roman",30),fg="#ffffff", bg="#102027").place(x=230,y=10)
                self.tabla = ttk.Treeview(self.win,columns = 1)
                self.tabla.grid(row=1,column=0,columnspan=1)
                self.tabla.place(x=100,y=100)
                self.tabla.heading("#0",text="No.",anchor=SW)
                self.tabla.heading("#1",text="Datos",anchor=CENTER)
                cont = len(self.z)
                for i in self.z:
                    tmp = ""
                    for j in i:
                        tmp += str(j) + ","
                    tmp = tmp[:-1]
                    tmp = tmp.replace(" ","_")
                    self.tabla.insert('',0,text=cont,values=tmp)
                    cont -= 1

            else:
                messagebox.showinfo(message="Por favor ingrese los campos o\nla tabla seleccionada no contiene Datos",
                            title="Datos Incompletos")

    def resize_image(self,event):
        self.W = event.width
        self.H = event.height
        self.image = self.copy.resize((self.W, self.H))
        self.foto = ImageTk.PhotoImage(self.image)
        self.label.config(image = self.foto)
        self.label.image = self.foto

    def RangleTB(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Extraer Rango de una Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
        
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=100)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=100)
        Button(self.ndb, text="Aceptar", command=self._RangleTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=100)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=105)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _RangleTB(self):
        if self.com.get() != "Seleccionar":
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=150)
            Button(self.ndb, text="Aceptar", command=self.__RangleTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)
            self.con.place(x=240,y=150)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)
    
    def __RangleTB(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar":
            r = B.serializar.rollback("BDD")
            a = r.dicDB[str(self.com.get())][str(self.con.get())][1]-1
            Label(self.ndb,text="Numero de Columna: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=200)
            Label(self.ndb,text="Limite Inferior: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=250)
            Label(self.ndb,text="Limite Superior: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=300)
            
            self.num = StringVar()
            self.lower = StringVar()
            self.upper = StringVar()
            if a > 0:
                self.r = Spinbox(self.ndb, from_= 0,to =a,font=("Times New Roman",15),fg="black", bg="white",state="readonly",width=10,textvariable = self.num)
            else:
                self.r = Spinbox(self.ndb, values=0,font=("Times New Roman",15),fg="black", bg="white",state="readonly",width=10,textvariable = self.num)
            self.r.place(x=300,y=202)

            Entry(self.ndb,font=("Times New Roman",15),fg="black", bg="white",width=15,textvariable = self.lower).place(x=300,y=250)
            Entry(self.ndb,font=("Times New Roman",15),fg="black", bg="white",width=15,textvariable = self.upper).place(x=300,y=300)
            Button(self.ndb, text="Aceptar", command=self.ShowRangle,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)
            
    def ShowRangle(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar":
            self.z = B.extractRangeTable(str(self.com.get()),str(self.con.get()),int(self.num.get()),self.lower.get(),self.upper.get())
            
            if self.z != None and self.z !=[]:
                self.win = Toplevel()
                self.win.geometry("600x400")
                self.win.configure(bg="#102027")
                Label(self.win,text="Tytus 2020",font=("Times New Roman",30),fg="#ffffff", bg="#102027").place(x=230,y=10)
                self.tabla = ttk.Treeview(self.win,columns = 1)
                self.tabla.grid(row=1,column=0,columnspan=1)
                self.tabla.place(x=100,y=100)
                self.tabla.heading("#0",text="No.",anchor=CENTER)
                self.tabla.heading("#1",text="Datos",anchor=CENTER)
                cont = len(self.z)
                
                for i in self.z:
                    tmp = ""
                    for j in i:
                        tmp += j + ","
                    tmp = tmp[:-1]
                    tmp = tmp.replace(" ", "_")
                    self.tabla.insert('',0,text=cont,values=tmp)
                    cont -= 1

            else:
                messagebox.showinfo(message="Por favor ingrese los campos o\nla tabla seleccionada no contiene Datos",
                            title="Datos Incompletos")

    def AddPK(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Agregar Primary Key a una Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
        
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=150)
        Button(self.ndb, text="Aceptar", command=self._AdPK,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)
        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _AdPK(self):
        if self.com.get() != "Seleccionar":
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Button(self.ndb, text="Aceptar", command=self.__AdPK,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)

    def __AdPK(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar":
            Label(self.ndb,text="Numeros de Columna: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=250)
            self.keys = StringVar()
            Entry(self.ndb,font=("Times New Roman",15),fg="black", bg="white",width=15,textvariable = self.keys).place(x=300,y=250)
            Button(self.ndb, text="Aceptar", command=self.LlaveAd,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)
    
    def LlaveAd(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar" and self.keys.get()!="":
            a = self.keys.get().split(",")
            n = []
            for i in a:
                n.append(int(i))
            c = B.alterAddPK(self.com.get(),self.con.get(),n)
            if c == 0:
                messagebox.showinfo(message="Operacion Realizada con Exito\n",
                            title="Succes")
            elif c == 1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                            title="Error")
            elif c == 2:
                messagebox.showinfo(message="La base de Datos no Existe\n",
                            title="Base de Datos no Existe")
            elif c == 3:
                messagebox.showinfo(message="La Tabla no existe\n",
                            title="Tabla no Existe")
            elif c == 4:
                messagebox.showinfo(message="Llave primaria existente\n",
                            title="Primary Key")
            elif c == 5:
                messagebox.showinfo(message="Columnas Fuera de Rango\n",
                            title="Columns out range")

    def DropPK(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Eiminar Primary Key de una Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
        
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=150)
        Button(self.ndb, text="Aceptar", command=self._DropPK,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _DropPK(self):
        if self.com.get() != "Seleccionar":
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Button(self.ndb, text="Aceptar", command=self.__DropPK,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)

    def __DropPK(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar":
            c = B.alterDropPK(self.com.get(),self.con.get())
            if c == 0:
                messagebox.showinfo(message="Operacion Realizada con Exito\n",
                            title="Succes")
            elif c == 1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                            title="Error")
            elif c == 2:
                messagebox.showinfo(message="La base de Datos no Existe\n",
                            title="Base de Datos no Existe")
            elif c == 3:
                messagebox.showinfo(message="La Tabla no existe\n",
                            title="Tabla no Existe")
            elif c == 4:
                messagebox.showinfo(message="Llave primaria no existente\n",
                            title="Not Primary Key")

    def AlterTB(self):
        if self.dell:
            self.ndb.destroy()
            self.dell = False
        else:
            self.Funciones.destroy()
        self.isPantFunciones = 1
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Cambiar nombre a una Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
        
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=150)
        Button(self.ndb, text="Aceptar", command=self._AlterTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _AlterTB(self):
        if self.com.get() != "Seleccionar":
            self.name = StringVar()
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Label(self.ndb,text="Nuevo Nombre: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=250)
            Button(self.ndb, text="Aceptar", command=self.__AlterTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=225)
            Entry(self.ndb,font=("Times New Roman",15),fg="black", bg="white",width=20,textvariable = self.name).place(x=250,y=250)
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)

    def __AlterTB(self):
        if self.com.get() != "Seleccionar" and self.con.get()!="Seleccionar" and self.name.get()!="":
            c = B.alterTable(self.com.get(),self.con.get(),self.name.get())
            if c == 0:
                messagebox.showinfo(message="Operacion Realizada con Exito\n",
                            title="Succes")
            elif c == 1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                            title="Error")
            elif c == 2:
                messagebox.showinfo(message="La base de Datos no Existe\n",
                            title="Base de Datos no Existe")
            elif c == 3:
                messagebox.showinfo(message="La Tabla no existe\n",
                            title="Tabla no Existe")
            self.dell = True
            self.AlterTB()
    
    def AddCL(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Agregar una columna una Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
        
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=150)
        Button(self.ndb, text="Aceptar", command=self._AddCl,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)
        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _AddCl(self):
        if self.com.get() != "Seleccionar":
            self.name = StringVar()
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Button(self.ndb, text="Aceptar", command=self.__AddCl,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0) 

    def __AddCl(self):
        if self.com.get() != "Seleccionar" and self.con.get()!="Seleccionar":
            self.addcol = StringVar()
            Label(self.ndb,text="Dato a ingresar: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=250)
            Entry(self.ndb,font=("Times New Roman",15),fg="black", bg="white",width=20,textvariable = self.addcol).place(x=250,y=250)
            Button(self.ndb, text="Aceptar", command=self.AddColumna,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)

    def AddColumna(self):
        if self.com.get() != "Seleccionar" and self.con.get()!="Seleccionar" and self.addcol.get()!="":
            c = B.alterAddColumn(self.com.get(),self.con.get(),self.addcol.get())
            if c == 0:
                messagebox.showinfo(message="Operacion Realizada con Exito\n",
                            title="Succes")
            elif c == 1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                            title="Error")
            elif c == 2:
                messagebox.showinfo(message="La base de Datos no Existe\n",
                            title="Base de Datos no Existe")
            elif c == 3:
                messagebox.showinfo(message="La Tabla no existe\n",
                            title="Tabla no Existe")
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Error")

    def DropCL(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Eliminar una columna una Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
        
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=150)
        Button(self.ndb, text="Aceptar", command=self._DropCL,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _DropCL(self):
        if self.com.get() != "Seleccionar":
            self.name = StringVar()
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Button(self.ndb, text="Aceptar", command=self.__DropCL,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0) 

    def __DropCL(self):
        if self.com.get() != "Seleccionar" and self.con.get()!="Seleccionar":
            a = B.b.dicDB[str(self.com.get())][str(self.con.get())][1]
            self.dropcl = StringVar()
            Label(self.ndb,text="Columna: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=125,y=250)
            Spinbox(self.ndb,from_=0,to=a-1,font=("Times New Roman",15),fg="black", bg="white",width=20,textvariable = self.dropcl).place(x=250,y=250)
            Button(self.ndb, text="Aceptar", command=self.DeleteCol,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)

    def DeleteCol(self):
        if self.com.get() != "Seleccionar" and self.con.get()!="Seleccionar" and self.dropcl.get()!="":
            c = B.alterDropColumn(self.com.get(),self.con.get(),int(self.dropcl.get()))
            if c == 0:
                messagebox.showinfo(message="Operacion Realizada con Exito\n",
                            title="Succes")
            elif c == 1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                            title="Error")
            elif c == 2:
                messagebox.showinfo(message="La base de Datos no Existe\n",
                            title="Base de Datos no Existe")
            elif c == 3:
                messagebox.showinfo(message="La Tabla no existe\n",
                            title="Tabla no Existe")

        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Error")

    def DropTB(self):
        if self.dell:
            self.ndb.destroy()
            self.dell = False
        else:
            self.Funciones.destroy()
        self.isPantFunciones = 1
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Eliminar una Tabla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
        
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=200)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=300,y=350)
        Button(self.ndb, text="Aceptar", command=self._DropTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=205)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _DropTB(self):
        if self.com.get() != "Seleccionar":
            self.name = StringVar()
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=250)
            Button(self.ndb, text="Aceptar", command=self.__DropTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=250)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0) 

    def __DropTB(self):
        if self.com.get() != "Seleccionar" and self.con.get()!="Seleccionar":
            a = messagebox.askquestion(message="Seguro que desea eliminar la\n   Tabla"+str(self.con.get()+"\nesta accion no puede revertirse"),
                                title="Confirmacion")
            if a != "no":
                c = B.dropTable(self.com.get(),self.con.get())
                if c == 0:
                    messagebox.showinfo(message="Operacion Realizada con Exito\n",
                                title="Succes")
                elif c == 1:
                    messagebox.showinfo(message="Ha ocurrido un error\n",
                                title="Error")
                elif c == 2:
                    messagebox.showinfo(message="La base de Datos no Existe\n",
                                title="Base de Datos no Existe")
                elif c == 3:
                    messagebox.showinfo(message="La Tabla no existe\n",
                                title="Tabla no Existe")
                self.dell = True
                self.DropTB()
            else:
                self.con.current(0)
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Error")

#--------------------------FUNCIONES DE TUPLAS ------------------------#
    def insertTP(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Insertar una tupla",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)
        
        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=650,y=150)
        Button(self.ndb, text="Aceptar", command=self._insertTP,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _insertTP(self):
        if self.com.get() != "Seleccionar":
            self.tupla = StringVar()
            Label(self.ndb,text="Tablas: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Label(self.ndb,text="Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=250)
            Button(self.ndb, text="Aceptar", command=self.__insert,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            Entry(self.ndb,font=("Times New Roman",15),fg="black", bg="white",width=20,textvariable = self.tupla).place(x=250,y=250)
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)

    def __insert(self):
        if self.com.get() != "Seleccionar" and self.con.get()!="Seleccionar" and self.tupla.get()!="":
            a = self.tupla.get().split(",")
            c = B.insert(self.com.get(),self.con.get(),a)
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
                messagebox.showinfo(message="Llave primaria duplicada\n",
                            title="Duplicate Primay Key")
            elif c == 5:
                messagebox.showinfo(message="Columnas fuera de limites\n",
                            title="Columns out range")
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Something's wrong")

    def CargarCSV(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Cargar un archivo",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=300,y=350)
        Button(self.ndb, text="Aceptar", command=self._CargarCSV,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

    def _CargarCSV(self):
        if self.com.get() != "Seleccionar":
            self.name = StringVar()
            Label(self.ndb,text="Tabla: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=200)
            Label(self.ndb,text="Archivo: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=250)
            Button(self.ndb, text="Aceptar", command=self.__CargarCSV,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=225)
            Entry(self.ndb,font=("Times New Roman",15),fg="black", bg="white",width=20,textvariable = self.name).place(x=250,y=250)
            
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)

    def __CargarCSV(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Selecionar" and self.name.get() != "":
            z = B.loadCSV(str(self.name.get()),str(self.com.get()),str(self.con.get()))
            succes = False
            for c in z:
                if c == 0:
                    succes = True
                elif c == 1:
                    messagebox.showinfo(message="Ha ocurrido un error\n  en una fila",
                                title="Error")
                elif c == 2:
                    messagebox.showinfo(message="La base de Datos no Existe\n",
                                title="Data Base does not exist")
                elif c == 3:
                    messagebox.showinfo(message="La Tabla no existe\n",
                                title="Table does not exist")
                elif c == 4:
                    messagebox.showinfo(message="Llave primaria duplicada\n en una fila",
                                title="Duplicate Primay Key")
                elif c == 5:
                    messagebox.showinfo(message="Columnas fuera de limites\n de una fila",
                                title="Columns out range")
            if succes:
                messagebox.showinfo(message="Operacion realizada con exito\n",
                                title="Succes")
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Something's wrong")

    def ExtRow(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Extraer una Fila",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=300,y=400)
        Button(self.ndb, text="Aceptar", command=self._ExtRow,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

    def _ExtRow(self):
        if self.com.get() != "Seleccionar":
            self.colums = StringVar()
            Label(self.ndb,text="Tabla: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=200)
            Button(self.ndb, text="Aceptar", command=self.ExR,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)

    def ExR(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Selecionar":
            Label(self.ndb,text="Llaves: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=250)
            self.nodos = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.nodos.place(x=240,y=250)
            aux = ["Seleccionar"]
            self.o = B.serializar.rollback(str(self.com.get())+"-"+str(self.con.get())+"-B").Keys()
            for i in self.o:
                aux.append(i)
            self.nodos["values"] = aux
            self.nodos.current(0)
            Button(self.ndb, text="Aceptar", command=self.__ExtRow,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)

    def __ExtRow(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Selecionar" and self.nodos.get() != "":
            a = str(self.nodos.get())
            k = a.split("_")
            c = B.extractRow(str(self.com.get()),str(self.con.get()),k)
            if c != []:
                z = ""
                for i in c:
                    z += str(i) + ", "
                z = z[:-2]
                Label(self.ndb,text= z ,font=("Times New Roman",20),fg="black", bg="white",width=50).place(x=25,y=310)
            else:
                messagebox.showinfo(message="Fila vacia\n",
                            title="Empty Row")
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Something's wrong")
    
    def Up(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Actualizar una Fila",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=300,y=400)
        Button(self.ndb, text="Aceptar", command=self._Up,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

    def _Up(self):
        if self.com.get() != "Seleccionar":
            Label(self.ndb,text="Tabla: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Button(self.ndb, text="Aceptar",font=("Times New Roman",15),command = self.__Up,fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)
    
    def __Up(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Selecionar":
            
            self.register = StringVar()
            self.nodos = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.nodos.place(x=240,y=250)
            aux = ["Seleccionar"]
            self.o = B.serializar.rollback(str(self.com.get())+"-"+str(self.con.get())+"-B").Keys()
            for i in self.o:
                aux.append(i)
            self.nodos["values"] = aux
            self.nodos.current(0)
            Label(self.ndb,text="Llaves: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=250)
            Label(self.ndb,text="Registro: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=140,y=300)
            Entry(self.ndb,font=("Times New Roman",15),fg="black", bg="white",width=20,textvariable = self.register).place(x=250,y=305)
            Button(self.ndb, text="Aceptar", command=self.Upp,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=275)
            
    def Upp(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Selecionar" and self.nodos!="Seleccionar" and self.register!="":
            a = self.register.get()
            b = a.split(",")
            c = []
            dic = {}
            for i in b:
                c.append(i.split(":"))
            for i in c:
                dic[int(i[0])] = str(i[1])
            d = str(self.nodos.get()) # Se hace casteo porque daba error hacer el split directo
            e = d.split(",")
            z = B.update(str(self.com.get()),str(self.con.get()),dic,e)
            if z == 0:
                messagebox.showinfo(message="Operacion Realizada con Exito\n",
                            title="Succes")
            elif z == 1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                            title="Error")
            elif z == 2:
                messagebox.showinfo(message="La base de Datos no Existe\n",
                            title="Data Base does not exist")
            elif z == 3:
                messagebox.showinfo(message="La Tabla no existe\n",
                            title="Table does not exist")
            elif z == 4:
                messagebox.showinfo(message="Llave primaria no existe\n",
                            title="Primay Key does not exist")
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Something's wrong")

    def DeleteTP(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Eliminar una Fila",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=300,y=400)
        Button(self.ndb, text="Aceptar", command=self._DeleteTP,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)

    def _DeleteTP(self):
        if self.com.get() != "Seleccionar":
            self.register = StringVar()
            Label(self.ndb,text="Tabla: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            
            Button(self.ndb, text="Aceptar",font=("Times New Roman",15),command = self.__DeleteTP,fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)

    def __DeleteTP(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar":
            self.nodos = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.nodos.place(x=240,y=250)
            aux = ["Seleccionar"]
            self.o = B.serializar.rollback(str(self.com.get())+"-"+str(self.con.get())+"-B").Keys()
            for i in self.o:
                aux.append(i)
            self.nodos["values"] = aux
            self.nodos.current(0)
            Label(self.ndb,text="Llaves: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=250)
            Button(self.ndb, text="Aceptar", command=self.F,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=250)

    def F(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar" and self.nodos.get()!="Seleccionar":
            a = messagebox.askquestion(message="Seguro que desea eliminar la\n       la fila "+str(self.nodos.get()+"\nesta accion no puede revertirse"),
                                title="Confirmacion")
            if a != "no":
                z = B.delete(str(self.com.get()), str(self.con.get()),self.nodos.get().split("_"))
                if z == 0:
                    messagebox.showinfo(message="Operacion Realizada con Exito\n",
                                title="Succes")
                elif z == 1:
                    messagebox.showinfo(message="Ha ocurrido un error\n",
                                title="Error")
                elif z == 2:
                    messagebox.showinfo(message="La base de Datos no Existe\n",
                                title="Data Base does not exist")
                elif z == 3:
                    messagebox.showinfo(message="La Tabla no existe\n",
                                title="Table does not exist")
                elif z == 4:
                    messagebox.showinfo(message="Llave primaria no existe\n",
                                title="Primay Key does not exist")
            else:
                self.nodos.current(0)
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Something's wrong")

    def TruncateTB(self):
        if self.dell:
            self.ndb.destroy()
            self.dell = False
        else:
            self.Funciones.destroy()
        self.isPantFunciones = 1
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Eliminar una Fila",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.ndb,text="Bases de Datos: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=50,y=150)
        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=240,y=155)
        aux = ["Seleccionar"]
        for i in B.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=300,y=300)
        Button(self.ndb, text="Aceptar", command=self._TruncateTB,font=("Times New Roman",15),fg="#102027",bg="#ff6f00",width=10).place(x=500,y=150)
    
    def _TruncateTB(self):
        if self.com.get() != "Seleccionar":
            self.register = StringVar()
            Label(self.ndb,text="Tabla: ",font=("Times New Roman",20),fg="#ffffff", bg="#37474f").place(x=150,y=200)
            Button(self.ndb, text="Aceptar",font=("Times New Roman",15),command = self.__TruncateTB,fg="#102027",bg="#ff6f00",width=10).place(x=500,y=200)
            
            self.con = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
            self.con.place(x=240,y=200)
            aux = ["Seleccionar"]
            for i in B.showTables(str(self.com.get())):
                aux.append(i)
            self.con["values"] = aux
            self.con.current(0)

    def __TruncateTB(self):
        if self.com.get() != "Seleccionar" and self.con.get() != "Seleccionar":
            a = messagebox.askquestion(message="Seguro que desea eliminar\n       todos los registros de \n"+str(self.con.get()+"\n   esta accion no puede revertirse"),
                                title="Confirmacion")
            if a != "no":
                z = B.truncate(str(self.com.get()), str(self.con.get()))
                if z == 0:
                    messagebox.showinfo(message="Operacion Realizada con Exito\n",
                                title="Succes")
                elif z == 1:
                    messagebox.showinfo(message="Ha ocurrido un error\n",
                                title="Error")
                elif z == 2:
                    messagebox.showinfo(message="La base de Datos no Existe\n",
                                title="Data Base does not exist")
                elif z == 3:
                    messagebox.showinfo(message="La Tabla no existe\n",
                                title="Table does not exist")
                self.dell = True
                self.TruncateTB()
            else:
                self.con.current(0)
        else:
            messagebox.showinfo(message="Algo anda mal\n",
                            title="Something's wrong")

    def AcercaDe(self):
        self.FrameInicial.destroy()
        self.isAcerca = True
        self.isPantFunciones = 0
        self.Acerca = Frame(height=500, width=800)
        self.Acerca.config(bg="#37474f")
        self.Acerca.pack(padx=15, pady=15)
        self.t3 = PhotoImage(file="team17/docs/img/t3.png")
        Label(self.Acerca, image = self.t3, bg="#37474f").place(x=575,y=300)
        Label(self.Acerca,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.Acerca,text="Acerca De",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        Label(self.Acerca,text="Universidad San Carlos de Guatemala",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=100)
        Label(self.Acerca,text="Facultad de Ingeniera",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=125)
        Label(self.Acerca,text="Escuela de Ciencias y Sistemas",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=150)
        Label(self.Acerca,text="Estructuras de Datos",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=175)
        Label(self.Acerca,text="Ing. Luis Espino",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=200)
        Label(self.Acerca,text="Aux. Andree Avalos",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=225)

        Label(self.Acerca,text="Programadadores: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=250,y=265)
        Label(self.Acerca,text="Adrian Samuel Molina Cabrera",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=300,y=300)
        Label(self.Acerca,text="Diego Andrés Obín Rosales",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=300,y=325)
        Label(self.Acerca,text="German José Paz Cordón",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=300,y=350)
        Button(self.Acerca,text="Atras",font=("Times New Roman",15),fg="black",bg="white",command=self.pantalla1, width=10).place(x=325,y=400)

#--------------------------------SALIR----------------------------------------#
    def Salir(self):
        messagebox.showinfo(message="Hasta la proximaaaa\n",title="Exit")
        self.PP.destroy()
