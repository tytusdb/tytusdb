from analizer_pl.abstract.expression import Expression
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code


class Assignment(Expression):
    def __init__(self, id, value, row, column):
        super().__init__(row, column)
        self.id = id
        self.value = value

    def execute(self, environment):
        exp = self.value.execute(environment)
        # TODO: Error
        if environment.getVar(self.id) != None:
            self.value = exp.value + self.id + " = " + str(exp.temp) + "\n"
            return code.C3D(self.value, self.id, self.row, self.column)
