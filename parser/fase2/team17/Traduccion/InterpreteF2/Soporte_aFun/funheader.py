from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

class funheader(NodoArbol):

    def __init__(self, identificador, argumentos, line, coliumn):
        super().__init__(line, coliumn)
        self.argumentos = argumentos
        self.identificador = identificador

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        if self.argumentos == None:
            pass
        else:
            for item in self.argumentos:
                item.traducir(entorno, arbol)
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getID(self):
        return self.identificador

    def getArgumentos(self):
        argumentos = ""
        contador = 0
        if self.argumentos == None:
            pass
        else:
            for item in self.argumentos:
                if contador == 0:
                    argumentos = argumentos + str(item.getID())
                    contador = 1
                else:
                    argumentos = argumentos + ', ' + str(item.getID())
        return argumentos
