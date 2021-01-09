from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class ShowDataBases(instruction.Instruction):
    def __init__(self, like, row, column):
        instruction.Instruction.__init__(self, row, column)
        if like != None:
            self.like = like[1 : len(like) - 1]
        else:
            self.like = None

    def execute(self, environment):
        try:
            out = "fase1.execution("
            out += '"'
            out += "SHOW DATABASES"
            out += self.like + ";"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "show_databases", self.row, self.column)
        except:
            grammar.PL_errors.append(
                "Error P0000: plpgsql fatal error \n Hint---> Show"
            )

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SHOW")