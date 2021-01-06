from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


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
        return code.C3D(out, "drop_tb", self.row, self.column)
