from sys import path
from os.path import dirname as dir
import os
path.append(dir(path[0]))
from tkinter import ttk
import tkinter as tk
from tkinter import *
from ui.Pantalla_TS import *
#from ui.Pantalla_AST import *
from ui.Pantalla_Error import *
import tkinter.messagebox
from analizer import interpreter
from analizer.gramaticaFase2 import parserTo3D , getCodigo
from analizer.reports import BnfGrammar
import json
from json2html import *

class Pantalla:
    def __init__(self):
        self.lexicalErrors = list()
        self.syntacticErrors = list()
        self.semanticErrors = list()
        self.postgreSQL = list()
        self.ts = list()
        self.inicializarScreen()

    def inicializarScreen(self):
        # inicializacion de la pantalla
        self.window = Tk()
        self.window.geometry("700x750")
        self.window.resizable(0, 0)
        self.window.title("Query Tool")
        self.window.config(bg="black")
        self.frame_entrada = Frame(
            self.window, height=300, width=520, bd=10, bg="black"
        )
        self.txt_scroll = Scrollbar(self.frame_entrada)
        self.txt_scroll.pack(side=RIGHT, fill=Y)
        self.txt_entrada = tk.Text(
            self.frame_entrada, yscrollcommand=self.txt_scroll.set, height=15, width=80
        )
        self.txt_entrada.pack(side=TOP)
        self.txt_scroll.config(command=self.txt_entrada.yview)
        self.frame_entrada.pack()
        # Definicion del menu de items
        navMenu = Menu(self.window)
        navMenu.add_command(label="TABLA DE SIMBOLOS", command=self.open_ST)
        navMenu.add_command(label="AST", command=self.open_AST)
        navMenu.add_command(label="REPORTE GRAMATICAL",
                            command=self.reporteGramatical)
        navMenu.add_command(label="REPORTE DE ERRORES",
                            command=self.open_Reporte)
        navMenu.add_command(label="OPTIMIZAR",
                    command=self.optimizar)

        self.window.config(menu=navMenu)
        frame_btn = Frame(self.window)
        btn = Button(frame_btn, text="Ejecutar F1", command=self.analize)
        btn.pack(side=LEFT, anchor=E, padx=25, pady=20)
    
        btn_codigo_3d = Button(
            frame_btn, text="Generar Codigo 3D", command=self.generarCodigo3d)
        btn_codigo_3d.pack(side=LEFT, anchor=E, padx=25, pady=20)
        frame_btn.configure(bg="black")
        frame_btn.pack()
        # Creacion del notebook
        self.tabControl = ttk.Notebook(self.window, width=650, height=300)
        console_frame = Frame(self.tabControl, height=20,
                              width=150, bg="#d3d3d3")
        self.text_Consola = tk.Text(console_frame, height=20, width=150)
        self.text_Consola.pack(fill=BOTH)
        console_frame.pack(fill=BOTH)
        self.tabControl.add(console_frame, text="Consola")
        self.tabControl.pack()
        self.window.mainloop()

    def show_result(self, consults):
        if consults != None:
            i = 0
            for consult in consults:
                i += 1
                if consult != None:
                    frame = Frame(self.tabControl, height=300,
                                  width=450, bg="#d3d3d3")
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
                    self.fill_table(consult[0], consult[1], table)
                    table_scroll.pack(side=RIGHT, fill=Y)
                    table_scrollX.pack(side=BOTTOM, fill=X)
                    table.pack(side=LEFT, fill=BOTH)
                    frame.pack(fill=BOTH)
                    self.tabControl.add(frame, text="Consulta " + str(i))
                else:
                    self.text_Consola.insert(
                        INSERT, "Error: Consulta sin resultado" + "\n"
                    )
        self.tabControl.pack()

    def parse(self):
        self.refresh()
        input = ""
        input = self.txt_entrada.get(
            "1.0", END
        )  # variable de almacenamiento de la entrada
        result = interpreter.parser(input)
        if len(result["lexical"]) + len(result["syntax"]) == 0:
            tkinter.messagebox.showerror(
                title="Mensaje", message="La consulta no contiene errores"
            )
        else:
            self.lexicalErrors = result["lexical"]
            self.syntacticErrors = result["syntax"]
            tkinter.messagebox.showerror(
                title="Error", message="La consulta contiene errores"
            )

    def analize(self):
        self.refresh()
        entrada = ""
        entrada = self.txt_entrada.get(
            "1.0", END
        )  # variable de almacenamiento de la entrada
        result = interpreter.execution(entrada)
        self.lexicalErrors = result["lexical"]
        self.syntacticErrors = result["syntax"]
        self.semanticErrors = result["semantic"]
        self.postgreSQL = result["postgres"]
        self.ts = result["symbols"]
        if (
            len(self.lexicalErrors)
            + len(self.syntacticErrors)
            + len(self.semanticErrors)
            + len(self.postgreSQL)
            > 0
        ):
            tkinter.messagebox.showerror(
                title="Error", message="La consulta contiene errores"
            )
            if len(self.postgreSQL) > 0:
                i = 0
                self.text_Consola.insert(
                    INSERT, "-----------ERRORS----------" + "\n")
                while i < len(self.postgreSQL):
                    self.text_Consola.insert(INSERT, self.postgreSQL[i] + "\n")
                    i += 1
        querys = result["querys"]
        self.show_result(querys)
        messages = result["messages"]
        if len(messages) > 0:
            i = 0
            self.text_Consola.insert(
                INSERT, "-----------MESSAGES----------" + "\n")
            while i < len(messages):
                self.text_Consola.insert(INSERT, str(messages[i]) + "\n")
                i += 1

        self.tabControl.pack()

    def generarCodigo3d(self):
        """
        TODO: METODO para mostrar el codigo 3D en la interfaz
        """
        self.refresh()
        entrada = ""
        entrada = self.txt_entrada.get("1.0", END)
        res = interpreter.generar_codigo_3d(entrada)
        self.lexicalErrors = res["err_lexicos"]
        self.syntacticErrors = res["err_sintacticos"]
        self.semanticErrors = res["semantic"]
        self.ts = res["symbols"]
        if (
            len(self.lexicalErrors)
            + len(self.syntacticErrors)
           + len(self.semanticErrors)
           # + len(self.postgreSQL)
            > 0
           ):
            tkinter.messagebox.showerror(
                title="Error", message="la entrada posee errores"
            )
        else:
            cadena_codigo_3d = getCodigo()
            self.text_Consola.insert(INSERT, cadena_codigo_3d)

    def refresh(self):
        tabls = self.tabControl.tabs()
        i = 1
        while i < len(tabls):
            self.tabControl.forget(tabls[i])
            i += 1
        self.text_Consola.delete("1.0", "end")
        self.semanticErrors.clear()
        self.syntacticErrors.clear()
        self.lexicalErrors.clear()
        self.postgreSQL.clear()
        self.ts.clear()

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

    def open_ST(self):  # Abre la pantalla de la table de simbolos
        # info = self.read('Database.json')
        # f = open("tb.html", "w")
        # f.write(json2html.convert(json=info))
        # f.close()
        # os.system('tb.html')
        windowTableS = Pantalla_TS(self.window, self.ts)
    def read(self ,path: str) -> dict:
        with open(path) as file:
            return json.load(file)
    def open_AST(self):  # Abre la pantalla del AST
        os.system('cd ./test-output & round-table.gv.svg')


    def open_Reporte(self):  # Abre la pantalla de los reportes de errores
        windowTableS = Pantalla_Error(
            self.window, self.lexicalErrors, self.syntacticErrors, self.semanticErrors
        )
    def optimizar(self):
        pass#metodo cante :v

    def reporteGramatical(self):
        os.system('cd test-output & ReporteGramatica.bnf')


def main():  # Funcion main
    queryTool = Pantalla()
    return 0


if __name__ == "__main__":
    main()