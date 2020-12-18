from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class substring(instruccion):
    def __init__(self,subst,expresiones1,expresiones2,expresiones3, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones1=expresiones1
        self.expresiones2=expresiones2
        self.expresiones3=expresiones3

        self.subst=subst

        self.nodo = nodo_AST(subst,num_nodo)
        self.nodo.hijos.append(expresiones1.nodo)
        self.nodo.hijos.append(expresiones2.nodo) 
        self.nodo.hijos.append(expresiones3.nodo) 

    def ejecutar(self):
        pass 