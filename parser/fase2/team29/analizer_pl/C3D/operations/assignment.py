from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl import grammar


class Assignment(Instruction):
    def __init__(self, id, value, row, column):
        super().__init__(row, column)
        self.id = id
        self.value = value

    def execute(self, environment):
        try:
            exp = self.value.execute(environment)
            # TODO: Error
            if environment.getVar(self.id) != None:
                self.value = exp.value + "\t" + self.id + " = " + str(exp.temp) + "\n"
                grammar.optimizer_.addScalarAsig(self.id, exp.temp, self.row, True)
                return code.C3D(self.value, self.id, self.row, self.column)
            else:
                grammar.PL_errors.append("Error P0000: La variable "+self.id+" no esta declarada")
        except:
            grammar.PL_errors.append("Error P0000: Error en la asignacion de valor")

    def dot(self):
        new = Nodo("ASSIGMENT")
        n1 = Nodo(str(self.id))
        new.addNode(n1)
        if self.value != None:
            new.addNode(self.value.dot())
        return new