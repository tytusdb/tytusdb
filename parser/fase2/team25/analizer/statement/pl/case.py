import sys

sys.path.append("../../..")
from analizer.abstract import instruction
from analizer.reports import Nodo
from analizer.symbol.environment import Environment

class Case(instruction.Instruction):
    def __init__(self, expresion, cases, elseIns, row, column) -> None:
        self.expression = expresion
        self.cases = cases
        self.elseIns = elseIns
        super().__init__(row, column)

    def execute(self, environment):
        pass

    def generate3d(self, environment, instanciaAux):
        lExit = instanciaAux.getNewLabel()
        cond = self.expression.generate3d(environment,instanciaAux)

        tempTag = []

        for caso in self.cases:
            exp = caso.expression.generate3d(environment,instanciaAux)
            lCaso = instanciaAux.getNewLabel()
            instanciaAux.addToCode(f'\tif {cond} == {exp}: goto .{lCaso}')
            tempTag.append(lCaso)
        if self.elseIns:
            for ins in self.elseIns:
                ins.generate3d(environment,instanciaAux)
        instanciaAux.addToCode(f'\tgoto .{lExit}')   

        aux = 0
        for caso in self.cases:
            instanciaAux.addToCode(f'\tlabel .{tempTag[aux]}')
            caso.generate3d(environment,instanciaAux)
            instanciaAux.addToCode(f'\tgoto .{lExit}')
            aux += 1

        instanciaAux.addToCode(f'\tlabel .{lExit}')
                

class CaseWhen(instruction.Instruction):
    def __init__(self, expression, body, row, column) -> None:
        self.expression = expression
        self.body = body
        super().__init__(row, column)

    def generate3d(self, environment, instanciaAux):
        for ins in self.body:
            ins.generate3d(environment,instanciaAux)
        