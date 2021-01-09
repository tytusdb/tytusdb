import arbol.AST as a
import gramatica2 as g
import os
from tkinter import *
from reportes import *
from subprocess import check_call
from Entorno.Entorno import Entorno
from storageManager import jsonMode
from Expresion.variablesestaticas import variables
from graphviz import Digraph

#variables.ventana = Tk()
variables.ventana.geometry("1245x600")
variables.ventana.resizable(False,False)
variables.ventana.config(background="gray25")

global tablaSym
tablaSym = Digraph("TablaSym",node_attr={'shape':'record'})

contenidoSym:str = ""

global ErroresS
ErroresS = Digraph("reporte",node_attr={'shape':'record'})
ErroresS.attr(style='rounded',color='#4b8dc5')
contenidoE:str = ""

def send_data():
    print("Analizando Entrada:")
    print("==============================================")
    # reporteerrores = []
    contenido = Tentrada.get(1.0, 'end')
    variables.consola.delete(1.0, "end")
    variables.consola.configure(state='normal')

    # print(contenido)
    Principal = Entorno()
    jsonMode.dropAll()

    # Principal.database = "DB1"
    instrucciones = g.parse(contenido)
    variables.consola.insert(INSERT, "Salida de consultas\n")
    for instr in instrucciones:
        if instr != None:
            instr.ejecutar(Principal)
                
    variables.consola.configure(state='disabled')
    #variables.consola.configure()

    setContenido(Principal.mostrarSimbolos())

def reporte_lex_sin():
    if len(reporteerrores) != 0:
        global contenidoE 
        contenidoE += "<<TABLE border= \"2\"  cellspacing= \"-1\" color=\"#4b8dc5\">"
        contenidoE += "<TR><TD bgcolor=\"#1ED0EC\">Tipo</TD><TD bgcolor=\"#1ED0EC\">Linea</TD>"
        contenidoE += "<TD bgcolor=\"#1ED0EC\">Columna</TD><TD bgcolor=\"#1ED0EC\">Descripcion</TD></TR>"

        for error in reporteerrores:
            contenidoE += '<TR> <TD>' + error.tipo + '</TD><TD>' + error.linea + '</TD> <TD>' + error.columna + '</TD><TD>' + error.descripcion + '</TD></TR>'

        contenidoE += '</TABLE>>'



def mostrarimagenre():
    reporte_lex_sin()
    ErroresS.node("ErroresR",label=contenidoE)
    ErroresS.render('erroresr', view=True)  # doctest: +SKIP
    'erroresr.pdf'

def setContenido(cont:str):
    global contenidoSym
    contenidoSym = cont
    

def arbol_ast():
    contenido = Tentrada.get(1.0, 'end')
    a.generarArbol(contenido)

def verSimbolos():
    tablaSym.node("TS",contenidoSym)
    tablaSym.render('ts', view=True)  # doctest: +SKIP
    'ts.pdf'

def gramatica():
    contenido = Tentrada.get(1.0,'end')
    g.generaReporteBNF(contenido)


entrada = StringVar()
Tentrada = Text(variables.ventana)
Tentrada.config(width=150, height=20)
Tentrada.config(background="gray18")
Tentrada.config(foreground="white")
Tentrada.config(insertbackground="white")
Tentrada.place(x=10, y=10)

variables.consola = Text(variables.ventana)
variables.consola.config(width=150, height=15)
variables.consola.config(background="gray10")
variables.consola.config(foreground="white")
variables.consola.config(insertbackground="white")
variables.consola.place(x=10, y=350)
variables.consola.configure(state='disabled')
menu_bar = Menu(variables.ventana)

variables.ventana.config(menu=menu_bar)
# Menu Ejecutar
ej_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Ejecutar", menu=ej_menu)
ej_menu.add_command(label="Analizar Entrada", command=send_data)

# Menu Reportes

reps_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Reportes", menu=reps_menu)
reps_menu.add_command(label="Errores Lexicos y Sintacticos", command=mostrarimagenre)
reps_menu.add_command(label="Tabla de Simbolos", command=verSimbolos)
reps_menu.add_command(label="AST", command=arbol_ast)
reps_menu.add_command(label="Gramatica", command=gramatica)

variables.ventana.mainloop()