from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos

class UNITARIO(NodoArbol):

    def __init__(self, izq, tipo, line, coliumn):
        super().__init__(line, coliumn)
        self.izq = izq
        self.tipo = tipo

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        try:
            izquierdo = self.izq.traducir(entorno, arbol)  # <-- tiene un temporal
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = " + str(self.tipo) + str(izquierdo))
            return tmp
        except:
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = 0")
            return tmp


    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol) -> str:
        cadena: str = str(self.tipo) + str(self.izq)
        return cadena

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        izquierdo: Valor = self.izq.getValueAbstract(entorno, arbol)  # <-- tiene un temporal
        return izquierdo

    def esNecesarioOptimizar(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return False

