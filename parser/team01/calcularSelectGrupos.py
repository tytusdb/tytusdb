import sys 
import ts as TS
import instrucciones as Instruccion
import tempfile
from datetime import datetime
from pprint import pprint

lstResultado = []

contador = 1
x = 0

def inc():
    global x
    x += 1
    return x

def calcularSelectGrupos(arbol,ts):
    global lstResultado
    global contador
    contador += 1
    id = inc()
    #arbol = arbol.hijos
    #ts.agregarGrupoSelect(str(arbol[0].lexema))

    if(len(arbol.hijos)==1):
        if(arbol.hijos[0].esHoja == 'S'):
            ts.agregarGrupoSelect(str(arbol.hijos[0].lexema))
        else:
            calcularSelectGrupos(arbol.hijos[0],ts)

    elif(len(arbol.hijos)==2):
        #calcularSelectGrupos(arbol[0],ts)
        if(arbol.hijos[0].esHoja == 'S'):
            ts.agregarGrupoSelect(str(arbol.hijos[0].lexema))
        else:
            calcularSelectGrupos(arbol.hijos[0],ts)

        #calcularSelectGrupos(arbol[1],ts)
        if(arbol.hijos[1].esHoja == 'S'):
            ts.agregarGrupoSelect(str(arbol.hijos[1].lexema))
        else:
            calcularSelectGrupos(arbol.hijos[1],ts)


    return id
