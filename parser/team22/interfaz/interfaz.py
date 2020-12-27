from tkinter import ttk,scrolledtext,Frame,Scrollbar,Canvas,Menu,Tk,VERTICAL,HORIZONTAL,CENTER
from tkinter.font import Font
from funciones import Funciones_

class Interfaz_Ml:

    def __init__(self,ventana):
        #########################__Contenedor Principal__#######################
        self.raiz = ventana
        self.creaVentana()
    
    def creaVentana(self):
        funcion = Funciones_()
        contenedor = self.raiz
        contenedor.resizable(False,False)
        contenedor.title("TytusDB")

        #########################__ScrollBar de ventana__#######################
        contenedorPrincipal = Frame(contenedor, bg = "light sky blue")
        estilos = Canvas(contenedorPrincipal, bg = "light sky blue")
        scrolBar = Scrollbar(contenedorPrincipal, orient = VERTICAL, command = estilos.yview)
        scrol = Frame(estilos, bg = "light sky blue")

        #########################__Configuracion de scrollBar y titulo en ventana__#######################
        scrol.bind("<Configure>",lambda e: estilos.configure(scrollregion = estilos.bbox("all")))
        estilos.create_window((0, 0), window = scrol, anchor="nw")
        estilos.configure(yscrollcommand = scrolBar.set, width = 1500, height = 700)

        ttk.Label(scrol, text = "TytusDB", font = ("Arial", 17), background='light sky blue', foreground = "gray").grid(column = 0, row = 0)
        ttk.Label(scrol, text = "[12.2020]", font = ("Arial", 17), background='light sky blue', foreground = "gray").grid(column = 0, row = 1)
        ttk.Label(scrol, text = "COMPILADORES 2", font = ("Arial", 17), background='light sky blue', foreground = "gray").grid(column = 1, row = 0)
        ttk.Label(scrol, text = "USAC", font = ("Arial", 17), background='light sky blue', foreground = "gray").grid(column = 1, row = 1)

        #########################__Area de trabajo y consola__#######################

        editor = scrolledtext.ScrolledText(scrol, undo = True, width = 80, height = 14, font = ("Arial", 12), background = "mint cream",  foreground = "black")
        editor.grid(column = 0, row = 2, pady = 25, padx = 25)

        consola = scrolledtext.ScrolledText(scrol, undo = True, width = 80, height = 14, font = ("Arial", 12), background = "black",  foreground = "green3")
        consola.grid(column = 0, row = 3, pady = 25, padx = 25)

        #########################__Salida y area de reportes__#######################
        tabs = ttk.Notebook(scrol, width = 600)
        salida = Frame(tabs, width = 80)
        tabla_simbolos = Frame(tabs, width = 80)
        lexico_errores = Frame(tabs, width = 80)
        sintactico_errores = Frame(tabs, width = 80)
        semantico_errores = Frame(tabs, width = 80)

        ttk.Label(salida, text = "\n Salida de Datos \n", font = ("Arial", 17)).grid(column = 2, row = 2)
        ttk.Label(tabla_simbolos, text = "\n Tabla de Simbolos \n", font = ("Arial", 17)).grid(column = 2, row = 2)
        ttk.Label(lexico_errores, text = "\n Errores Lexicos \n", font = ("Arial", 17)).grid(column = 2, row = 2)
        ttk.Label(sintactico_errores, text = "\n Errores Sintacticos \n", font = ("Arial", 17)).grid(column = 2, row = 2)
        ttk.Label(semantico_errores, text = "\n Errores Semanticos \n", font = ("Arial", 17)).grid(column = 2, row = 2)

        #----------------------------Tabla Repore Lexico-------------------------------#
        tabla_lexico = ttk.Treeview(lexico_errores, columns = ("#1","#2","#3"), height = 23)
        tabla_lexico.grid(row = 3, column = 2)
        tabla_lexico.heading("#0", text = "NO.")
        tabla_lexico.heading("#1", text = "LINEA")
        tabla_lexico.heading("#2", text = "ERROR")
        tabla_lexico.heading("#3", text = "DESCRIPCION")
        tabla_lexico.column("#0", width = 60, minwidth = 60, stretch = "no", anchor = "center")
        tabla_lexico.column("#1", width = 90, minwidth = 90, stretch = "no", anchor = "center")
        tabla_lexico.column("#2", width = 120, minwidth = 120, stretch = "no", anchor = "center")
        tabla_lexico.column("#3", width = 381, minwidth = 381, stretch = "no", anchor = "center")
        
        table_scrol = Scrollbar(lexico_errores, orient = VERTICAL, command  = tabla_lexico.yview)
        table_scrol.grid(row = 3, column = 3, sticky = "ns")
        table_scrolx = Scrollbar(lexico_errores, orient = HORIZONTAL, command  = tabla_lexico.xview)
        table_scrolx.grid(row = 4, column = 2, columnspan = 2, sticky = "we")
        tabla_lexico.configure(yscrollcommand = table_scrol.set, xscrollcommand = table_scrolx.set)

        #----------------------------Tabla Repore Sintactico-------------------------------#
        tabla_sintactico = ttk.Treeview(sintactico_errores, columns = ("#1","#2","#3"), height = 23)
        tabla_sintactico.grid(row = 3, column = 2)
        tabla_sintactico.heading("#0", text = "NO.")
        tabla_sintactico.heading("#1", text = "LINEA")
        tabla_sintactico.heading("#2", text = "ERROR")
        tabla_sintactico.heading("#3", text = "DESCRIPCION")
        tabla_sintactico.column("#0", width = 60, minwidth = 60, stretch = "no", anchor = "center")
        tabla_sintactico.column("#1", width = 90, minwidth = 90, stretch = "no", anchor = "center")
        tabla_sintactico.column("#2", width = 120, minwidth = 120, stretch = "no", anchor = "center")
        tabla_sintactico.column("#3", width = 381, minwidth = 381, stretch = "no", anchor = "center")

        table_scrol_sintactico = Scrollbar(sintactico_errores, orient = VERTICAL, command  = tabla_sintactico.yview)
        table_scrol_sintactico.grid(row = 3, column = 3, sticky = "ns")
        table_scrolx_sintactico = Scrollbar(sintactico_errores, orient = HORIZONTAL, command  = tabla_sintactico.xview)
        table_scrolx_sintactico.grid(row = 4, column = 2, columnspan = 2, sticky = "we")
        tabla_sintactico.configure(yscrollcommand = table_scrol_sintactico.set, xscrollcommand = table_scrolx_sintactico.set)

        #----------------------------Tabla Repore Semantico-------------------------------#
        ttk.Style(semantico_errores).configure('tabla_semantico.Treeview', rowheight = 50)
        tabla_semantico = ttk.Treeview(semantico_errores, style = "tabla_semantico.Treeview", columns = ("#1","#2","#3"), height = 9)
        tabla_semantico.grid(row = 3, column = 2)
        tabla_semantico.heading("#0", text = "NO.")
        tabla_semantico.heading("#1", text = "LINEA")
        tabla_semantico.heading("#2", text = "ERROR")
        tabla_semantico.heading("#3", text = "DESCRIPCION")
        tabla_semantico.column("#0", width = 60, minwidth = 60, stretch = "no", anchor = "center")
        tabla_semantico.column("#1", width = 90, minwidth = 90, stretch = "no", anchor = "center")
        tabla_semantico.column("#2", width = 120, minwidth = 120, stretch = "no", anchor = "center")
        tabla_semantico.column("#3", width = 381, minwidth = 381, stretch = "no", anchor = "center")

        table_scrol_semantico = Scrollbar(semantico_errores, orient = VERTICAL, command  = tabla_semantico.yview)
        table_scrol_semantico.grid(row = 3, column = 3, sticky = "ns")
        table_scrolx_semantico = Scrollbar(semantico_errores, orient = HORIZONTAL, command  = tabla_semantico.xview)
        table_scrolx_semantico.grid(row = 4, column = 2, columnspan = 2, sticky = "we")
        tabla_semantico.configure(yscrollcommand = table_scrol_semantico.set, xscrollcommand = table_scrolx_semantico.set)

        #----------------------------Tabla Tabla de Simbolos-------------------------------#
        tabla_tb_simbolos = ttk.Treeview(tabla_simbolos, columns = ("#1","#2","#3"), height = 23)
        tabla_tb_simbolos.grid(row = 3, column = 2)
        tabla_tb_simbolos.heading("#0", text = "LINEA")
        tabla_tb_simbolos.heading("#1", text = "ID")
        tabla_tb_simbolos.heading("#2", text = "TIPO")
        tabla_tb_simbolos.heading("#3", text = "VALOR")
        tabla_tb_simbolos.column("#0", width = 158, minwidth = 158, stretch = "no", anchor = "center")
        tabla_tb_simbolos.column("#1", width = 163, minwidth = 163, stretch = "no", anchor = "center")
        tabla_tb_simbolos.column("#2", width = 163, minwidth = 163, stretch = "no", anchor = "center")
        tabla_tb_simbolos.column("#3", width = 167, minwidth = 167, stretch = "no", anchor = "center")

        table_scrol_simbolos = Scrollbar(tabla_simbolos, orient = VERTICAL, command  = tabla_tb_simbolos.yview)
        table_scrol_simbolos.grid(row = 3, column = 3, sticky = "ns")
        table_scrolx_simbolos = Scrollbar(tabla_simbolos, orient = HORIZONTAL, command  = tabla_tb_simbolos.xview)
        table_scrolx_simbolos.grid(row = 4, column = 2, columnspan = 2, sticky = "we")
        tabla_tb_simbolos.configure(yscrollcommand = table_scrol_simbolos.set, xscrollcommand = table_scrolx_simbolos.set)

        tabs.add(salida, text = 'SALIDA')
        tabs.add(tabla_simbolos, text = 'TABLA DE SIMBOLOS')
        tabs.add(lexico_errores, text = 'ERRORES LEXICOS')
        tabs.add(sintactico_errores, text = 'ERRORES SINTACTICOS')
        tabs.add(semantico_errores, text = "ERRORES SEMANTICOS")

        tabs.grid(column = 1, row = 2, rowspan = 5, pady = 25, padx = 25, sticky = "ns")

        #########################__Barra de herramientas__#######################
        barraHerramientas = Menu(contenedor)
        contenedor.config(menu = barraHerramientas, width = 1500, height = 700)

        opcionArchivo = Menu(barraHerramientas, tearoff = 0)
        opcionArchivo.add_command(label = "Nuevo", command = lambda : funcion.nuevo(editor))
        opcionArchivo.add_command(label = "Abrir", command = lambda : funcion.abrir(editor))
        opcionArchivo.add_command(label = "Guardar", command = lambda : funcion.guardarArchivo(editor))
        opcionArchivo.add_command(label = "Guardar Como", command = lambda : funcion.guardarComo(editor))
        opcionArchivo.add_command(label = "Analizar Reporetes", command = lambda : funcion.analiza2(editor))

        objetos = [editor,consola,tabla_lexico,tabla_sintactico,tabla_semantico,tabla_tb_simbolos,salida]

        opcionReporte = Menu(barraHerramientas, tearoff = 0)
        opcionReporte.add_command(label = "Reporte AST", command = lambda : funcion.reporte("as"))
        opcionReporte.add_command(label = "Reporte Gramatical", command = lambda : funcion.reporte("gr"))

        barraHerramientas.add_cascade(label = "Archivo", menu = opcionArchivo)
        barraHerramientas.add_command(label = "Ejecutar Analisis", command = lambda : funcion.analizar(objetos))
        barraHerramientas.add_cascade(label = "Ver", menu = opcionReporte)
        barraHerramientas.add_command(label = "Informacion", command = lambda : funcion.info())
        barraHerramientas.add_command(label = "Salir", command = lambda : funcion.salir(contenedor))

        contenedorPrincipal.grid(sticky = "news")
        estilos.grid(row = 0, column = 1)
        scrolBar.grid(row = 0, column = 2, sticky = "ns")
        editor.focus()
    
    def aumentaHeight(self,font,style):
        font['size'] += 1
        style.configure('Lexico.Treeview', rowheight = font.metrics()['linespace'] * 3)

    def disminuyeHeight(self,font,style):
        font['size'] -= 1
        style.configure('Lexico.Treeview', rowheight=font.metrics()['linespace'] * 3)    

if __name__ == '__main__':
    ventana = Tk()
    app = Interfaz_Ml(ventana)
    ventana.mainloop()
