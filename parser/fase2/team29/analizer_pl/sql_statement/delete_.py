from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo

class Delete(instruction.Instruction):
    def __init__(self, fromcl, wherecl, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "DELETE "
        out += self.exists + " "
        out += self.name + " ("
        out += self.columns + " )"
        out += self.inherits + ";"
        out += '")\n'
        return code.C3D(out, "delete", self.row, self.column)
    def dot(self):
        return Nodo("SQL_INSTRUCTION:_DELETE")