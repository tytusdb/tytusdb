from abstract.expresion import * 
from tools.tabla_tipos import *
from abstract.retorno import *

class tableId(expresion):
    def __init__(self, valor, line, column, tipo, num_nodo):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo

        #Nodo AST 
        self.nodo = nodo_AST('ID', num_nodo)
        self.nodo.hijos.append(nodo_AST(str(valor), num_nodo+1))

        #Gramatica
        self.grammar_ = '<TR><TD> ID ::= ' + str(valor) +' </TD><TD> ID = new ID(' + str(valor) + '); </TD></TR>'

    def ejecutar(self):
        return retorno(self.valor, self.tipo)