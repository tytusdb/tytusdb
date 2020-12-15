from abstract.instruccion import *
from tools.tabla_tipos import *

class unique_simple(instruccion):

    def __init__(self, constrain, dato, line, column, num_nodo):

        super().__init__(line,column)
        self.contrain = constrain
        self.dato = dato

        self.nodo = nodo_AST('condition_column',num_nodo)

        if constrain != None:
            self.nodo.hijos.append(constrain.nodo)

        self.nodo.hijos.append(nodo_AST('UNIQUE',num_nodo+1))

        if dato != None:
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))

            for aux in dato:
                self.nodo.hijos.append(aux.nodo)

            self.nodo.hijos.append(nodo_AST(')', num_nodo + 3))


    def ejecutar(self):
        pass