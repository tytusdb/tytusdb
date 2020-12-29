import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Windows5
import os
import ISAMMode as j

class Ventana(tk.Toplevel):
    def __init__(self, parent,namebase):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 6")
        self.namebase=namebase
        label1 = Label(self,text=self.namebase)
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        label2 = Label(self,text="¡ Select your Funtion : ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)
        boton1 = tk.Button(self, text="createTable", width=20, command=self.createTable)
        boton1.grid(row=5, column=2, padx=20, pady=30)
        boton2 = tk.Button(self, text="extractTable", width=20, command=self.extractTable)
        boton2.grid(row=5, column=3, padx=20, pady=30)
        boton3 = tk.Button(self, text="extractRangeTable", width=20, command=self.extractRangeTable)
        boton3.grid(row=5, column=4, padx=20, pady=30)
        boton4 = tk.Button(self, text="alterAddPK", width=20, command=self.alterAddPK)
        boton4.grid(row=5, column=5, padx=20, pady=30)
        boton5 = tk.Button(self, text="alterDropPK", width=20, command=self.alterDropPK)
        boton5.grid(row=6, column=2, padx=20, pady=30)
        boton6 = tk.Button(self, text="showTable", width=20, command=self.showTable)
        boton6.grid(row=6, column=3, padx=20, pady=30)
        boton7 = tk.Button(self, text="alterTable", width=20, command=self.alterTable)
        boton7.grid(row=6, column=4, padx=20, pady=30)
        boton10 = tk.Button(self, text="alterAddColumn", width=20, command=self.alteraddColumn)
        boton10.grid(row=6, column=5, padx=20, pady=30)
        boton9 = tk.Button(self, text="alterDropColumn", width=20, command=self.alterDropColumn)
        boton9.grid(row=7, column=3, padx=20, pady=30)
        boton8 = tk.Button(self, text="dropTable", width=20, command=self.dropTable)
        boton8.grid(row=7, column=4, padx=20, pady=30)
        label3 = Label(self,text="\nInsert Parameters")
        label3.config(font=("Verdana", 12))
        label3.grid(row=9, column=3)  
        

        boton = tk.Button(self, text="Atras", width=20, command=self.ventana3)
        boton.grid(row=17, column=1, padx=15, pady=30)
        
        self.parent.withdraw()

    def ventana3(self):
        self.destroy()
        Windows5.Ventana(self.parent,self.namebase)
        
    def close(self):
        self.parent.destroy()
    
    def createTable(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)
        base=Entry(self,width=15)
        base.grid(row=10,column=2)
        t=Label(self,text="Table")
        t.grid(row=11,column=1)
        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)
        n=Label(self,text="numberColumns")
        n.grid(row=12,column=1)
        ncol=Entry(self,width=15)
        ncol.grid(row=12,column=2)
        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.createTable1(base.get(),tabla.get(),int(ncol.get())))
        boton34.grid(row=16, column=3, padx=20, pady=30)
   
    def showTable(self):
        messagebox.showinfo("Funcion de base de datos",str(j.showTables(self.namebase)))
        j.graficoTablas(self.namebase)
        os.system('dot -Tpng grafoT.dot -o grafotabla.png')
        os.system('grafotabla.png')
        img=Image.open("grafotabla.png")
        img.show()
    def extractTable(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)
        base=Entry(self,width=15)
        base.grid(row=10,column=2)
        t=Label(self,text="Table")
        t.grid(row=11,column=1)
        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)
        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.extractTable1(base.get(),tabla.get()))
        boton34.grid(row=16, column=3, padx=20, pady=30)
   


   
    def extractRangeTable(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)
        base=Entry(self,width=15)
        base.grid(row=10,column=2)
        t=Label(self,text="Table")
        t.grid(row=11,column=1)
        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)
        n=Label(self,text="numberColumns")
        n.grid(row=12,column=1)
        ncol=Entry(self,width=15)
        ncol.grid(row=12,column=2)
        l=Label(self,text="lower")
        l.grid(row=10,column=3)
        low=Entry(self,width=15)
        low.grid(row=10,column=4)
        up=Label(self,text="upper")
        up.grid(row=11,column=3)
        upper=Entry(self,width=15)
        upper.grid(row=11,column=4)
        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.extractRangeTable1(base.get(),tabla.get(),int(ncol),low.get(),upper.get()))
        boton34.grid(row=16, column=3, padx=20, pady=30)
   

    def alterAddPK(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)

        base=Entry(self,width=15)
        base.grid(row=10,column=2)

        t=Label(self,text="Table")
        t.grid(row=11,column=1)

        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)

        n=Label(self,text="Columns")
        n.grid(row=12,column=1)

        ncol=Entry(self,width=15)
        ncol.grid(row=12,column=2)

        

        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.alterAddPK1(base.get(),tabla.get(),ncol.get()))
        boton34.grid(row=16, column=3, padx=20, pady=30)


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
                numero.append(int(i))
            print(numero)
            return numero
        else:
            return int(string)

    def alterDropPK(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)
        base=Entry(self,width=15)
        base.grid(row=10,column=2)
        t=Label(self,text="Table")
        t.grid(row=11,column=1)
        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)
        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.alterDropPK1(base.get(),tabla.get()))
        boton34.grid(row=16, column=3, padx=20, pady=30)
   
        
        
    def alterTable(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)
        base=Entry(self,width=15)
        base.grid(row=10,column=2)
        t=Label(self,text="TableOld")
        t.grid(row=11,column=1)
        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)
        n=Label(self,text="TableNew")
        n.grid(row=12,column=1)
        ncol=Entry(self,width=15)
        ncol.grid(row=12,column=2)

        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.alterTable1(base.get(),tabla.get(),ncol.get()))
        boton34.grid(row=16, column=3, padx=20, pady=30)


    def alteraddColumn(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)
        base=Entry(self,width=15)
        base.grid(row=10,column=2)
        t=Label(self,text="Table")
        t.grid(row=11,column=1)
        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)
        n=Label(self,text="Default")
        n.grid(row=12,column=1)
        ncol=Entry(self,width=15)
        ncol.grid(row=12,column=2)

        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.alteraddColumn1(base.get(),tabla.get(),ncol.get()))
        boton34.grid(row=16, column=3, padx=20, pady=30)




    def alterDropColumn(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)
        base=Entry(self,width=15)
        base.grid(row=10,column=2)
        t=Label(self,text="Table")
        t.grid(row=11,column=1)
        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)
        n=Label(self,text="ColumnNumber")
        n.grid(row=12,column=1)
        ncol=Entry(self,width=15)
        ncol.grid(row=12,column=2)

        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.alterDropColumn1(base.get(),tabla.get(),int(ncol.get())))
        boton34.grid(row=16, column=3, padx=20, pady=30)




    def dropTable(self):
        b=Label(self,text="Database")
        b.grid(row=10,column=1)
        base=Entry(self,width=15)
        base.grid(row=10,column=2)
        t=Label(self,text="Table")
        t.grid(row=11,column=1)
        tabla=Entry(self,width=15)
        tabla.grid(row=11,column=2)
        boton34= tk.Button(self, text="Aplicar Cambios", width=20, command=lambda:self.dropTable1(base.get(),tabla.get()))
        boton34.grid(row=16, column=3, padx=20, pady=30)
   
        











    
    def createTable1(self,base,tabla,columna):
        messagebox.showinfo("Funcion de base de datos",str(j.createTable(base,tabla,int(columna))))

    def extractTable1(self,base,tabla):
        messagebox.showinfo("Funcion de base de datos",str(j.extractTable(base,tabla)))

    def extractRangeTable1(self,base,tabla,columna,lower,upper):
        messagebox.showinfo("Funcion de base de datos",str(j.extractRangeTable(base,tabla,int(columna),lower,upper)))

    def alterAddPK1(self,base,tabla,columnas):
        lista=self.verificadorlista(columnas)
        print(lista)
        messagebox.showinfo("Funcion de base de datos",str(j.alterAddPK(base,tabla,lista)))


    def alterDropPK1(self,base,tabla):
        messagebox.showinfo("Funcion de base de datos",str(j.alterDropPK(base,tabla)))


    def alterTable1(self,base,viejo,nuevo):
        messagebox.showinfo("Funcion de base de datos",str(j.alterTable(base,viejo,nuevo)))

    def alteraddColumn1(self,base,tabla,cual):
        messagebox.showinfo("Funcion de base de datos",str(j.alterAddColumn(base,tabla,cual)))

    def alterDropColumn1(self,base,tabla,columna):
        messagebox.showinfo("Funcion de base de datos",str(j.alterDropColumn(base,tabla,int(columna))))

    def dropTable1(self,base,tabla):
        messagebox.showinfo("Funcion de base de datos",str(j.dropTable(base,tabla)))
