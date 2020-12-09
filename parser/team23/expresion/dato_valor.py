from abstract.expresion import *
from tools.tabla_tipos import *
from abstract.retorno import *

class literal(expresion):
    def __init__(self, line, column, valor, tipo, num_nodo):
        super().__init__(line, column)
        self.valor = valor
        self.tipo = tipo

        #Nodo AST Literal
        self.nodo = nodo_AST(valor, num_nodo)

    def ejecutar(self, ambiente):
        if self.tipo == tipo_primitivo.DECIMAL or self.tipo == tipo_primitivo.ENTERO:
            return retorno(int(self.valor), self.tipo)
        else:
            return retorno(self.valor, self.tipo)