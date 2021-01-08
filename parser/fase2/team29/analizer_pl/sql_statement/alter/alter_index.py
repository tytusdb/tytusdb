from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar
from analizer_pl.reports.Nodo import Nodo


class AlterIndex(instruction.Instruction):
    def __init__(self, exists, idIndex, columnIndex, row, column, idOrNumber):
        super().__init__(row, column)
        self.exists = exists
        self.idIndex = idIndex
        self.columnIndex = columnIndex
        self.idOrNumber = idOrNumber

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "ALTER INDEX "
            out += self.exists + " "
            out += self.idIndex + " "
            if self.idOrNumber == "":
                out += "RENAME TO "
            else:
                out += "ALTER "
            out += self.columnIndex + " "
            out += str(self.idOrNumber) + " ;"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "alter_index", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Alter Index")
    def dot(self):
        return Nodo("SQL_INSTRUCTION:_ALTER_INDEX")
