import tablaDGA as TS

from variables import tabla as ts
from reportAST import *
from reportAST import *
import grammar2 as g
import pickle
from reportTable import *




pila = ''
Listaselects = []
correlativos = []
contador = -1
jsonObject = None

def execute(script: str):
    global Listaselects
    global ts
    if 'SELECT * FROM temp' in script:
        try:
            Listaselects = cargar()
            s = Listaselects.pop()
            print('Se debe hacer un select')
            x = s.ejecutar()
            serialaizer()
        except:
            '''Error'''
    else:
        raiz = g.parse(script)

        try:
            for a in raiz:
                a.ejecutar()
        except:
            print('Error' + script)
    return



def execute1(script: str):
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
        for a in raiz:
            print(a)
            a.ejecutar()
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


def carga():
    with open('table.pickle', 'rb') as f:
        return pickle.load(f)

def guarda():
    with open('table.pickle', 'wb') as f:
        pickle.dump(ts, f, pickle.DEFAULT_PROTOCOL)