from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class Truncate(instruction.Instruction):
    def __init__(self, name, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.name = name

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "TRUNCATE "
        out += self.name + ";"
        out += '")\n'
        return code.C3D(out, "truncate_database", self.row, self.column)
