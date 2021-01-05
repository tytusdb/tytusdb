import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import Windows6
import Windows7
import Windows3
import ISAMMode as m
import os

import WindowMain

class Ventana(tk.Toplevel):
    def __init__(self, parent,namebase):
        super().__init__(parent)
        self.parent = parent
        self.namebase=namebase
        self.basesdatos=[]
        self.b()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 4")
        if len(m.showTables(self.namebase))==0:
            print("")
        else:
            m.graficoTablas(self.namebase)
        if os.path.exists("grafotabla.png"):
            print("si existe")
            canvas=Canvas(self)
            canvas.pack()
            img=Image.open('grafotabla.png')
            canvas.image =ImageTk.PhotoImage(img)
            canvas.create_image(0,0,image=canvas.image,anchor='nw')
            canvas.grid(row=2,column=10)
            os.system('grafotabla.png')
            img=Image.open("grafotabla.png")
            img.show()
            
        label1 = Label(self,text=namebase)
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        label2 = Label(self,text="¡ Tablas : ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)
        label5=Label(self,text="representacion de las tablas")


        label5.config(font=("Verdana", 20))
        label5.grid(row=5, column=3)


        self.bases=tk.StringVar(self)
        self.bases.set('Seleccionar...')
        
        menu = tk.OptionMenu(self, self.bases, *self.basesdatos)
        menu.config(width=20)
        menu.grid(row = 7, column = 10, padx = 30, pady = 30)


        button1 = Button(self, text= 'Atras', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana7)
        button1.grid(row=8, column=0)
        button5 = Button(self, text= 'Enter a tabla', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana3)
        button5.grid(row=8, column=10)
        button2 = Button(self, text= 'Function en Tablas', padx= 15, pady=6, bg= 'grey',fg='white',command=self.funciones)
        button2.grid(row=8, column=15)
        
        
        self.parent.withdraw()

    def ventana7(self):
        self.destroy()
        Windows3.Ventana(self.parent)

    def ventana3(self):
        self.destroy()
        Windows7.Ventana(self.parent,self.namebase,self.bases.get())

    def funciones(self):
        self.destroy()
        Windows6.Ventana(self.parent,self.namebase)
    def close(self):
        self.parent.destroy()
        
    def b(self):
        self.basesdatos.clear()
        if len(m.showTables(self.namebase))!=0:
            for k in m.showTables(self.namebase):
                self.basesdatos.append(k)
        elif len(self.basesdatos)==0:
            self.basesdatos.append("No hay tablas")
