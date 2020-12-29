import tkinter
from tkinter import *
from tkinter import ttk, scrolledtext, filedialog, messagebox

from Statics.console import Console
from Statics.errorTable import ErrorTable
from Statics.symbolTable import SymbolTable

from Interpreter import ascparse
from Interpreter.ast import Ast

from .entrada import EntradaEditor


class Window():

    def __init__(self):
        self.window = Tk()

        self.window.title("Query Tool")
        self.window.minsize(900, 600)

        # MENÚ 'Principal':
        main_menu = Menu(self.window)
        self.window['menu'] = main_menu

        main_menu.add_command(label='Abrir',
                              command=self.open,
                              underline=0, accelerator="Ctrl+a",
                              compound=LEFT)

        main_menu.add_command(label='Ejecutar',
                              command=self.execute,
                              underline=0, accelerator="Ctrl+r",
                              compound=LEFT)

        # INPUT:
        self.notebook = ttk.Notebook(self.window, height="350", width="900")
        self.notebook.pack()
        # Editor de texto
        frame = tkinter.Frame(self.notebook, bg='white')
        self.notebook.add(frame, text="Entrada")
        self.entradaEditor = EntradaEditor(frame)

        # OUTPUT:
        self.out = ttk.Notebook(self.window, height="185", width="900")
        self.out.pack()
        # Consola
        frame = tkinter.Frame(self.out, bg='white')
        self.out.add(frame, text="Consola")
        Console.create(frame)
        # Tabla de reporte de errores
        frame = tkinter.Frame(self.out, bg='white')
        self.out.add(frame, text="Reporte de errores")
        ErrorTable.create(frame)
        # Tabla de simbolos
        frame = tkinter.Frame(self.out, bg='white')
        self.out.add(frame, text="Tabla de Símbolos")
        SymbolTable.create(frame)

        """ initInput = "./Scripts/Consultas.sql"
        data = open(initInput).read()
        self.entradaEditor.text.insert(END, data + "\n") """

        self.window.mainloop()

    def execute(self):
        Console.clear()
        data = self.entradaEditor.text.get("1.0", END)
        root = ascparse.parse(data)
        AST = Ast(root)
        AST.execute()
        AST.getGraph()

    def open(self):
        file_path = filedialog.askopenfilename()
        f = open(file_path, 'r')
        input = f.read()
        input = input.lower()
        f.close()
        self.entradaEditor.text.delete('1.0', END)
        self.entradaEditor.text.insert(END, input + "\n")
