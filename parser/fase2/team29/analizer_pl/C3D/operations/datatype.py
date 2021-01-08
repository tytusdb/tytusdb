from analizer_pl.abstract.expression import Expression
from analizer_pl.modules.expressions import C3D
from analizer_pl.C3D.operations import operation
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.global_env import GlobalEnvironment
from analizer_pl import grammar


class Identifier(Expression):
    def __init__(self, id, isBlock, row, column) -> None:
        super().__init__(row, column)
        self.id = id
        self.isBlock = isBlock

    def execute(self, environment):
        if self.isBlock:
            return C3D("", self.id, self.row, self.column)
        if environment.isBlock:
            return C3D("", self.id, self.row, self.column)
        if not isinstance(environment, GlobalEnvironment):
            if environment.getVar(self.id):
                return C3D("", '"+str(' + self.id + ')+"', self.row, self.column)
            else:
                grammar.PL_errors.append("Error P0000: La variable "+self.id+" no esta declarada")
        return C3D("", self.id, self.row, self.column)

    def dot(self):
        nod = Nodo(self.id)
        return nod


class TernaryExpression(Expression):
    def __init__(self, temp, exp1, exp2, exp3, operator, isBlock, row, column):
        super().__init__(row, column)
        self.temp = temp
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.operator = operator
        self.isBlock = isBlock

    def execute(self, environment):
        if self.isBlock:
            op = operation.Ternary(
                self.temp,
                self.exp1,
                self.exp2,
                self.exp3,
                self.operator,
                self.row,
                self.column,
            )
            return op.execute(environment)

        c3d = ""
        val1 = self.exp1.execute(environment)
        c3d += val1.temp
        c3d += " " + operators.get(self.operator, self.operator) + " "
        val2 = self.exp2.execute(environment)
        c3d += val2.temp
        c3d += " AND "
        val3 = self.exp3.execute(environment)
        c3d += val3.temp
        return C3D(val1.value + val2.value + val3.value, c3d, self.row, self.column)

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        n3 = self.exp3.dot()
        new = Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        new.addNode(n3)
        return new

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

        space = ""
        if self.operator == "AND" or self.operator == "OR":
            space = " "
        c3d = ""
        val1 = self.exp1.execute(environment)
        c3d += val1.temp
        c3d += space + self.operator + space
        val2 = self.exp2.execute(environment)
        c3d += val2.temp
        return C3D(val1.value + val2.value, c3d, self.row, self.column)

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

        val = self.exp.execute(environment)
        if self.operator == "-" or self.operator == "+" or self.operator == "NOT":
            c3d = self.operator
            c3d += val.temp
        else:
            c3d = val.temp
            c3d += operators.get(self.operator, self.operator)

        return C3D(val.value, c3d, self.row, self.column)

    def dot(self):
        n = self.exp.dot()
        new = Nodo(self.operator)
        new.addNode(n)
        return new


class Aggrupation(Expression):
    def __init__(self, exp, isBlock, row, column):
        super().__init__(row, column)
        self.exp = exp
        self.isBlock = isBlock

    def execute(self, environment):
        val = self.exp.execute(environment)
        if self.isBlock:
            return val
        c3d = "(" + val.temp + ")"
        return C3D(val.value, c3d, self.row, self.column)

    def dot(self):
        n = self.exp.dot()
        return n


operators = {
    "ISNULL": " IS NULL ",
    "ISTRUE": " IS TRUE ",
    "ISFALSE": " IS FALSE ",
    "ISUNKNOWN": " IS UNKNOWN ",
    "ISNOTNULL": " IS NOT NULL ",
    "ISNOTTRUE": " IS NOT TRUE ",
    "ISNOTFALSE": " IS NOT FALSE ",
    "ISNOTUNKNOWN": " IS NOT UNKNOWN ",
    "NOTBETWEEN": "NOT BETWEEN",
    "BETWEENSYMMETRIC": "BETWEEN SYMMETRIC",
}
