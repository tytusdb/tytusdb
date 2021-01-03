from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

class SUMA(NodoArbol):

    def __init__(self, izq: NodoArbol, der: NodoArbol, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.der = der

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        tipoRes = COMPROBADOR_deTipos(self.izq.analizar_semanticamente(entorno, arbol), self.der.analizar_semanticamente(entorno, arbol), "+")
        if tipoRes != -1:
            return tipoRes.getTipoResultante()
        else:
            # ERROR SEMANTICO de tipo
            pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        izquierdo: Valor = self.izq.traducir(entorno, arbol)
        derecho: Valor = self.der.traducir(entorno, arbol)
        if self.analizar_semanticamente(entorno, arbol) == 0:
            newValor:Valor = Valor(TIPO.ENTERO, izquierdo.data + derecho.data)
            return newValor
        elif self.analizar_semanticamente(entorno, arbol) == 1:
            newValor:Valor = Valor(TIPO.DECIMAL, izquierdo.data + derecho.data)
            return newValor
        elif self.analizar_semanticamente(entorno, arbol) == 2:
            newValor:Valor = Valor(TIPO.CADENA, str(izquierdo.data) + str(derecho.data))
            print(newValor.data)
            return newValor

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol) -> str:
        cadena:str = self.izq.getString(entorno, arbol) + str(" + ") + self.der.getString(entorno, arbol)
        return cadena

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
