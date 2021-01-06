from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO

class BOOLEANO(NodoArbol):

    def __init__(self, data, line, column):
        super().__init__(line, column)
        self.data = data

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return 3

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        temp = arbol.getTemp()
        arbol.addC3D(temp + " = " + str(self.data))
        return temp

    def execute(self, entorno:Tabla_de_simbolos, arbol:Arbol):
        value:Valor = Valor(TIPO.BOOLEAN, self.data)
        return value

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        return str(self.data)

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        value: Valor = Valor(3, self.data)
        return value