from analizer_pl.abstract.expression import Expression
from analizer_pl.modules.expressions import C3D
from analizer_pl.C3D.operations import operation
from analizer_pl.reports.Nodo import Nodo


class Identifier(Expression):
    def __init__(self, id, isBlock, row, column) -> None:
        super().__init__(row, column)
        self.id = id
        self.isBlock = isBlock

    def execute(self, environment):
        if self.isBlock:
            return C3D("", self.id, self.row, self.column)
        if environment.getVar(self.id):
            return C3D("", '"' + self.id + '"', self.row, self.column)
        return C3D("", self.id, self.row, self.column)

    def dot(self):
        nod = Nodo(self.id)
        return nod


class BinaryExpression(Expression):
    def __init__(self, temp, exp1, exp2, operator, isBlock, row, column):
        super().__init__(row, column)
        self.temp = temp
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.isBlock = isBlock

    def execute(self, environment):
        if self.isBlock:
            op = operation.Binary(
                self.temp, self.exp1, self.exp2, self.operator, self.row, self.column
            )
            return op.execute(environment)

        c3d = self.exp1.execute(environment).temp
        c3d += self.operator.execute(environment).temp
        c3d += self.exp2.execute(environment).temp
        return C3D("", c3d, self.row, self.column)

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        new = Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        return new


class UnaryExpression(Expression):
    def __init__(self, temp, exp, operator, isBlock, row, column):
        super().__init__(row, column)
        self.temp = temp
        self.exp = exp
        self.operator = operator
        self.isBlock = isBlock

    def execute(self, environment):
        if self.isBlock:
            op = operation.Unary(
                self.temp, self.exp, self.operator, self.row, self.column
            )
            return op.execute(environment)

        c3d = self.operator.execute(environment).temp
        c3d = self.exp.execute(environment).temp
        return C3D("", c3d, self.row, self.column)

    def dot(self):
        n = self.exp.dot()
        new = Nodo(self.operator)
        new.addNode(n)
        return new
