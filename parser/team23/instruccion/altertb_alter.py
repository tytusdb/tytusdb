from abstract.instruccion import *
from tools.tabla_tipos import *

class altertb_alter(instruccion):
    def __init__(self, ID, opcion, line, column, num_nodo):

        super().__init__(line, column)
        self.ID = ID
        self.opcion = opcion

        #Nodo de ALTER
        self.nodo  = nodo_AST('ALTER', num_nodo)
        self.nodo.hijos.append(nodo_AST('ALTER', num_nodo+1))
        self.nodo.hijos.append(nodo_AST('COLUMN', num_nodo+2))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 3))
        self.nodo.hijos.append(opcion.nodo)

    def ejecutar(self):
        pass