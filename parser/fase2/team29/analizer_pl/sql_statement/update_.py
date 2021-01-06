from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class Update(instruction.Instruction):
    def __init__(self, fromcl, values, wherecl, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl
        self.values = values

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "UPDATE "
        out += self.exists + " "
        out += self.name + " ("
        out += self.columns + " )"
        out += self.inherits + ";"
        out += '")\n'
        return code.C3D(out, "update", self.row, self.column)
