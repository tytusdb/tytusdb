import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')

from instruccion import *
from Error import *
from Primitivo import *

class Arithmetic(Instruccion):

    def __init__(self, leftOperator, rightOperator, sign):
        self.leftOperator = leftOperator
        self.rightOperator = rightOperator
        self.sign = sign

    def execute(self):
        left = self.leftOperator.execute()
        if isinstance(left, Error) :
            return left
        right = self.rightOperator.execute()
        if isinstance(right, Error) :
            return right

        print(self.sign)

        if self.sign == '+' :
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                res = int(left.val) + int(right.val)
                if isinstance(res, float) : return Primitive('float', res)
                else : return Primitive('integer', res)
            else:
                error = Error('Semántico', 'Error de tipos en MAS, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '-' :
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                res = int(left.val) - int(right.val)
                if isinstance(res, float) : return Primitive('float', res)
                else : return Primitive('integer', res)
            else:
                error = Error('Semántico', 'Error de tipos en MENOS, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '*' :
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                res = int(left.val) * int(right.val)
                if isinstance(res, float) : return Primitive('float', res)
                else : return Primitive('integer', res)
            else:
                error = Error('Semántico', 'Error de tipos en MULTIPLICACION, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '/' :
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                if int(right.val) == 0 :
                    error = Error('Semántico', 'No es posible la division con 0', 0, 0)
                    return error
                res = int(left.val) / int(right.val)
                print(res)
                if isinstance(res, float) : return Primitive('float', res)
                else : return Primitive('integer', res)
            else:
                error = Error('Semántico', 'Error de tipos en DIVISION, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '%' :
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                res = int(left.val) % int(right.val)
                if isinstance(res, float) : return Primitive('float', res)
                else : return Primitive('integer', res)
            else:
                error = Error('Semántico', 'Error de tipos en MODULO, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '^' :
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                res = int(left.val) ** int(right.val)
                if isinstance(res, float) : return Primitive('float', res)
                else : return Primitive('integer', res)
            else:
                error = Error('Semántico', 'Error de tipos en POTENCIA, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
                
    def __repr__(self):
        return str(self.__dict__)
