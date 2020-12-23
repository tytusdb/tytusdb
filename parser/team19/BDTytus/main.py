import Gramatica.Gramatica as g
import TablaSimbolos.TS as ts
import graphviz
import sys
import threading
import Errores.Nodo_Error as error
import Errores.ListaErrores as lista_err
from Reportes.ReporteError import ReporteError
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from tkinter import ttk

#------------------------------------ Interfaz ----------------------------------------------------------
class Interfaz():
    def __init__(self):
        self.root = Tk()
        self.root.title('TytusDB - Team 19')
        self.root.geometry("1000x750")
        self.errors = None
        self.raizAST = None
        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open', compound='left', underline=0, command=self.open_File)
        file_menu.add_command(label='Ejecutar', compound='left', underline=0, command=self.ejecutar)
        menu_bar.add_cascade(label='File', menu=file_menu)
        reportes_menu = Menu(menu_bar, tearoff=0)
        reportes_menu.add_command(label='Ventana de Reporte de Errores', compound='left', underline=0, command=self.errores_r)
        reportes_menu.add_separator()
        reportes_menu.add_command(label='Reporte de Errores HTML', compound='left', underline=0,command=self.mostrar_reporte_errores)
        reportes_menu.add_separator()
        reportes_menu.add_command(label='Reporte Gramaticas', compound='left', underline=0)
        reportes_menu.add_separator()
        reportes_menu.add_command(label='Reporte AST', compound='left', underline=0, command=self.mostrar_reporte_AST)
        reportes_menu.add_separator()
        reportes_menu.add_command(label='Tabla de Simbolos', compound='left', underline=0)
        menu_bar.add_cascade(label='Reportes', menu=reportes_menu)
        self.show_line_number = IntVar()
        self.show_line_number.set(1)
        self.root.config(menu=menu_bar)

        my_frame = Frame(self.root)
        my_frame.pack(pady=10)

        text_scroll = Scrollbar(my_frame)
        text_scroll.pack(side=RIGHT, fill=Y)

        self.line_number_bar = Text(my_frame, width=4, padx=3, takefocus=0, fg='white', border=0, background='#282828',
                               state='disabled', wrap='none')
        self.line_number_bar.pack(side='left', fill='y')

        self.my_text = Text(my_frame, width=110, height=30, selectforeground="black", yscrollcommand=text_scroll.set)
        text_scroll.config(command=self.my_text.yview)

        separator = ttk.Separator(self.root, orient='horizontal')
        separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)

        self.Output = Text(self.root, height=10, width=115, bg="light cyan")
        self.my_text.bind('<Any-KeyPress>', self.on_content_changed)

        entrada = self.my_text.get("1.0", END)

        self.my_text.pack()
        separator.pack()
        self.Output.pack()

        self.root.mainloop()

    def ejecutar(self):
        reporteg = []
        global errores, raizAST
        errores = lista_err.ListaErrores()
        entrada = self.my_text.get("1.0", END)
        raizAST = g.parse(entrada, errores)
        self.Output.delete(1.0, "end")
        TS = ts.TabladeSimbolos("global")
        if errores.principio is None:
            respuestaConsola = str(raizAST.ejecutar(TS, errores))
        else:
            respuestaConsola = "Hubieron errores ve a Reporte -> Errores"
            self.errors = errores
        self.Output.insert("1.0", respuestaConsola)

    def open_File(self):
        try:
            text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Text File",
                                                   filetypes=(("Text Files", "*.txt"),))
            text_file = open(text_file, 'r')
            stuff = text_file.read()

            self.my_text.insert(END, stuff)
            self.update_line_numbers()
            text_file.close()
            global raizAST, errores
            raizAST = errores = None
        except FileNotFoundError:
            messagebox.showinfo("Informacion", "No se seleccionó un archivo")


    def mostrar_reporte_errores(self):
        reporte_error = ReporteError(self.errors)
        reporte_error.open_file_on_my_computer()


    def mostrar_reporte_AST(self):
        global raizAST
        if raizAST is not None:
            raizAST.graficarasc()
        else:
            messagebox.showinfo("Informacion", "No hay arbol para mostrar presione ejecutar primero...")

    def errores_r(self):
        ventana = Toplevel(self.root)
        ventana.title('TytusDB - Team 19 | Reporte de Errores')
        tree_errores = ttk.Treeview(ventana)
        tree_errores["columns"] = ("Tipo", "Descripcion", "Fila", "Columna")
        tree_errores.grid(column=1, row=2, sticky=S)
        tree_errores.column("#0", width=0, stretch=NO)
        tree_errores.column("Tipo", width=200, minwidth=200, stretch=NO)
        tree_errores.column("Descripcion", width=400, minwidth=400)
        tree_errores.column("Fila", width=100, minwidth=100)
        tree_errores.column("Columna", width=100, minwidth=100)
        tree_errores.heading("#0", text="No", anchor=W)
        tree_errores.heading("Descripcion", text="Descripcion", anchor=W)
        tree_errores.heading("Tipo", text="Tipo", anchor=W)
        tree_errores.heading("Fila", text="Fila", anchor=W)
        tree_errores.heading("Columna", text="Columna", anchor=W)

        if self.errors.principio is not None:
            reporte_errores = self.errors.principio
            cuenta = 1
            while reporte_errores is not None:
                tree_errores.insert("", cuenta, cuenta, values=(
                reporte_errores.tipo, reporte_errores.descripcion, str(reporte_errores.fila),
                str(reporte_errores.columna)))
                reporte_errores = reporte_errores.siguiente
                cuenta += 1

    def get_line_numbers(self):
        output = ''
        if self.show_line_number.get():
            row, col = self.my_text.index("end").split('.')
            for i in range(1, int(row)):
                output += str(i) + '\n'
        return output

    def on_content_changed(self, event=None):
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        line_numbers = self.get_line_numbers()
        self.line_number_bar.config(state='normal')
        self.line_number_bar.delete('1.0', 'end')
        self.line_number_bar.insert('1.0', line_numbers)
        self.line_number_bar.config(state='disabled')



Interfaz()

