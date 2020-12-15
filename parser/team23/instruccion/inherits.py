from abstract.instruccion import *
from tools.tabla_tipos import *

class inherits(instruccion):
    def __init__(self, ID, line, column, num_nodo):
        super().__init__(line,column)
        self.ID = ID

        #Nodo INHERITS
        self.nodo = nodo_AST('INHERITS', num_nodo)
        self.nodo.hijos.append(nodo_AST('INHERITS', num_nodo+1))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 3))
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 4))

    def ejecutar(self):
        pass