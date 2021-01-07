from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment


class DropTable(instruction.Instruction):
    """"""

    def __init__(self, name, exists, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.name = name
        self.exists = exists

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "DROP "
        out += "TABLE "
        out += self.exists
        out += self.name + ";"
        out += '")\n'
        if isinstance(environment, Environment):
            out = "\t" + out
        return code.C3D(out, "drop_tb", self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_DROP_TABLE")