from abstract.expresion import *
from tools.tabla_tipos import *

class literal(expresion):
    def __init__(self, line, column, valor, tipo, num_nodo):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo

        #Nodo AST Literal
        self.nodo = nodo_AST(valor, num_nodo)

    def ejecutar(self):
        pass