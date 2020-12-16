import json
import sys, os.path
import os

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\storageManager')
sys.path.append(storage)

from jsonMode import *


class Column():
    def __init__(self):
        self.name = None
        self.type = None
        self.isUnique = None
        self.check = None
        self.default = None
        self.isNull = None

class Check():
    def __init__(self):
        self.name = None

class Unique():
    def __init__(self):
        self.name = None


class Table():
    def __init__(self):
        self.name = None
        self.columnas = []

    def crearColumna(self, parent):
        columna = Column()
        columna.name = parent.hijos[0].valor
        


    
    def execute(self, parent):
        for hijo in parent.hijos:
            if hijo.nombreNodo == "IDENTIFICADOR" :
                self.name = hijo.nombreNodo
            elif hijo.nombreNodo == "ATRIBUTO_COLUMNA" :
                print("Se debe crear una columna o constraint")
            elif hijo.nombreNodo == "ATRIBUTO_UNIQUE" :
                print("Se debe crear una columna o constraint")
            elif hijo.nombreNodo == "ATRIBUTO_CHECK" :
                print("Se debe crear una columna o constraint")