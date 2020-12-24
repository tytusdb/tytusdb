from abstract.expresion import * 
from tools.tabla_tipos import *
from abstract.retorno import *

class primitivo(expresion):
    def __init__(self, line, column, valor, tipo, num_nodo):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo

        #Nodo AST 
        self.nodo = nodo_AST('PRIMITIVO', num_nodo)
        self.nodo.hijos.append(nodo_AST(str(valor), num_nodo+1))

        #Gramatica
        self.grammar_ = '<TR><TD> PRIMITIVO ::= ' + str(valor) +' </TD><TD> PRIMITIVO = new primitivo(' + str(valor) + '); </TD></TR>'

    def ejecutar(self, list_tb):
        return retorno(self.valor, self.tipo)
