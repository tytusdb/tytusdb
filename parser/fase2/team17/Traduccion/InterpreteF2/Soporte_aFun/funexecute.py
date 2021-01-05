from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

class funexecute(NodoArbol):

    def __init__(self, header, stmt_declare, stmt_body, line, coliumn):
        super().__init__(line, coliumn)
        self.header = header
        self.stmt_declare = stmt_declare
        self.stmt_body = stmt_body

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        arbol.switchC3Dfunciones()

        argumentos_puros = self.header.getArgumentos()
        arbol.addC3D("def " + str(self.header.getID()) + "(" + str(argumentos_puros) + "):")

        arbol.resetIdentacion_funciones()
        arbol.addIdentacion()

        self.header.traducir(entorno, arbol)
        for item in self.stmt_declare:
            item.traducir(entorno, arbol)
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
