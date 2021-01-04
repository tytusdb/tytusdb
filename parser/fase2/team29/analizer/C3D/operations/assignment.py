from analizer.abstract.expression import Expression
from analizer.abstract.expression import TYPE
from analizer.statement.expressions import code


class Assignment(Expression):
    def __init__(self, id, value, row, column):
        super().__init__(row, column)
        self.id = id
        self.value = value

    def execute(self, environment):
        exp = self.value.execute(environment)
        self.value = exp.value+ self.id +" = "+ str(exp.temp)
        print(self.value)
        return code.C3D(self.value,self.id,self.row,self.column)

  