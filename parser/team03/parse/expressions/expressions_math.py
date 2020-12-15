import sys
import math
import random
import numpy as np
from parse.ast_node import ASTNode


# From here on, classes describing various mathematical operations
# TODO: minScale, scale, trimScale, widthBucket
class Abs(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return abs(self.exp)


class Cbrt(ASTNode):  # TODO CHECK GRAMMAR, It receives an array and grammar probably doesn't support it
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return np.cbrt(self.exp)


class Ceil(ASTNode):  # Same for ceiling. Only receives float value, check in grammar or semantic error? 
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.ceil(self.exp)


class Degrees(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.degrees(self.exp)


class Div(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.exp1 // self.exp2


class Exp(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.exp(self.exp)


class Factorial(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.factorial(self.exp)


class Floor(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.floor(self.exp)


class Gcd(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.gcd(self.exp1, self.exp2)


class Lcm(ASTNode):  # Only available on Python 3.9+, please update your python version
    def __init__(self, exp1, exp2, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.lcm(self.exp1, self.exp2)


class Ln(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.log2(self.exp)


class Log(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.log(self.exp)

    
class Log10(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.log10(self.exp)


class MinScale(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Mod(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.fmod(self.exp1, self.exp2)


class PI(ASTNode):
    def __init__(self, line, column):
        ASTNode.__init__(self, line, column)

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.pi


class Power(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.pow(self.exp1, self.exp2)


class Radians(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.radians(self.exp)


class Random(ASTNode): # TODO check SQL docs, it has a range or something?
    def __init__(self, line, column):
        ASTNode.__init__(self, line, column)

    def execute(self, table, tree):
        super().execute(table, tree)
        return random.random()


class Round(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return round(self.exp)


class Scale(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class SetSeed(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return random.seed(self.exp)


class Sign(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return np.sign(self.exp)


class Sqrt(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.sqrt(self.exp)


class TrimScale(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Trunc(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.trunc(self.exp)


class WithBucket(ASTNode):
    def __init__(self, exp1, exp2, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, table, tree):
        super().execute(table, tree)
        return True
