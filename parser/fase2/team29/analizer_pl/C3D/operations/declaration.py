from analizer_pl.abstract.expression import Expression
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code
from analizer_pl.abstract.environment import Environment


class Declaration(Expression):
    def __init__(self, id, type, ass, row, column):
        super().__init__(row, column)
        self.id = id
        self.type = type
        self.ass = ass

    def execute(self, environment: Environment):
        environment.addVar(self.id, self.id, self.type, self.row, self.column)
        val = ""
        tmp = self.id
        if self.ass:
            a = self.ass.execute(environment)
            val = a.value
            tmp = a.temp
        return code.C3D(val, tmp, self.row, self.column)
