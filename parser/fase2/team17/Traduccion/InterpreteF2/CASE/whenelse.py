from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.CASE.when import When


class WhenElse(NodoArbol):
    def __init__(self, line, column, condition_, instructions_, elsecase_, expression_=None):
        super().__init__(line, column)
        self.condition = condition_
        self.instructions = instructions_
        self.elsecase = elsecase_
        self.expression = expression_

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        # Se genera la etiqueta de inicio, final, temporal y la variable de expresion si la hay
        startlabel = '.' + str(arbol.getLabel())
        finallabel = '.' + str(arbol.getLabel())
        templabel = '.' + str(arbol.getLabel())
        var_add = " "
        # Si el case trae una expresion
        if self.expression is not None:
            # Se obtiene la variable y se genera la comparacion
            var_add = " " + self.expression.traducir(entorno, arbol) + " = "
            # Se asigna la expresion al siguiente caso del case si no es un else
            if isinstance(self.elsecase, WhenElse) or isinstance(self.elsecase, When):
                self.elsecase.expression = self.expression
        arbol.addC3D("if" + var_add + self.condition.traducir(entorno, arbol) + " goto " + str(startlabel))
        arbol.addC3D("goto " + finallabel)
        arbol.addC3D('label ' + startlabel)
        arbol.addIdentacion()
        for instruction in self.instructions:
            instruction.traducir(entorno, arbol)
        arbol.popIdentacion()
        arbol.addC3D("goto " + templabel)
        arbol.addC3D('label ' + finallabel)
        if isinstance(self.elsecase, WhenElse) or isinstance(self.elsecase, When):
            arbol.addC3D(self.elsecase.traducir(entorno, arbol))
        else:
            for ins in self.elsecase:
                ins.traducir(entorno, arbol)
        arbol.addC3D('label ' + templabel)

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass