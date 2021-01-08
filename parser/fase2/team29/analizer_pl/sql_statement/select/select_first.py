from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class SelectOnlyParamsFirst(instruction.Instruction):
    def __init__(self, temp, select) -> None:
        super().__init__(select.row, select.column)
        self.params = select.params
        self.temp = "t" + temp

    def execute(self, environment):
        parVal = ""
        out = self.temp + " = "
        out += "fase1.selectFirstValue(dbtemp + "
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
            out = "\t" + out
        return code.C3D(parVal + out, self.temp, self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SELECT")

class SelectFirstValue(instruction.Instruction):
    def __init__(self, temp, select):
        instruction.Instruction.__init__(self, select.row, select.column)
        self.distinct = select.distinct
        self.params = select.params
        self.orderByCl = select.orderByCl
        self.fromcl = select.fromcl
        self.wherecl = select.wherecl
        self.groupbyCl = select.groupbyCl
        self.limitCl = select.limitCl
        self.temp = "t" + temp

    def execute(self, environment):
        parVal = ""
        out = self.temp + " = "
        out += "fase1.selectFirstValue(dbtemp + "
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

        out += ";"
        out += '")\n'

        # TODO: optimizacion
        if isinstance(environment, Environment):
            grammar.optimizer_.addIgnoreString(out, self.row, True)
            out = "\t" + out
        else:
            grammar.optimizer_.addIgnoreString(out, self.row, False)
        return code.C3D(parVal + out, self.temp, self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SELECT")
