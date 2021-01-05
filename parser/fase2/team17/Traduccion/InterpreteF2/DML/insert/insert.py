from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos


class insert(NodoArbol):

    def __init__(self, identificador, expres, tipoInsert, line, coliumn):
        super().__init__(line, coliumn)
        self.identificador = identificador
        self.expres = expres
        self.tipoInsert = tipoInsert

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        if self.tipoInsert == 1:
            argumentos = ''
            contador = 0
            for i in self.expres:
                if contador == 0:
                    argumentos = argumentos + i.getString(entorno, arbol)
                    contador = 1
                else:
                    argumentos = argumentos + ',' + i.getString(entorno, arbol)
            arbol.addC3D('heap = \'' + 'insert into ' + str(self.identificador) + ' values (' + argumentos + ');' + '\'')
            temp = arbol.getTemp()
            arbol.addC3D(temp + ' = inter()')
            return temp
        else:
            pass

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass