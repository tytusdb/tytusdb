from tkinter import *
import shutil
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb
from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, \
    Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog, font
import tkinter as tk
from tabulate import tabulate
import os

from grammarReview import *


class query_tool:
    def __init__(self, window):
        self.vp = window
        self.rutaArchivo = ""
        self.nombreArchivo = ""
        self.extension = ""
        self.texto = ""
        self.txtConsola = ""
        self.inputText = ""

        ###################################################### INTERFAZ GRÁFICA ######################################################
        # Ventana Principal
        self.vp.title("Tytus - Query Tool")
        self.barraMenu = Menu(self.vp)
        self.vp.configure(menu=self.barraMenu)

        # Labels
        tk.Label(self.vp, fg="white", bg="#154360", text="TYTUS - Query Tool", font=("Arial Bold", 15)).grid(row=0,
                                                                                                             column=1,
                                                                                                             sticky=E + W)
        tk.Label(self.vp, fg="white", bg="#154360", text="Linea : 1 Columna : 1", font=("Arial Bold", 10)).grid(row=2,
                                                                                                                column=1,
                                                                                                                sticky=E + W)

        # Canvas
        self.canvas1 = tk.Canvas(self.vp, width=1300, height=300)
        self.canvas1.grid(row=4, column=1, sticky=E + W)

        self.canvas2 = tk.Canvas(self.vp, width=1200, height=275)
        self.canvas2.grid(row=5, column=1, sticky='news')

        # Frames
        self.frame1 = tk.LabelFrame(self.canvas1, bg="#154360", text="Entrada:", font=("Arial Bold", 10),
                                    foreground="white")
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frame2 = tk.LabelFrame(self.canvas2, bg="#154360", text="Resultados:", font=("Arial Bold", 10),
                                    foreground="white")
        self.frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

        # TextArea
        self.entrada = tk.Text(self.frame1, font=("Courier New", 10), foreground="#154360")
        self.entrada.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)

        self.scrollbarEntradaX = tk.Scrollbar(self.entrada, orient=tk.HORIZONTAL)
        self.scrollbarEntradaX.pack(side="bottom", fill="x")

        self.scrollbarEntradaY = tk.Scrollbar(self.entrada)
        self.scrollbarEntradaY.pack(side="right", fill="y")

        self.entrada.config(wrap="none", xscrollcommand=self.scrollbarEntradaX.set,
                            yscrollcommand=self.scrollbarEntradaY.set)
        self.scrollbarEntradaY.config(command=self.entrada.yview)
        self.scrollbarEntradaX.config(command=self.entrada.xview)

        # Consola
        self.consola = tk.Text(self.frame2, font=("Courier New", 9), background="black", foreground="yellow")
        self.consola.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)

        self.scrollbarConsolaX = tk.Scrollbar(self.consola, orient=tk.HORIZONTAL)
        self.scrollbarConsolaX.pack(side="bottom", fill="x")

        self.scrollbarConsolaY = tk.Scrollbar(self.consola)
        self.scrollbarConsolaY.pack(side="right", fill="y")

        self.consola.config(wrap="none", xscrollcommand=self.scrollbarConsolaX.set,
                            yscrollcommand=self.scrollbarConsolaY.set)
        self.scrollbarConsolaY.config(command=self.consola.yview)
        self.scrollbarConsolaX.config(command=self.consola.xview)

        # Menu Archivo
        self.archivoMenu = Menu(self.barraMenu, tearoff=0)
        self.archivoMenu.add_command(label="New", command=self.NewFile)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Open file", command=self.OpenFile)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Save", command=self.Save)
        self.archivoMenu.add_command(label="Save As...", command=self.SaveAs)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Exit", command=self.vp.quit)
        # Menu Edit
        self.editMenu = Menu(self.barraMenu, tearoff=0)
        self.editMenu.add_command(label="Cut", \
                                  accelerator="Ctrl+X", \
                                  command=lambda: \
                                      self.entrada.event_generate('<<Cut>>'))
        self.editMenu.add_command(label="Copy", \
                                  accelerator="Ctrl+C", \
                                  command=lambda: \
                                      self.entrada.event_generate('<<Copy>>'))
        self.editMenu.add_command(label="Paste", \
                                  accelerator="Ctrl+V", \
                                  command=lambda: \
                                      self.entrada.event_generate('<<Paste>>'))
        # Menu Run
        self.runMenu = Menu(self.barraMenu, tearoff=0)
        self.runMenu.add_command(label="Run", command=self.Run, accelerator="Ctrl+R")
        self.runMenu.add_command(label="Generate", command=self.generate, accelerator="Ctrl+G")
        self.runMenu.add_command(label="Clear Execution", command=self.clear_files, accelerator="Ctrl+Z")
        # Menu Archivo
        self.reportsMenu = Menu(self.barraMenu, tearoff=0)
        self.reportsMenu.add_command(label="Symbol Table", command=self.getST)
        self.reportsMenu.add_command(label="Optimizations", command=self.getOptimization)
        self.reportsMenu.add_separator()
        self.reportsMenu.add_command(label="Errors", command=self.openErrors)
        self.reportsMenu.add_separator()
        self.reportsMenu.add_command(label="AST", command=self.openAST)
        self.reportsMenu.add_separator()
        self.reportsMenu.add_command(label="DDS", command=self.openBNF)
        self.reportsMenu.add_separator()
        self.reportsMenu.add_command(label="Asc Grammar", command=self.openBNFasc)
        self.reportsMenu.add_command(label="Desc Grammar", command=self.openBNFdesc)
        self.reportsMenu.add_command(label="Grammar Analysis", command=self.openBNFanalysis)
        # Menu Help
        self.helpMenu = Menu(self.barraMenu, tearoff=0)
        self.helpMenu.add_command(label="About", command=self.seeAbout)
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label="Technical Manual", command=self.openTechnical)
        self.helpMenu.add_command(label="User Manual", command=self.openUser)
        # Barra de Menú
        self.barraMenu.add_cascade(label="File", menu=self.archivoMenu)
        self.barraMenu.add_cascade(label="Edit", menu=self.editMenu)
        self.barraMenu.add_cascade(label="Run", menu=self.runMenu)
        self.barraMenu.add_cascade(label="Reports", menu=self.reportsMenu)
        self.barraMenu.add_cascade(label="Help", menu=self.helpMenu)

        self.vp.columnconfigure(0, weight=0)
        self.vp.columnconfigure(1, weight=1)

        window.bind('<Control-r>', self.run_listener)
        window.bind('<Control-g>', self.generate_listener)
        window.bind('<Control-z>', self.clear_listener)

        def callback(event):
            '''
            Permite actualizar la posicion actual del puntero en el text de entrada
            '''
            puntero = self.entrada.index(tk.INSERT)
            p = puntero.split(".")
            col = p[1]
            t = "Linea: " + p[0] + " Columna: " + str(int(col) + 1)
            tk.Label(self.vp, fg="white", bg="#154360", text=t, font=("Arial Bold", 10)).grid(row=2, column=1,
                                                                                              sticky=E + W)

        self.entrada.bind("<Button-1>", callback)
        self.entrada.bind("<Return>", callback)
        self.entrada.bind("<Any-KeyPress>", callback)
        self.entrada.bind("<Motion>", callback)
        self.entrada.bind("<FocusIn>", callback)

        self.entrada.focus()

    ###################################################### METODOS ######################################################
    def NewFile(self):
        '''
        Creación de un nuevo archivo en blanco
        '''
        self.rutaArchivo = ""
        self.texto = ""
        self.extension = ""
        self.entrada.delete(1.0, END)
        self.consola.delete(1.0, END)

    def OpenFile(self):
        '''
        Abrir un archivo local de texto plano y colocar su contenido en el area de entrada
        '''
        self.txtConsola = ""
        self.consola.delete(1.0, END)
        self.rutaArchivo = filedialog.askopenfilename(title="Open File")

        getNameAndExtensionFile(self)

        fileAbierto = open(self.rutaArchivo, encoding="utf-8")
        self.texto = fileAbierto.read()
        self.entrada.delete(1.0, END)
        self.entrada.insert(INSERT, self.texto)
        fileAbierto.close();

    def SaveAs(self):
        '''
        Permite guardar un nuevo archivo con el contenido del área de entrada en la ruta que el usuario elija
        '''
        ruta = filedialog.asksaveasfilename(title="Save As...")
        fguardar = open(ruta, "w+", encoding="utf-8")
        fguardar.write(self.entrada.get(1.0, END))
        fguardar.close()
        self.rutaArchivo = ruta
        getNameAndExtensionFile(self)

    def Save(self):
        '''
        Guarda el texto actual en el archivo abierto
        '''
        if self.rutaArchivo == "":
            self.guardarComo()
        else:
            archivoA = open(self.rutaArchivo, "w", encoding="utf-8")
            archivoA.write(self.entrada.get(1.0, END))
            archivoA.close()

    def run_listener(self, event):
        self.Run()

    def generate_listener(self, event):
        self.generate()

    def clear_listener(self, event):
        self.clear_files()

    def clear_files(self):
        if os.path.exists('data'):
            shutil.rmtree('data')
        if os.path.exists('opt_report.txt'):
            os.remove('opt_report.txt')

    def Run(self):
        '''
        Llamada a la clase main del proyecto, envía el texto que está en el área de entrada
        '''

        self.consola.delete(1.0, END)
        self.inputText = self.entrada.get("1.0", "end")
        grammarReview(self.inputText)
        gr = grammarReview.get_result(self)
        self.consola.insert(INSERT, gr)

    def generate(self):
        self.consola.delete(1.0, END)
        self.inputText = self.entrada.get("1.0", "end")
        generation = GrammarGenerate(self.inputText)
        result = generation.get_result()
        self.consola.insert(INSERT, result)

    def openErrors(self):
        ST0 = '\n\n\n============== ERROR REPORT ==============\n'
        ST1 = grammarReview.report_errors(self)
        ST2 = '\n'
        self.consola.insert(INSERT, ST0)
        self.consola.insert(INSERT, ST1)
        self.consola.insert(INSERT, ST2)

    def getST(self):
        ST0 = '\n\n\n+------------- SYMBOL TABLE REPORT --------------+\n'
        ST1 = grammarReview.getTablaTabulada(self)
        ST2 = '\n'
        self.consola.insert(INSERT, ST0)
        self.consola.insert(INSERT, ST1)
        self.consola.insert(INSERT, ST2)

    def getOptimization(self):
        ST0 = '\n\n\n+------------- OPTIMIZATION REPORT --------------+\n'
        # ST1 = grammarReview.getTablaTabulada(self)
        file = open('opt_report.txt', 'r')
        ST1 = file.read()
        ST2 = '\n'
        self.consola.insert(INSERT, ST0)
        self.consola.insert(INSERT, ST1)
        self.consola.insert(INSERT, ST2)

    def seeAbout(self):
        mb.showinfo("About",
                    "TYTUS\n Universidad de San Carlos de Guatemala \nOLC 2\nCuso de vacaciones \nDiciembre \nAño 2020\nCoautores: \n\t201020126 - Sandy Fabiola Merida Hernandez  \n\t201020252 - Sergio Ariel Ramirez Castro \n\t201020260 - Victor Augusto Lopez Hernandez \n\t201020697 - Esteban Palacios Kestler ")

    def openAST(self):
        a = os.popen('grap.png')

    def openBNF(self):
        a = os.popen('reportGrammar.md')

    def openBNFasc(self):
        a = os.popen('docs\grammars\gramatica-ascendente.md')

    def openBNFdesc(self):
        a = os.popen('docs\grammars\gramatica-descendente.md')

    def openBNFanalysis(self):
        a = os.popen('docs\grammars\grammar-analysis.md')

    def openTechnical(self):
        a = os.popen('docs\\manuals\\technical-manual.md')

    def openUser(self):
        a = os.popen('docs\\manuals\\user-manual.md')


def getNameAndExtensionFile(self):
    rutaSpliteada = self.rutaArchivo.split("/")
    ultimaPos = len(rutaSpliteada) - 1
    self.nombreArchivo = rutaSpliteada[ultimaPos]

    ext = self.nombreArchivo.split(".")
    self.extension = ext[1]


def CleanConsole(self):
    self.consola.delete(1.0, END)
    self.consola.insert(INSERT, self.txtConsola)


if __name__ == '__main__':
    window = Tk()
    window.resizable(1, 0)
    app = query_tool(window)
    window.mainloop()
