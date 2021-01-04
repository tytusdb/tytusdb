import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Windows5
import os
import ISAMMode as j

class Ventana(tk.Toplevel):
    def __init__(self, parent,namebase,nametable):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 7")
        self.namebase=namebase
        self.nametable=nametable
        label1 = Label(self,text=self.namebase + " --- "+self.nametable)
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)
        self.graficotupla(namebase,nametable)
        label2 = Label(self,text="¡ FUNCIONES EN TUPLAS ! ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)
        boton1 = tk.Button(self, text="insertar", width=20, command=self.insertar)
        boton1.grid(row=5, column=2, padx=20, pady=30)
        boton2 = tk.Button(self, text="extractRow", width=20, command=self.extractRow)
        boton2.grid(row=5, column=3, padx=20, pady=30)
        boton3 = tk.Button(self, text="update", width=20, command=self.update)
        boton3.grid(row=5, column=4, padx=20, pady=30)
        boton4 = tk.Button(self, text="truncate", width=20, command=self.truncate)
        boton4.grid(row=5, column=5, padx=20, pady=30)
        boton5 = tk.Button(self, text="DELETe", width=20, command=self.delete)
        boton5.grid(row=6, column=2, padx=20, pady=30)
        label3 = Label(self,text="\nInsert Parameters")
        label3.config(font=("Verdana", 12))
        label3.grid(row=9, column=3)  
        
        boton = tk.Button(self, text="Atras", width=20, command=self.atras)
        boton.grid(row=16, column=1, padx=20, pady=30)
        if os.path.exists("grafotupla.png"):
            img=Image.open("grafotupla.png")
            img.show()
        self.parent.withdraw()

    def atras(self):
        self.destroy()
        print(self.namebase)
        Windows5.Ventana(self.parent,self.namebase)
        
    def close(self):
        self.parent.destroy()
    
    def insertar(self):        
        self.b=tk.StringVar() 
        j=Label(self,text="DataBase")
        j.grid(row=11,column=0)
        base=Entry(self, width=15,textvariable=self.b)
        base.grid(row=11,column=1)
        self.t=tk.StringVar() 
        jt=Label(self,text="Table")
        jt.grid(row=12,column=0)
        tablita=Entry(self, width=15,textvariable=self.t)
        tablita.grid(row=12,column=1)
        self.l=tk.StringVar() 
        jl=Label(self,text="Register")
        jl.grid(row=13,column=0)
        lista=Entry(self, width=15,textvariable=self.l)
        lista.grid(row=13,column=1)

        boton22 = tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.insertar1(base.get(),tablita.get(),lista.get()))
        boton22.grid(row=16, column=3, padx=20, pady=30)

    def verificadorlista(self,string):
        b1=False
        b2=False
        converterlist=''
        for i in string:
            if i=="[":
                b1=True
            elif i=="]":
                b2=True
            else:
                converterlist+=i
        if b1 and b2 :
            numero=[]
            lista=converterlist.split(",")  
            for i in lista:
                numero.append(i)
            print(numero)
            return numero
        else:
            return string
        

    def extractRow(self):
        self.b=tk.StringVar() 
        j=Label(self,text="DataBase")
        j.grid(row=11,column=0)
        base=Entry(self, width=15,textvariable=self.b)
        base.grid(row=11,column=1)
        self.t=tk.StringVar() 
        jt=Label(self,text="Table")
        jt.grid(row=12,column=0)
        tablita=Entry(self, width=15,textvariable=self.t)
        tablita.grid(row=12,column=1)
        self.l=tk.StringVar() 
        jl=Label(self,text="Column")
        jl.grid(row=13,column=0)
        lista=Entry(self, width=15,textvariable=self.l)
        lista.grid(row=13,column=1)
        boton33= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.extractRow1(base.get(),tablita.get(),lista.get()))
        boton33.grid(row=16, column=3, padx=20, pady=30)

    def update(self):
        j=Label(self,text="DataBase")
        j.grid(row=11,column=0)
        base=Entry(self, width=15)
        base.grid(row=11,column=1)
        jt=Label(self,text="Table")
        jt.grid(row=12,column=0)
        tablita=Entry(self, width=15)
        tablita.grid(row=12,column=1)
        jl=Label(self,text="Register")
        jl.grid(row=13,column=0)
        lista=Entry(self, width=15)
        lista.grid(row=13,column=1)
        jdl=Label(self,text='ingresa tu diccionario sin llaves "{" "}"  ')
        jdl.grid(row=13,column=2)
        l=Label(self,text="Columns")
        l.grid(row=14,column=0)
        columns=Entry(self, width=15)
        columns.grid(row=14,column=1)

        #revisar
        register=lista.get()
        colum=columns.get()
        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.update1(base.get(),tablita.get(),register.rsplit(","),colum.rsplit(",")))
        boton34.grid(row=16, column=3, padx=20, pady=30)

    def truncate(self):
        j=Label(self,text="DataBase")
        j.grid(row=11,column=0)
        base=Entry(self, width=15)
        base.grid(row=11,column=1)
        jt=Label(self,text="Table")
        jt.grid(row=12,column=0)
        tablita=Entry(self, width=15)
        tablita.grid(row=12,column=1)
        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.truncate1(base.get(),tablita.get()))
        boton34.grid(row=16, column=3, padx=20, pady=30)


    def delete(self):
        self.b=tk.StringVar() 
        j=Label(self,text="DataBase")
        j.grid(row=11,column=0)
        base=Entry(self, width=15,textvariable=self.b)
        base.grid(row=11,column=1)
        self.t=tk.StringVar() 
        jt=Label(self,text="Table")
        jt.grid(row=12,column=0)
        tablita=Entry(self, width=15,textvariable=self.t)
        tablita.grid(row=12,column=1)
        self.l=tk.StringVar() 
        jl=Label(self,text="Column")
        jl.grid(row=13,column=0)
        lista=Entry(self, width=15,textvariable=self.l)
        lista.grid(row=13,column=1)
        boton33= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.delete1(self.b,self.t,self.l))
        boton33.grid(row=16, column=3, padx=20, pady=30)



    def insertar1(self,base,tabla,arreglo):    
        lista=self.verificadorlista(arreglo)    
        messagebox.showinfo("Funcion de base de datos",str(j.insert(base,tabla,lista)))
        print(j.extractTable(base,tabla)) 

    def extractRow1(self,base,tabla,columna):
        lista=self.verificadorlista(columna)
        messagebox.showinfo("Funcion de base de datos",str(j.extractRow(base,tabla,lista)))

    def update1(self,data,table,register,columns):
        registro=self.verificardiccionario(register)
        lista=self.verificadorlista(columns)
        messagebox.showinfo("Funcion de base de datos",str(j.update(data,table,registro,lista)))
   
    def truncate1(self,base,tabla):

        messagebox.showinfo("Funcion de base de datos",str(j.truncate(base,tabla)))


    def delete1(self,base,tabla,columna):
        lista=self.verificadorlista(columna)
        messagebox.showinfo("Funcion de base de datos",str(j.delete(base,tabla,lista)))


    def verificardiccionario(self,dic):

        diccionario={}
        linea=dic.split(',')
        for line in linea:
            g=line.split(":")
            diccionario[g[0]]=g[1]

        return diccionario
