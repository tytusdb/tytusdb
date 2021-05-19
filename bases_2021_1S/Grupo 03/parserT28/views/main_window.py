from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.font import Font
from prettytable import PrettyTable
from parserT28.Optimizador.reglas import regla1, regla2, regla3, regla4y5, regla6, regla7
from parserT28.Optimizador.clases3d import Goto, LabelIF, ifStatement
from parserT28.Optimizador.syntactic import parse_optimizacion
from parserT28.Optimizador.optimization import ReportOfOptimization
from parserT28.controllers.optimization_controller import OptimizationController

import os
import json

from parserT28.utils.analyzers.syntactic import *
from parserT28.controllers.ast_construction import *
from parserT28.utils.reports.generate_ast import GraficarAST
from parserT28.controllers.error_controller import ErrorController
from parserT28.utils.reports.report_error import ReportError
from parserT28.utils.reports.symbol_report import SymbolTableReport
from parserT28.utils.reports.tchecker_report import TypeCheckerReport
from parserT28.controllers.three_address_code import ThreeAddressCode
from parserT28.views.data_window import DataWindow
from parserT28.models.Other.ambito import Ambito
report_optimization = None
report_error = None
report_ast = None


class MainWindow(object):
    archivo = ''

    def __init__(self, window):
        self.ventana = window
        # Defino un titulo para el GUI
        self.ventana.title('Query Tool')
        # Defino un fondo para usar, pueden cambiarlo por otro color mas bonito
        self.ventana.configure(background='#3c3f41')

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        # Creo un frame para que contenga la intefaz, es como en java se hace con swing
        frame = LabelFrame(self.ventana)
        # Posiciono el frame
        frame.grid(row=0, column=0, columnspan=10, pady=10)
        # Defino un fondo para usar, pueden cambiarlo por otro color mas bonito
        frame.configure(background='#3c3f41', borderwidth=0)
        #############################################_MENU_#############################################
        # Creo un menu, es decir una lista desplegable
        barraMenu = Menu(self.ventana)
        self.ventana.config(menu=barraMenu)
        archivoMenu = Menu(barraMenu, tearoff=0)
        #############################################MENU Abrir#############################################
        archivoOpen = Menu(archivoMenu, tearoff=0)
        archivoOpen.add_command(label='Abrir Archivo',
                                command=self.open_file_editor)
        #############################################MENU Archivo#############################################
        archivoMenu.add_command(label='Nuevo', command=self.nuevo)
        archivoMenu.add_separator()
        archivoMenu.add_cascade(label='Abrir', menu=archivoOpen)
        archivoMenu.add_separator()
        archivoMenu.add_command(label='Guardar', command=self.guardar)
        archivoMenu.add_command(label='Guardar como...',
                                command=self.guardar_como)
        archivoMenu.add_separator()
        archivoMenu.add_command(label='Ejecutar SQL',
                                command=self.ejecutar_sql)
        archivoMenu.add_separator()
        archivoMenu.add_command(label='Generar TAC',
                                command=self.generar_tac)
        archivoMenu.add_separator()
        archivoMenu.add_command(label='Generar Optimizacion',
                                command=self.generar_optimization)
        archivoMenu.add_separator()
        archivoMenu.add_command(label='Ejecutar TAC',
                                command=ThreeAddressCode().executeFile)
        archivoMenu.add_separator()
        archivoMenu.add_command(label='Salir', command=self.terminar)
        #############################################MENU WINDOWS##############################################
        windows_menu = Menu(barraMenu, tearoff=0)
        windows_menu.add_command(label='AST',
                                 command=self.report_ast_windows)
        windows_menu.add_separator()
        windows_menu.add_command(label='Tabla de errores',
                                 command=self.report_errors_windows)
        windows_menu.add_separator()
        windows_menu.add_command(label='Tabla de simbolos',
                                 command=self.report_symbols_windows)
        windows_menu.add_separator()
        windows_menu.add_command(label='Reporte de Optimizacion',
                                 command=self.report_optimization_windows)
        windows_menu.add_separator()
        windows_menu.add_command(label='Type Checker',
                                 command=self.report_typeChecker_windows)
        windows_menu.add_separator()
        windows_menu.add_command(label='Reporte Gramatical',
                                 command=self.report_bnf_windows)
        #############################################MENU LINUX################################################
        ubuntu_menu = Menu(barraMenu, tearoff=0)
        ubuntu_menu.add_command(label='AST',
                                command=self.report_ast_ubuntu)
        ubuntu_menu.add_separator()
        ubuntu_menu.add_command(label='Tabla de errores',
                                command=self.report_errors_ubuntu)
        ubuntu_menu.add_separator()
        ubuntu_menu.add_command(label='Tabla de simbolos',
                                command=self.report_symbols_ubuntu)
        ubuntu_menu.add_separator()
        ubuntu_menu.add_command(label='Reporte de Optimizacion',
                                command=self.report_optimization_ubuntu)
        ubuntu_menu.add_separator()
        ubuntu_menu.add_command(label='Type Checker',
                                command=self.report_typeChecker_ubuntu)
        ubuntu_menu.add_separator()
        ubuntu_menu.add_command(label='Reporte Gramatical',
                                command=self.report_bnf_ubuntu)
        #############################################MENU REPORTES#############################################
        archivoReportes = Menu(barraMenu, tearoff=0)
        archivoReportes.add_cascade(label='Windows', menu=windows_menu)
        archivoReportes.add_separator()
        archivoReportes.add_cascade(label='Linux', menu=ubuntu_menu)
        #############################################MENU PRINCIPAL#############################################
        barraMenu.add_cascade(label='Archivo',
                              menu=archivoMenu)  # anade submenu
        barraMenu.add_cascade(label='Reportes', menu=archivoReportes)
        barraMenu.configure(background='SpringGreen')
        ############################################_ENTRADA_############################################
        Label(frame, text='Archivo de Entrada', borderwidth=0,
              font='Arial 15 bold', width=52, bg='#3c3f41', foreground='#fff').grid(row=3, column=0)

        hor_scroll = Scrollbar(frame, orient='horizontal')
        ver_scroll = Scrollbar(frame, orient='vertical')
        # Crea un scroll por si el texto es muy largo
        self.entrada = Text(frame, borderwidth=0, height=35,
                            width=70, bg='#2e2e31', foreground='#fff', undo=True, wrap='none',
                            xscrollcommand=hor_scroll.set, yscrollcommand=ver_scroll.set)
        self.entrada.grid(row=4, column=0, padx=30)

        ver_scroll.config(command=self.entrada.yview)
        ver_scroll.grid(column=0, row=4, sticky='NE', ipady=255, padx=12)
        hor_scroll.config(command=self.entrada.xview)
        hor_scroll.grid(column=0, row=5, sticky='NS', ipadx=255)

        # Para este editor aun hay que ver si lo usamos como consola para errores, si no lo quitamos
        dataWindow = DataWindow()
        dataWindow.console = frame
        self.console = dataWindow.console
        self.console.grid(row=4, column=1, padx=30)
        # self.salida.insert(INSERT, 'Some text')
        # self.salida.insert(END, my_table)

        # END
        # Metodo para abrir archivo y colocarlo en el editor

    def open_file_editor(self):
        filename = askopenfilename(title='Abrir Archivo')
        archivo = open(filename, 'r')
        texto = archivo.read()
        self.entrada.insert(INSERT, texto)
        archivo.close()
        messagebox.showinfo('CARGA', 'SE CARGO CORRECTAMENTE EL ARCHIVO SQL')
        return
    # Crea una nueva pestana

    def nuevo(self):
        self.entrada.delete(1.0, END)
        DataWindow().clearConsole()
        self.archivo = ''

    # Guarda el archivo
    def guardar(self):
        if self.archivo == '':
            self.guardar_como()
        else:
            guardar_info = open(self.archivo, 'w')
            guardar_info.write(self.entrada.get('1.0', END))
            guardar_info.close()

    # Opcion para guardar como
    def guardar_como(self):
        guardar_info = asksaveasfilename(title='Guardar Archivo')
        write_file = open(guardar_info, 'w+')
        write_file.write(self.entrada.get('1.0', END))
        write_file.close()
        self.archivo = guardar_info

    # Opcion para ejecutar el texto de entrada del editor
    def ejecutar_sql(self):
        global report_error
        global report_ast

        DataWindow().clearConsole()
        SymbolTable().destroy()
        ThreeAddressCode().destroy()

        texto = self.entrada.get('1.0', END)
        result = parse(texto)
        # jsonStr = json.dumps(result, default=lambda o: o.__dict__) #Convierte el AST a formato JSON para poder saber como se esta formando
        # print(result)  # Imprime el AST

        report_error = ReportError()
        if len(ErrorController().getList()) > 0:
            messagebox.showerror('ERRORES', 'Se encontraron errores')
        else:
            result2 = parse2(texto)
            report_ast = result2

            # ---------- TEST ---------
            for inst in result:
                # esto es por los select anidados (subquerys), no encontre otra menera
                # de retornar la tabla dibujada, lo hacia en mi clase
                # pero si lo dejaba ahi me tronaban las subquery,
                # prueben que no les de problema
                if isinstance(inst, Select):
                    result = inst.process(0)
                    if isinstance(result, DataFrame):
                        DataWindow().consoleText(format_df(result))
                    elif isinstance(result, list):
                        DataWindow().consoleText(format_table_list(result))
                else:
                    inst.process(0)
            # ---------- TEST ---------

    def generar_tac(self):
        global report_error
        global report_ast

        DataWindow().clearConsole()
        SymbolTable().destroy()
        ThreeAddressCode().destroy()

        texto = self.entrada.get('1.0', END)
        result = parse(texto)
        print(result)  # Imprime el AST
        report_error = ReportError()

        if len(ErrorController().getList()) > 0:
            messagebox.showerror('ERRORES', 'Se encontraron errores')
        else:

            ambito = Ambito(None)
            for inst in result:
                inst.compile(ambito)

            DataWindow().consoleText(ThreeAddressCode().getCode())
            ThreeAddressCode().writeFile()

            result2 = parse2(texto)  # AST GRAFICO
            report_ast = result2

    def generar_optimization(self):
        global report_error
        global report_ast
        global report_optimization

        DataWindow().clearConsole()
        OptimizationController().destroy()

        texto = self.entrada.get('1.0', END)
        list_instrucciones = parse_optimizacion(texto)
        # print(result)  # Imprime el AST
        report_error = ReportError()
        report_optimization = ReportOfOptimization()
        if len(ErrorController().getList()) > 0:
            messagebox.showerror('ERRORES', 'Se encontraron errores')
        else:
            for index, inst in enumerate(list_instrucciones):
                if inst != None:
                    result = inst.process(0)
                    regla1(result, list_instrucciones, index)
                    regla2(result, list_instrucciones, index)
                    regla3(result, list_instrucciones, index)
                    regla4y5(result, list_instrucciones, index)
                    regla6(result, list_instrucciones, index)
                    regla7(result, list_instrucciones, index)
            DataWindow().consoleText('CD3 RETURNED: Optimization Finished')

    # Para mostrar el editor

    def report_ast_ubuntu(self):
        global report_ast
        graficadora = GraficarAST()
        report = open('./team28/ast.dot', 'w')
        report.write(graficadora.generate_string(report_ast))
        report.close()
        os.system('dot -Tpdf  ast.dot -o ast.pdf')
        # Si estan en ubuntu dejan esta linea si no la comentan y descomentan la otra para windows
        os.system('xdg-open ast.pdf')
        # os.open('ast.png')
        # os.startfile('ast.png')

    def report_optimization_windows(self):
        global report_optimization
        report = open('optiimization.dot', 'w')
        report.write(report_optimization.get_report())
        report.close()
        os.system('dot -Tpdf optiimization.dot -o optiimization.pdf')
        os.startfile('optiimization.pdf')

    def report_optimization_ubuntu(self):
        global report_optimization
        report = open('optiimization.dot', 'w')
        report.write(report_optimization.get_report())
        report.close()
        os.system('dot -Tpdf optiimization.dot -o optiimization.pdf')
        os.system('xdg-open  optiimization.pdf')

    def report_errors_ubuntu(self):
        global report_error
        report = open('./team28/errors.dot', 'w')
        report.write(report_error.get_report())
        report.close()
        os.system('dot -Tpdf errors.dot -o error.pdf')
        os.system('xdg-open  error.pdf')

    def report_symbols_ubuntu(self):
        report = open('symbolTable.dot', 'w')
        report.write(SymbolTableReport().generateReport())
        report.close()
        os.system('dot -Tpdf symbolTable.pdf -o symbolTable.pdf')
        os.system('xdg-open symbolTable.pdf')

    def report_typeChecker_ubuntu(self):
        report = open('typeChecker.dot', 'w')
        report.write(TypeCheckerReport().generateReport())
        report.close()
        os.system('dot -Tpdf typeChecker.dot -o typeChecker.pdf')
        os.system('xdg-open typeChecker.pdf')

    def report_bnf_ubuntu(self):
        global report_ast
        report = open('bfn.txt', 'w')
        report.write(report_ast.production)
        report.close()
        os.system('xdg-open bfn.txt')

    def report_ast_windows(self):
        global report_ast
        graficadora = GraficarAST()
        report = open('ast.dot', 'w')
        report.write(graficadora.generate_string(report_ast))
        report.close()
        os.system('dot -Tpdf ast.dot -o ast.pdf')
        os.startfile('ast.pdf')

    def report_errors_windows(self):
        global report_error
        report = open('errors.dot', 'w')
        report.write(report_error.get_report())
        report.close()
        os.system('dot -Tpdf errors.dot -o  error.pdf')
        os.startfile('error.pdf')

    def report_symbols_windows(self):
        report = open('symbolTable.dot', 'w')
        report.write(SymbolTableReport().generateReport())
        report.close()
        os.system('dot -Tpdf symbolTable.dot -o symbolTable.pdf')
        os.startfile('symbolTable.pdf')

    def report_typeChecker_windows(self):
        report = open('typeChecker.dot', 'w')
        report.write(TypeCheckerReport().generateReport())
        report.close()
        os.system('dot -Tpdf typeChecker.dot -o typeChecker.pdf')
        os.startfile('typeChecker.pdf')

    def report_bnf_windows(self):
        global report_ast
        report = open('bfn.txt', 'w')
        report.write(report_ast.production)
        report.close()
        os.startfile('bfn.txt')

    # Para salir de la aplicacion
    def terminar(self):
        salir = messagebox.askokcancel('Salir', 'Está seguro que desea salir?')
        if salir:
            self.ventana.destroy()
        return
