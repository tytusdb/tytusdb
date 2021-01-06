from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class CreateTable(instruction.Instruction):
    def __init__(self, exists, name, inherits, row, column, columns=""):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.columns = columns
        self.inherits = inherits

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "CREATE "
        out += "TABLE "
        out += self.exists + " "
        out += self.name + " ("
        out += self.columns + " )"
        out += self.inherits + ";"
        out += '")\n'
        return code.C3D(out, "create_tb", self.row, self.column)
