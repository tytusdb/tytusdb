from analizer_pl.abstract.instruction import Instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl.C3D.operations.func_call import FunctionCall
from analizer_pl import grammar


class Execute(Instruction):
    def __init__(self, procedures, row, column) -> None:
        super().__init__(row, column)
        self.procedures = procedures

    def execute(self, environment):
        try:
            cd = "\n"
            p = self.procedures
            temp = p.execute(environment).value
            cd += temp
            cd += "\n"
            grammar.optimizer_.addIgnoreString(str(temp), self.row, False)
            return code.C3D(cd, "execute", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Execute Function")

    def dot(self):
        new = Nodo("EXECUTE")
        new.addNode(self.procedures.dot())
        return new