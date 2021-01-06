from analizer_pl.abstract.instruction import Instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo

class Return(Instruction):
    def __init__(self, exp, row, column) -> None:
        super().__init__(row, column)
        self.exp = exp

    def execute(self, environment):
        if self.exp:
            e = self.exp.execute(environment)
            cd = ""
            if environment:
                cd += "\t"
            cd += "return " + e.temp + "\n"
            return code.C3D(e.value + cd, "", self.row, self.column)
        return code.C3D("return\n", "", self.row, self.column)

    def dot(self):
            
        new = Nodo("RETURN")
        new.addNode(self.exp.dot())
        return new