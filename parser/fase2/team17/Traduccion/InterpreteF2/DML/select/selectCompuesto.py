from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos


class SelectCompuesto(NodoArbol):

    def __init__(self, string1_, string2_, string3_, line, coliumn):
        super().__init__(line, coliumn)
        self.string1 = string1_
        self.string2 = string2_
        self.string3 = string3_

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        arbol.addC3D('heap = ' + '\'' + str(self.string1) + ' ' + str(self.string2) + ' ' + str(self.string3) + ';\'')
        temp = arbol.getTemp()
        arbol.addC3D(temp + ' = inter()')
        return temp

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass