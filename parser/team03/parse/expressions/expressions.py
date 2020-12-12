import sys
import math
import random
import numpy as np
from expression_enum import *

sys.path.insert(0, '..')
from ast_node import ASTNode


class BinaryExpression(ASTNode):
    # Class that handles every expression with two components, like add, times, module and so on

    def __init__(self, exp1, exp2, operator, line, column):
        super().__init__(line, column)
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


# From here on, classes describing various mathematical operations
# PENDING: div, minScale, scale, trimScale, widthBucket
class Abs(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return abs(self.exp)


class Cbrt(ASTNode):  # TODO CHECK GRAMMAR, It receives an array and grammar probably doesn't support it
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return np.cbrt(self.exp)


class Ceil(ASTNode):  # Same for ceiling. Only receives float value, check in grammar or semantic error? 
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.ceil(self.exp)


class Degrees(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.degrees(self.exp)

    
class Factorial(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.factorial(self.exp)


class Floor(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.floor(self.exp)


class Gcd(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        super().__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.gcd(self.exp1, self.exp2)


class Lcm(ASTNode):  # Only available on Python 3.9+, please update your python version
    def __init__(self, exp1, exp2, line, column):
        super().__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.lcm(self.exp1, self.exp2)


class Ln(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.log2(self.exp)


class Log(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.log(self.exp)

    
class Log10(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.log10(self.exp)


class Mod(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        super().__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.fmod(self.exp1, self.exp2)


class PI(ASTNode):
    def __init__(self, line, column):
        super().__init__(self, line, column)

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.pi


class Power(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        super().__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.pow(self.exp1, self.exp2)


class Radians(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.radians(self.exp)


class Random(ASTNode): # TODO check SQL docs, it has a range or something?
    def __init__(self, line, column):
        super().__init__(self, line, column)

    def execute(self, table, tree):
        super().execute(table, tree)
        return random.random()


class Round(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return round(self.exp)


class SetSeed(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return random.seed(self.exp)


class Sign(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return np.sign(self.exp)


class Sqrt(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.sqrt(self.exp)


class Trunc(ASTNode):
    def __init__(self, exp, line, column):
        super().__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.trunc(self.exp)
