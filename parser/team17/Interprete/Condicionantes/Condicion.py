from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor

class Condicion(NodoArbol):

    def __init__(self, condicionante:NodoArbol, tipocondicionante, line, column):
        super().__init__(line,column)
        self.condicionante = condicionante
        self.tipocondicionante = tipocondicionante

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        if self.tipocondicionante == "where":
            value:Valor = self.condicionante.execute(entorno,arbol)
            return value

        val: Valor = Valor(3, False)
        return val