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

# variables.ventana = Tk()
variables.ventana.geometry("1200x650")
variables.ventana.resizable(False, False)
variables.ventana.config(bg="gray25")  # color de fondo, background
variables.ventana.config(cursor="pirate")  # tipo de cursor (arrow defecto)
variables.ventana.config(relief="sunken")  # relieve del root
variables.ventana.config(bd=12)  # tamaño del borde en píxeles

global tablaSym
tablaSym = Digraph("TablaSym", node_attr={'shape': 'record'})

contenidoSym: str = ""

global ErroresS
ErroresS = Digraph("reporte", node_attr={'shape': 'record'})
ErroresS.attr(style='rounded', color='#4b8dc5')
contenidoE: str = ""


def send_data():
    print("Analizando Entrada:")
    print("==============================================")
    # reporteerrores = []
    contenido = Tentrada.get(1.0, 'end')
    variables.consola.delete("1.0", "end")
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
            string=str(instr)
            intrprueba=string

    variables.consola.configure(state='disabled')
    # variables.consola.configure()

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
    ErroresS.node("ErroresR", label=contenidoE)
    ErroresS.render('erroresr', view=True)  # doctest: +SKIP
    'erroresr.pdf'


def setContenido(cont: str):
    global contenidoSym
    contenidoSym += cont


def arbol_ast():
    contenido = Tentrada.get(1.0, 'end')
    a.generarArbol(contenido)


def verSimbolos():
    tablaSym.node("TS", contenidoSym)
    tablaSym.render('ts', view=True)  # doctest: +SKIP
    'ts.pdf'


def gramatica():
    contenido = Tentrada.get(1.0, 'end')
    g.generaReporteBNF(contenido)


frame1 = Frame(variables.ventana,width=60,height=10)
frame1.pack()
frame1.config(cursor="")  # Tipo de cursor
frame1.config(relief="sunken")  # relieve del frame hundido
frame1.config(bd=8)  # tamaño del borde en píxeles

scrollbar = Scrollbar(frame1, orient='horizontal')
scrollbar.pack(side = BOTTOM, fill = X)

text_scroll = Scrollbar(frame1)
text_scroll.pack(side=RIGHT, fill=Y)


entrada = StringVar()
Tentrada = Text(frame1, wrap="none", xscrollcommand = scrollbar.set,yscrollcommand=text_scroll.set)
Tentrada.config(width=142, height=18)
Tentrada.config(background="gray3")
Tentrada.config(foreground="white")
Tentrada.config(insertbackground="white")
frame1.place(x=3, y=3)
Tentrada.pack()

scrollbar.config(command = Tentrada.xview)


frame2 = Frame(variables.ventana, width=60, height=10)
frame2.pack()
frame2.config(cursor="")  # Tipo de cursor
frame2.config(relief="sunken")  # relieve del frame hundido
frame2.config(bd=8)  # tamaño del borde en píxeles
scrollbar2 = Scrollbar(frame2, orient='horizontal')
scrollbar2.pack(side=BOTTOM, fill=X)
text_scroll2 = Scrollbar(frame2)
text_scroll2.pack(side=RIGHT, fill=Y)

variables.consola = Text(frame2, wrap="none", xscrollcommand = scrollbar2.set,yscrollcommand=text_scroll2.set)
variables.consola.config(width=142, height=16)
variables.consola.config(background="gray5")
variables.consola.config(foreground="orange")
variables.consola.config(insertbackground="orange")
variables.consola.config(state='disabled')
frame2.place(x=3, y=332)
variables.consola.pack()
scrollbar2.config(command=variables.consola.xview)


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
class Interfaz:
    def desplegarinterfaz(self):
        variables.ventana.mainloop()

inter=Interfaz()
inter.desplegarinterfaz()

