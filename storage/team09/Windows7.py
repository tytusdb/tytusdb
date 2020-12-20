import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Windows5
import WindowMain

class Ventana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 7")

        label1 = Label(self,text="Nombre base")
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)
        label11 = Label(self,text="Tablas")
        label11.config(font=("Verdana", 25))
        label11.grid(row=2, column=3)

        label2 = Label(self,text="¡ Select your Funtion : ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)

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

        boton = tk.Button(self, text="Atras", width=20, command=self.ventana5)
        boton.grid(row=13, column=0, padx=20, pady=30)
        self.parent.withdraw()

    def guardado(self):
        messagebox.showinfo("Tablas", "Se actualizo Informacion")

    def ventana5(self):
        self.destroy()
        Windows5.Ventana(self.parent)
        
    def close(self):
        self.parent.destroy()
        