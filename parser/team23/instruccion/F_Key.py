from abstract.instruccion import *
from tools.tabla_tipos import *

class F_key(instruccion):
    def __init__(self, dato1, ID, dato2, line, column, num_nodo):
        super().__init__(line,column)
        self.dato1 = dato1
        self.dato2 = dato2
        self.ID = ID

        #Nodo FOREIGN
        self.nodo = nodo_AST('FOREIGN KEY', num_nodo)
        self.nodo.hijos.append(nodo_AST('FOREIGN KEY', num_nodo + 1))
        if dato1 != None:
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))

            for aux in dato1:
                self.nodo.hijos.append(aux.nodo)

            self.nodo.hijos.append(nodo_AST(')', num_nodo + 3))

        self.nodo.hijos.append(nodo_AST('REFERENCES', num_nodo + 4))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 5))

        if dato2 != None:
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 6))

            for aux in dato2:
                self.nodo.hijos.append(aux.nodo)

            self.nodo.hijos.append(nodo_AST(')', num_nodo + 7))

    def ejecutar(self):
                pass