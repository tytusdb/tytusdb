from tkinter import ttk
import tkinter as tk
from tkinter import *


class Pantalla_Error:
    def __init__(self, parent, lexical, sintactic, semantic):
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry("700x660")
        self.top.resizable(0, 0)
        self.top.title("Reporte de Errores")
        label = Label(self.top, text="Reporte de Errores")
        label.config(font=("Verdana", 16, "bold"))
        label.pack(anchor=W)
        label2 = Label(self.top, text="Errores Lexicos")
        label2.config(font=("Verdana", 10, "bold"))
        label2.pack(anchor=W)
        # Creacion del frame
        frame = Frame(self.top, height=300, width=600)
        frame.pack(pady=20)
        # Creacion del scrollbar
        tabla_scroll = Scrollbar(frame)
        tabla_scroll.pack(side=RIGHT, fill=Y)
        # Creacion de la tabla
        self.tablaErroresLexicos = ttk.Treeview(
            frame, yscrollcommand=tabla_scroll.set, height=5
        )
        self.tablaErroresLexicos.pack(fill=X)
        # Configurando el scrollbar
        tabla_scroll.config(command=self.tablaErroresLexicos.yview)
        self.fill_table(lexical, self.tablaErroresLexicos)
        label3 = Label(self.top, text="Errores Sintacticos")
        label3.config(font=("Verdana", 10, "bold"))
        label3.pack(anchor=W)
        # Creacion del frame
        frame2 = Frame(self.top, height=300, width=600)
        frame2.pack(pady=20)
        # Creacion del scrollbar
        tabla_scroll2 = Scrollbar(frame2)
        tabla_scroll2.pack(side=RIGHT, fill=Y)
        # Creacion de la tabla
        self.tablaErroresSintacticos = ttk.Treeview(
            frame2, yscrollcommand=tabla_scroll2.set, height=5
        )
        self.tablaErroresSintacticos.pack(fill=X)
        # Configurando el scrollbar
        tabla_scroll2.config(command=self.tablaErroresSintacticos.yview)
        self.fill_table(sintactic, self.tablaErroresSintacticos)
        label4 = Label(self.top, text="Errores Semanticos")
        label4.config(font=("Verdana", 10, "bold"))
        label4.pack(anchor=W)
        # Creacion del frame
        frame3 = Frame(self.top, height=300, width=600)
        frame3.pack(pady=20)
        # Creacion del scrollbar
        tabla_scroll3 = Scrollbar(frame3)
        tabla_scroll3.pack(side=RIGHT, fill=Y)
        # Creacion de la tabla
        self.tablaErroresSemanticos = ttk.Treeview(
            frame3, yscrollcommand=tabla_scroll3.set, height=5
        )
        self.tablaErroresSemanticos.pack(fill=X)
        # Configurando el scrollbar
        tabla_scroll3.config(command=self.tablaErroresSemanticos.yview)
        self.fill_table(semantic, self.tablaErroresSemanticos)
        frame3.grid_columnconfigure(0, weight=1)
        frame3.pack()
        btn = Button(self.top, text="Regresar", command=self.close)
        btn.pack(side=TOP, anchor="center", padx=25, pady=10)
        self.top.mainloop()

    def show_errors(self, lex_errors, sintac_errors, semantic_errors):
        self.fill_table(lex_errors, self.tablaErroresLexicos)
        self.fill_table(sintac_errors, self.tablaErroresSintacticos)
        self.fill_table(semantic_errors, self.tablaErroresSemanticos)

    def fill_table(self, rows, table):
        table.delete(*table.get_children())
        table["columns"] = ("DESCRIPCION", "LINEA")
        # Formato de las columnas
        table.column("#0", width=15, minwidth=5)
        table.column("DESCRIPCION", anchor=W, width=200)
        table.column("LINEA", anchor=W, width=200)
        # Crear Header
        table.heading("#0", text="#", anchor=CENTER)
        table.heading("DESCRIPCION", text="Descripcion", anchor=CENTER)
        table.heading("LINEA", text="Linea", anchor=CENTER)
        """
        Insercion de filas
      """
        i = 0
        for row in rows:
            i += 1
            table.insert(parent="", index="end", iid=i, text=i, values=(row))
        table.pack()

    def close(self):
        self.top.destroy()
