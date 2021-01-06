from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo


class Assignment(Instruction):
    def __init__(self, id, value, row, column):
        super().__init__(row, column)
        self.id = id
        self.value = value

    def execute(self, environment):
        exp = self.value.execute(environment)
        # TODO: Error
        if environment.getVar(self.id) != None:
            self.value = exp.value + "\t" + self.id + " = " + str(exp.temp) + "\n"
            return code.C3D(self.value, self.id, self.row, self.column)

    def dot(self):
        new = Nodo("ASSIGMENT")
        n1 = Nodo(str(self.id))
        new.addNode(n1)
        if self.value != None:
            new.addNode(self.value.dot())
        return new