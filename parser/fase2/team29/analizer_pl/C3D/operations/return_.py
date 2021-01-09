from analizer_pl.abstract.instruction import Instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class Return(Instruction):
    def __init__(self, exp, row, column) -> None:
        super().__init__(row, column)
        self.exp = exp

    def execute(self, environment):
        try:
            tab = ""
            cd = ""
            tab1 = False
            if isinstance(environment, Environment):
                tab += "\t"
                tab1 = True
            if self.exp:
                e = self.exp.execute(environment)
                cd += tab + "stack.append(" + e.temp + ")\n"
                grammar.optimizer_.addIgnoreString(
                    str("stack.append(" + e.temp + ")"), self.row, tab1
                )
                cd += tab + "goto .endLabel\n"
                grammar.optimizer_.addGoto(str("endLabel"), self.row, tab1)
                return code.C3D(e.value + cd, "return", self.row, self.column)
            cd = tab + "stack.append(None)\n"
            grammar.optimizer_.addIgnoreString(
                str("stack.append(None)"), self.row, tab1
            )
            cd += tab + "goto .endLabel\n"
            grammar.optimizer_.addGoto(str("endLabel"), self.row, tab1)
            return code.C3D(cd, "return", self.row, self.column)
        except:
            grammar.PL_errors.append(
                "Error P0000: plpgsql fatal error \n Hint---> Return Expresion"
            )

    def dot(self):

        new = Nodo("RETURN")
        new.addNode(self.exp.dot())
        return new
