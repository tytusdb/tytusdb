from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Reporteria.ReporteTS_Indice import ReportIndice
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos


class alterindex(NodoArbol):

    def __init__(self, name, newname , line, coliumn):
        super().__init__(line, coliumn)
        self.name = name
        self.rename = newname

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        i=0
        while i < len(arbol.ReporteTS_Indice):
            report:ReportIndice = arbol.ReporteTS_Indice[i]
            if str(report.nombre) == str(self.name):
                arbol.ReporteTS_Indice[i].nombre = str(self.rename)
                arbol.ReporteTS_Indice[i].alias = str(self.rename)
                return
            i+=1

        error: ErroresSemanticos = ErroresSemanticos('No  existe el index \'' + self.name + '\'', self.linea, self.columna,'alterindex')
        arbol.ErroresSemanticos.append(error)
        return


    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass


class alterindexColumn(NodoArbol):

    def __init__(self, name,beforecolumn,actualcolumn ,line, coliumn):
        super().__init__(line, coliumn)
        self.name = name
        self.beforecolumn = beforecolumn
        self.actualcolumn = actualcolumn

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        i=0
        while i < len(arbol.ReporteTS_Indice):
            report:ReportIndice = arbol.ReporteTS_Indice[i]
            if str(report.nombre) == str(self.name):

                for j in range(len(report.columnas)):
                    col:str = report.columnas[j]
                    if col == self.beforecolumn:
                        arbol.ReporteTS_Indice[i].columnas[j]=self.actualcolumn
                        return

                error: ErroresSemanticos = ErroresSemanticos('No existe un index para la columna  \'' + self.beforecolumn + '\'', self.linea, self.columna, 'alterindex')
                arbol.ErroresSemanticos.append(error)
                return
            i+=1

        error: ErroresSemanticos = ErroresSemanticos('No  existe el index \'' + self.name + '\'', self.linea, self.columna,'alterindex')
        arbol.ErroresSemanticos.append(error)
        return

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass


