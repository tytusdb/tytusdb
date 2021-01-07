
#import Interfaz
from InstruccionesDGA import tabla
import tablaDGA as TabladeSimbolos
from reportAST import *
from reportAST import *
import grammar2 as g
import pickle


default_db = 'DB1'
ts = TabladeSimbolos.Tabla()

pila = ''
Listaselects = []
correlativos = []
contador = -1
jsonObject = None

def execute(script: str):
    global contador
    global pila
    contador = contador+1
    if script == '3D':
        cargar()
        raiz = g.parse(pila)
        Listaselects = cargar()
        for s in Listaselects:
            if isinstance(raiz, list):
                try:
                    raiz.insert(correlativos.pop(), s)
                except:
                    '''No hay selects'''
        executeGraphTree(raiz)
    elif 'SELECT * FROM temp' in script:
        correlativos.append(contador)
    else:
        pila+= '\n' + script


def serialaizer():
    with open('data.pickle', 'wb') as f:
        pickle.dump(Listaselects, f, pickle.DEFAULT_PROTOCOL)

def insertarS(s):
    Listaselects.append(s)

def cargar():
    with open('data.pickle', 'rb') as f:
        return pickle.load(f)