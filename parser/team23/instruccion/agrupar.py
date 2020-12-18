from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class agrupar(instruccion):
    def __init__(self,agrupacion, expresiones, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones=expresiones
        self.agrupacion=agrupacion
        self.nodo = nodo_AST(agrupacion,num_nodo)
        self.nodo.hijos.append(expresiones.nodo)         
        
    def ejecutar(self):
        pass 