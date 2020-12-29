from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.simbolo import Simbolo
from Interprete.Manejo_errores import ErroresSemanticos
from Interprete.Manejo_errores import ErroresSintacticos

class Condicion(NodoArbol):

    def __init__(self, condicionante, tipocondicionante, extra1, line, column):
        super().__init__(line,column)
        self.condicionante = condicionante
        self.tipocondicionante = tipocondicionante
        self.extra1 = extra1

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        if self.tipocondicionante == "where":
            self.condicionante.execute(entorno, arbol)
            return
        if self.tipocondicionante == "ORDER":
            TablaResult: Valor = entorno.obtener_varibale("TablaResult")
            TablaResult.inicializarPrettybabe()
            consola = TablaResult.order(str(self.condicionante.referencia), str(self.extra1))
            simbol: Simbolo = Simbolo("TablaResult", 0, TablaResult)
            entorno.insertar_variable(simbol)
            arbol.console.append("\n" + consola + "\n")
        if self.tipocondicionante == "LIMIT":
            limitador = self.condicionante.execute(entorno, arbol)
            TablaResult: Valor = entorno.obtener_varibale("TablaResult")
            TablaResult.inicializarPrettybabe()
            consola = TablaResult.limit(int(limitador.data))
            simbol: Simbolo = Simbolo("TablaResult", 0, TablaResult)
            entorno.insertar_variable(simbol)
            arbol.console.append("\n" + consola + "\n")

        val: Valor = Valor(3, False)
        return val