import sys
sys.path.append('../G26/Utils')

from Error import *

def compararTiposBin(arg1, arg2, sign):
    try:
        s = arg1.type
        l = arg1
    except:
        ''

    try:
        s = arg2.type
        r = arg2
    except:
        ''

    left = l
    right = r

    if sign == '+':
        if left.type == 'integer' or left.type == 'float':
            if right.type == 'integer' or right.type == 'float':
                return False
        return Error('Semántico', 'Error de tipos en MAS, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '-':
        if left.type == 'integer' or left.type == 'float':
            if right.type == 'integer' or right.type == 'float':
                return False
        return Error('Semántico', 'Error de tipos en MENOS, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '/':
        if left.type == 'integer' or left.type == 'float':
            if right.type == 'integer' or right.type == 'float':
                if right.val == 0:
                    return Error('Semántico', 'No es posible la division con 0', 0, 0)
                return False
        return Error('Semántico', 'Error de tipos en DIVISION, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '*':
        if left.type == 'integer' or left.type == 'float':
            if right.type == 'integer' or right.type == 'float':
                return False
        return Error('Semántico', 'Error de tipos en MULTIPLICACION, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '%':
        if left.type == 'integer' or left.type == 'float':
            if right.type == 'integer' or right.type == 'float':
                return False
        return Error('Semántico', 'Error de tipos en PORCENTAJE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '^':
        if left.type == 'integer' or left.type == 'float':
            if right.type == 'integer' or right.type == 'float':
                return False
        return Error('Semántico', 'Error de tipos en POTENCIA, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    return False
