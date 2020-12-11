import sys
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
