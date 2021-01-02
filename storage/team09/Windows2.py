import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox  # message box
import WindowMain
import Windows3
import ISAM as m

class Ventana2(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.basesdatos=[]
        self.tablasbase=[]
        self.b()
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
     
     #label3.place(x=0,y=0,relwidth=1.0,relheight=1.0)
        label1=Label(self, text="Cargando Datos a Tuplas ")
        label1.config(font=("Verdana",50))
        label1.grid(row=1, column=3)
        self.bases=tk.StringVar(self)
        self.bases.set("seleccione bases")
        menub = tk.OptionMenu(self, self.bases, *self.basesdatos)
        menub.config(width=20)
        menub.grid(row = 7, column = 1, padx = 30, pady = 30)
        button6 = tk.Button(self, text= 'actualizar', padx= 15, pady=6, bg= 'grey',fg='white',command=self.actualizar)
        button6.grid(row=8, column=2)
        
        
        button1 = Button(self, text= 'Atras', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana1)
        button1.grid(row=15, column=0)


        


        self.parent.withdraw()


    def actualizar(self):
        self.bio()
        self.tablas=tk.StringVar(self)
        self.tablas.set("seleccione tabla")
        
        menu = tk.OptionMenu(self, self.tablas, *self.tablasbase)
        menu.config(width=20)
        menu.grid(row = 7, column = 3, padx = 30, pady = 30)

        self.ruta= Entry(self)
        self.ruta.grid(row=8, column=3)

        act = Button(self, text= 'Cargar CSV', padx= 15, pady=6, bg= 'grey',fg='white',command=self.cargarcsv)
        act.grid(row=8, column=4)


    def cargarcsv(self):
        print(self.ruta.get()+" "+self.bases.get()+ " "+ self.tablas.get())
        print(m.loadCSV(self.ruta.get(),self.bases.get(),self.tablas.get()))
        print(m.extractTable(self.bases.get(),self.tablas.get()))
       
    def ventana1(self):
        self.parent.deiconify()
        self.destroy()

    def Ventana3(self):
        self.destroy()
        Windows3.Ventana(self.parent)
    
    def close(self):
        self.parent.destroy()

    def imagen(self):
        image= tk.PhotoImage(file="imagen.png")
        image=image.subsample(3,3)
        Label7=tk.Label(image=image)
        Label7.pack()


            
    def b(self):
        self.basesdatos.clear()
        if len(m.showDatabases())!=0:
            for k in m.showDatabases():
                self.basesdatos.append(k)
        elif len(self.basesdatos)==0:
            self.basesdatos.append("vacio")

    def bio(self):
        self.tablasbase.clear()
        if len(m.showTables(self.bases.get()))!=0:
            for k in m.showTables(self.bases.get()):
                self.tablasbase.append(k)
        elif len(self.tablasbase)==0:
            self.tablasbase.append("vacio")
