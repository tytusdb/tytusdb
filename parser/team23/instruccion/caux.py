from abstract.instruccion import *
from tools.tabla_tipos import *

class caux(instruccion):

    def __init__(self, dato, line, column, num_nodo):

        super().__init__(line,column)
        self.dato = dato

        #Nodo AST CONSTRAINT
        self.nodo = nodo_AST('CONSTRAIN', num_nodo)
        self.nodo.hijos.append(nodo_AST('CONSTRAIN', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo + 2))

        #Gramatica
        self.grammar_ = '<TR><TD> CONSTRAINT ::= CONSTRAINT ' + dato + '</TD><TD> CONSTRAINT = new caux(' + dato + '); </TD></TR>'

    def ejecutar(self):
        pass