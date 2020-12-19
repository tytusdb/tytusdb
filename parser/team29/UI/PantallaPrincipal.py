from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
from tkinter import ttk
import tkinter as tk
from tkinter import *
from ui.Pantalla_TS import *
from ui.Pantalla_AST import *
from ui.Pantalla_Error import *
import tkinter.messagebox
from analizer import grammar


class Pantalla:
    def __init__(self):
        self.lexicalErrors = list()
        self.sintacticErrors = list()
        self.semanticErrors = list()
        self.inicializarScreen()

    def inicializarScreen(self):
        # inicializacion de la pantalla
        self.window = Tk()
        self.window.geometry("700x700")
        self.window.resizable(0, 0)
        self.window.title("Query Tool")
        self.txtEntrada = tk.Text(self.window, height=15, width=80)
        self.txtEntrada.pack(side=TOP)
        # Definicion del menu de items
        navMenu = Menu(self.window)
        navMenu.add_command(
            label="               Tabla de Simbolos             ", command=self.open_ST
        )
        navMenu.add_command(
            label="                    AST                      ", command=self.open_AST
        )
        navMenu.add_command(
            label="              Reporte de errores              ",
            command=self.open_Reporte,
        )
        self.window.config(menu=navMenu)
        btn = Button(self.window, text="Consultar", command=self.analize)
        btn.pack(side=TOP, anchor=E, padx=25, pady=20)
        self.frame = Frame(self.window, height=300, width=520, bd=10, bg="#d3d3d3")
        # Creacion del scrollbar
        self.tabla_scroll = Scrollbar(self.frame)
        self.tabla_scroll.pack(side=RIGHT, fill=Y)
        self.tabla_scrollX = Scrollbar(self.frame, orient="horizontal")
        self.tabla_scrollX.pack(side=BOTTOM, fill=X)
        self.tabla = ttk.Treeview(
            self.frame,
            yscrollcommand=self.tabla_scroll.set,
            xscrollcommand=self.tabla_scrollX.set,
            height=12,
        )
        self.tabla_scroll.config(command=self.tabla.yview)
        self.tabla_scrollX.config(command=self.tabla.xview)
        self.window.mainloop()

    def analize(self):
        self.tabla.pack_forget()
        self.tabla_scroll.pack_forget()
        self.tabla_scrollX.pack_forget()
        entrada = self.txtEntrada.get(
            "1.0", END
        )  # variable de almacenamiento de la entrada
        result = grammar.parse(entrada)
        self.lexicalErrors = grammar.returnLexicalErrors()
        self.sintacticErrors = grammar.returnSintacticErrors()
        if len(self.lexicalErrors) + len(self.sintacticErrors) > 0:
            tkinter.messagebox.showerror(
                title="Error", message="El archivo contiene errores"
            )

    def fill_table(
        self, columns, rows
    ):  # funcion que muestra la salida de la/s consulta/s
        self.tabla["columns"] = columns
        """
        Definicion de columnas y encabezado
        """
        self.tabla.column("#0", width=25, minwidth=50)
        i = 0
        while i < len(columns):
            self.tabla.column(str(columns[i]), width=100, minwidth=50)
            i += 1
        self.tabla.heading("#0", text="#", anchor=CENTER)
        i = 0
        while i < len(columns):
            self.tabla.heading(str(columns[i]), text=str(columns[i]), anchor=CENTER)
            i += 1
        """
        Insercion de filas
        """
        i = 0
        for row in rows:
            i += 1
            self.tabla.insert(parent="", index="end", iid=i, text=i, values=(row))
        self.tabla_scroll.pack(side=RIGHT, fill=Y)
        self.tabla_scrollX.pack(side=BOTTOM, fill=X)
        self.tabla.pack(expand=0)
        self.frame.pack(expand=0)

    def open_ST(self):  # Abre la pantalla de la tabla de simbolos
        windowTableS = Pantalla_TS(self.window)

    def open_AST(self):  # Abre la pantalla del AST
        windowTableS = Pantalla_AST(self.window)

    def open_Reporte(self):  # Abre la pantalla de los reportes de errores
        windowTableS = Pantalla_Error(
            self.window, self.lexicalErrors, self.sintacticErrors, self.semanticErrors
        )


def main():  # Funcion main
    queryTool = Pantalla()
    return 0


if __name__ == "__main__":
    main()
