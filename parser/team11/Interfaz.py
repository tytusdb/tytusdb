from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as FileDialog
from tkinter import ttk
import tkinter as tk
import webbrowser
#from graphviz import Digraph
import json
import os
from string import Template

from io import open
import re
from tabulate import tabulate
import os
import glob
ruta = ""  # La utilizaremos para almacenar la ruta del fichero

# esto es para la interfaz--------------------------------------------------------------------------------------------------------------------------------------------------------


def run():
    mb.showinfo("ANALISIS COMPLETADO", "Analisis Completado")
    consola_text.configure(state='normal')
    consola_text.insert(INSERT, "LA CONSOLA FUNCIONA")
    consola_text.configure(state='disabled')
    
    # END


def test():
    mb.showinfo("TytusDB",
                "Universidad de San Carlos de Guatemala\n\tFacultad de Ingenieria\n\tOrganización de lenguajes y compiladores 2\n\tversion 1.0\n\tGRUPO 11\n\tMaria Andrea Duarte Saenz\n\t201503484")  # título, mensaje
    # END


def nuevo():
    global ruta
    mensaje.set("Nuevo archivo")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("TytusDB")
    # END


def abrir():
    global ruta
    mensaje.set("Abrir archivo")
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("HTML", "*.html"), ("CSS", "*.css"), ("JavaScript",
                                                          "*.js"), ("Arbol sintactico", "*.rmt"), ("All files", "*.*")),
        title="Abrir un archivo")

    if ruta != "":
        fichero = open(ruta, 'r', encoding="utf-8")
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        print(contenido)
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - DBMS Usac editor")
    # END


def guardar():
    mensaje.set("Guardar archivo")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+', encoding="utf-8")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Archivo guardado correctamente")
    else:
        guardar_como()
    # END


def guardar_como():
    global ruta
    mensaje.set("Guardar como")

    fichero = FileDialog.asksaveasfile(title="Guardar archivo",
                                       mode="w", filetypes=(("SQL", "*.sql"), ("All files", "*.*")))

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+', encoding="utf-8")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Archivo guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

    # END