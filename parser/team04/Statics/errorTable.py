from tkinter import *
from tkinter.ttk import *


class ErrorTable:
    errors = []
    treeview = None

    @staticmethod
    def create(parent):
        tree = Treeview(parent)
        tree['columns'] = ('description', 'line')
        tree.heading('#0', text='Tipo')
        tree.column('#0', anchor='center', width=25)
        tree.heading('description', text='Descripción')
        tree.column('description', anchor='center', width=200)
        tree.heading('line', text='Línea')
        tree.column('line', anchor='center', width=25)
        tree.grid(sticky=(N, S, W, E))

        ErrorTable.treeview = tree

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    @staticmethod
    def load():
        for i in range(len(ErrorTable.errors)):
            ErrorTable.treeview.insert('', 'end', text=ErrorTable.errors[i][0], values=(
                ErrorTable.errors[i][1], ErrorTable.errors[i][2]))
        ErrorTable.errors = []

    @staticmethod
    def clear():
        ErrorTable.treeview.delete(*ErrorTable.treeview.get_children())

    @staticmethod
    def add(list):
        ErrorTable.errors.append(list)
