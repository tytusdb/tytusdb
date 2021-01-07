from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos


class Delete(NodoArbol):

    def __init__(self, identificador, wherexp_, line, coliumn):
        super().__init__(line, coliumn)
        self.identificador = identificador
        self.wherexp = wherexp_

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        where = ''
        if self.wherexp is not None:
            where = ' WHERE ' + self.wherexp.getString(entorno, arbol)
        arbol.addC3D('heap = ' + '\'' + 'DELETE FROM ' + str(self.identificador) + where + ';\'')
        temp = arbol.getTemp()
        arbol.addC3D(temp + ' = inter()')
        return temp

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass