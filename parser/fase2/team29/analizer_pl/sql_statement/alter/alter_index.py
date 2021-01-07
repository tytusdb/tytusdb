from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class AlterIndex(instruction.Instruction):
    def __init__(self, exists, idIndex, columnIndex, row, column, idOrNumber):
        super().__init__(row, column)
        self.exists = exists
        self.idIndex = idIndex
        self.columnIndex = columnIndex
        self.idOrNumber = idOrNumber

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "ALTER INDEX "
        out += self.exists + " "
        out += self.idIndex + " "
        if self.idOrNumber == "":
            out += "RENAME TO "
        else:
            out += "ALTER "
        out += self.columnIndex + " "
        out += str(self.idOrNumber) + " ;"
        out += '")\n'
        return code.C3D(out, "alter_index", self.row, self.column)
