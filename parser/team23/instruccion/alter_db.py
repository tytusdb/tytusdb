from abstract.instruccion import *
from tools.tabla_tipos import *

class alter_db(instruccion):
    def __init__(self, ID, rename, line, column, num_nodo):

        super().__init__(line, column)
        self.ID = ID
        self.rename = rename

        #Nodo ALTER
        self.nodo = nodo_AST('ALTER', num_nodo)
        self.nodo.hijos.append(nodo_AST('ALTER', num_nodo+1))
        self.nodo.hijos.append(nodo_AST('DATABASE', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 3))
        if rename != None:
            self.nodo.hijos.append(rename.nodo)

    def ejecutar(self):
        pass
