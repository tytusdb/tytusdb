from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from datetime import datetime


class insert(NodoArbol):

    def __init__(self, identificador, expres, idlist, tipoInsert, line, coliumn):
        super().__init__(line, coliumn)
        self.identificador = identificador
        self.expres = expres
        self.tipoInsert = tipoInsert
        self.idlist = idlist

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        if self.tipoInsert == 1:
            argumentos = ''
            contador = 0
            for i in self.expres:
                if contador == 0:
                    argumento = i.getString(entorno, arbol)
                    if str(argumento) == 'now()':
                        ahora = '\'' + str(datetime.now()) + '\''
                        argumentos = argumentos + ahora
                    else:
                        argumentos = argumentos + argumento
                    contador = 1
                else:
                    argumento = i.getString(entorno, arbol)
                    if str(argumento) == 'now':
                        ahora = '\'' + str(datetime.now()) + '\''
                        argumentos = argumentos + ',' + ahora
                    else:
                        argumentos = argumentos + ',' + argumento

            arbol.addC3D('heap = \'' + 'insert into ' + str(self.identificador) + ' values (' + argumentos + ');' + '\'')
            temp = arbol.getTemp()
            arbol.addC3D(temp + ' = inter()')
            return temp
        else:
            lista_id = ''
            contador_1 = 0
            for i in self.idlist:
                if contador_1 == 0:
                    lista_id = lista_id + str(i)
                    contador_1 = 1
                else:
                    lista_id = lista_id + ',' + str(i)
            argumentos = ''
            contador = 0
            for i in self.expres:
                if contador == 0:
                    argumentos = argumentos + i.getString(entorno, arbol)
                    contador = 1
                else:
                    argumentos = argumentos + ',' + i.getString(entorno, arbol)
            arbol.addC3D(
                'heap = \'' + 'insert into ' + str(self.identificador) + ' (' + lista_id + ') values (' + argumentos + ');' + '\'')
            temp = arbol.getTemp()
            arbol.addC3D(temp + ' = inter()')
            return temp

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass