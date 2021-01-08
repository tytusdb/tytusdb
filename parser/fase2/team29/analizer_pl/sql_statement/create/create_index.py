from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class CreateIndex(instruction.Instruction):
    def __init__(
        self, unique, idIndex, idTable, usingMethod, whereCl, row, column, optList
    ):
        super().__init__(row, column)
        self.unique = unique
        self.idIndex = idIndex
        self.idTable = idTable
        self.optList = optList
        self.whereCl = whereCl
        self.usingMethod = usingMethod

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "CREATE "
            out += self.unique + " "
            out += "INDEX "
            out += self.idIndex + " "
            out += "ON "
            out += self.idTable
            out += self.usingMethod + " ("
            out += self.optList + ")"
            out += self.whereCl + ";"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "create_index", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Create Index")
    def dot(self):
        return Nodo("SQL_INSTRUCTION:_CREATE_INDEX")