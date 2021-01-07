from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo

class CreateType(instruction.Instruction):
    def __init__(self, exists, name, row, column, values):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.values = values

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "CREATE "
        out += "TYPE "
        out += self.exists + " "
        out += self.name + " AS ENUM ("
        out += self.values + ");"
        out += '")\n'
        return code.C3D(out, "create_type", self.row, self.column)
    def dot(self):
        return Nodo("SQL_INSTRUCTION:_CREATE_TYPE")