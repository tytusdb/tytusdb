import sys
from expression_enum import OpArithmetic, OpRelational

sys.path.insert(0, '..')
from ast_node import ASTNode


class Numeric(ASTNode):
    def __init__(self, val, line, column):
        ASTNode.__init__(self, line, column)
        self.val = val

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val


class NumericNegative(ASTNode):
    def __init__(self, val, line, column):
        ASTNode.__init__(self, line, column)
        self.val = val

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val * -1


class Text(ASTNode):
    def __init__(self, val, line, column):
        ASTNode.__init__(self, line, column)
        self.val = val

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val


class BinaryExpression(ASTNode):
    # Class that handles every arithmetic expression

    def __init__(self, exp1, exp2, operator, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.operador == OpArithmetic.PLUS:
            return self.exp1 + self.exp2
        if self.operador == OpArithmetic.MINUS:
            return self.exp1 - self.exp2
        if self.operador == OpArithmetic.TIMES:
            return self.exp1 * self.exp2
        if self.operador == OpArithmetic.DIVIDE:
            return self.exp1 / self.exp2
        if self.operador == OpArithmetic.MODULE:
            return self.exp1 % self.exp2
        if self.operador == OpArithmetic.POWER:
            return pow(self.exp1, self.exp2)


class RelationalExpression(ASTNode):
    # Class that handles every relational expression

    def __init__(self, exp1, exp2, operator, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.operador == OpRelational.GREATER:
            return self.exp1 > self.exp2
        if self.operador == OpRelational.LESS:
            return self.exp1 < self.exp2
        if self.operador == OpRelational.EQUALS:
            return self.exp1 == self.exp2
        if self.operador == OpRelational.NOT_EQUALS:
            return self.exp1 != self.exp2
        if self.operador == OpRelational.GREATER_EQUALS:
            return self.exp1 >= self.exp2
        if self.operador == OpRelational.LESS_EQUALS:
            return self.exp1 <= self.exp2
        if self.operador == OpRelational.LIKE: # TODO add execution to [NOT] LIKE, Regex maybe?
            return self.exp1 == self.exp2
        if self.operador == OpRelational.NOT_LIKE:
            return self.exp1 >= self.exp2