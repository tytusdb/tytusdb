from abstract.instruccion import *
from tools.tabla_tipos import *

class condicion_simple(instruccion):
    def __init__(self, comando, ID, key, line, column, num_nodo):

        super().__init__(line,column)
        self.comando = comando
        self.ID = ID
        self.key = key


        #Nodos

        if comando.lower() == 'default':
            print("entro 5")
            self.nodo = nodo_AST('DEFAULT', num_nodo)
            self.nodo.hijos.append(nodo_AST('DEFAULT', num_nodo + 1))
            self.nodo.hijos.append(nodo_AST(ID, num_nodo + 2))

        elif comando.lower() == 'null':

            self.nodo = nodo_AST('NULL', num_nodo)
            self.nodo.hijos.append(nodo_AST('NULL', num_nodo + 1))

        elif comando.lower() == 'not':

            self.nodo = nodo_AST('NOT NULL', num_nodo)
            self.nodo.hijos.append(nodo_AST('NOT NULL', num_nodo + 1))

        elif comando.lower() == 'reference':

            self.nodo = nodo_AST('REFERENCE', num_nodo)
            self.nodo.hijos.append(nodo_AST('REFERENCE', num_nodo + 1))
            self.nodo.hijos.append(nodo_AST(ID, num_nodo + 2))

        elif comando.lower() == 'constraint':

            self.nodo = nodo_AST('CONSTRAINT', num_nodo)
            self.nodo.hijos.append(nodo_AST('CONSTRAINT', num_nodo + 1))
            self.nodo.hijos.append(nodo_AST(ID, num_nodo + 2))
            #self.nodo.hijos.append(key.nodo)


    def ejecutar(self):
        pass