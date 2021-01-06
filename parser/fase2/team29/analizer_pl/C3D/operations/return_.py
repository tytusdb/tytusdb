from analizer_pl.abstract.instruction import Instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment


class Return(Instruction):
    def __init__(self, exp, row, column) -> None:
        super().__init__(row, column)
        self.exp = exp

    def execute(self, environment):
        tab = ""
        cd = ""
        if isinstance(environment, Environment):
            tab += "\t"
        if self.exp:
            e = self.exp.execute(environment)
            cd += tab + "stack.append(" + e.temp + ")\n"
            cd += tab + "goto .endLabel\n"
            return code.C3D(e.value + cd, "return", self.row, self.column)
        cd = tab + "stack.append(None)\n"
        cd += tab + "goto .endLabel\n"
        return code.C3D(cd, "return", self.row, self.column)

    def dot(self):

        new = Nodo("RETURN")
        new.addNode(self.exp.dot())
        return new