import sys
import math

from parse.ast_node import ASTNode


# From here on, classes describing various trigonometric operations
# TODO: acosd, asind, atand, atand2, cosd, sind, tand
class Acos(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.acos(self.exp)


class Acosh(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.acosh(self.exp)


class Atan(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.atan(self.exp)


class Atan2(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.atan2(self.exp1, self.exp2)


class Atanh(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.atanh(self.exp)


class Cos(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.cos(self.exp)


class Cosh(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.cosh(self.exp)


class Cot(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return 1 / math.tan(self.exp)


class Sin(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.sin(self.exp)


class Sinh(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.sinh(self.exp)


class Tan(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.tan(self.exp)


class Tanh(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.tanh(self.exp)
