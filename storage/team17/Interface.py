from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from DataBase import *

class PP:
    b = DB()
    def __init__(self):
        self.PP = Tk()
        self.PP.resizable(True,False)
        self.PP.title("Tytus 2020")
        self.PP.geometry("1000x500")
        self.PP.configure(bg="#102027")
        self.isPantalla1 = 0
        self.isPantallaBases = 0
        self.isPantFunciones = 0
        self.pantalla1()

    def pantalla1(self):
        if self.isPantalla1 == 1:
            self.FrameBases.destroy()
        elif self.isPantalla1 == 2:
            self.Funciones.destroy()
        self.isPantalla1 = 0
        self.FrameInicial = Frame(height=500, width=800)
        self.FrameInicial.config(bg="#37474f")
        self.FrameInicial.pack(padx=25, pady=25)

        Label(self.FrameInicial,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Button(self.FrameInicial, text="Ingresar a una base de datos", command=self.AccederPestanaBases,font=("Times New Roman",15),fg="#102027", bg="#ff6f00").place(x=270,y=150)
        Button(self.FrameInicial, text="Opción funciones", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=305,y=225)
        Label(self.FrameInicial,text="USAC",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=300,y=350)
        self.FrameInicial.mainloop()

    def AccederPestanaBases(self):
        self.FrameInicial.destroy()
        self.isPantalla1 = 1

        if self.isPantallaBases != 0:
            self.FrameTablas.destroy()

        self.isPantallaBases = 0
        self.FrameBases = Frame(height=500, width=800)
        self.FrameBases.config(bg="#37474f")
        self.FrameBases.pack(padx=25, pady=25)

        Label(self.FrameBases,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.FrameBases,text="Bases De Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.BasesBox = ttk.Combobox(self.FrameBases,state="readonly",font=("Times New Roman",15))
        self.BasesBox.place(x=260,y=150)
        aux = ["Seleccionar"]
        for i in b.showDatabases():
            aux.append(i)
        self.BasesBox["values"] = aux
        self.BasesBox.current(0)
        
        Button(self.FrameBases, text="Aceptar", command=self.AccederPestanaTablas,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=360,y=225)

        Button(self.FrameBases, text="Atras", command=self.pantalla1,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=275,y=225)

    def AccederPestanaTablas(self):
        if self.BasesBox.get() != "Seleccionar":
            bd = str(self.BasesBox.get())
            self.FrameBases.destroy()
            self.isPantallaBases = 1

            self.FrameTablas = Frame(height=500, width=800)
            self.FrameTablas.config(bg="#37474f")
            self.FrameTablas.pack(padx=25, pady=25)

            Label(self.FrameTablas,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
            Label(self.FrameTablas,text="Tablas",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

            self.TablasBox = ttk.Combobox(self.FrameTablas, state="readonly",font=("Times New Roman",15))
            self.TablasBox.place(x=260,y=150)
            aux = ["Seleccionar"]
            aux2 = b.showTables(bd)
            for i in aux2:
                aux.append(i)
            self.TablasBox["values"] = aux
            self.TablasBox.current(0)

            # Button(self.FrameTablas, text="Aceptar", command=self.ShowTree,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=360,y=225)
            Button(self.FrameTablas, text="Atras", command=self.AccederPestanaBases,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=275,y=225)
        else:
            messagebox.showinfo(message="Debe seleccionar una base de\ndatos para poder continuar",
                                title="BD no seleccionada")

    def AccederPestanaFunciones(self):
        if self.isPantFunciones ==0:
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

        Button(self.Funciones, text="Eliminar \nTabla",font=("Times New Roman",10),fg="#102027",bg="#ff6f00",width=10).place(x=570,y=300)

        #TUPLAS
        Label(self.Funciones,text="Tuplas",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=180,y=250)

        Button(self.Funciones, text="Insertar\n Tupla",font=("Times New Roman",10),fg="#102027", bg="#ff6f00",width=10).place(x=70,y=300)
        Button(self.Funciones, text="Cargar\n CSV",font=("Times New Roman",10),fg="#102027",bg="#ff6f00",width=10).place(x=170,y=300)
        Button(self.Funciones, text="Extraer\n Tupla",font=("Times New Roman",10),fg="#102027",bg="#ff6f00",width=10).place(x=270,y=300)

        Button(self.Funciones, text="Update\n Tupla",font=("Times New Roman",10),fg="#102027", bg="#ff6f00",width=10).place(x=70,y=350)
        Button(self.Funciones, text="Eliminar\n Tupla",font=("Times New Roman",10),fg="#102027", bg="#ff6f00",width=10).place(x=170,y=350)
        Button(self.Funciones, text="Truncate\n Tabla",font=("Times New Roman",10),fg="#102027", bg="#ff6f00",width=10).place(x=270,y=350)
        
        #REGRESAR A PANTALLA INICIAL
        Button(self.Funciones, text="Atras", command=self.pantalla1,font=("Times New Roman",15),fg="#102027",bg="red",width=10).place(x=350,y=425)

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

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red").place(x=300,y=300)
        Button(self.ndb, text="Aceptar", command=self._NewBD,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=400,y=300)

    def _NewBD(self):
        if str(self.name.get()) != "":
            a = b.createDatabase(str(self.name.get()))
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
        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red").place(x=300,y=400)
        Button(self.ndb, text="Aceptar", command=self._NewBD,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=400,y=400)

        a = b.showDatabases()
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
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Renombrar Base de Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.ndb,text="Seleccione la Base de Datos: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=50,y=200)
        Label(self.ndb,text="Nuevo Nombre: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=150,y=300)

        Entry(self.ndb,textvariable=self.name,font=("Times New Roman",15),fg="black").place(x=300,y=300)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red").place(x=300,y=400)
        Button(self.ndb, text="Aceptar", command=self._ReBD,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=400,y=400)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=300,y=200)
        aux = ["Seleccionar"]
        for i in b.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)

    def _ReBD(self):
        if str(self.com.get()) != "Seleccionar" and str(self.name.get()) != "":
            a = b.alterDatabase(str(self.com.get()),str(self.name.get()))
            if a == 0:
                messagebox.showinfo(message="Operacion realizada\ncon exito",
                                title="BD")
                self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
                self.com.place(x=300,y=200)
                aux = ["Seleccionar"]
                for i in b.showDatabases():
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
        else:
            messagebox.showinfo(message="Por favor ingrese los campos\n",
                                title="Datos Incompletos")
            self.com.current(0)

    def DelBD(self):
        self.isPantFunciones = 1
        self.Funciones.destroy()
        self.ndb = Frame(height=500, width=800)
        self.ndb.config(bg="#37474f")
        self.ndb.pack(padx=15, pady=15)
        Label(self.ndb,text="Tytus 2020",font=("Times New Roman",40),fg="#ffffff", bg="#37474f").place(x=250,y=10)
        Label(self.ndb,text="Eliminar Base de Datos",font=("Times New Roman",10),fg="#ffffff", bg="#37474f").place(x=250,y=70)

        self.name = StringVar()
        Label(self.ndb,text="Seleccione la Base de Datos: ",font=("Times New Roman",15),fg="#ffffff", bg="#37474f").place(x=80,y=200)

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red").place(x=300,y=300)
        Button(self.ndb, text="Aceptar", command=self._DelBD,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=400,y=300)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=350,y=200)
        aux = ["Seleccionar"]
        for i in b.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)
    
    def _DelBD(self):
        if str(self.com.get()) != "Seleccionar":
            a = messagebox.askquestion(message="Seguro que desea eliminar la\n       Base de Datos "+str(self.com.get()+"\nesta accion no puede revertirse"),
                                title="Confirmacion")
            if a != "no":
                z = b.dropDatabase(str(self.com.get()))
                if z == 0:
                    messagebox.showinfo(message="Operacion realizada\n      con exito",
                                    title="BD")
                    self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
                    self.com.place(x=300,y=200)
                    aux = ["Seleccionar"]
                    for i in b.showDatabases():
                        aux.append(i)
                    self.com["values"] = aux
                    self.com.current(0)
                elif z==1:
                    messagebox.showinfo(message="Ha ocurrido un error\n",
                                    title="BD")
                    self.com.current(0)
            else:
                self.com.current(0)            
        else:
            messagebox.showinfo(message="Por favor ingrese los campos\n",
                                title="Datos Incompletos")
            self.com.current(0)

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

        Button(self.ndb, text="Atras", command=self.AccederPestanaFunciones,font=("Times New Roman",15),fg="#102027",bg="red").place(x=300,y=400)
        Button(self.ndb, text="Aceptar", command=self._NewTable,font=("Times New Roman",15),fg="#102027",bg="#ff6f00").place(x=400,y=400)

        Spinbox(self.ndb, from_=1,to=10000,font=("Times New Roman",15),fg="black", bg="white",state="readonly",textvariable = self.num).place(x=350,y=300)

        self.com = ttk.Combobox(self.ndb,state="readonly",font=("Times New Roman",15))
        self.com.place(x=350,y=200)
        aux = ["Seleccionar"]
        for i in b.showDatabases():
            aux.append(i)
        self.com["values"] = aux
        self.com.current(0)
    
    def _NewTable(self):
        if str(self.com.get()) != "Seleccionar" and str(self.name.get()) != "":
            a = b.createTable(str(self.com.get()),str(self.name.get()), int(self.num.get()))
            if a == 0:
                messagebox.showinfo(message="Operacion realizada\ncon exito",
                                title="BD")
                self.com.current(0)
            elif a==1:
                messagebox.showinfo(message="Ha ocurrido un error\n",
                                title="BD")
                self.com.current(0)
            elif a==3:
                messagebox.showinfo(message="La Tabla en la Base de Datos\n       ya existe",
                                title="BD")
                self.com.current(0)
        else:
            messagebox.showinfo(message="Por favor ingrese los campos\n",
                                title="Datos Incompletos")
            self.com.current(0)  
