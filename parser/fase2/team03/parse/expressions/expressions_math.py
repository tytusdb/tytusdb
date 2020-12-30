import math
import random
import numpy as np
from parse.ast_node import ASTNode
from parse.errors import Error, ErrorType


# From here on, classes describing various mathematical operations

class Abs(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return abs(exp)
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))


class Cbrt(ASTNode):  
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return np.cbrt(exp)
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))


class Ceil(ASTNode): 
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.ceil(exp)
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))


class Degrees(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.degrees(exp)
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))


class Div(ASTNode):
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
            return exp1 // exp2
        except ZeroDivisionError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ZeroDivisionError: integer division or modulo by zero'))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: Both arguments must be a real number'))


class Exp(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.exp(exp)
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))

class Factorial(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:            
            return math.factorial()
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: only accepts integral positive values'))


class Floor(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.floor(exp)
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))

class Gcd(ASTNode):
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
            return math.gcd(exp1, exp2)
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: Both arguments must be a integral number'))


class Lcm(ASTNode):  # Only available on Python 3.9+, please update your python version
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
            return math.lcm(exp1, exp2)
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: Both arguments must be a integral number'))


class Ln(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.log2(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: math domain error'))
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))



class Log(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.log(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: math domain error'))
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))



class Log10(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.log10(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: math domain error'))
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))

#TODO MINSCALE() function not implemented, only returns the value of the argument
class MinScale(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        if isinstance(exp,int) or isinstance(exp,float):
            return exp
        else:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))

class Mod(ASTNode):
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
            return math.fmod(exp1, exp2)
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: Both arguments must be a number'))


class PI(ASTNode):
    def __init__(self, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return math.pi


class Power(ASTNode):
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
            return math.pow(exp1, exp2)
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: Both arguments must be a real number'))


class Radians(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.radians(exp)
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))
        
        


class Random(ASTNode):  
    def __init__(self, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return random.random()


class Round(ASTNode):
    def __init__(self, exp1, exp2, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp1 = self.exp1.execute(table, tree)
        if self.exp2 != 0:
            exp2 = self.exp2.execute(table, tree)
        #try:
        if self.exp2 == 0:
            return round(exp1)
        else:
            return round(exp1, exp2)            
        #except :
        #    raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: Both arguments must be a real number'))


class Scale(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        r = self.exp.execute(table, tree)
        if isinstance(r, float) or isinstance(r,int):
            if isinstance(r, float):
                arr = r.__str__().split(".")
                if len(arr) == 1:
                    return 0
                else:
                    return len(arr[1])
            else:
                return 0
        else:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(r))))


class SetSeed(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return random.seed(exp)
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: Math domain error'))



class Sign(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            if isinstance(exp, float) or isinstance(exp,int):
                exp = int(np.sign(exp))
                return exp
            else:
                raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError:  must be real number'))
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))


class Sqrt(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.sqrt(exp)
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: only accepts integral positive values'))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))

#TODO TRIMSCALE() function not implemented, only returns the value of the argument
class TrimScale(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        if isinstance(exp,int) or isinstance(exp,float):
            return exp
        else:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))


class Trunc(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp = self.exp.execute(table, tree)
        try:
            return math.trunc(exp)
        except :
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError: must be real number, not '+ str(type(exp))))


#TODO WIDTHBUCKET()function not implemented, only returns the sum of the arguments
class WidthBucket(ASTNode):
    def __init__(self, exp1, exp2, exp3, exp4, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        exp1 = self.exp1.execute(table, tree)
        exp2 = self.exp2.execute(table, tree)
        exp3 = self.exp3.execute(table, tree)
        exp4 = self.exp4.execute(table, tree)

        try:
            if exp3 == exp2: 
                return 0
            else:
                return math.ceil( (exp4 * exp1) / (exp3 - exp2) ) 
        except ValueError:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'ValueError: only accepts integral positive values'))
        except:
            raise(Error(self.line, self.column, ErrorType.SEMANTIC, 'TypeError:all arguments must be integers'))