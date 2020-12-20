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
        self.frame_entrada= Frame(self.window,height=300,width=520,bd=10,bg='#d3d3d3')
        self.txt_scroll = Scrollbar(self.frame_entrada)
        self.txt_scroll.pack(side=RIGHT, fill=Y)
        self.txt_entrada = tk.Text(self.frame_entrada,yscrollcommand=self.txt_scroll.set,height=15,width=80)
        self.txt_entrada.pack(side=TOP)
        self.txt_scroll.config(command=self.txt_entrada.yview)
        self.frame_entrada.pack()
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
        #Creacion del notebook
        self.tabControl = ttk.Notebook(self.window,width=650,height=300)
        self.tabControl.pack()
        #data=[[["columna1","columna2","columna1","columna2","columna1","columna2"],[["dato1","dato2","dato1","dato2","dato1","dato2"],["dato3","dato4","dato1","dato2","dato1","dato2"]]],[["columan23","columna234"],[["dato3","dato4"],["dato5","dato6"]]]]
        #self.show_result(data)
        self.window.mainloop()

    def show_result(self, consults):
        i=0
        for consult in consults:
            i+=1
            frame = Frame(self.tabControl, height=300, width=450, bg="#d3d3d3")
            # Creacion del scrollbar
            tabla_scroll = Scrollbar(frame,orient='vertical')            
            tabla_scrollX = Scrollbar(frame, orient="horizontal")
            tabla = ttk.Treeview(frame,yscrollcommand=tabla_scroll.set,xscrollcommand=tabla_scrollX.set,height=12)
            tabla_scroll.config(command=tabla.yview)
            tabla_scrollX.config(command=tabla.xview)
            self.fill_table(consult[0],consult[1],tabla)
            tabla_scroll.pack(side=RIGHT, fill=Y)
            tabla_scrollX.pack(side=BOTTOM, fill=X)
            tabla.pack(side=LEFT,fill=BOTH)                      
            frame.pack(fill=BOTH)
            self.tabControl.add(frame, text='Consulta '+str(i))
        self.tabControl.pack()

    def analize(self):
        entrada = self.txtEntrada.get("1.0", END)  # variable de almacenamiento de la entrada
        result = grammar.parse(entrada)
        self.lexicalErrors = grammar.returnLexicalErrors()
        self.sintacticErrors = grammar.returnSintacticErrors()
        self.semanticErrors = grammar.returnSemanticErrors()
        self.postgreSQL = grammar.returnPostgreSQLErrors()
        if len(self.lexicalErrors) + len(self.sintacticErrors) + len(self.semanticErrors) > 0:
            tkinter.messagebox.showerror( title="Error", message="El archivo contiene errores" )
        
        
    def fill_table(
        self, columns, rows,tabla
    ):  # funcion que muestra la salida de la/s consulta/s
        tabla["columns"] = columns
        """
        Definicion de columnas y encabezado
        """
        tabla.column("#0", width=25, minwidth=50)
        i = 0
        while i < len(columns):
            tabla.column(str(i), width=100, minwidth=50)
            i += 1
        tabla.heading("#0", text="#", anchor=CENTER)
        i = 0
        while i < len(columns):
            tabla.heading(str(i), text=str(columns[i]), anchor=CENTER)
            i += 1
        """
        Insercion de filas
        """
        i = 0
        for row in rows:
            i += 1
            tabla.insert(parent="", index="end", iid=i, text=i, values=(row))
        

    def open_ST(self):  # Abre la pantalla de la tabla de simbolos
        windowTableS = Pantalla_TS(self.window)

    def open_AST(self):  # Abre la pantalla del AST
        windowTableS = Pantalla_AST(self.window)

    def open_Reporte(self):  # Abre la pantalla de los reportes de errores
        windowTableS = Pantalla_Error(self.window, self.lexicalErrors, self.sintacticErrors, self.semanticErrors)


def main():  # Funcion main
    queryTool = Pantalla()
    return 0


if __name__ == "__main__":
    main()