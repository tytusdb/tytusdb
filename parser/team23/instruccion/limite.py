from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class limite(instruccion):
    def __init__(self, primero, segundo, line, column, num_nodo):
        super().__init__(line,column)
        self.primero=primero
        self.segundo=segundo
        
        print(str (segundo)+' --<')

        self.nodo = nodo_AST('LIMITE',num_nodo)
        self.nodo.hijos.append(nodo_AST(primero,num_nodo+1))
        self.nodo.hijos.append(nodo_AST(segundo,num_nodo+2))
        
         
        
    def ejecutar(self):
        pass 