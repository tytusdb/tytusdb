from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class CreateTable(instruction.Instruction):
    def __init__(self, exists, name, inherits, row, column, columns=""):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.columns = columns
        self.inherits = inherits

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "CREATE "
            out += "TABLE "
            out += self.exists + " "
            out += self.name + " ("
            out += self.columns + " )"
            out += self.inherits + ";"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "create_tb", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Create Table")

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_CREATE_TABLE")