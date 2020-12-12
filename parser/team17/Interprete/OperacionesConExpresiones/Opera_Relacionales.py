from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor

class Opera_Relacionales(NodoArbol):

    def __init__(self, izq:NodoArbol, der:NodoArbol, tipoOperaRelacional, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der
        self.tipoOperaRelacional = tipoOperaRelacional

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        izquierdo = self.izq#.execute(entorno, arbol)
        derecho = self.der#.execute(entorno, arbol)

        if self.tipoOperaRelacional == "=":
            retorno:Valor = Valor(3, True);
            return  retorno;