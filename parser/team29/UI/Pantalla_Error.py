from tkinter import ttk
import tkinter as tk
from tkinter import *

class Pantalla_Error():

     def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry('700x660')
        self.top.resizable(0,0)
        self.top.title('Reporte de Errores')
        label = Label(self.top,text="Reporte de Errores")
        label.config(font=("Verdana",16,'bold')) 
        label.pack(anchor=W)
        label2 = Label(self.top,text="Errores Lexicos")
        label2.config(font=("Verdana",10,'bold')) 
        label2.pack(anchor=W)
        #Creacion del frame
        frame= Frame(self.top,height=300,width=600)
        frame.pack(pady=20)
        #Creacion del scrollbar
        tabla_scroll = Scrollbar(frame)
        tabla_scroll.pack(side=RIGHT, fill=Y)
        #Creacion de la tabla
        tabla = ttk.Treeview(frame,yscrollcommand=tabla_scroll.set,height=5)
        tabla.pack(fill=X)
        #Configurando el scrollbar
        tabla_scroll.config(command=tabla.yview)
        #Definiendo columnas
        tabla['columns'] = ("DESCRIPCION","LINEA")
        #Formato de las columnas
        tabla.column("#0",width=15,minwidth=5)
        tabla.column("DESCRIPCION", anchor=W,width=200)
        tabla.column("LINEA", anchor=W,width=200)
        #Crear Header
        tabla.heading("#0",text="#",anchor=CENTER)
        tabla.heading("DESCRIPCION",text="Descripcion",anchor=CENTER)
        tabla.heading("LINEA",text="Linea",anchor=CENTER)
        label3 = Label(self.top,text="Errores Sintacticos")
        label3.config(font=("Verdana",10,'bold')) 
        label3.pack(anchor=W)
       #Creacion del frame
        frame2= Frame(self.top,height=300,width=600)
        frame2.pack(pady=20)
        #Creacion del scrollbar
        tabla_scroll2 = Scrollbar(frame2)
        tabla_scroll2.pack(side=RIGHT, fill=Y)
        #Creacion de la tabla
        tabla2 = ttk.Treeview(frame2,yscrollcommand=tabla_scroll2.set,height=5)
        tabla2.pack(fill=X)
        #Configurando el scrollbar
        tabla_scroll2.config(command=tabla2.yview)
        #Definiendo columnas
        tabla2['columns'] = ("DESCRIPCION","LINEA")
        #Formato de las columnas
        tabla2.column("#0",width=15,minwidth=5)
        tabla2.column("DESCRIPCION", anchor=W,width=200)
        tabla2.column("LINEA", anchor=W,width=200)
        #Crear Header
        tabla2.heading("#0",text="#",anchor=CENTER)
        tabla2.heading("DESCRIPCION",text="Descripcion",anchor=CENTER)
        tabla2.heading("LINEA",text="Linea",anchor=CENTER)  
        label4 = Label(self.top,text="Errores Semanticos")
        label4.config(font=("Verdana",10,'bold')) 
        label4.pack(anchor=W)
        #Creacion del frame
        frame3= Frame(self.top,height=300,width=600)
        frame3.pack(pady=20)
        #Creacion del scrollbar
        tabla_scroll3 = Scrollbar(frame3)
        tabla_scroll3.pack(side=RIGHT, fill=Y)
        #Creacion de la tabla
        tabla3 = ttk.Treeview(frame3,yscrollcommand=tabla_scroll3.set,height=5)
        tabla3.pack(fill=X)
        #Configurando el scrollbar
        tabla_scroll3.config(command=tabla3.yview)
        #Definiendo columnas
        tabla3['columns'] = ("DESCRIPCION","LINEA")
        #Formato de las columnas
        tabla3.column("#0",width=15,minwidth=5)
        tabla3.column("DESCRIPCION", anchor=W,width=200)
        tabla3.column("LINEA", anchor=W,width=200)
        #Crear Header
        tabla3.heading("#0",text="#",anchor=CENTER)
        tabla3.heading("DESCRIPCION",text="Descripcion",anchor=CENTER)
        tabla3.heading("LINEA",text="Linea",anchor=CENTER)
        frame3.grid_columnconfigure(0,weight=1)
        frame3.pack()
        btn = Button(self.top, text="Regresar",command=self.close)
        btn.pack(side=TOP, anchor="center", padx=25, pady=10)
        self.top.mainloop()
    
     def close(self):
        self.top.destroy()