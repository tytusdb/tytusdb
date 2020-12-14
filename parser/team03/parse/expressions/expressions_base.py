import sys
from . expression_enum import OpArithmetic, OpRelational, OpLogic, OpPredicate
from datetime import date

##sys.path.insert(0, '..')
##from ast_node import ASTNode
from .. ast_node import ASTNode


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


class Now(ASTNode):
    def __init__(self, line, column):
        ASTNode.__init__(self, line, column)

    def execute(self, table, tree):
        super().execute(table, tree)
        return date.today()


class BinaryExpression(ASTNode):
    # Class that handles every arithmetic expression

    def __init__(self, exp1, exp2, operator, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator

    def execute(self, table, tree):
        super().execute(table, tree)
        print("slef.operator: ",self.operator)
        if self.operator == None: #'Number' or 'artirmetic function' production for example
            return self.exp1.val
        if self.operator == OpArithmetic.PLUS:          
            return self.exp1.execute(None,None) + self.exp2.execute(None,None)
        if self.operator == OpArithmetic.MINUS:                    
            return self.exp1.execute(None,None) - self.exp2.execute(None,None)
        if self.operator == OpArithmetic.TIMES:
            return self.exp1.execute(None,None) * self.exp2.execute(None,None)
        if self.operator == OpArithmetic.DIVIDE:
            return self.exp1.execute(None,None) / self.exp2.execute(None,None)
        #if self.operator == OpArithmetic.MODULE:
        #    return self.exp1.execute(None,None)  self.exp2.execute(None,None)
        if self.operator == OpArithmetic.POWER:
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
        if self.operador == OpRelational.LIKE:  # TODO add execution to [NOT] LIKE, Regex maybe?
            return self.exp1 == self.exp2
        if self.operador == OpRelational.NOT_LIKE:
            return self.exp1 >= self.exp2


class PredicateExpression(ASTNode):
    # Class that handles every logic expression

    def __init__(self, exp1, exp2, operator, line, column):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.operador == OpPredicate.NULL:
            return self.exp1 is None
        if self.operador == OpPredicate.NOT_NULL:
            return self.exp1 is not None
        if self.operador == OpPredicate.DISTINCT:  # Improve logic in order to allow null and 0 to be the same
            return self.exp1 != self.exp2
        if self.operador == OpPredicate.NOT_DISTINCT:  # Improve logic in order to allow null and 0 to be the same
            return self.exp1 != self.exp2
        if self.operador == OpPredicate.TRUE:
            return self.exp1 is True
        if self.operador == OpPredicate.NOT_TRUE:
            return self.exp1 is False
        if self.operador == OpPredicate.FALSE:
            return self.exp1 is False
        if self.operador == OpPredicate.NOT_FALSE:
            return self.exp1 is True
        if self.operador == OpPredicate.UNKNOWN:  # TODO do actual comparison to Unknown... No ideas right now
            return False
        if self.operador == OpPredicate.NOT_UNKNOWN:  # Same as previous comment about Unknown
            return False
