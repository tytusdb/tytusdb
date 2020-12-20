import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import Windows8

import WindowMain

class Ventana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 6")

        label1 = Label(self,text="FUNCIONES DE TUPLAS")
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        funcion1 = Button(self, text= 'Funcion 1', padx= 15, pady=6, bg= 'grey',fg='white',command=self.guardado)
        funcion1.grid(row=7, column=3)
        funcion2 = Button(self, text= 'Funcion2', padx= 15, pady=6, bg= 'grey',fg='white',command=self.guardado)
        funcion2.grid(row=7, column=5)
        funcion3 = Button(self, text= 'Funcion3', padx= 15, pady=6, bg= 'grey',fg='white',command=self.guardado)
        funcion3.grid(row=7, column=8)
        funcion4 = Button(self, text= 'Funcion4', padx= 15, pady=6, bg= 'grey',fg='white',command=self.guardado)
        funcion4.grid(row=8, column=3)
        funcion5 = Button(self, text= 'Funcion5', padx= 15, pady=6, bg= 'grey',fg='white',command=self.guardado)
        funcion5.grid(row=8, column=5)
        funcion6 = Button(self, text= 'Funcion6', padx= 15, pady=6, bg= 'grey',fg='white',command=self.guardado)
        funcion6.grid(row=8, column=8)
        button1 = Button(self, text= 'Atras', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana8)
        button1.grid(row=10, column=0)
        
        
        self.parent.withdraw()
    def guardado(self):
        messagebox.showinfo("Tablas", "Se actualizo Informacion")

    def ventana8(self):
        self.destroy()
        Windows8.Ventana(self.parent)
        
    def close(self):
        self.parent.destroy()
        