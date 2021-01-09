from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos


class retorno_simple(NodoArbol):

    def __init__(self, exp, line, coliumn):
        super().__init__(line, coliumn)
        self.exp = exp

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        try:
            if self.exp == None:
                arbol.addC3D("return")
            else:
                try:
                    tmp = self.exp.traducir(entorno, arbol)
                    arbol.addC3D("return " + str(tmp) + "")
                except:
                    arbol.addC3D("return")
                    descripcion = 'Expresion invalida para el retorn'
                    reportero = ErroresSemanticos(descripcion, str(self.linea), str(self.columna), 'retorn')
                    arbol.ErroresSemanticos.append(reportero)
        except:
            arbol.addC3D("return")
            descripcion = 'Expresion invalida para el retorn'
            reportero = ErroresSemanticos(descripcion, str(self.linea), str(self.columna), 'retorn')
            arbol.ErroresSemanticos.append(reportero)
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass