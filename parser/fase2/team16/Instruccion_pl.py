from six import string_types
from expresiones import *
from Instruccion import *

class If_inst(Instruccion):
    def __init__(self, condicion, instIf, instElse):
        self.condicion = condicion
        self.instIf = instIf
        self.instElse = instElse

class Elsif_inst(Instruccion):
    def __init__(self, condicion, instIf, listaElsif,instElse):
        self.condicion = condicion
        self.instIf = instIf
        self.listaElsif = listaElsif
        self.instElse = instElse

class elsif_obj(Instruccion):
    def __init__(self, condicion, inst):
        self.condicion = condicion
        self.inst = inst

class Optimizacion():
    def __init__(self, original, optimizado):
        self.original = original
        self.optimizado = optimizado

class OptAsignacion():
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der

class Print_I(Instruccion):
    def __init__(self, id):
        self.id = id


