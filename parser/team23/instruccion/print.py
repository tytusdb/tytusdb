from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *

class print_(instruccion):
    def __init__(self, valor, line, column, num_nodo):
        super().__init__(line, column)
        self.valor = valor

        #Nodo AST Print
        self.nodo = nodo_AST('print', num_nodo)
        self.nodo.hijos.append(nodo_AST('print', num_nodo+1))
        self.nodo.hijos.append(nodo_AST('(', num_nodo+2))
        self.nodo.hijos.append(valor.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo+3))
    
    def ejecutar(self, ambiente):
        try:
            value = self.valor.ejecutar(ambiente)  
            add_text(value.valor)
        except:
            pass
        