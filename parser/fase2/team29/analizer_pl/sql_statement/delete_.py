from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class Delete(instruction.Instruction):
    def __init__(self, fromcl, wherecl, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "DELETE "
            out += self.fromcl + " "
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
            return code.C3D(parVal + out, "delete", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: Plpgsql Fatal Error -> Hint Delete")

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_DELETE")