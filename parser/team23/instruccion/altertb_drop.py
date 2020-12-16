from abstract.instruccion import *
from tools.tabla_tipos import *

class altertb_drop(instruccion):
    def __init__(self,alterdrop, ID, line, column, num_nodo):
        super().__init__(line, column)
        self.alterdrop = alterdrop
        self.ID = ID

        #Nodo ALTER DROP
        self.nodo = nodo_AST('DROP', num_nodo)
        self.nodo.hijos.append(nodo_AST('DROP',num_nodo+1))
        self.nodo.hijos.append(nodo_AST(alterdrop, num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 3))

    def ejecutar(self):
        pass