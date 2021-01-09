from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ReporteTS import ReporteTS


class indice(NodoArbol):

    def __init__(self, identificador, linea, columna):
        super().__init__(linea, columna)
        self.identificador = identificador
        self.linea = linea
        self.columna = columna

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        for i in range(len(arbol.ReporteTS)):
            temp:ReporteTS =arbol.ReporteTS[i]
            if temp.nombre == self.identificador:
                pass



        nodo = ReporteTS(str(self.identificador), str(self.identificador), 'index', 'ASC', str(self.linea), str(self.columna))
        arbol.ReporteTS.append(nodo)
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass