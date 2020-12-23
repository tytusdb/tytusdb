from tkinter import *
from tkinter.ttk import *


class SymbolTable:
    symbols = []
    treeview = None

    @staticmethod
    def create(parent):
        tree = Treeview(parent)
        tree['columns'] = ('tipo', 'nombreTabla')
        tree.heading('#0', text='Nombre')
        tree.column('#0', anchor='center', width=25)
        tree.heading('tipo', text='TIPO')
        tree.column('tipo', anchor='center', width=200)
        tree.heading('nombreTabla', text='Nombre Tabla')
        tree.column('nombreTabla', anchor='center', width=25)

        tree.grid(sticky=(N, S, W, E))

        SymbolTable.treeview = tree

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    @staticmethod
    def load():
        for i in range(len(SymbolTable.symbols)):
            SymbolTable.treeview.insert('', 'end', text=SymbolTable.symbols[i][0], values=(
                SymbolTable.symbols[i][1], SymbolTable.symbols[i][2]))
        SymbolTable.symbols = []

    @staticmethod
    def clear():
        SymbolTable.treeview.delete(*SymbolTable.treeview.get_children())

    @staticmethod
    def add(list):
        SymbolTable.symbols.append(list)
