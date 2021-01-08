from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar

class Select(instruction.Instruction):
    def __init__(self, distinct, params,fromcl, wherecl, groupbyCl, limitCl, orderByCl, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.distinct = distinct
        self.params = params
        self.orderByCl = orderByCl
        self.fromcl = fromcl
        self.wherecl = wherecl
        self.groupbyCl = groupbyCl
        self.limitCl = limitCl


    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "SELECT "
        out += self.distinct + " "
        out += self.params + " "
        out += self.fromcl + " "
        out += self.wherecl + " "
        if self.groupbyCl:
            groupbyCl = ""
            for g in self.groupbyCl[0]:
                groupbyCl += ", "
                if type(g) == int:
                    groupbyCl += str(g)
                else:
                    groupbyCl += g.id

            out += "GROUP BY " + groupbyCl[2:] + self.groupbyCl[1] + " "
        out += self.limitCl + " "
        out += self.orderByCl + " ;"
        out += '")\n'

        if isinstance(environment, Environment):
            grammar.optimizer_.addIgnoreString(out, self.row, True)
            out = "\t" + out
        else:
            grammar.optimizer_.addIgnoreString(out, self.row, False)

        return code.C3D(out, "select", self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SELECT")