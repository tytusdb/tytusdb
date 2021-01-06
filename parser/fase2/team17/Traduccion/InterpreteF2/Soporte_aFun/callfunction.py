from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos


class callfunction(NodoArbol):

    def __init__(self, identificador, expres, line, coliumn):
        super().__init__(line, coliumn)
        self.expres = expres
        self.identificador = identificador

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        argumentos = ''
        contador = 0

        try:
            for i in self.expres:
                if contador == 0:
                    argumentos = argumentos + i.getString(entorno, arbol)
                    contador = 1
                else:
                    argumentos = argumentos + ',' + i.getString(entorno, arbol)
        except:
            argumentos = ''

        temp = arbol.getTemp()
        arbol.addC3D(temp + ' = ' + str(self.identificador) + '(' + argumentos + ')')
        return temp

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        temporal = '\' + str(' + str(self.traducir(entorno, arbol)) + ') + \''
        return temporal

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

