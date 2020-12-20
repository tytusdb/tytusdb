from ast.Expresion import Expresion
from ast.Symbol import Symbol
from ast.Expresion import Expresion
from ast.Symbol import TIPOVAR as Tipo

class Declarevar(Expresion):

    def __init__(self,id,value,line, column,declare):
        self.id = id
        self.line= line
        self.column = column
        self.value = value
        self.declare = declare

    def ejecutar(self,entorno,tree):
        simbolo = Symbol(self.id,self.value,self.line,self.column,self.declare)

        if(entorno.existe(self.id)):
            entorno.replacesymbol(simbolo)
        else:
            entorno.add(simbolo)

        return False
