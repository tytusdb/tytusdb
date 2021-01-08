from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class AlterTable(instruction.Instruction):
    def __init__(self, table, row, column, params=[]):
        instruction.Instruction.__init__(self, row, column)
        self.table = table
        self.params = params

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "ALTER "
            out += "TABLE "
            out += self.table + " "
            out += self.params
            out += ";"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "alter_db", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Alter Table")

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_ALTER_TABLE")
