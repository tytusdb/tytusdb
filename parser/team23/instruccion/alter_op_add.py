from abstract.instruccion import *
from tools.tabla_tipos import *

class alter_op_add(instruccion):
    def __init__(self, opcion, line, column, num_nodo):

        super().__init__(line, column)
        self.opcion = opcion

        #Nodo de op_add

        self.nodo = nodo_AST('alter_op', num_nodo)
        self.nodo.hijos.append(nodo_AST('ADD', num_nodo + 1))
        self.nodo.hijos.append(opcion.nodo)


    def ejecutar(self):
        pass