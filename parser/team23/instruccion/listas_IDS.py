from abstract.instruccion import *
from tools.tabla_tipos import *

class listas_IDS(instruccion):

    def __init__(self,  dato, line, column, num_nodo):

        super().__init__(line,column)
        self.dato = dato

        self.nodo = nodo_AST(dato, num_nodo)

    def ejecutar(self):
        pass