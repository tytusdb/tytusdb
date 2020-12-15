from abstract.instruccion import *
from tools.tabla_tipos import *

class caux(instruccion):

    def __init__(self,  dato, line, column, num_nodo):

        super().__init__(line,column)
        self.dato = dato

        self.nodo = nodo_AST('CONSTRAIN', num_nodo)
        self.nodo.hijos.append(nodo_AST('CONSTRAIN', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo + 2))

    def ejecutar(self):
        pass