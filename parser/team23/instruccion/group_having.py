from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class group_having(instruccion):
    def __init__(self,expresiones, line, column, num_nodo):
        super().__init__(line,column)
        self.expresiones=expresiones
        
        self.nodo = nodo_AST('HAVING',num_nodo)
        self.nodo.hijos.append(nodo_AST('HAVING',num_nodo+1))
        
         
        
    def ejecutar(self):
        pass 