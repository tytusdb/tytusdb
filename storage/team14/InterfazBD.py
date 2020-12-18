from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import StorageManager as Storage
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
        #self.vectorBases.append(valv)
        
        (Storage.createDatabase(valv))
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

