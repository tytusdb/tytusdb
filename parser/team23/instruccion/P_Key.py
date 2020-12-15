from abstract.instruccion import *
from tools.tabla_tipos import *

class P_Key(instruccion):
    def __init__(self, dato, line, column, num_nodo):

        super().__init__(line, column)
        self.dato = dato

        #Nodo Primary key
        self.nodo = nodo_AST('PRIMARY KEY', num_nodo)
        self.nodo.hijos.append(nodo_AST('PRIMARY KEY', num_nodo + 1))

        if dato != None:
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))

            for aux in dato:
                self.nodo.hijos.append(aux.nodo)

            self.nodo.hijos.append(nodo_AST(')', num_nodo + 3))

    def ejecutar(self):
        pass