from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Reporteria.ReporteTS import ReporteTS
from InterpreteF2.Reporteria.ReporteTS_Indice import ReportIndice

class dropindex(NodoArbol):

    def __init__(self, listid, line, coliumn):
        super().__init__(line, coliumn)
        self.listid:list = listid

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        i=0
        while i < len(arbol.ReporteTS_Indice):
            report:ReportIndice = arbol.ReporteTS_Indice[i]
            j = 0
            while j < len(self.listid):
                identificador = self.listid[j]
                if str(report.nombre) == str(identificador):
                    self.listid.pop(j)
                    arbol.ReporteTS_Indice.pop(i)
                j += 1
            i+=1




    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass