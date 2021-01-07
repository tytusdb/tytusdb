from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO

class CADENAS(NodoArbol):

    def __init__(self, data, line, column):
        super().__init__(line, column)
        self.data = data

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        value:Valor = Valor(TIPO.CADENA, self.data)
        return value