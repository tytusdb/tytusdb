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

        # REGLA 4
        if self.exp.validador_Regla4(entorno, Arbol):
            return self.traducir_regla4(entorno, arbol)
        # REGLA 5
        if self.exp.validador_Regla5(entorno, Arbol):
            return self.traducir_regla5(entorno, arbol)

        Bv = arbol.getLabel()
        Bf = arbol.getLabel()
        validacion = str(self.exp.traducir(entorno, arbol))
        arbol.addC3D("if " + validacion + ':')

        arbol.addIdentacion()
        arbol.addC3D("goto ." + str(Bv))
        arbol.popIdentacion()

        arbol.addC3D('else:')
        arbol.addIdentacion()
        arbol.addC3D("goto ." + Bf)
        arbol.popIdentacion()

        arbol.addC3D('label .' + Bv)
        for item in self.body:
            item.traducir(entorno, arbol)
        arbol.addC3D('label .' + Bf)

        # optimizacion ---------------------------
        # Regla no.3:
        original = "if " + validacion + " goto " + str(Bv) + ' goto ' + str(Bf)
        optimizado = "if " + validacion + " goto " + str(Bf)
        reportero = ReporteOptimizacion('Regla 3', original, optimizado, str(self.linea), str(self.columna))
        arbol.ReporteOptimizacion.append(reportero)
        # ----------------------------------------------------------------
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    # Reglas de optimizacion

    # Regla 4
    def traducir_regla4(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        Bv = arbol.getLabel()
        Bf = arbol.getLabel()
        validacion = str(self.exp.traducir(entorno, arbol))

        arbol.addC3D("if " + validacion + ':')
        arbol.addIdentacion()
        arbol.addC3D("goto ." + str(Bv))
        arbol.popIdentacion()

        arbol.addC3D('else:')
        arbol.addIdentacion()
        arbol.addC3D("goto ." + Bf)
        arbol.popIdentacion()

        arbol.addC3D('label .' + Bv)
        for item in self.body:
            item.traducir(entorno, arbol)
        arbol.addC3D('label .' + Bf)

        # optimizacion ---------------------------
        # Regla no.4:
        original = "if " + validacion + " goto " + str(Bv) + ' goto ' + str(Bf)
        optimizado = "goto " + str(Bv)
        reportero = ReporteOptimizacion('Regla 4', original, optimizado, str(self.linea), str(self.columna))
        arbol.ReporteOptimizacion.append(reportero)
        # ----------------------------------------------------------------

        return

    # Regla 5
    def traducir_regla5(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        Bv = arbol.getLabel()
        Bf = arbol.getLabel()
        validacion = str(self.exp.traducir(entorno, arbol))

        arbol.addC3D("if " + validacion + ':')
        arbol.addIdentacion()
        arbol.addC3D("goto ." + str(Bv))
        arbol.popIdentacion()

        arbol.addC3D('else:')
        arbol.addIdentacion()
        arbol.addC3D("goto ." + Bf)
        arbol.popIdentacion()

        arbol.addC3D('label .' + Bv)
        for item in self.body:
            item.traducir(entorno, arbol)
        arbol.addC3D('label .' + Bf)

        # optimizacion ---------------------------
        # Regla no.5:
        original = "if " + validacion + " goto " + str(Bv) + ' goto ' + str(Bf)
        optimizado = "goto " + str(Bf)
        reportero = ReporteOptimizacion('Regla 5', original, optimizado, str(self.linea), str(self.columna))
        arbol.ReporteOptimizacion.append(reportero)
        # ----------------------------------------------------------------
        return