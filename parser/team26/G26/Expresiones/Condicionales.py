import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')

from instruccion import *
from Error import *
from Primitivo import *
from Identificador import *

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

    def executeInsert(self, data, listaColumnas, valoresTabla, posColumna):
        try:
            left = self.leftOperator.execute()
        except:
            left = self.leftOperator.execute(data, listaColumnas, valoresTabla)

        try:
            right = self.rightOperator.execute()
        except:
            right = self.rightOperator.execute(data, listaColumnas, valoresTabla)

        if self.sign == '>':
            if left.type == 'integer' or left.type == 'float':
                if right.type == 'integer' or right.type == 'float':
                    return int(left.val) > int(right.val)
            elif (left.type == 'string' and right.type == 'time') or (right.type == 'string' and left.type == 'time'):
                try:
                    horaIzq = left.val
                    horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                    horaDer = right.val
                    horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                    return horaValIzq > horaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
                    return error
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaIzq = left.val
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                    fechaDer = right.val
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                    return fechaValIzq > fechaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                    return error
            else:
                error = Error('Semántico', 'Error de tipos en MAYOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '<':
            if left.type == 'integer' or left.type == 'float':
                if right.type == 'integer' or right.type == 'float':
                    return int(left.val) < int(right.val)
            elif (left.type == 'string' and right.type == 'time') or (right.type == 'string' and left.type == 'time'):
                try:
                    horaIzq = left.val
                    horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                    horaDer = right.val
                    horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                    return horaValIzq < horaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
                    return error
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaIzq = left.val
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                    fechaDer = right.val
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                    return fechaValIzq < fechaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                    return error
            else:
                error = Error('Semántico', 'Error de tipos en MENOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '<=':
            if left.type == 'integer' or left.type == 'float':
                if right.type == 'integer' or right.type == 'float':
                    return int(left.val) <= int(right.val)
            elif (left.type == 'string' and right.type == 'time') or (right.type == 'string' and left.type == 'time'):
                try:
                    horaIzq = left.val
                    horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                    horaDer = right.val
                    horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                    return horaValIzq <= horaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
                    return error
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaIzq = left.val
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                    fechaDer = right.val
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                    return fechaValIzq <= fechaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                    return error
            else:
                error = Error('Semántico', 'Error de tipos en MENOR IGUAL QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '>=':
            if left.type == 'integer' or left.type == 'float':
                if right.type == 'integer' or right.type == 'float':
                    return int(left.val) >= int(right.val)
            elif (left.type == 'string' and right.type == 'time') or (right.type == 'string' and left.type == 'time'):
                try:
                    horaIzq = left.val
                    horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                    horaDer = right.val
                    horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                    return horaValIzq >= horaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
                    return error
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaIzq = left.val
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                    fechaDer = right.val
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                    return fechaValIzq >= fechaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                    return error
            else:
                error = Error('Semántico', 'Error de tipos en MAYOR IGUAL QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '<>':
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                return int(left.val) != int(right.val)
            elif (left.type == 'string' and right.type == 'string') or (left.type == 'boolean' and right.type == 'boolean'):
                return left.val != right.val
            elif (left.type == 'string' and right.type == 'time') or (right.type == 'string' and left.type == 'time'):
                try:
                    horaIzq = left.val
                    horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                    horaDer = right.val
                    horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                    return horaValIzq != horaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
                    return error
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaIzq = left.val
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                    fechaDer = right.val
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                    return fechaValIzq != fechaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                    return error
            else:
                error = Error('Semántico', 'Error de tipos en DIFERENTE QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error
        elif self.sign == '=':
            if (left.type == 'integer' and right.type == 'integer') or (left.type == 'float' and right.type == 'float') or (left.type == 'float' and right.type == 'integer') or (left.type == 'integer' and right.type == 'float'):
                return int(left.val) == int(right.val)
            elif (left.type == 'string' and right.type == 'string') or (left.type == 'boolean' and right.type == 'boolean'):
                return left.val == right.val
            elif (left.type == 'string' and right.type == 'time') or (right.type == 'string' and left.type == 'time'):
                try:
                    horaIzq = left.val
                    horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                    horaDer = right.val
                    horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                    return horaValIzq == horaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
                    return error
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaIzq = left.val
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                    fechaDer = right.val
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                    return fechaValIzq == fechaValDer
                except ValueError:
                    error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                    return error
            else:
                error = Error('Semántico', 'Error de tipos en IGUAL, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                return error

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
