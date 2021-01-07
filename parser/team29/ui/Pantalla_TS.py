from tkinter import ttk
import tkinter as tk
from tkinter import *


class Pantalla_TS:
    def __init__(self, parent, ts, indexes):
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry("700x400")
        self.top.resizable(0, 0)
        self.top.title("Tabla de Simbolos")
        label = Label(self.top, text="Tabla de Simbolos")
        label.config(font=("Verdana", 20, "bold"))
        label.pack(anchor=W)
        self.tabControl = ttk.Notebook(self.top, width=650, height=300)
        self.show_symbolTable(ts)
        self.show_index(indexes, "Indices")
        self.tabControl.pack()
        btn = Button(self.top, text="Regresar", command=self.close)
        btn.pack(side=TOP, anchor=E, padx=25)
        self.top.mainloop()

    def show_index(self, table, name):
        if table != None:
            self.create_table(table, name)

    def show_symbolTable(self, consults):
        if consults != None:
            i = 0
            for consult in consults:
                i += 1
                if consult != None:
                    self.create_table(consult, "Tabla de Simbolos " + str(i))
        self.tabControl.pack()

    def create_table(self,input,name):
        frame = Frame(self.tabControl, height=300, width=450, bg="#d3d3d3")
        # Creacion del scrollbar
        table_scroll = Scrollbar(frame, orient="vertical")
        table_scrollX = Scrollbar(frame, orient="horizontal")
        table = ttk.Treeview(
            frame,
            yscrollcommand=table_scroll.set,
            xscrollcommand=table_scrollX.set,
            height=12,
        )
        table_scroll.config(command=table.yview)
        table_scrollX.config(command=table.xview)
        self.fill_table(input[0], input[1], table)
        table_scroll.pack(side=RIGHT, fill=Y)
        table_scrollX.pack(side=BOTTOM, fill=X)
        table.pack(side=LEFT, fill=BOTH)
        frame.pack(fill=BOTH)
        self.tabControl.add(frame, text=name)

    def fill_table(
        self, columns, rows, table
    ):  # funcion que muestra la salida de la/s consulta/s
        table["columns"] = columns
        """
        Definicion de columnas y encabezado
        """
        table.column("#0", width=25, minwidth=50)
        i = 0
        ancho = int(600 / len(columns))
        if ancho < 100:
            ancho = 100
        while i < len(columns):
            table.column(str(i), width=ancho, minwidth=50, anchor=CENTER)
            i += 1
        table.heading("#0", text="#", anchor=CENTER)
        i = 0
        while i < len(columns):
            table.heading(str(i), text=str(columns[i]), anchor=CENTER)
            i += 1
        """
        Insercion de filas
        """
        i = 0
        for row in rows:
            i += 1
            table.insert(parent="", index="end", iid=i, text=i, values=(row))

    def close(self):
        self.top.destroy()
