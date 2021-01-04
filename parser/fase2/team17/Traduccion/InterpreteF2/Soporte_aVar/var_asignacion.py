from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.simbolo import Simbolo

class var_asignacion(NodoArbol):

    def __init__(self, identificador, exp, line, coliumn):
        super().__init__(line, coliumn)
        self.identificador = identificador
        self.exp = exp
        self.tipo = 0

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        self.tipo = self.exp.analizar_semanticamente(entorno, arbol)
        return TIPO(self.tipo)

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        valeria:Valor = self.exp.getValueAbstract(entorno, arbol)
        val:Valor = Valor(self.tipo, valeria.data)
        simbol:Simbolo = Simbolo(self.identificador, self.tipo, val)
        entorno.insertar_variable(simbol)
        print("NH -> var " + str(self.identificador) + " ingresada a TS con valor: " + str(valeria.data))
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
