from .expression_enum import OpArithmetic, OpRelational, OpLogic, OpPredicate
from datetime import date, datetime
from parse.errors import Error, ErrorType
from parse.ast_node import ASTNode


class Numeric(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val


class NumericNegative(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val * -1


class Text(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val


class BoolAST(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val


class DateAST(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.graph_ref = graph_ref
        try:
            self.val = datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
        except:
            print("String format not avalible!!!")
            self.val = None

    def execute(self, table, tree):
        super().execute(table, tree)
        return self.val


class ColumnName(ASTNode):
    def __init__(self, tName, cName, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.tName = tName
        self.cName = cName
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        print("TEXT: ", self.tName, ".", self.cName)
        if self.tName is None or self.tName == "":
            return self.cName
        else:
            return self.tName + "." + self.cName  # TODO check if is necesary go to symbol table to get the value or check if the object exists


class Now(ASTNode):
    def __init__(self, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return date.today()


''''class Expression(ASTNode):    
    def __init__(self,exp1,line,column, graph_ref):
        ASTNode.__init__(self,line,column)
        self.exp1 = exp1
    def execute(self, table, tree):
        super().execute(table, tree)
        #TODO: check each value or AST node which can reduce...
'''


class BinaryExpression(ASTNode):
    # Class that handles every arithmetic expression
    def __init__(self, exp1, exp2, operator, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        # TODO: Validate type
        if self.operator is None:  # 'Number' or 'artirmetic function' production for example
            return self.exp1.execute(table, tree)
        if self.operator == OpArithmetic.PLUS:
            return self.exp1.execute(table, tree) + self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.MINUS:
            return self.exp1.execute(table, tree) - self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.TIMES:
            return self.exp1.execute(table, tree) * self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.DIVIDE:
            return self.exp1.execute(table, tree) / self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.MODULE:
            return self.exp1.execute(table, tree) % self.exp2.execute(table, tree)
        if self.operator == OpArithmetic.POWER:
            return pow(self.exp1, self.exp2)


class RelationalExpression(ASTNode):
    # Class that handles every relational expression

    def __init__(self, exp1, exp2, operator, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.operator == OpRelational.GREATER:
            return self.exp1.execute(table, tree) > self.exp2.execute(table, tree)
        if self.operator == OpRelational.LESS:
            return self.exp1.execute(table, tree) < self.exp2.execute(table, tree)
        if self.operator == OpRelational.EQUALS:
            return self.exp1.execute(table, tree) == self.exp2.execute(table, tree)
        if self.operator == OpRelational.NOT_EQUALS:
            return self.exp1.execute(table, tree) != self.exp2.execute(table, tree)
        if self.operator == OpRelational.GREATER_EQUALS:
            return self.exp1.execute(table, tree) >= self.exp2.execute(table, tree)
        if self.operator == OpRelational.LESS_EQUALS:
            return self.exp1.execute(table, tree) <= self.exp2.execute(table, tree)
        if self.operator == OpRelational.LIKE:  # TODO add execution to [NOT] LIKE, Regex maybe?
            return self.exp1.execute(table, tree) == self.exp2.execute(table, tree)
        if self.operator == OpRelational.NOT_LIKE:
            return self.exp1.execute(table, tree) != self.exp2.execute(table, tree)


class PredicateExpression(ASTNode):  # TODO check operations and call to exceute function
    # Class that handles every logic expression

    def __init__(self, exp1, exp2, operator, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.operator == OpPredicate.NULL:
            return self.exp1 is None
        if self.operator == OpPredicate.NOT_NULL:
            return self.exp1 is not None
        if self.operator == OpPredicate.DISTINCT:  # Improve logic in order to allow null and 0 to be the same
            return self.exp1 != self.exp2
        if self.operator == OpPredicate.NOT_DISTINCT:  # Improve logic in order to allow null and 0 to be the same
            return self.exp1 != self.exp2
        if self.operator == OpPredicate.TRUE:
            return self.exp1 is True
        if self.operator == OpPredicate.NOT_TRUE:
            return self.exp1 is False
        if self.operator == OpPredicate.FALSE:
            return self.exp1 is False
        if self.operator == OpPredicate.NOT_FALSE:
            return self.exp1 is True
        if self.operator == OpPredicate.UNKNOWN:  # TODO do actual comparison to Unknown... No ideas right now
            return False
        if self.operator == OpPredicate.NOT_UNKNOWN:  # Same as previous comment about Unknown
            return False
