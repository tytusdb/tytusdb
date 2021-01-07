from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment


class ShowDataBases(instruction.Instruction):
    def __init__(self, like, row, column):
        instruction.Instruction.__init__(self, row, column)
        if like != None:
            self.like = like[1 : len(like) - 1]
        else:
            self.like = None

    def execute(self, environment):
        out = "fase1.execution("
        out += '"'
        out += "SHOW DATABASES"
        out += self.like + ";"
        out += '")\n'
        if isinstance(environment, Environment):
            out = "\t" + out
        return code.C3D(out, "show_databases", self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_SHOW")