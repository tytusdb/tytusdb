from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo

class union(NodoArbol):

    def __init__(self, select_1, select_2, line, coliumn):
        super().__init__(line, coliumn)
        self.select_1 = select_1
        self.select_2 = select_2

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        TV_select1: Valor = self.select_1.execute(entorno, arbol)
        TV_select2: Valor = self.select_2.execute(entorno, arbol)

        arbol.console.append("\n" + "Union ---> GO" + "\n")
        arbol.console.append(TV_select1.union(TV_select2))
        arbol.console.append("\n" + "Union ---> END" + "\n")


