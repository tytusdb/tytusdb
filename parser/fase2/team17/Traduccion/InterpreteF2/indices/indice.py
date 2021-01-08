from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ReporteTS import ReporteTS
from InterpreteF2.Reporteria.ReporteTS_Indice import ReportIndice
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos

class indice(NodoArbol):

    def __init__(self, identificador, linea, columna):
        super().__init__(linea, columna)
        self.identificador = identificador
        self.linea = linea
        self.columna = columna

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        for i in range(len(arbol.ReporteTS_Indices)):
            temp:ReportIndice =arbol.ReporteTS_Indices[i]
            if temp.nombre == self.identificador:
                error:ErroresSemanticos = ErroresSemanticos('Ya existe el index \''+temp.nombre+'\'', self.linea, self.columna, 'Indice')
                arbol.ErroresSemanticos.append(error)
                return

        nodo = ReportIndice(self.identificador,self.identificador,'index','columnas','consideracion', self.columna, self.columna)

        arbol.ReporteTS_Indices.append(nodo)
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass