import os
from tkinter import *


class mainwindow:
    def __init__(self, app):
        app.title("TytusDB - Compiladores 2")
        app.geometry("1100x560")

        window = Frame(app)
        window.pack(pady=5)
        # scroll bar
        textarea_scroll = Scrollbar(window)
        textarea_scroll.pack(side=RIGHT, fill=Y)
        # textarea for SQL code
        textarea = Text(window, width=97, height=25, font=("Arial, 12"))
        textarea.pack()

        # Config of scrollbar
        textarea_scroll.config(command=textarea.yview)

        # Barra de opciones
        menubar = Menu(app)
        app.config(menu=menubar)
        # Menu de analizador
        analizador_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Analizador", menu=analizador_menu)
        analizador_menu.add_command(label="Parsear", command="parse_grammar")

        # Menu de reportes
        reportes_menu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Reportes", menu=reportes_menu)
        reportes_menu.add_command(label="AST")
        reportes_menu.add_command(label="TablaSimbolos")
        reportes_menu.add_command(label="Gramatical")

        # Status bar
        statusbar = Label(app, text="Listo ", anchor=E)
        statusbar.pack(fill=X, side=BOTTOM, ipady=5)

    def parse_grammar(self):
        cadena = textarea.get(1.0, END)


if __name__ == "__main__":
    app = Tk()
    Interfaz = mainwindow(app)
    app.mainloop()
