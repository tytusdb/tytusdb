from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class CreateType(instruction.Instruction):
    def __init__(self, exists, name, row, column, values):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.values = values

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "CREATE "
            out += "TYPE "
            out += self.exists + " "
            out += self.name + " AS ENUM ("

            j = 0
            for i in range(len(self.values) - 1):
                j = i + 1
                pval = self.values[i].execute(environment)
                out += pval.temp + ", "
            pval = self.values[j].execute(environment)
            out += pval.temp
            out += ");"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "create_type", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Create Type")

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_CREATE_TYPE")