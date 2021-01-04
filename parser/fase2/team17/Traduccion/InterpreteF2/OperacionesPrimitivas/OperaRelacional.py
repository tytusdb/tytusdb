from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

class OperaRelacional(NodoArbol):

    def __init__(self, izq, der, tipoOperaRelacional, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der
        self.tipoOperaRelacional = tipoOperaRelacional

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        tipoRes = COMPROBADOR_deTipos(self.izq.analizar_semanticamente(entorno, arbol), self.der.analizar_semanticamente(entorno, arbol), "+")
        if tipoRes != -1:
            return tipoRes.getTipoResultante()
        else:
            # ERROR SEMANTICO de tipo
            pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        izquierdo = self.izq.traducir(entorno, arbol) # <-- tiene un temporal
        derecho = self.der.traducir(entorno, arbol) # <-- tiene un temporal
        tmp = str(izquierdo) + " " + str(self.tipoOperaRelacional) + " " + str(derecho)
        return tmp

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

