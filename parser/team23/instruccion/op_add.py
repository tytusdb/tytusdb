from abstract.instruccion import *
from tools.tabla_tipos import *

class op_add(instruccion):
    def __init__(self, comando, dato1, dato2, line, column, num_nodo):

        super().__init__(line, column)
        self.comando = comando
        self.dato1 = dato1
        self.dato2 = dato2

        #Nodo de op_add

        if comando.lower() == 'check':

            self.nodo = nodo_AST('op_add', num_nodo)
            self.nodo.hijos.append(nodo_AST('CHECK', num_nodo + 1))
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))
            self.nodo.hijos.append(nodo_AST(dato1, num_nodo + 3))
            self.nodo.hijos.append(nodo_AST('<>', num_nodo + 4))
            self.nodo.hijos.append(nodo_AST(dato2, num_nodo + 5))
            self.nodo.hijos.append(nodo_AST(')', num_nodo + 6))

        elif comando.lower() == 'constraint':

            self.nodo = nodo_AST('op_add', num_nodo)
            self.nodo.hijos.append(nodo_AST('CONSTRAINT', num_nodo + 1))
            self.nodo.hijos.append(nodo_AST(dato1, num_nodo + 2))
            self.nodo.hijos.append(nodo_AST('UNIQUE', num_nodo + 3))
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 4))
            self.nodo.hijos.append(nodo_AST(dato2, num_nodo + 5))
            self.nodo.hijos.append(nodo_AST(')', num_nodo + 6))


    def ejecutar(self):
        pass