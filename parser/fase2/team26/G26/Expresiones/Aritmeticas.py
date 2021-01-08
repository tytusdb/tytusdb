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

        try:
            left = self.leftOperator.execute()
        except:
            try:
                left = self.leftOperator.executeInsert(data, valoresTabla)
            except:
                left = self.leftOperator.execute(data, valoresTabla)
            

        try:
            right = self.rightOperator.execute()
        except:
            try:
                right = self.rightOperator.executeInsert(data, valoresTabla)
            except:
                right = self.rightOperator.execute(data, valoresTabla)
            

        #checking returns of both arguments in case of error
        if isinstance(left, Error) :
            return left
        if isinstance(right, Error) :
            return right

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

class ArithmeticUnary(Instruccion):

    def __init__(self, rightOperator, sign):
        self.rightOperator = rightOperator
        self.sign = sign

    def __repr__(self):
        return str(self.__dict__)

    def execute(self):
        
        try:
            right = self.rightOperator.execute()
        except:
            try:
                right = self.rightOperator.executeInsert(data, valoresTabla)
            except:
                right = self.rightOperator.execute(data, valoresTabla)
            

        #checking returns of both arguments in case of error
        if isinstance(right, Error) :
            return right

        if self.sign == '-' :
            try:
                res = -1 * right.val
                return Primitive(right.type, res)
            except :
                error = Error('Semántico', 'Error de tipos, no se puede operar -1 con ' + right.type, 0, 0)
                return error
        