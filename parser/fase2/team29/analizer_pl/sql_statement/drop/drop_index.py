from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.abstract.environment import Environment


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
        if isinstance(environment, Environment):
            out = "\t" + out
        return code.C3D(out, "drop_index", self.row, self.column)
