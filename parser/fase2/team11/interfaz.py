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
from funciones import Funciones2

import Ast as ast

from io import open
import re
#from tabulate import tabulate
import os
import glob
ruta = ""  # La utilizaremos para almacenar la ruta del fichero
from optimizacion import Optimizacion

# esto es para la interfaz--------------------------------------------------------------------------------------------------------------------------------------------------------



def test():
    mb.showinfo("TytusDB",
                "Universidad de San Carlos de Guatemala\n\tFacultad de Ingenieria\n\tOrganización de lenguajes y compiladores 2\n\tversion 1.0\n\tGRUPO 11")  # título, mensaje
    # END
    

def borrar():
    output_text.delete("1.0","end")
    errores_text.delete("1.0","end")
    texto3d.delete("1.0","end")
    textoopt.delete("1.0","end")
    texto.delete("1.0","end")

def opt():
    contenido = []
    # Optimizacion(Funciones2.hola, contenido)
    # contenido = Optimizacion.optimizando(Funciones2.hola)
    # print(contenido)
    # for inst in contenido:
    #     textoopt.insert('insert', inst)
    #     print("->", inst)
 
        
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
        filetypes=(("SQL", "*.sql"),("All files", "*.*")),
        title="Abrir un archivo")

    if ruta != "":
        fichero = open(ruta, 'r', encoding="utf-8")
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        print(contenido)
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - TytusDB Usac editor")
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
#opera_path = "C:\\Users\\mads3\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
#webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_path))

def abrirERRORES(): 
    erro_path = "Errores.html"
    webbrowser.open(erro_path)
# _____________________________________________INTERFAZ----------------------------------------------------
def abrirTS(): 
    ts_path = "repoteTS.html"
    webbrowser.open(ts_path)

def abritSVG():
    svg_path = "ast.dot.svg"
    webbrowser.open(svg_path)

def abrirOpt():
    opt_path = "reporteOptimizacion.html"
    webbrowser.open(opt_path)


root = Tk()
root.title("TytusDB")
root.resizable(1, 1)
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
editmenu.add_command(label="Run", command = lambda : funcion.analizar(texto,consola_text,output_text, errores_text))
editmenu.add_command(label="Borrar todo", command = borrar)
#editmenu.add_command(label="Analizar HTML", command = analizarHTML)
#editmenu.add_command(label="Analizar RMT", command = analizarRMT)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de...", command=test)

fase2 = Menu(menubar, tearoff = 0)
# fase2.add_command(Label = "De SQL a C3D")
# fase2.add_command(Label = "De C3D a Optimizado")
# fase2.add_command(label = "Reporte optimizacion")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Analizar", menu=editmenu)
menubar.add_cascade(label="Acerca de..", menu=helpmenu)
menubar.add_cascade(label = "Fase2", menu = fase2)




# Frame 1
frame1 = Frame(root, width=1210, height=650)
frame1.pack()  # se agrega pa paquete
frame1.config(bg="lightblue2")

frame1.config(relief="groove")
frame1.config(bd=18)
frame1.config(cursor="spider")


fname = "./img/logo.png"
imagen = PhotoImage(file=fname)
fondo = Label(frame1, image=imagen).place(x=0, y=0)
# Labels
# VIEW TREE
my_tree = ttk.Treeview(frame1)

# Definiendo las columnas
my_tree['columns'] = ("Hola")

#tv = Treeview(frame1, width = 20, height = 20)
# Seperator object
separator = ttk.Separator(frame1, orient='vertical')
separator.place(relx=0.20, rely=0, relwidth=0.001, relheight=1)

# Caja de texto

areaTexto = ttk.Notebook(frame1, width=720, height=275)
areaTexto.pack(fill='none', expand='yes')
areaTexto.pack(expand=1)
areaTexto.place(x=250, y=25)


texto = Text(areaTexto, width=90, height=15, fg="gray40")
texto.config(bd=0, font=("Consolas", 12))
texto.configure(state='normal')

texto3d = Text(areaTexto, width=90, height=15, fg="black")
texto3d.config(bd=0, font=("Consolas", 12))
texto3d.configure(state='normal')

textoopt = Text(areaTexto, width=90, height=15, fg="gray25")
textoopt.config(bd=0, font=("Consolas", 12))
textoopt.configure(state='normal')


areaTexto.add(texto, text="Codigo SQL", padding=5)
areaTexto.add(texto3d, text="Codigo 3d", padding=5)
areaTexto.add(textoopt, text="Codigo Optimizado", padding=5)
#-----------------------------------------------------------------------------------------------------------------
# Notebook
texto4 = ttk.Notebook(frame1, width=720, height=200)
texto4.pack(fill='none', expand='yes', side='bottom')
texto4.pack(expand=1)
texto4.place(x=250, y=340)


consola_text = Text(texto4, width=120, height=15,
                    bg="gray40", fg="spring green")
consola_text.config(bd=0, font=("Consolas", 12))
consola_text.configure(state='normal')

output_text = Text(texto4, width=120, height=15,
                    bg="gray40", fg="white")
output_text.config(bd=0, font=("Consolas", 12))
# output_text.configure(state='disabled')

errores_text = Text(texto4, width=120,  height=15,
                    bg="gray40", fg="DarkOrange1")
errores_text.config(bd=0, font=("Consolas", 12))
errores_text.configure(state='normal')

texto4.add(output_text, text="Output", padding=5)
texto4.add(errores_text, text="Errores", padding=5)

funcion = Funciones2()
# Botones
fname2 = "./img/run.png"
img = PhotoImage(file=fname2)

btn = Button(frame1, image=img, bg="gray93", command=lambda : funcion.traducir(texto,consola_text,output_text, errores_text, texto3d, areaTexto)).place(x=1025, y=100)

fname3 = "./img/optimizar.png"
img2 = PhotoImage(file=fname3)
btn2 = Button(frame1, image=img2, bg="gray93", command = lambda : funcion.opt(textoopt, areaTexto)).place(x=1025, y=190)


fname8 = "./img/borrar.png"
img8 = PhotoImage(file=fname8)

btn8 = Button(frame1, image=img8, bg="gray93", command = borrar).place(x=1025, y=280)

fname4 = "./img/error.png"
img3 = PhotoImage(file=fname4)
btn3 = Button(frame1, bg="gray93", command = abrirERRORES, image=img3, text="Errores", height=70,
              width=100, font=("Berlin Sans FB", 15)).place(x=70, y=100)

fname5 = "./img/tabla.png"
img4 = PhotoImage(file=fname5)
btn4 = Button(frame1, bg="gray93", command = abrirTS, image=img4, text="Tabla", height=70,
              width=100, font=("Berlin Sans FB", 15)).place(x=70, y=190)

fname6 = "./img/AST.png"
img5 = PhotoImage(file=fname6)
btn5 = Button(frame1, bg="gray93", command = abritSVG,image=img5, text="AST", height=70,
              width=100, font=("Berlin Sans FB", 15)).place(x=70, y=280)

fname7 = "./img/reporte.png"
img6 = PhotoImage(file=fname7)
btn6 = Button(frame1, bg="gray93",command = abrirOpt, image=img6, text="Optimizar", height=70,
              width=100, font=("Berlin Sans FB", 15)).place(x=70, y=370)


# Monitor inferior
mensaje = StringVar()
mensaje.set("TytusDB")
monitor = Label(root, textvar=mensaje, font=("Berlin Sans FB", 15))
monitor.pack(side="left")

root.config(menu=menubar)

root.mainloop()

