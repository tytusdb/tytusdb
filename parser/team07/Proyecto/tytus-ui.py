import os
from tkinter import *
from tkinter import ttk
import gramatica as g


class menubar:
    def __init__(self, parent):
        self.app = parent.app

        self.menubar = Menu(self.app)
        self.app.config(menu=self.menubar)
        # Menu de analizador
        self.analizador_menu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Analizador", menu=self.analizador_menu)
        self.analizador_menu.add_command(
            label="Parsear", command="parse_grammar")

        # Menu de reportes
        self.reportes_menu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Reportes", menu=self.reportes_menu)
        self.reportes_menu.add_command(label="AST")
        self.reportes_menu.add_command(label="TablaSimbolos")
        self.reportes_menu.add_command(label="Gramatical")


class Pytext:
    def __init__(self, parent):
        self.app = parent.app
        self.parent = parent
        # scroll bar
        self.scroll = Scrollbar(parent.tab1, command=self.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.line_number_bar = Text(parent.tab1, width=4, padx=3, takefocus=0, border=0,
                                    background='khaki', state='disabled', wrap='none', yscrollcommand=self.scroll.set)
        self.line_number_bar.pack(side=LEFT, fill=Y)
        # textarea for SQL code
        self.textarea = Text(parent.tab1, width=97,
                             height=25, font=("Arial, 12"), yscrollcommand=self.scroll.set)
        self.textarea.pack()
        self.textarea.bind('<Any-KeyPress>', self.cambio_contenido_text)

        self.menu = menubar(self)

    def yview(self, *args):
        self.textarea.yview(*args)
        self.line_number_bar.yview(*args)

    def cambio_contenido_text(self, event=None):
        self.generar_numero_lineas()

    def generar_numero_lineas(self, event=None):
        line_numbers = self.get_line_numbers()
        self.line_number_bar.config(state='normal')
        self.line_number_bar.delete('1.0', 'end')
        self.line_number_bar.insert('1.0', line_numbers)
        self.line_number_bar.config(state='disabled')

    def get_line_numbers(self):
        output = ''
        row, col = self.textarea.index('end').split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
        return output


class tabs:
    def __init__(self, frame, app):
        self.app = app

        shortcut_bar = Frame(frame.upper_frame,  height=25,
                             background='deep sky blue')
        shortcut_bar.pack(expand='no', fill='x')

        # Agrego pestañas
        self.tab_control = ttk.Notebook(frame.upper_frame)

        # definicion de tabs
        self.tab1 = Frame(self.tab_control)

        self.tab_control.add(self.tab1, text='SQL Editor')
        self.tab_control.pack(expand=True, fill=BOTH, padx=10, pady=10)

        self.textArea = Pytext(self)

        # Creo el text area y le agrego el sroll
        self.ConsolaName = Label(frame.middle_frame, text='Consola:')
        self.ConsolaName.pack(padx=10, pady=10)
        self.ConsolaFrame = Frame(frame.buttom_frame,  bg='grey')
        self.ConsolaFrame.pack(padx=10, pady=10)
        self.consola = Text(self.ConsolaFrame)
        self.scroll = Scrollbar(
            self.ConsolaFrame, command=self.consola.yview)
        self.consola.configure(yscrollcommand=self.scroll.set)
        self.consola.pack(side=LEFT, fill=BOTH)
        self.scroll.pack(side=RIGHT, fill=Y)

    def parse_gramar(self):
        cadena = self.textArea.textarea.get(1.0, tk.END)
        instrucciones = g.parse(cadena)


class mainwindow:
    def __init__(self, app):
        app.title("TytusDB Team07 - Compiladores 2")
        app.geometry("1000x700")

        self.app = app

        self.upper_frame = Frame(app,  bg='grey')
        self.upper_frame.pack(fill=BOTH)
        self.middle_frame = Frame(app,  bg='grey')
        self.middle_frame.pack(fill=BOTH)
        self.buttom_frame = Frame(app,  bg='grey')
        self.buttom_frame.pack(fill=BOTH)

        self.pestanas = tabs(self, app)


if __name__ == "__main__":
    app = Tk()
    Interfaz = mainwindow(app)
    app.mainloop()
