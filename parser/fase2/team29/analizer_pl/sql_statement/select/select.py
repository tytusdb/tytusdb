from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class SelectParam(instruction.Instruction):
    def __init__(self, exp, alias, row, column) -> None:
        super().__init__(row, column)
        self.exp = exp
        self.alias = alias

    def execute(self, environment):
        pval = self.exp.execute(environment)
        c3d = pval.temp
        if self.alias != "":
            c3d += self.alias
        return code.C3D(pval.value, c3d, self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SELECT")

class SelectOnlyParams(instruction.Instruction):
    def __init__(self, params, row, column) -> None:
        super().__init__(row, column)
        self.params = params

    def execute(self, environment):
        parVal = ""
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "SELECT "
        j = 0
        for i in range(len(self.params) - 1):
            j = i + 1
            pval = self.params[i].execute(environment)
            parVal += pval.value
            out += pval.temp + ", "
        pval = self.params[j].execute(environment)
        parVal += pval.value
        out += pval.temp
        out += ";"
        out += '")\n'
        if isinstance(environment, Environment):
            grammar.optimizer_.addIgnoreString(out, self.row, True)
            out = "\t" + out
        else:
            grammar.optimizer_.addIgnoreString(out, self.row, False)
        return code.C3D(parVal + out, "select", self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SELECT")

class Select(instruction.Instruction):
    def __init__(
        self,
        distinct,
        params,
        fromcl,
        wherecl,
        groupbyCl,
        limitCl,
        orderByCl,
        row,
        column,
    ):
        instruction.Instruction.__init__(self, row, column)
        self.distinct = distinct
        self.params = params
        self.orderByCl = orderByCl
        self.fromcl = fromcl
        self.wherecl = wherecl
        self.groupbyCl = groupbyCl
        self.limitCl = limitCl

    def execute(self, environment):
        parVal = ""
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "SELECT "
        out += self.distinct + " "
        # SelectParams
        j = 0
        for i in range(len(self.params) - 1):
            j = i + 1
            pval = self.params[i].execute(environment)
            parVal += pval.value
            out += pval.temp + ", "
        pval = self.params[j].execute(environment)
        parVal += pval.value
        out += pval.temp
        # From
        out += " " + self.fromcl + " "
        # where
        pval = self.wherecl.execute(environment)
        if pval.temp != "":
            out += "WHERE " + pval.temp + " "
        parVal += pval.value
        # group by
        if self.groupbyCl:
            groupbyCl = ""
            for g in self.groupbyCl[0]:
                groupbyCl += ", "
                if type(g) == int:
                    groupbyCl += str(g)
                else:
                    groupbyCl += g.id

            out += "GROUP BY " + groupbyCl[2:] + self.groupbyCl[1] + " "
        # limit
        out += self.limitCl + " "
        # order by
        if self.orderByCl:
            orderbyCl = ""
            for o in self.orderByCl:
                orderbyCl += ", "
                if type(o[0]) == int:
                    orderbyCl += str(o[0]) + o[1] + o[2]
                else:
                    orderbyCl += o[0].id + o[1] + o[2]
            out += "ORDER BY " + orderbyCl[2:]
        out = out.rstrip() + ";"
        out += '")\n'
        # TODO: optimizacion
        if isinstance(environment, Environment):
            grammar.optimizer_.addIgnoreString(out, self.row, True)
            out = "\t" + out
        else:
            grammar.optimizer_.addIgnoreString(out, self.row, False)
        return code.C3D(parVal + out, "select", self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SELECT")
