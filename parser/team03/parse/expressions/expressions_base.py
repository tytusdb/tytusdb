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


class NumericPositive(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        self.val = self.val.execute(table, tree)
        print(type(self.val))
        if(type(self.val) == int or type(self.val) == float):
            return self.val * 1
        else:
            raise Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be number')
        


class NumericNegative(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        self.val = self.val.execute(table, tree)
        if(type(self.val) == int or type(self.val) == float):
            return self.val * -1
        else:
            raise Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be number')
        


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
        self.val = (str(val).upper() == "TRUE")
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
            return self.exp1.execute(table, tree) is None
        if self.operator == OpPredicate.NOT_NULL:
            return self.exp1.execute(table, tree) is not None
        if self.operator == OpPredicate.DISTINCT:  # Improve logic in order to allow null and 0 to be the same
            return self.exp1.execute(table, tree) != self.exp2.execute(table, tree)
        if self.operator == OpPredicate.NOT_DISTINCT:  # Improve logic in order to allow null and 0 to be the same
            return self.exp1.execute(table, tree) == self.exp2.execute(table, tree)
        if self.operator == OpPredicate.TRUE:
            return self.exp1.execute(table, tree) is True
        if self.operator == OpPredicate.NOT_TRUE:
            return self.exp1.execute(table, tree) is False
        if self.operator == OpPredicate.FALSE:
            return self.exp1.execute(table, tree) is False
        if self.operator == OpPredicate.NOT_FALSE:
            return self.exp1.execute(table, tree) is True
        if self.operator == OpPredicate.UNKNOWN:  # TODO do actual comparison to Unknown... No ideas right now
            return False
        if self.operator == OpPredicate.NOT_UNKNOWN:  # Same as previous comment about Unknown
            return False


class BoolExpression(ASTNode):
    def __init__(self, exp1, exp2, operator, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.graph_ref = graph_ref
    def execute(self, table, tree):
        super().execute(table, tree)
        exec1 = self.exp1.execute(table, tree)
        exec2 = self.exp2.execute(table, tree)

        if isinstance(exec1,bool) and isinstance(exec2,bool):
            if self.operator == OpLogic.AND:
                return exec1 and exec2
            if self.operator == OpLogic.OR:
                return exec1 or exec2
        else:
            raise Exception("The result of operation isn't boolean value")
        

class Negation(ASTNode):
    def __init__(self, exp1, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1        
        self.graph_ref = graph_ref
    def execute(self, table, tree):
        super().execute(table, tree)
        exec1 = self.exp1.execute(table, tree)
        
        if isinstance(exec1,bool):          
            return not exec1
        else:
            raise Exception("The result of operation isn't boolean value")
        

class Identifier(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val
        self.graph_ref = graph_ref

    #Must return lexeme of ID
    def execute(self, table, tree): 
        super().execute(table, tree)
        return self.val

    def executeSTVal(self, table, tree): #TODO: Symbol value from ST :S
        super().execute(table, tree)
        return self.val


class TypeDef(ASTNode):
    def __init__(self, val, min_size, max_size, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val #token name: CHAR, INTEGER,...
        self.min_size = min_size,
        self.max_size = max_size,
        self.graph_ref = graph_ref

    #Must return lexeme of ID
    def execute(self, table, tree): 
        super().execute(table, tree)
        return self.val

    def minSize(self, table, tree): 
        super().execute(table, tree)
        return self.min_size
    
    def maxSize(self, table, tree): 
        super().execute(table, tree)
        return self.max_size


class Nullable(ASTNode):
    def __init__(self, val, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.val = val #True: accept null values other wise False
        self.graph_ref = graph_ref
    
    def execute(self, table, tree): 
        super().execute(table, tree)
        return self.val

    
