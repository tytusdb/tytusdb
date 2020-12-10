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
# _____________________________________________INTERFAZ----------------------------------------------------

root = Tk()
root.title("TytusDB")
root.resizable(0, 0)
# root.iconbitmap("monitor.ico")
root.config(bg="gray75")
# Menú superior
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_separator()
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar Como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Run")
editmenu.add_command(label="Borrar todo")
#editmenu.add_command(label="Analizar HTML", command = analizarHTML)
#editmenu.add_command(label="Analizar RMT", command = analizarRMT)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de...", command=test)
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Analizar", menu=editmenu)
menubar.add_cascade(label="Acerca de..", menu=helpmenu)

# Frame 1
frame1 = Frame(root, width=1485, height=820)
frame1.pack()  # se agrega pa paquete
frame1.config(bg="lightblue2")

frame1.config(relief="groove")
frame1.config(bd=18)
frame1.config(cursor="spider")


fname = "./img/logo.png"
imagen = PhotoImage(file=fname)
fondo = Label(frame1, image=imagen).place(x=0, y=0)