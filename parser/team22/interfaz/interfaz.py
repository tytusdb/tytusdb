from tkinter import ttk,scrolledtext,Frame,Scrollbar,Canvas,Menu,Tk,VERTICAL
from funciones import Funciones_

class Interfaz_Ml:

    def __init__(self,ventana):
        #########################__Contenedor Principal__#######################
        self.raiz = ventana
        self.creaVentana()
    
    def creaVentana(self):
        funcion = Funciones_()
        contenedor = self.raiz
        contenedor.title("TytusDB")

        #########################__ScrollBar de ventana__#######################
        contenedorPrincipal = Frame(contenedor, bg = "light sky blue")
        estilos = Canvas(contenedorPrincipal, bg = "light sky blue")
        scrolBar = Scrollbar(contenedorPrincipal, orient = VERTICAL, command = estilos.yview)
        scrol = Frame(estilos, bg = "light sky blue")

        #########################__Configuracion de scrollBar y titulo en ventana__#######################
        scrol.bind("<Configure>",lambda e: estilos.configure(scrollregion = estilos.bbox("all")))
        estilos.create_window((0, 0), window = scrol, anchor="nw")
        estilos.configure(yscrollcommand = scrolBar.set, width = 1572, height = 635)

        ttk.Label(scrol, text = "TytusDB", font = ("Arial", 17), background='light sky blue', foreground = "gray").grid(column = 0, row = 0)
        ttk.Label(scrol, text = "[12.2020]", font = ("Arial", 17), background='light sky blue', foreground = "gray").grid(column = 0, row = 1)
        ttk.Label(scrol, text = "COMPILADORES 2", font = ("Arial", 17), background='light sky blue', foreground = "gray").grid(column = 1, row = 0)
        ttk.Label(scrol, text = "USAC", font = ("Arial", 17), background='light sky blue', foreground = "gray").grid(column = 1, row = 1)

        editor = scrolledtext.ScrolledText(scrol, undo = True, width = 80, height = 28, font = ("Arial", 12), background = "mint cream",  foreground = "black")
        editor.grid(column = 0, row = 2, pady = 25, padx = 25)

        consola = scrolledtext.ScrolledText(scrol, undo = True, width = 80, height = 28, font = ("Arial", 12), background = "black",  foreground = "white")
        consola.grid(column = 1, row = 2, pady = 25, padx = 25)

        #########################__Barra de herramientas__#######################
        barraHerramientas = Menu(contenedor)
        contenedor.config(menu = barraHerramientas, width = 1572, height = 635)

        opcionReporte = Menu(barraHerramientas, tearoff = 0)
        opcionReporte.add_command(label = "Reporte Errores Lexicos", command = lambda : funcion.reporte("ls"))
        opcionReporte.add_command(label = "Reporte Errores Sintacticos", command = lambda : funcion.reporte("st"))
        opcionReporte.add_command(label = "Reporte Errores Semanticos", command = lambda : funcion.reporte("sm"))
        opcionReporte.add_command(label = "Reporte Tabla de Simbolos", command = lambda : funcion.reporte("tb"))
        opcionReporte.add_command(label = "Reporte AST", command = lambda : funcion.reporte("as"))
        opcionReporte.add_command(label = "Reporte Gramatical", command = lambda : funcion.reporte("gr"))

        barraHerramientas.add_command(label = "Ejecutar Analisis", command = lambda : funcion.analizar(editor,consola))
        barraHerramientas.add_cascade(label = "Ver", menu = opcionReporte)
        barraHerramientas.add_command(label = "Informacion", command = lambda : funcion.info())
        barraHerramientas.add_command(label = "Salir", command = lambda : funcion.salir(contenedor))

        contenedorPrincipal.grid(sticky = "news")
        estilos.grid(row = 0, column = 1)
        scrolBar.grid(row = 0, column = 2, sticky = "ns")
        editor.focus()

if __name__ == '__main__':
    ventana = Tk()
    app = Interfaz_Ml(ventana)
    ventana.mainloop()
