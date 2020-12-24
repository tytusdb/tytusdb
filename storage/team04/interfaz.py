from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from binario import *
from isam import *
from PIL import Image


def cargarbotones(nodos): 
    contenedor=Frame(root)
    canvas=Canvas(contenedor,width=75,height=700)
    scrollbar=Scrollbar(contenedor, orient="vertical",command=canvas.yview)
    scrollable_frame=Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0,0),window=scrollable_frame,anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    for nodo in nodos:
        Button(scrollable_frame,text="Base: "+nodo.node_id,command=lambda x=str(nodo.node_id):controlbotones(x,nodos),activebackground="#900C3F").pack()
    contenedor.pack(side="left")
    canvas.pack(side="left",fill="x",expand=True)
    scrollbar.pack(side="left",fill="y")

def clear():
    i=0

def regresar():
    mostrarbases()

def mostrartabla():
    bases=binario.rollback(r".\data\bases")
    nodos=bases.get_all()
    cargarbotones(nodos)
    bases.draw("basesdedatos",False)
    myframe=Frame(root)
    myframe.pack(fill="both",expand=True)
    img=Image.open("basesdedatos.png")
    newimg=img.resize((1000,500))
    newimg.save("newbasesdatos.png","png")
    imagen=PhotoImage(file="newbasesdatos.png")
    imagen2=Label(myframe,image=imagen)
    imagen2.place(x="35",y="30")
    root.mainloop()

def mostrarbases():
    bases=binario.rollback(r".\data\bases")
    nodosb=bases.get_all()
    cargarbotones(nodosb)
    bases.draw("basesdedatos",False)
    myframe=Frame(root)
    myframe.pack(fill="both",expand=True)
    img=Image.open("basesdedatos.png")
    newimg=img.resize((1000,500))
    newimg.save("newbasesdatos.png","png")
    imagen=PhotoImage(file="newbasesdatos.png")
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
#Labels del formulario
miframe=Frame()
miframe.pack()
lbltitulo=Label(miframe,text="Bases de datos - EDD")
lbltitulo.grid(row=0,column=0)
lbltitulo.config(font=('Arial',18))
#Crear boton que llama a la imagen
btnmostrar=Button(root,text="Mostrar estructura de bases de datos",command=mostrarbases,activebackground="#900C3F").pack()  
btnregresar=Button(root,text="Regresar",command=regresar,activebackground="#900C3F",state=DISABLED).pack()   
root.mainloop()