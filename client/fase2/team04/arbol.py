from tkinter import Menu, Tk, Text, DISABLED, RAISED,Frame, FLAT, Button, Scrollbar, Canvas, END
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
import json

class Arbol(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        # Estilos del Treeview, solamente para vista
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            background = "gray21",
            foreground = "white",
            fieldbackground = "silver",
            activebackground="gray59"
            )
        
        # Crear las imagenes que iran en el treeview, 
        # Folder para Bases y File para tablas

        # Creando el treeview
        self.treeview = ttk.Treeview(self)
        self.treeview.heading("#0", text="Navegador")
        self.treeview.pack(side="top", fill="both", expand=True)
        self.pack(side="top", fill="both", expand=True)
        # Se llena el ultimo nivel del arbol, como es el ultimo nivel 
        # solo se llaman los inserts sin crear una variable item nueva.
        # self.treeview.insert(subitem, END, text="Empleado",image=self.file_image)
        # self.treeview.insert(subitem, END, text="Cliente",image=self.file_image)
        # self.treeview.insert(subitem, END, text="Producto",image=self.file_image)

        # Nuevo subitem con item como padre
        # subitem = self.treeview.insert(item, END, text="Aurora",image=self.folder_image)
        # Llenando este subitem
        # self.treeview.insert(subitem, END, text="Animal",image=self.file_image)
        # self.treeview.insert(subitem, END, text="Habitat",image=self.file_image)
        # self.treeview.insert(subitem, END, text="Alimento",image=self.file_image)

        # Colocando el arbol en el frame
        

    def entregado(self, data):
        print(data)
        persons = json.loads(data)
        
        # Encabezado de treeview
        self.file_image = tk.PhotoImage(file="resources/file.png")
        self.folder_image = tk.PhotoImage(file="resources/folder.png")
        self.file_image = self.file_image.subsample(35)
        self.folder_image = self.folder_image.subsample(38)

        for i in self.treeview.get_children():
            self.treeview.delete(i)
        
        item = self.treeview.insert("", END, text="Bases de datos")

        for key, value in persons.items():
            

            subitem = self.treeview.insert(item, END, text=key,image=self.folder_image)

            for key2, value2 in value.items():

                self.treeview.insert(subitem, END, text=key2,image=self.file_image)
                print (key2, value2)
        
        