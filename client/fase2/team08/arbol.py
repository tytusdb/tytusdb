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
            if data_1!="":
                lista = str(data_1).split("}},")
                #print(lista[0])
                #print(lista[1])
                for x in range(0,len(lista)):
                    lista2 = str(lista[x]).split("},")
                    padre=lista2[0].split("\"")
                    # Se crea un subitem que sera una base de datos
                    # Se puede repetir este proceso cuantas veces se desee para aumentar
                    # los niveles del treeview, por ahora solo seran 3 niveles
                    # Adentro del insertar va el item padre
                    if len(padre)>3:
                        subitem = self.treeview.insert(item, END, text=padre[1],image=self.folder_image)
                        self.treeview.insert(subitem, END, text=padre[3],image=self.file_image)
                        for y in range(1, len(lista2)):
                            temp= lista2[y].split("\"")
                            self.treeview.insert(subitem, END, text=temp[1],image=self.file_image)
            else:
                print("Error BASE DE DATOS")
                #consola.config(state=NORMAL)
                #consola.insert(INSERT,"\nHa ocurrido un error.")
                #consola.config(state=DISABLED)
            myConnection.close()

        #

        
        

        # Colocando el arbol en el frame
        self.treeview.pack(side="top", fill="both", expand=True)
        self.pack(side="top", fill="both", expand=True)
