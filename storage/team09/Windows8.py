import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import Windows6,Windows5

import WindowMain

class Ventana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 8")

        label1 = Label(self,text="Nombre base")
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        label11 = Label(self,text="Nombre de la base")
        label11.config(font=("Verdana", 25))
        label11.grid(row=3, column=3)

        label12 = Label(self,text="Tupla")
        label12.config(font=("Verdana", 15))
        label12.grid(row=4, column=3)




        button1 = Button(self, text= 'Atras', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana5)
        button1.grid(row=8, column=0)
        button5 = Button(self, text= 'Funciones de Tuplas', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana6)
        button5.grid(row=8, column=10)
       # button2 = Button(self, text= 'Function Data', padx= 15, pady=6, bg= 'grey',fg='white',command=self.Ventana4)
        #button2.grid(row=8, column=15)
        
        
        self.parent.withdraw()

    def ventana5(self):
        self.destroy()
        Windows5.Ventana(self.parent)
    
    def ventana6(self):
        self.destroy()
        Windows6.Ventana(self.parent)
        
    def close(self):
        self.parent.destroy()
        