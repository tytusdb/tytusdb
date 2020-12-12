import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')

from instruccion import *
from Error import *
from Primitivo import *

class Condicionales(Instruccion):

    def __init__(self, leftOperator, rightOperator, sign, extra):
        self.leftOperator = leftOperator
        self.rightOperator = rightOperator
        self.sign = sign
        self.extra = extra

    def execute(self):
        left = self.leftOperator.execute()
        if isinstance(left, Error) :
            return left
        right = self.rightOperator.execute()
        if isinstance(right, Error) :
            return right

        if self.sign == '>' :
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                comp = int(left.val) > int(right.val)
                return Primitive('boolean', comp)
            else:
                error = Error('Semántico', 'Error de tipos en MAYOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        else :
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                comp = int(left.val) < int(right.val)
                return Primitive('boolean', comp)
            else:
                error = Error('Semántico', 'Error de tipos en MENOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error

    def __repr__(self):
        return str(self.__dict__)

class Between(Instruccion):

    def __init__(self, type, val1, val2):
        self.type = type
        self.val1 = val1
        self.val2 = val2

    def __repr__(self):
        return str(self.__dict__)

class IsNotOptions(Instruccion):

    def __init__(self, notv, val, distinct):
        self.notv = notv
        self.val = val
        self.distinct = distinct

    def execute(self):
        return self.notv

    def __repr__(self):
        return str(self.__dict__)
