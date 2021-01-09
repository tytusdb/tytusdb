from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class DropTable(instruction.Instruction):
    """"""

    def __init__(self, name, exists, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.name = name
        self.exists = exists

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "DROP "
            out += "TABLE "
            out += self.exists
            out += self.name + ";"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "drop_tb", self.row, self.column)
        except:
            grammar.PL_errors.append(
                "Error P0000: plpgsql fatal error \n Hint---> Drop Table"
            )

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_DROP_TABLE")