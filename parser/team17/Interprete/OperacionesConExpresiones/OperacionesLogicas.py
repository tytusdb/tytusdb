from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo

class OperacionesLogicas(NodoArbol):

    def __init__(self, izq, der, tipoOperaRelacional, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der
        self.tipoOperaRelacional = tipoOperaRelacional

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        izquierdo:Valor = self.izq.execute(entorno, arbol)
        derecho:Valor = self.der.execute(entorno, arbol)