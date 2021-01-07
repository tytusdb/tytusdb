from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO

class BOOLEANO(NodoArbol):

    def __init__(self, data, line, column):
        super().__init__(line, column)
        self.data = data

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return 3

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        temp = arbol.getTemp()
        if self.data.lower() == "true":
            arbol.addC3D(temp + " = " + "True")
        elif self.data.lower() == "false":
            arbol.addC3D(temp + " = " + "False")
        return temp

    def execute(self, entorno:Tabla_de_simbolos, arbol:Arbol):
        value:Valor = Valor(TIPO.BOOLEAN, self.data)
        return value

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        return str(self.data)

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        value: Valor = Valor(3, self.data)
        return value