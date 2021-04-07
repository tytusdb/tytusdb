from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code
from analizer_pl.abstract.environment import Environment
from analizer_pl.reports.Nodo import Nodo
from analizer_pl import grammar


class Declaration(Instruction):
    def __init__(self, id, type, ass, row, column):
        super().__init__(row, column)
        self.id = id
        self.type = type
        self.ass = ass

    def execute(self, environment: Environment):
        try:
            environment.addVar(self.id, self.id, self.type, self.row, self.column)
            val = ""
            tmp = self.id
            if self.ass:
                a = self.ass.execute(environment)
                val = a.value
                tmp = a.temp
            else:
                val = "\t" + self.id + " = None\n"
            return code.C3D(val, tmp, self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error ")

    def dot(self):
        new = Nodo("DECLARATION")
        typ = Nodo(str(self.type))

        new.addNode(typ)
        if self.ass:
            new.addNode(self.ass.dot())
        else:
            n1 = Nodo(str(self.id))
            new.addNode(n1)
        # ast.makeAst(new)
        return new