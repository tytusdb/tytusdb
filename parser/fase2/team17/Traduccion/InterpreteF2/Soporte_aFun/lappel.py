from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos
from datetime import datetime


class lappel(NodoArbol):

    def __init__(self, identificador, expres, line, coliumn):
        super().__init__(line, coliumn)
        self.expres = expres
        self.identificador = identificador
        self.linea = line
        self.columna = coliumn

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        # verificar si la fun esta activa:
        if arbol.lFun_isINACTIVE(str(self.identificador)):
            descripcion = 'Funcion ' + str(self.identificador) + ' esta inactivado, no puede usarse'
            reportero = ErroresSemanticos(descripcion, str(self.linea), str(self.columna), 'lappel')
            arbol.ErroresSemanticos.append(reportero)
            temp = arbol.getTemp()
            arbol.addC3D(temp + ' = \'\'')
            return temp
        #------------------------------------------

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
        if str(self.identificador) == 'now':
            ahora = '\'' + str(datetime.now()) + '\''
            arbol.addC3D(temp + ' = ' + ahora)
        else:
            arbol.addC3D(temp + ' = ' + str(self.identificador) + '(' + argumentos + ')')
        return temp


    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        temporal = '\' + str(' + str(self.traducir(entorno, arbol)) + ') + \''
        return temporal

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass