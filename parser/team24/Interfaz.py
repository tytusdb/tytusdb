from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import re
import os
import defasc

root = Tk()

"""INTERFAZ GRAFICA"""
#PROPIEDADES DE LA VENTANA
root.geometry("1100x650")
root.title("[OLC2]Fase 1")
root.configure(bg='grey')
#FUNCIONES MENU
ruta = ""
nombrearchivo = ""
def Salir():
    root.quit()
def AcercaDe():
    messagebox.showinfo("Acerca de [OLC2]Fase 1", "Organización de Lenguajes y Compiladores 2")
def Abrir():
    global ruta 
    global nombrearchivo
    ruta = filedialog.askopenfilename(title="Seleccionar Archivo", filetypes=(("Todos los archivos","*.*"),("Archivos txt","*.txt")))
    nombrearchivo=os.path.basename(ruta)
    try:
        archivo = open(ruta,"r")
        texto.delete('1.0',END)
        contenido = archivo.read()
        texto.insert(END,contenido)
        archivo.close()
    except:
        print("ERROR")
def Guardar():
    global ruta
    cont = texto.get("1.0",END)
    try:
        archivo = open(ruta,"w")
        archivo.write(cont)
        archivo.close()
    except:
        print("Error al guardar archivo")
def GuardarComo():
    global ruta
    ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Todos los archivos","*.*"),("Archivos txt","*.txt")))
    cont = texto.get("1.0",END)
    try:
        archivo = open(ruta,"w")
        archivo.write(cont)
        archivo.close()
    except:
        print("Error al guardar como archivo")
    return  
def LimpiarTexto():
    texto.delete('1.0',END)
def AnalizadorASC():
    contenido = ""
    contenido = texto.get("1.0",END)
    consola.delete('1.0', END)
    consola.insert(END,defasc.Analizar(contenido))
#CREACION DE COMPONENTES GRAFICOS
BarraMenu=Menu(root)  
root.config(menu=BarraMenu)
MenuArchivo= Menu(BarraMenu, tearoff=0)
MenuArchivo.add_command(label="Arbrir",command=Abrir)  
MenuArchivo.add_command(label="Guardar",command=Guardar)  
MenuArchivo.add_command(label="Guardar Como...",command=GuardarComo)
MenuArchivo.add_separator() 
MenuArchivo.add_command(label="Salir", command=Salir) 
BarraMenu.add_cascade(label="Archivo", menu=MenuArchivo)

MenuEditar= Menu(BarraMenu, tearoff=0)  
MenuEditar.add_command(label="Limpiar Texto",command=LimpiarTexto)
BarraMenu.add_cascade(label="Editar", menu=MenuEditar)

MenuAnalizador= Menu(BarraMenu, tearoff=0)  
MenuAnalizador.add_command(label="Analizar Ascendente", command=AnalizadorASC)
MenuAnalizador.add_command(label="Analizar Descendente")
BarraMenu.add_cascade(label="Analizar", menu=MenuAnalizador)

MenuReportes= Menu(BarraMenu, tearoff=0)
BarraMenu.add_cascade(label="Reportes", menu=MenuReportes)
MenuReportes.add_command(label="Generar Reporte") 

MenuAyuda= Menu(BarraMenu, tearoff=0)
MenuAyuda.add_command(label="Acerca de...",command=AcercaDe)
BarraMenu.add_cascade(label="Ayuda", menu=MenuAyuda)

lblanalizador = Label(root,text="Area del Analizador",bg='grey')
texto = scrolledtext.ScrolledText(root, height=35, width=80,borderwidth=1,wrap="none")
textHsb = Scrollbar(root, orient="horizontal", command=texto.xview)
texto.configure(xscrollcommand=textHsb.set)

lblconsola = Label(root,text="Area de la consola",bg='grey')
consola = scrolledtext.ScrolledText(root, height=35, width=50,bg="black",fg="#bbd500",borderwidth=1,wrap="none")
consolaHsb = Scrollbar(root, orient="horizontal", command=consola.xview)
consola.configure(xscrollcommand=consolaHsb.set)
# COLOCACION DE COMPONENTES
lblanalizador.grid(row=1,column=0)
lblconsola.grid(row=1,column=1)
texto.grid(row=2,column=0)
textHsb.grid(row=3, column=0, sticky="ew")
consola.grid(row=2,column=1)
consolaHsb.grid(row=3, column=1, sticky="ew")
"""FIN INTERFAZ GRAFICA"""
root.mainloop()