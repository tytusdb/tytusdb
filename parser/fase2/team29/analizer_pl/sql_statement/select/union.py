from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class Select(instruction.Instruction):
    def __init__(self, type_, select1, select2, all, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.type = type_
        self.select1 = select1
        self.select2 = select2
        self.all = all

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            select1 = self.select1.execute(environment).value.strip()
            select1 = select1[27 : len(select1) - 3]
            select2 = self.select2.execute(environment).value.strip()
            select2 = select2[27 : len(select2) - 3]
            select1
            out += '" (' + select1.strip() + ") "
            out += self.type + " "
            out += self.all + " "
            out += "(" + select2.strip() + ");"
            out += '")\n'

            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "select", self.row, self.column)
        except:
            grammar.PL_errors.append(
                "Error P0000: plpgsql fatal error \n Hint---> Union"
            )

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SELECT")