from tkinter import ttk
import tkinter as tk
from tkinter import *


class Pantalla_TS:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry("700x400")
        self.top.resizable(0, 0)
        self.top.title("Tabla de Simbolos")
        label = Label(self.top, text="Tabla de Simbolos")
        label.config(font=("Verdana", 20, "bold"))
        label.pack(anchor=W)
        # Creacion del frame
        frame = Frame(self.top, height=300, width=600)
        frame.pack(pady=20)
        # Creacion del scrollbar
        tabla_scroll = Scrollbar(frame)
        tabla_scroll.pack(side=RIGHT, fill=Y)
        # Creacion de la tabla
        tabla = ttk.Treeview(frame, yscrollcommand=tabla_scroll.set, height=12)
        tabla.pack(fill=X)
        # Configurando el scrollbar
        tabla_scroll.config(command=tabla.yview)
        # Definiendo columnas
        tabla["columns"] = ("ID", "TIPO", "DIMENSION", "DECLARACION", "REFERENCIA")
        # Formato de las columnas
        tabla.column("#0", width=15, minwidth=5)
        tabla.column("ID", anchor=CENTER, width=100)
        tabla.column("TIPO", anchor=W, width=100)
        tabla.column("DIMENSION", anchor=W, width=100)
        tabla.column("DECLARACION", anchor=W, width=100)
        tabla.column("REFERENCIA", anchor=W, width=100)
        # Crear Header
        tabla.heading("#0", text="#", anchor=CENTER)
        tabla.heading("ID", text="Id", anchor=CENTER)
        tabla.heading("TIPO", text="Tipo", anchor=CENTER)
        tabla.heading("DIMENSION", text="Dimension", anchor=CENTER)
        tabla.heading("DECLARACION", text="Declaracion", anchor=CENTER)
        tabla.heading("REFERENCIA", text="Referencia", anchor=CENTER)
        btn = Button(self.top, text="Regresar", command=self.close)
        btn.pack(side=TOP, anchor=E, padx=25)
        self.top.mainloop()

    def close(self):
        self.top.destroy()
