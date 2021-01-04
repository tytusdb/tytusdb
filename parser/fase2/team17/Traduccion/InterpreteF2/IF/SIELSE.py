from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

class SIELSE(NodoArbol):

    def __init__(self, exp, body, contrabody, line, coliumn):
        super().__init__(line, coliumn)
        self.exp = exp
        self.body = body
        self.contrabody = contrabody

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        Bv = arbol.getLabel()
        Bf = arbol.getLabel()
        Btemporal = arbol.getLabel()
        arbol.addC3D("if " + self.exp.traducir(entorno, arbol) + " goto " + str(Bv))
        arbol.addC3D("goto " + Bf)
        arbol.addC3D(Bv + ":")
        arbol.addC3D(self.body.traducir(entorno, arbol))
        arbol.addC3D("goto " + Btemporal)
        arbol.addC3D(Bf + ":")
        arbol.addC3D(self.contrabody.traducir(entorno, arbol))
        arbol.addC3D(Btemporal + ":")
        pass

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
