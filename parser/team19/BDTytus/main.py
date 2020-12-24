import Gramatica.Gramatica as g
import TablaSimbolos.TS as ts
import os
import graphviz
import sys
import threading
import Errores.Nodo_Error as error
import Errores.ListaErrores as lista_err
from Reportes.ReporteError import ReporteError
from Reportes.ReporteGramatical import ReporteGramatical
from Reportes.ReporteTS import ReporteTS
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
import os, shutil


if __name__=='__main__':
    from LineNumber import LineMain
    from Graphics import Tkinter
    from ColorLight import ColorLight
else:
    from LineNumber import LineMain
    from Graphics import Tkinter
    from ColorLight import ColorLight

class Connect:
    def __init__(self, pad):
        self.pad = pad
        self.modules_connections()

    def modules_connections(self):
        LineMain(self.pad)
        ColorLight(self.pad)
        return

class TextPad(Tkinter.Text):
    def __init__(self, *args, **kwargs):
        Tkinter.Text.__init__(self, *args, **kwargs)
        self.storeobj = {"Root": self.master}
        self.Connect_External_Module_Features()
        self.config(font=("Consolas", 11), padx=2, pady=2)
        self._pack()

    def Connect_External_Module_Features(self):
        Connect(self)
        return

    def _pack(self):
        self.pack(expand = True, fill = "both")
        return

