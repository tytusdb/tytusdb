from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos


class Update(NodoArbol):

    def __init__(self, line, column, id_, columns_, wherexp_=None):
        super().__init__(line, column)
        self.id = id_
        self.columns = columns_
        self.wherexp = wherexp_

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        argumentos, where = '', ''

        contador = 0
        for i in self.columns:
            if contador == 0:
                argumentos = argumentos + i.getString(entorno, arbol)
                contador = 1
            else:
                argumentos = argumentos + ',' + i.getString(entorno, arbol)
        if self.wherexp is not None:
            where = ' WHERE ' + self.wherexp.getString(entorno, arbol)
        arbol.addC3D('heap = \'' + 'UPDATE ' + str(self.id) + ' SET ' + argumentos + where + ';' + '\'')
        temp = arbol.getTemp()
        arbol.addC3D(temp + ' = inter()')
        return temp

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass