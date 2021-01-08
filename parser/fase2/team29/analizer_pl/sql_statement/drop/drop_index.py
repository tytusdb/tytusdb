from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar
from analizer_pl.reports.Nodo import Nodo


class DropIndex(instruction.Instruction):
    def __init__(self, exists, idList, row, column):
        super().__init__(row, column)
        self.exists = exists
        self.idList = idList

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "DROP INDEX "
            out += self.exists + " "
            out += self.idList + ";"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "drop_index", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Drop Index")

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_DROP_INDEX")