from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class Select(instruction.Instruction):
    def __init__(
        self,
        params,
        fromcl,
        wherecl,
        groupbyCl,
        havingCl,
        limitCl,
        orderByCl,
        distinct,
        row,
        column,
    ):
        instruction.Instruction.__init__(self, row, column)
        self.params = params
        self.wherecl = wherecl
        self.fromcl = fromcl
        self.groupbyCl = groupbyCl
        self.havingCl = havingCl
        self.limitCl = limitCl
        self.orderByCl = orderByCl
        self.distinct = distinct

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "SELECT "
        out += self.exists + " "
        out += self.name + " ("
        out += self.columns + " )"
        out += self.inherits + ";"
        out += '")\n'
        return code.C3D(out, "select", self.row, self.column)
