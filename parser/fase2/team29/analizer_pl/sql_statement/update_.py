from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class Update(instruction.Instruction):
    def __init__(self, fromcl, values, wherecl, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl
        self.values = values

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "UPDATE "
            out += self.fromcl + " SET "
            i = 0
            # values
            for id, value in self.values:
                value = value.execute(environment)
                t = id + " = " + value.temp
                out += t
                if i < len(self.values) - 1:
                    out += ", "
                else:
                    out += " "
                i += 1
            # where
            pval = self.wherecl.execute(environment)
            if pval.temp != "":
                out += "WHERE " + pval.temp + " "
            parVal = pval.value
            out = out.rstrip() + ';")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(parVal + out, "update", self.row, self.column)
        except:
            grammar.PL_errors.append(
                "Error P0000: Plpgsql Fatal error \n Hint---> Update"
            )

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_UPDATE")