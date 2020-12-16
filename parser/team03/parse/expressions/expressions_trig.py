import sys
import math
from parse.ast_node import ASTNode


class Acos(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.acos(exp)


         
class Acosd(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.degrees(math.acos(exp))


         
class Asin(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.asin(exp)


         
class Asind(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.degrees(math.asin(exp))


         
class Atan(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.atan(exp)


         
class Atand(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.degrees(math.atan(exp))


         
class Atan2(ASTNode):
    def __init__(self, exp1, exp2, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp1 = self.exp1.execute(table, tree)
        exp2 = self.exp2.execute(table, tree)
        return math.atan2(exp1, exp2)


         
class Atan2d(ASTNode):
    def __init__(self, exp1, exp2, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp1 = self.exp1.execute(table, tree)
        exp2 = self.exp2.execute(table, tree)
        return math.degrees(math.atan2(exp1, exp2))


         
class Cos(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.cos(exp)


         
class Cosd(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.cos(math.radians(exp))


         
class Cot(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return 1/math.tan(exp)


         
class Cotd(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return 1/math.tan(math.radians(exp))


         
class Sin(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.sin(exp)


         
class Sind(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.sin(math.radians(exp))


         
class Tan(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.tan(exp)


         
class Tand(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.tan(math.radians(exp))


         
class Sinh(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.sinh(exp)


         
class Cosh(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.cosh(exp)


         
class Tanh(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.tanh(exp)


         
class Asinh(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.asinh(exp)


         
class Acosh(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.acosh(exp)


         
class Atanh(ASTNode):
    def __init__(self, exp, line, column,id):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.id=id

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        return math.atanh(exp)