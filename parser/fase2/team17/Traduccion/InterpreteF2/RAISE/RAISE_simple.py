from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO

class RAISE_simple(NodoArbol):

    def __init__(self, exp, line, column):
        super().__init__(line, column)
        self.exp = exp

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return TIPO.CADENA

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        tmp = self.exp.traducir(entorno, arbol)
        #temp = arbol.getTemp()
        #arbol.addC3D(temp + " = " + '\'' + str(value) + '\'')
        arbol.addC3D("print(str(" + str(tmp) + "))")
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return str(self.data)

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
