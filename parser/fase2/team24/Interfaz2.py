#IMPORTS
import importlib
from tkinter import *

import grammar2
import grammar2 as g
import tablaDGA as TabladeSimbolos
from reports.reportAST import *
from reports.reportError import *
from reports.reportTable import *
import prettytable as pt
from reports.reportBNF import *
import webbrowser as wb

default_db = 'DB1'
import pickle
importlib.reload(grammar2)
ts = TabladeSimbolos.Tabla()
default_db = 'DB1'
STACK_INSTRUCCIONES = []

try:
    with open('tablaGuardada.pickle','wb') as f:
        ts = pickle.load(f)
except:
    ts = TabladeSimbolos.Tabla()


def analiz(input):
    print(input)
    raiz = g.parse(input)
    results = []
    executeGraphTree(raiz)
def analiz(input):
    graphTable(ts)
    report_errors()
    report_BNF()

    return results

def traducir(input):
    global STACK_INSTRUCCIONES
    STACK_INSTRUCCIONES = str(input).split(';')
    raiz = g.parse(input)
    results = []
    for val in raiz:
        res = val.traducir()
        if isinstance(res, CError):
            print('')
        else:
            results.append(res)

root = Tk()
cont = 1
def Analizar():
    global cont
    for res in results:
        consola.insert(str(float(cont)), res)
        print(str(float(cont)), res)
        if isinstance(res,pt.PrettyTable):
            cont += (res.get_string().count('\n')+2)
        else:
            cont += (res.count('\n')+2)
        consola.insert(str(float(cont)), '\n')
        print(str(float(cont)), res)

def Analizar2(texto: str):
    results = analiz(texto)
    global cont
    for res in results:
        consola.insert(str(float(cont)), res)
        print(str(float(cont)), res)
        if isinstance(res,pt.PrettyTable):
            cont += (res.get_string().count('\n')+2)
        else:
            cont += (res.count('\n')+2)
        consola.insert(str(float(cont)), '\n')
        print(str(float(cont)), res)

def Traducir():
    traducir(texto.get("1.0", "end-1c"))

def AbrirAST():
    wb.open_new(r'tree.gv.pdf')
def AbrirBNF():
    BarraMenu.add_cascade(label="Editar", menu=MenuEditar)

MenuAnalizador= Menu(BarraMenu, tearoff=0)
MenuAnalizador.add_command(label="Ejecutar Analisis",command=Analizar)
MenuAnalizador.add_command(label="Traducir a 3D",command=Traducir)
BarraMenu.add_cascade(label="Analizar", menu=MenuAnalizador)

MenuReportes= Menu(BarraMenu, tearoff=0)