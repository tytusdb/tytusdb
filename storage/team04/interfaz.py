from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from binario import *

base_actual = None
tabla_actual = None
tupla_actual = None

def cargarbotones(nodos):
    global contenedor
    clearframe_sp(contenedor)
    canvas=Canvas(contenedor,width=250,height=700)
    scrollbar=Scrollbar(contenedor, orient="vertical",command=canvas.yview)
    scrollable_frame=Frame(canvas)
    clearframe_sp(scrollable_frame)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0,0),window=scrollable_frame,anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    for nodo in nodos:
        Button(scrollable_frame,text="Acceder a: "+nodo.node_id,command=lambda x=str(nodo.node_id):controlbotones(x,nodos),activebackground="#900C3F").pack()
    contenedor.pack(side="left")
    canvas.pack(side="left",fill="x",expand=True)
    scrollbar.pack(side="left",fill="y")

def controlbotones(node_id, nodos):
    for nodo in nodos:
        if node_id == nodo.node_id:
            # Cargar lista
            global tabla_actual
            global base_actual
            if tabla_actual != None:
                # Está en una tabla
                mostrartupla(nodo)
            elif base_actual != None:
                # Está en una base de datos
                mostrartabla(nodo)
            else:
                # Está en la lista de bases de datos
                mostrarbase(nodo)


def clear():
    i=0

def regresar():
    global tabla_actual
    global base_actual
    global tupla_actual
    if tupla_actual != None:
        # Regresar a la tabla
        tupla_actual = None
        mostrartabla(tabla_actual)
    elif tabla_actual != None:
        # Regresar a la base de datos
        tabla_actual = None
        mostrarbase(base_actual)
    elif base_actual != None:
        # Regresar a la lista de bases de datos
        base_actual = None
        mostrarbases()
    else:
        # Quedarse en la lista de bases de datos
        mostrarbases()

def clearframe():
    global myframe
    for widget in myframe.winfo_children():
        widget.destroy()

def clearframe_sp(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def irainicio():
    global tabla_actual
    global base_actual
    global tupla_actual
    tabla_actual = None
    base_actual = None
    tupla_actual = None
    mostrarbases()

def mostrarbases():
    clearframe()
    lista_bases=binario.rollback("bases")
    bases=lista_bases.get_all()
    cargarbotones(bases)
    lista_bases.draw(r"./img/bases",False)
    global myframe
    myframe.pack(fill="both",expand=True)
    imagen=PhotoImage(file="./img/bases.png")
    imagen2=Label(myframe,image=imagen)
    imagen2.place(x="35",y="30")
    root.mainloop()

def mostrarbase(nodo_base):
    clearframe()
    global base_actual
    base_actual = nodo_base
    base=nodo_base.data.get_all()
    cargarbotones(base)
    nodo_base.data.draw(r"./img/base",False)
    global myframe
    myframe.pack(fill="both",expand=True)
    imagen=PhotoImage(file="./img/base.png")
    imagen2=Label(myframe,image=imagen)
    imagen2.place(x="35",y="30")
    root.mainloop()

def mostrartabla(nodo_tabla):
    clearframe()
    global tabla_actual
    tabla_actual = nodo_tabla
    tabla=binario.rollback(nodo_tabla.data)
    nodos_tabla = tabla.get_all()
    cargarbotones(nodos_tabla)
    tabla.draw(r"./img/tabla",False)
    global myframe
    myframe.pack(fill="both",expand=True)
    imagen=PhotoImage(file="./img/tabla.png")
    imagen2=Label(myframe,image=imagen)
    imagen2.place(x="35",y="30")
    root.mainloop()

def mostrartupla(nodo_tupla):
    clearframe()
    global tupla_actual
    tupla_actual = nodo_tupla
    nodo_tupla.draw(r"./img/tupla",False)
    global myframe
    myframe.pack(fill="both",expand=True)
    imagen=PhotoImage(file="./img/tupla.png")
    imagen2=Label(myframe,image=imagen)
    imagen2.place(x="35",y="30")
    root.mainloop()

def botonesdebasededatos(btn_id,nodos):
    for nodo in nodos:
        if nodo.node_id == btn_id:
            print(nodo.node_id)
            nodo.draw("tablas",True)
    lbltitulo.config(text="Hiciste click en el botón número {0}".format(btn_id))
 
root=Tk()
#Dimensiones del formulario
root.geometry("1200x710")
root.title("TyTus - DMBS EDD")
myframe=Frame(root)
contenedor=Frame(root)
#Labels del formulario
miframe=Frame()
miframe.pack()
lbltitulo=Label(miframe,text="Bases de datos - EDD")
lbltitulo.grid(row=0,column=0)
lbltitulo.config(font=('Arial',18))
#Crear boton que llama a la imagen
btnmostrar=Button(root,text="Inicio",command=irainicio,activebackground="#900C3F").pack()  
btnregresar=Button(root,text="Regresar",command=regresar,activebackground="#900C3F").pack()   
root.mainloop()