import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import Font
import gramatica as g
from tabla_Simbolos import tablaSimbolos
from Errores import errorReportar
from clasesAbstractas import instruccionAbstracta
from graficarArbol import GraphArbol
import jsonMode


class menubar:
    def __init__(self, parent):
        self.app = parent.app
        self.parent = parent

        self.menubar = Menu(self.app)
        self.app.config(menu=self.menubar)
        # Menu de analizador
        self.analizador_menu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Analizador", menu=self.analizador_menu)
        self.analizador_menu.add_command(
            label="Parsear", command=self.parent.parent.parse_grammar)

        # Menu de reportes
        self.reportes_menu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Reportes", menu=self.reportes_menu)
        self.reportes_menu.add_command(label="AST")
        self.reportes_menu.add_command(
            label="TablaSimbolos", command=self.parent.parent.TSReport)
        self.reportes_menu.add_command(label="Gramatical")
        self.reportes_menu.add_command(
            label="Errores", command=self.parent.parent.ErrorReport)
        self.reportes_menu.add_command(
            label="Mensajes", command=self.parent.parent.MensajesReport)


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
    global miListaErrores  # = []  # Inicializar
    miListaErrores = []
    global miTablaSimbolos
    miTablaSimbolos = tablaSimbolos.tablaDeSimbolos()

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

    def cut(self):
        self.textArea.textarea.event_generate("<<Cut>>")
        self.textArea.cambio_contenido_text()
        return "break"

    def copy(self):
        self.textArea.textarea.event_generate("<<Copy>>")
        return "break"

    def paste(self):
        self.textArea.textarea.event_generate("<<Paste>>")
        self.textArea.cambio_contenido_text()
        return "break"

    def undo(self):
        self.textArea.textarea.event_generate("<<Undo>>")
        self.textArea.cambio_contenido_text()
        return "break"

    def redo(self, event=None):
        self.textArea.textarea.event_generate("<<Redo>>")
        self.textArea.cambio_contenido_text()
        return 'break'

    def procesar_instrucciones(self, instrucciones, tablaSimbolos, listaErrores):
        for instrucion in instrucciones:

            if isinstance(instrucion, instruccionAbstracta.InstruccionAbstracta):
                instrucion.ejecutar(tablaSimbolos, listaErrores)
                print("entro")

    def parse_grammar(self):
        cadena = self.textArea.textarea.get(1.0, tk.END)
        global miTablaSimbolos
        global miListaErrores  # Será una lista de de objetos: errorReportar
        instrucciones = g.parse(cadena)
        # print(len(instrucciones.hijos))
        # print(instrucciones)
        self.procesar_instrucciones(instrucciones.hijos,
                                    miTablaSimbolos, miListaErrores)

        grafica = GraphArbol(instrucciones)
        grafica.crearArbol()

    def ErrorReport(self):
        global miListaErrores
        ventana_reporte_errores(app, miListaErrores)

    def TSReport(self):
        ventana_reporte_ts(app, miTablaSimbolos)

    def MensajesReport(self):
        global miTablaSimbolos
        ventana_reporte_mensajes(app, miTablaSimbolos)


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

# clase reporte de errores


class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(
            self, text=title, background="#7BD7E2", font=("Helvetica", 16))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers,
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")

        # Agregamos dos scrollbars
        vsbs = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsbs.pack(side='right', fill='y')
        hsbs = ttk.Scrollbar(self, orient="horizontal",
                             command=self._tree.xview)
        hsbs.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsbs.set, yscrollcommand=vsbs.set)
        self._tree.pack(side="left")

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True)

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                self._tree.column(self._headers[i], width=col_width)


def ventana_reporte_errores(parent, report):
    t3 = tk.Toplevel(parent, bg="#7BD7E2")
    t3.title("Reporte")
    t3.geometry('700x400')
    t3.configure(bg="#7BD7E2")
    t3.focus_set()
    t3.grab_set()

    errores_headers = (u" Fila ", u" Columna ", u"           Tipo         ",
                       u"             Descripicon            ")
    errores_tab = Table(t3, title="Reporte de Errores",
                        headers=errores_headers)
    errores_tab.pack()
    listaCad = []
    cont = 0
    if report != None:
        for x in report:
            a = [x.fila, x.columna, x.tipoError, x.descripcion]
            print(x.fila)
            listaCad.append(a)

    for row in listaCad:
        errores_tab.add_row(row)


def ventana_reporte_ts(parent, report):
    t3 = tk.Toplevel(parent, bg="#7BD7E2")
    t3.title("Reporte")
    t3.geometry('950x400')
    t3.configure(bg="#7BD7E2")
    t3.focus_set()
    t3.grab_set()

    ts_headers = (u"No.", u" Base de datos  ", u" Tablas    ",
                  u" Columna    ", u" Tipo de dato  ")
    ts_tab = Table(t3, title="Tabla de simbolos",
                   headers=ts_headers)
    ts_tab.pack()
    listaCad = []
    cont = 0
    value = report.basesDatos
    if value != None:
        for x in value:
            cont = cont+1
            try:
                a = [cont, x.nombre, "", "", ""]
                listaCad.append(a)
                value2 = x.tablas
                for y in value2:
                    cont = cont+1
                    b = [cont, x.nombre, y.nombre, "", ""]
                    listaCad.append(b)
                    value3 = y.columnas
                    for z in value3:
                        cont = cont+1
                        c = [cont, x.nombre, y.nombre, z.nombre, z.tipoDato]
                        listaCad.append(c)
            except:
                pass

    for row in listaCad:
        ts_tab.add_row(row)


def ventana_reporte_mensajes(parent, report):
    t3 = tk.Toplevel(parent, bg="#7BD7E2")
    t3.title("Mensajes")
    t3.geometry('700x400')
    t3.configure(bg="#7BD7E2")
    t3.focus_set()
    t3.grab_set()

    mensajes_headers = (u"No. ", u" Mensaje ")
    mensajes_tab = Table(t3, title="Reporte de mensajes",
                         headers=mensajes_headers)
    mensajes_tab.pack()
    listaCad = []
    cont = 0
    if report != None:
        value = report.listaMensajes
        for x in value:
            cont = cont + 1
            a = [cont, x]
            listaCad.append(a)

    for row in listaCad:
        mensajes_tab.add_row(row)


if __name__ == "__main__":
    app = Tk()
    Interfaz = mainwindow(app)
    app.mainloop()
