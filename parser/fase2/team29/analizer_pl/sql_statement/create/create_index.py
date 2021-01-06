from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class CreateIndex(instruction.Instruction):
    def __init__(
        self, unique, idIndex, idTable, usingMethod, whereCl, row, column, optList
    ):
        super().__init__(row, column)
        self.unique = unique
        self.idIndex = idIndex
        self.idTable = idTable
        self.optList = optList
        self.whereCl = whereCl
        self.usingMethod = usingMethod

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "CREATE "
        out += self.unique + " "
        out += "INDEX "
        out += self.idIndex + " "
        out += "ON "
        out += self.idTable
        out += self.usingMethod + " ("
        out += self.optList + ")"
        out += self.whereCl + ";"
        out += '")\n'
        return code.C3D(out, "create_index", self.row, self.column)
