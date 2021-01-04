import sys
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')

from Error import *
from Primitivo import *

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

    if arg1.type == 'error':
        return arg1

    if arg2.type == 'error':
        return arg2

    left = l
    right = r

    if sign == '+':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                if left.type == 'float' or right.type == 'float' or left.type == 'money' or right.type == 'money':
                    return Primitive('float', '')
                return Primitive('integer', '')
        return Error('Semántico', 'Error de tipos en MAS, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '-':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                if left.type == 'float' or right.type == 'float' or left.type == 'money' or right.type == 'money':
                    return Primitive('float', '')
                return Primitive('integer', '')
        return Error('Semántico', 'Error de tipos en MENOS, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '/':
        if left.type == 'integer' or left.type == 'float':
            if right.type == 'integer' or right.type == 'float':
                if right.val == 0:
                    return Error('Semántico', 'No es posible la division con 0', 0, 0)
                return Primitive('float', '')
        return Error('Semántico', 'Error de tipos en DIVISION, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '*':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                if left.type == 'float' or right.type == 'float' or left.type == 'money' or right.type == 'money':
                    return Primitive('float', '')
                return Primitive('integer', '')
        return Error('Semántico', 'Error de tipos en MULTIPLICACION, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '%':
        if left.type == 'integer' or left.type == 'float':
            if right.type == 'integer' or right.type == 'float':
                return Primitive('integer', '')
        return Error('Semántico', 'Error de tipos en PORCENTAJE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '^':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                if left.type == 'float' or right.type == 'float' or left.type == 'money' or right.type == 'money':
                    return Primitive('float', '')
                return Primitive('integer', '')
        return Error('Semántico', 'Error de tipos en POTENCIA, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    return Primitive('float', '')

def compararTiposCon(arg1, arg2, sign, arg3):
    try:
        s = arg1.type
        l = arg1
    except:
        ''

    try:
        s = arg2.type
        r = arg2
    except:
        r = ''

    try:
        s = arg3.type
        e = arg3
    except:
        e = ''

    print(arg1)
    print(arg2)
    print(arg3)

    if arg1.type == 'error':
        return arg1

    try:
        if arg2.type == 'error':
            return arg2
    except:
        ''

    try:
        if arg3.type == 'error':
            return arg3
    except:
        ''

    left = l
    right = r
    extra = e

    if sign == '<':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                return Primitive('boolean', '')
        if left.type == 'string' or left.type == 'date' or left.type == 'time':
            if right.type == 'string' or right.type == 'date' or right.type == 'time':
                return Primitive('boolean', '')
        return Error('Semántico', 'Error de tipos en MENOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '<=':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                return Primitive('boolean', '')
        if left.type == 'string' or left.type == 'date' or left.type == 'time':
            if right.type == 'string' or right.type == 'date' or right.type == 'time':
                return Primitive('boolean', '')
        return Error('Semántico', 'Error de tipos en MENOR IGUAL QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '>':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                return Primitive('boolean', '')
        if left.type == 'string' or left.type == 'date' or left.type == 'time':
            if right.type == 'string' or right.type == 'date' or right.type == 'time':
                return Primitive('boolean', '')
        if left.type == 'boolean' and right.type == 'boolean':
            return Primitive('boolean', '')
        return Error('Semántico', 'Error de tipos en MAYOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '>=':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                return Primitive('boolean', '')
        if left.type == 'string' or left.type == 'date' or left.type == 'time':
            if right.type == 'string' or right.type == 'date' or right.type == 'time':
                return Primitive('boolean', '')
        if left.type == 'boolean' and right.type == 'boolean':
            return Primitive('boolean', '')
        return Error('Semántico', 'Error de tipos en MAYOR IGUAL QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '=':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                return Primitive('boolean', '')
        if left.type == 'string' or left.type == 'date' or left.type == 'time':
            if right.type == 'string' or right.type == 'date' or right.type == 'time':
                return Primitive('boolean', '')
        if left.type == 'boolean' and right.type == 'boolean':
            return Primitive('boolean', '')
        return Error('Semántico', 'Error de tipos en IGUAL, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == '<>' or sign == '!=':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                return Primitive('boolean', '')
        if left.type == 'string' or left.type == 'date' or left.type == 'time':
            if right.type == 'string' or right.type == 'date' or right.type == 'time':
                return Primitive('boolean', '')
        if left.type == 'boolean' and right.type == 'boolean':
            return Primitive('boolean', '')
        return Error('Semántico', 'Error de tipos en DIFERENTE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    if sign == 'between' or sign == 'not':
        if left.type == 'integer' or left.type == 'float' or left.type == 'money':
            if right.type == 'integer' or right.type == 'float' or right.type == 'money':
                if extra.type == 'integer' or extra.type == 'float' or extra.type == 'money':
                    return Primitive('boolean', '')
        if left.type == 'string' or left.type == 'date' or left.type == 'time':
            if right.type == 'string' or right.type == 'date' or right.type == 'time':
                if extra.type == 'integer' or extra.type == 'float' or extra.type == 'money':
                    return Primitive('boolean', '')
        if left.type == 'boolean' and right.type == 'boolean' and extra.type == 'boolean':
            return Primitive('boolean', '')
        return Error('Semántico', 'Error de tipos en BETWEEN, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
    return Primitive('boolean', '')
