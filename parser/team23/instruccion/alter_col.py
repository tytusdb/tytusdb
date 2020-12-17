from abstract.instruccion import *
from tools.tabla_tipos import *

class alter_col(instruccion):
    def __init__(self, comando, ID, line, column, num_nodo):

        super().__init__(line, column)
        self.comando = comando
        self.ID = ID

        #Nodo opcion alter

        if comando.lower() == 'set':

            self.nodo = nodo_AST('alter_col_op', num_nodo)
            self.nodo.hijos.append(nodo_AST('SET', num_nodo+1))
            self.nodo.hijos.append(nodo_AST('NOT', num_nodo + 2))
            self.nodo.hijos.append(nodo_AST('NULL', num_nodo + 3))

        elif comando.lower() == 'type':

            self.nodo = nodo_AST('alter_col_op', num_nodo)
            self.nodo.hijos.append(nodo_AST('TYPE'), num_nodo + 1)
            self.nodo.hijos.append(nodo_AST(ID, num_nodo + 2))

    def ejecutar(self):
        pass