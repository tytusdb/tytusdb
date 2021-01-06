from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ReporteOptimizacion import ReporteOptimizacion

class SI(NodoArbol):

    def __init__(self, exp, body, line, coliumn):
        super().__init__(line, coliumn)
        self.exp = exp
        self.body = body
        self.linea = line
        self.columna = coliumn

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        Bv = arbol.getLabel()
        Bf = arbol.getLabel()
        validacion = str(self.exp.traducir(entorno, arbol))
        arbol.addC3D("if " + validacion + " goto " + str(Bf))
        arbol.addC3D(Bv + ":")
        arbol.addIdentacion()
        #arbol.addC3D(self.body.traducir(entorno, arbol))
        for item in self.body:
            item.traducir(entorno, arbol)
        arbol.popIdentacion()
        arbol.addC3D(Bf + ":")

        # optimizacion ---------------------------
        # Regla no.3:
        original = "if " + validacion + " goto " + str(Bv) + ' goto ' + str(Bf)
        optimizado = "if " + validacion + " goto " + str(Bf)
        reportero = ReporteOptimizacion('Regla 3', original, optimizado, str(self.linea), str(self.columna))
        # ----------------------------------------------------------------
        pass

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
