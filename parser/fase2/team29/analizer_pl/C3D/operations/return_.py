from analizer_pl.abstract.expression import Expression
from analizer_pl.statement.expressions import code


class Return(Expression):
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
