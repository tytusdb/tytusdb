from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ReporteTS_forFunction import ReporteTS_forFunction
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos

class funexecute(NodoArbol):

    def __init__(self, header, stmt_declare, stmt_body, line, coliumn):
        super().__init__(line, coliumn)
        self.header = header
        self.stmt_declare = stmt_declare
        self.stmt_body = stmt_body
        self.linea = line
        self.columna = coliumn

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):

        # codigo soporte para TS
        if arbol.existFun(str(self.header.getID())):

            if arbol.lFun_isINACTIVE(str(self.header.getID())):
                arbol.covertInactivaeTOactivate(str(self.header.getID()))
                return

            nota = 'Funcion ' + str(self.header.getID()) + ' ya existe, no soporte a sobrecarga'
            reportero = ErroresSemanticos(nota, self.linea, self.columna, 'funexecute')
            arbol.ErroresSemanticos.append(reportero)
            return

        reportero = ReporteTS_forFunction(str(self.header.getID()), str(self.header.getID()), 'Funcion', 'ACTIVO',
                                          str(self.linea), str(self.columna))
        arbol.ReporteTS_Funciones.append(reportero)
        # -------------------------------

        arbol.switchC3Dfunciones()

        argumentos_puros = self.header.getArgumentos()
        arbol.addC3D("def " + str(self.header.getID()) + "(" + str(argumentos_puros) + "):")

        arbol.resetIdentacion_funciones()
        arbol.addIdentacion()

        self.header.traducir(entorno, arbol)

        if self.stmt_declare == None:
            pass
        else:
            for item in self.stmt_declare:
                item.traducir(entorno, arbol)

        if self.stmt_body == None:
            arbol.addC3D('pass')
        else:
            for item in self.stmt_body:
                item.traducir(entorno, arbol)

        arbol.resetIdentacion_funciones()
        arbol.switchC3Dmain()

        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
