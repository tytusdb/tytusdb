from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ReporteTS_forFunction import ReporteTS_forFunction
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos


class dropfun(NodoArbol):

    def __init__(self, identificador, line, coliumn):
        super().__init__(line, coliumn)
        self.identificador = identificador

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        if arbol.existFun(str(self.identificador)):
            pass
        else:
            nota = 'Funcion ' + str(self.identificador) + ' no existe'
            reportero = ErroresSemanticos(nota, self.linea, self.columna, 'dropfun')
            arbol.ErroresSemanticos.append(reportero)
            return

        arbol.dropFuncione(str(self.identificador))
        print('NH -> funcion ' + str(self.identificador) + ' eliminada exitosamente')
        return


    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass