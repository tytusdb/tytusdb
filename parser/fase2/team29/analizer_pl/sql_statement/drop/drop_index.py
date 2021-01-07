from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class DropIndex(instruction.Instruction):
    def __init__(self, exists, idList, row, column):
        super().__init__(row, column)
        self.exists = exists
        self.idList = idList

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "DROP INDEX "
        out += self.exists + " "
        out += self.idList + ";"
        out += '")\n'
        return code.C3D(out, "drop_index", self.row, self.column)
