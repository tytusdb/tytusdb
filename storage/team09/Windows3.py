import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import Windows2
import Windows4
import Windows5
import WindowMain
import ISAMMode as m
import os


class Ventana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        if len(m.showDatabases())==0:
            print("")
        else:
            m.grafo()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.parent.title("ventana 3")
        self.basesdatos=[]
        self.b()
        self.parent.geometry("1000x600")
        self.parent.title(" [EDD] Fase-1")
        self.parent.configure(bg='#2C3E50')
        if os.path.exists("AvlData.png"):
            canvas=Canvas(self)
            canvas.pack()
            img=Image.open('AvlData.png')
            canvas.image =ImageTk.PhotoImage(img)
            canvas.create_image(0,0,image=canvas.image,anchor='nw')
            canvas.grid(row=0,column=10)

        label1 = Label(self, text="\nSelect your Data Base\n\n\n")
        label1.config(font=("Verdana", 15))
        label1.grid(row=1, column=10)

        self.bases=tk.StringVar(self)
        self.bases.set('Seleccionar...')
        menu = tk.OptionMenu(self, self.bases, *self.basesdatos)
        menu.config(width=20)
        menu.grid(row = 0, column = 1, padx = 30, pady = 30)

        

        button1 = Button(self, text= 'Atras', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana2)
        button1.grid(row=8, column=0)
        button5 = Button(self, text= 'Enter to Base', padx= 15, pady=6, bg= 'grey',fg='white',command=self.Ventana5)
        button5.grid(row=8, column=10)
        button2 = Button(self, text= 'Function Data', padx= 15, pady=6, bg= 'grey',fg='white',command=self.Ventana4)
        button2.grid(row=8, column=15)

        button3 = Button(self, text= 'cargar datos', padx= 15, pady=6, bg= 'grey',fg='white',command=self.cargar)
        button3.grid(row=8, column=13)       
        
        self.parent.withdraw()

    def ventana2(self):
        self.destroy()
        WindowMain.MainWindow(self.parent)

    def Ventana4(self):
        self.destroy()
        Windows4.Ventana(self.parent)

    def Ventana5(self):
        self.destroy()
        Windows5.Ventana(self.parent,self.bases.get())
        print(self.bases.get())
        
    def cargar(self):
        self.destroy()
        Windows2.Ventana2(self.parent)
        print(self.bases.get())
        

    def close(self):
        self.parent.destroy()

        
    def b(self):
        self.basesdatos.clear()
        if len(m.showDatabases())!=0:
            for k in m.showDatabases():
                self.basesdatos.append(k)
        elif len(self.basesdatos)==0:
            self.basesdatos.append("l")
            self.basesdatos.append("l")
