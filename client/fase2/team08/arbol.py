from tkinter import Menu, Tk, Text, DISABLED, RAISED,Frame, FLAT, Button, Scrollbar, Canvas, END
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
from PIL.ImagePalette import load
from PIL import ImageTk, Image
import os
import http.client
import json
import pathlib


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
        #
        myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)

        headers = {
            "Content-type": "application/json"
        }

        myConnection.request("GET", "/getDB", "", headers)
        response = myConnection.getresponse()
        print("GET: Status: {} and reason: {}".format(response.status, response.reason))
        if response.status == 200:       
            data = response.read() 
            data_1=  str(data.decode("utf-8"))
            print(data_1)
            lista = str(data_1).split("}},")
            #print(lista[0])
            #print(lista[1])
            for x in range(0,len(lista)):
                print("\n")
                lista2 = str(lista[x]).split("},")
                padre=lista2[0].split("\"")
                print("-------PADRE---------")
                print(padre[1])
                print("-----HIJOS------------")
                print(padre[3])
                for y in range(1, len(lista2)):
                    temp= lista2[y].split("\"")
                    print(temp[1])
        else:
            print("Error F")
            #consola.config(state=NORMAL)
            #consola.insert(INSERT,"\nHa ocurrido un error.")
            #consola.config(state=DISABLED)
        myConnection.close()

        #

        # Crear las imagenes que iran en el treeview, 
        # Folder para Bases y File para tablas

        #{"TEST": {"TBUSUARIO": {"NCOL": 3, "PKEY": [0]}, "TBROL": {"NCOL": 2, "PKEY": [0]}, "TBROLXUSUARIO": {"NCOL": 2}}}
        self.file_image = tk.PhotoImage(file="resources/file.png")
        self.folder_image = tk.PhotoImage(file="resources/folder.png")
        self.file_image = self.file_image.subsample(35)
        self.folder_image = self.folder_image.subsample(38)
        self.load = Image.open("../team08/resources/tytus.gif")
        self.render = ImageTk.PhotoImage(self.load)
        # Creando el treeview
        self.treeview = ttk.Treeview(self)
        # Encabezado de treeview
        self.treeview.heading("#0", text="Navegador")

        # Se crea el primer item del arbol que lo empaquete todo
        item = self.treeview.insert("", END, text="Bases de datos", image=self.render)
        # Se crea un subitem que sera una base de datos
        # Se puede repetir este proceso cuantas veces se desee para aumentar
        # los niveles del treeview, por ahora solo seran 3 niveles
        # Adentro del insertar va el item padre
        
        subitem = self.treeview.insert(item, END, text="Amazon",image=self.folder_image)
        # Se llena el ultimo nivel del arbol, como es el ultimo nivel 
        # solo se llaman los inserts sin crear una variable item nueva.
        self.treeview.insert(subitem, END, text="Empleado",image=self.file_image)
        self.treeview.insert(subitem, END, text="Cliente",image=self.file_image)
        self.treeview.insert(subitem, END, text="Producto",image=self.file_image)

        # Nuevo subitem con item como padre
        subitem = self.treeview.insert(item, END, text="Aurora",image=self.folder_image)
        # Llenando este subitem
        self.treeview.insert(subitem, END, text="Animal",image=self.file_image)
        self.treeview.insert(subitem, END, text="Habitat",image=self.file_image)
        self.treeview.insert(subitem, END, text="Alimento",image=self.file_image)

        # Colocando el arbol en el frame
        self.treeview.pack(side="top", fill="both", expand=True)
        self.pack(side="top", fill="both", expand=True)
