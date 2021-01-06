from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class IsNodistinct(instruccion):
    def __init__(self,agrupacion, expresiones,expresiones2, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones=expresiones
        self.expresiones2=expresiones2
        self.agrupacion=agrupacion
        self.nodo = nodo_AST(agrupacion,num_nodo)
        self.nodo.hijos.append(expresiones.nodo)
        self.nodo.hijos.append(nodo_AST('FROM', num_nodo+1))
        self.nodo.hijos.append(expresiones2.nodo) 

    def ejecutar(self):
        pass 