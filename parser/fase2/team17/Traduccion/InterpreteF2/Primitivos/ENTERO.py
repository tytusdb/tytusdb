from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO

class ENTERO(NodoArbol):

    def __init__(self, data, line, column):
        super().__init__(line, column)
        self.data = data

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return 0

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        temp = arbol.getTemp()
        arbol.addC3D(temp + " = " + str(self.data))
        return temp

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        value:Valor = Valor(TIPO.ENTERO, self.data)
        return value

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return str(self.data)

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        value:Valor = Valor(0, self.data)
        return value