#------------------------------------ Interfaz ----------------------------------------------------------
class Interfaz:
    def __init__(self):
        os.environ['DB'] = 'None'
        self.borrarArchivos()
        self.root = Tk()
        #self.root.attributes('-zoomed', True)
        self.root.title('TytusDB - Team 19')
        self.root.geometry("1100x700")
        self.root.resizable(1, 1)
        self.txtarea = TextPad(self.root, pady=5)
        self.consola = scrolledtext.ScrolledText(self.root, width=300, height=15, font=("Consolas", 11))
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=X, side='left')
        #self.tree_consultas = ttk.Treeview(self.frame)
        #self.tree_consultas["columns"] = ("Tipo", "Descripcion", "Fila", "Columna")
        #self.tree_consultas.grid(column=1, row=2, sticky=S)
        #self.tree_consultas.column("#0", width=600, stretch=NO)
        #self.tree_consultas.column("Tipo", width=50, minwidth=20, stretch=NO)
        #self.tree_consultas.column("Descripcion", width=50, minwidth=20)
        #self.tree_consultas.column("Fila", width=50, minwidth=20)
        #self.tree_consultas.column("Columna", width=50, minwidth=20)
        #self.tree_consultas.heading("#0", text="HOla", anchor=W)
        #self.tree_consultas.heading("Descripcion", text="Descripcion", anchor=W)
        #self.tree_consultas.heading("Tipo", text="Tipo", anchor=W)
        #self.tree_consultas.heading("Fila", text="Fila", anchor=W)
        #self.tree_consultas.heading("Columna", text="Columna", anchor=W)
        self.v = StringVar()
        lab = Label(self.root, textvariable=self.v, font=("Helvetica", 11, "bold"))
        self.v.set('Base de Datos: ' + os.environ['DB'])
        lab.pack(side=TOP, anchor=E)
        lbl = Label(self.root, text="Consola de Salida:", font=("Helvetica", 11))
        lbl.pack(side=TOP, anchor=W)
        #self.tree_consultas.pack(side=LEFT, fill=X, pady=5, padx=5)
        self.consola.pack(side=RIGHT)
        self.consola.config(foreground='white', bg = 'black')
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        archivo = Menu(self.menubar, tearoff=0)
        archivo.add_command(label="Limpiar Pantalla",
                            command=self.limpiar)
        archivo.add_separator()
        archivo.add_command(label="Abrir Archivo",
                            command=self.abriarchivo)
        archivo.add_separator()
        archivo.add_command(label="Guardar",
                            command=self.guardar)
        archivo.add_command(label="Guardar Como",
                            command=self.guardarcomo)
        self.menubar.add_cascade(label="Archivo", menu=archivo)
        ejecucioin = Menu(self.menubar, tearoff=0)
        ejecucioin.add_command(label="Ejecutar", command=self.ejecutar)

        self.menubar.add_cascade(label="Ejecucion", menu=ejecucioin)
        reportes = Menu(self.menubar, tearoff=0)
        reportes.add_command(label="Reporte AST", command=self.mostrar_reporte_AST)
        reportes.add_separator()
        reportes.add_command(label='Reporte Gramatica', command=self.mostrar_gramatica)
        reportes.add_separator()
        reportes.add_command(label='Reporte Errores', command=self.errores_r)
        reportes.add_command(label='Reporte Errores HTML', command=self.mostrar_reporte_errores)
        reportes.add_separator()
        reportes.add_command(label='Tabla de Simbolos', command=self.mostrar_reporte_TS)
        self.menubar.add_cascade(label="Reportes", menu=reportes)
        opciones = Menu(self.menubar, tearoff=0)
        opciones.add_command(label="Acerca de...")
        opciones.add_separator()
        opciones.add_command(label="Manual de Usuario")
        opciones.add_command(label="Manual Tecnico")
        self.menubar.add_cascade(label="Opciones", menu=opciones)

        self.errors = None
        self.raizAST = None
        self.TS:ts.TabladeSimbolos = None
        entrada = self.txtarea.get("1.0", END)
        self.root.mainloop()


    def limpiar(self):
        self.txtarea.delete(1.0, END)
        self.archivoactgual = "v"
        self.consola.delete(1.0,END)

    def abriarchivo(self):
        filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*")])
        if filename:
            self.archivoactgual = filename
            self.txtarea.delete(1.0, END)
            with open(filename, "r") as f:
                self.txtarea.insert(1.0, f.read())


    def guardar(self):
        if self.archivoactgual == '':
            filename = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=[("All Files", "*.*")])
        else:
            filename=self.archivoactgual
        if filename:
            try:
                contenido = self.txtarea.get(1.0, END)
                with open(filename, "w") as f:
                    f.write(contenido)
            except Exception as e:
                print(e)


    def guardarcomo(self):
        try:
            nuevoarchivo = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css")])
            contenido = self.txtarea.get(1.0, END)
            with open(nuevoarchivo, "w") as f:
                f.write(contenido)
        except Exception as e:
            print(e)


    def ejecutar(self):
        reporteg = []
        self.errors = lista_err.ListaErrores()
        entrada1 = self.txtarea.get("1.0", END)
        entrada = entrada1.lower()
        self.raizAST = g.parse(entrada, self.errors)
        self.consola.delete(1.0, "end")
        self.TS = ts.TabladeSimbolos()
        if self.errors.principio is None:
            respuestaConsola = str(self.raizAST.ejecutar(self.TS, self.errors))
            #respuestaConsola = 'Si paso'
        else:
            respuestaConsola = "Hubieron errores ve a Reporte -> Errores"
        self.v.set('Base de Datos: ' + os.environ['DB'])
        self.consola.insert("1.0", respuestaConsola)

    def entorno(self):
        print(os.environ['DB'])

    def open_File(self):
        try:
            text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Text File",
                                                   filetypes=(("Text Files", "*.txt"),))
            text_file = open(text_file, 'r')
            stuff = text_file.read()

            self.my_text.insert(END, stuff)
            self.update_line_numbers()
            text_file.close()
            self.TS = self.raizAST = self.errors = None
        except FileNotFoundError:
            messagebox.showinfo("Informacion", "No se seleccionó un archivo")

    def mostrar_gramatica(self):
        reporte = ReporteGramatical()
        reporte.open_file_on_my_computer()

    def mostrar_reporte_errores(self):
        reporte_error = ReporteError(self.errors)
        reporte_error.open_file_on_my_computer()


    def mostrar_reporte_AST(self):
        if self.raizAST is not None:
            self.raizAST.graficarasc()
        else:
            messagebox.showinfo("Informacion", "No hay arbol para mostrar presione ejecutar primero...")

    def mostrar_reporte_TS(self):
        reporteTS = ReporteTS(self.TS)
        reporteTS.open_file_on_my_computer()
            


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

    def borrarArchivos(self):
        folder = 'data/json'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

Interfaz()

