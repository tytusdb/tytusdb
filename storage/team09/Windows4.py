import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Windows3
import WindowMain
import ISAMMode as j

class Ventana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 4")

        label1 = Label(self,text="Nombre base")
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        label2 = Label(self,text="¡ Select your Funtion : ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)
        boton1 = tk.Button(self, text="Crear", width=20, command=self.crearbase)
        boton1.grid(row=5, column=2, padx=20, pady=30)
        boton2 = tk.Button(self, text="Cambiar Nombre", width=20, command=self.editarbase)
        boton2.grid(row=5, column=3, padx=20, pady=30)
        boton3 = tk.Button(self, text="Eliminar", width=20, command=self.eliminarbase)
        boton3.grid(row=5, column=4, padx=20, pady=30)
        boton3 = tk.Button(self, text="MostrarBases", width=20, command=self.mostrarbase)
        boton3.grid(row=5, column=5, padx=20, pady=30)
        label3 = Label(self,text="\nInsert Parameters")
        label3.config(font=("Verdana", 12))
        label3.grid(row=7, column=3)  
        
        self.parameters=tk.StringVar() 

        parametros=Entry(self, width=50,textvariable=self.parameters)
        parametros.grid(row=10,column=3)

        boton = tk.Button(self, text="Aplicar Cambios", width=20, command=self.ventana3)
        boton.grid(row=13, column=3, padx=20, pady=30)
        
        self.parent.withdraw()

    def ventana3(self):
        self.destroy()
        Windows3.Ventana(self.parent)
        
    def close(self):
        self.parent.destroy()
    
    def crearbase(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.createDatabase(para[0])))

    def editarbase(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.alterDatabase(para[0],para[1])))

    def eliminarbase(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.dropDatabase(para[0])))

    def mostrarbase(self):
        messagebox.showinfo("Funcion de base de datos",str(j.showDatabases()))
