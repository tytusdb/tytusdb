import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import Windows7, Windows8
import Windows3

import WindowMain

class Ventana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 4")

        label1 = Label(self,text="Nombre base")
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        label2 = Label(self,text="¡ Tablas : ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)
        label5=Label(self,text="representacion de las tablas")

        label2.config(font=("Verdana", 20))
        label2.grid(row=5, column=3)
        comboExample = ttk.Combobox(self,
                                    values=[
                                        "Tabla1",
                                        "Tabla2",
                                        "Tabla3",
                                        "Tabla4"])

        comboExample.grid(row=7,column=10)

        button1 = Button(self, text= 'Atras', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana3)
        button1.grid(row=8, column=0)
        button5 = Button(self, text= 'Enter to Table', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana8)
        button5.grid(row=8, column=8)
        button2 = Button(self, text= 'Funciones tablas', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana7)
        button2.grid(row=8, column=15)
        
        
        self.parent.withdraw()

    def ventana3(self):
        self.destroy()
        Windows3.Ventana(self.parent)

    def ventana7(self):
        self.destroy()
        Windows7.Ventana(self.parent)
        

    def ventana8(self):
        self.destroy()
        Windows8.Ventana(self.parent)

    def close(self):
        self.parent.destroy()
        