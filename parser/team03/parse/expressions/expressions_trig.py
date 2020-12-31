import math
from parse.ast_node import ASTNode
from parse.errors import Error, ErrorType


class Acos(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.acos(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ACOS() function argument error'))

class Acosd(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.degrees(math.acos(exp))
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ACOSD() function argument error'))


class Asin(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.asin(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ASIN() function argument error'))

class Asind(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.degrees(math.asin(exp))
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ASIND() function argument error'))


class Atan(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.atan(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ATAN() function argument error'))

class Atand(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.degrees(math.atan(exp))
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ATAND() function argument error'))


class Atan2(ASTNode):
    def __init__(self, exp1, exp2, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp1 = self.exp1.execute(table, tree)
        exp2 = self.exp2.execute(table, tree)
        try:
            return math.atan2(exp1, exp2)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: Both arguments must be a real number'))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ATAN2() function argument error'))


class Atan2d(ASTNode):
    def __init__(self, exp1, exp2, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp1 = self.exp1.execute(table, tree)
        exp2 = self.exp2.execute(table, tree)
        try:
            return math.degrees(math.atan2(exp1, exp2))
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: Both arguments must be a real number'))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ATAN2D() function argument error'))


class Cos(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.cos(exp)

        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'COS() function argument error'))
class Cosd(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.cos(math.radians(exp))
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'COSD() function argument error'))


class Cot(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return 1 / math.tan(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error.'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'Infinity: cotangent of zero doesn’t exist'))

class Cotd(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return 1 / math.tan(math.radians(exp))
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'Infinity: cotangent of zero doesn’t exist'))


class Sin(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.sin(exp)

        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'SIN() function argument error'))
class Sind(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.sin(math.radians(exp))
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'SIND() function argument error'))


class Tan(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.tan(exp)

        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TAN() function argument error'))
class Tand(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.tan(math.radians(exp))
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TAND() function argument error'))


class Sinh(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.sinh(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'SINH() function argument error'))

class Cosh(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.cosh(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'COSH() function argument error'))

class Tanh(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.tanh(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TANH() function argument error'))

class Asinh(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.asinh(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error.'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ASINH() function argument error'))


class Acosh(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.acosh(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error.'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ACOSH() function argument error'))


class Atanh(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.atanh(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error.'))
        except TypeError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ATANH function argument error'))
