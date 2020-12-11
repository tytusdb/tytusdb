from abstract.instruccion import *
from tools.tabla_tipos import *

class owner_mode(instruccion):
    def __init__(self, owner, dato, line, column, num_nodo):
        super().__init__(line, column)
        self.owner = owner
        self.dato = dato        

        #Nodo AST Owner Mode
        if owner:
            self.nodo = nodo_AST('OWNER', num_nodo)
            self.nodo.hijos.append(nodo_AST('OWNER', num_nodo+1))            
        else:
            self.nodo = nodo_AST('MODE', num_nodo)
            self.nodo.hijos.append(nodo_AST('MODE', num_nodo+1))            

        self.nodo.hijos.append(nodo_AST('=', num_nodo+2))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo+3))

    def ejecutar(self):
        pass