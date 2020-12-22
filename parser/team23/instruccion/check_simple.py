from abstract.instruccion import *
from tools.tabla_tipos import *
from expresion.primitivo import *

class check_simple(instruccion):

    def __init__(self, constrain, dato, line, column, num_nodo):

        super().__init__(line, column)
        self.contrain = constrain
        self.dato = dato

        #Nodo AST
        self.nodo = nodo_AST('condition_column', num_nodo)
        if constrain != None:
            self.nodo.hijos.append(constrain.nodo)
        self.nodo.hijos.append(nodo_AST('CHECK', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))
        if dato != None:
            self.nodo.hijos.append(dato.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 3))

    def ejecutar(self):
        pass

    def cargar_check(self, id_tb):
        # Recorrer todos los nodos de la expresion
        #try:
        #except:
        pass
            