from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from binario import *
from isam import *

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
        Button(scrollable_frame,text="Nodo: "+nodo.node_id,command=lambda x=str(nodo.node_id):controlbotones(x),activebackground="#900C3F").pack()
    contenedor.pack(side="left")
    canvas.pack(side="left",fill="x",expand=True)
    scrollbar.pack(side="left",fill="y")


def mostrarimagen():
    #Leer el archivo
    bases=binario.rollback(r".\data\base1_clientes")
    nodos=bases.get_all()
    cargarbotones(nodos)
    bases.draw("fakename",False)
    
    imagen=PhotoImage(file="fakename.png")
    graph=Label(root,image=imagen,bd=0)
    graph.pack()



    
root=Tk()
#Dimensiones del formulario
root.geometry("1000x710")
root.title("TyTus - DMBS EDD")
#Labels del formulario
miframe=Frame()
miframe.pack()
lbltitulo=Label(miframe,text="Bases de datos - EDD")
lbltitulo.grid(row=0,column=0)
lbltitulo.config(font=('Arial',18))
#Crear boton que llama a la imagen
Button(root,text="Mostrar estructura de bases de datos",command=mostrarimagen,activebackground="#900C3F").pack()  
Button(root,text="Regresar",command=regresaraestructura,activebackground="#900C3F").pack()   
root.mainloop()