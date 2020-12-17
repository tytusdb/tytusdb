from abstract.instruccion import *
from tools.tabla_tipos import *

class op_add_ke(instruccion):
    def __init__(self, key_, lista, line, column, num_nodo):

        super().__init__(line, column)
        self.key_ = key_
        self.lista = lista

        #Nodo de op_add

        self.nodo = nodo_AST('op_add', num_nodo)
        self.nodo.hijos.append(key_.nodo)
        self.nodo.hijos.append(nodo_AST('REFERENCES', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))
        if lista != None:
            for aux in lista:
                self.nodo.hijos.append(aux.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 6))


    def ejecutar(self):
        pass