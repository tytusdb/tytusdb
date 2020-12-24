from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class between1(instruccion):
    def __init__(self,expresiones1,between,expresiones2,operador,expresiones3, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones1=expresiones1
        self.expresiones2=expresiones2
        self.expresiones3=expresiones3

        self.between=between
        self.operador=operador

        self.nodo = nodo_AST(between,num_nodo)
        self.nodo.hijos.append(expresiones1.nodo)
        self.nodo.hijos.append(nodo_AST(between, num_nodo+1))
        self.nodo.hijos.append(expresiones2.nodo) 
        self.nodo.hijos.append(nodo_AST(operador, num_nodo+2))
        self.nodo.hijos.append(expresiones3.nodo) 

    def ejecutar(self):
        pass 