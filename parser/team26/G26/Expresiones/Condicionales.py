import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')

from instruccion import *
from Error import *
from Primitivo import *
from Identificador import *
from datetime import *

class Condicionales(Instruccion):

    def __init__(self, leftOperator, rightOperator, sign, extra):
        self.leftOperator = leftOperator
        self.rightOperator = rightOperator
        self.sign = sign
        self.extra = extra
    
    def validarcondicion(self, data, tbname):
        try:
            id1 = self.leftOperator.column
            i = 0
            for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
                if colu.name == id1.upper() :
                    return [True, i]
                i += 1
            return [False, None]
        except:
            print('L: not an id')
        
        try:
            id1 = self.rightOperator.column
            i = 0
            for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
                if colu.name == id1.upper() :
                    return [True, i]
                i += 1
            return [False, None]
        except:
            print('R: not an id')

        return False

    def execute(self):
        try:
            left = self.leftOperator.execute()
        except:
            left = self.leftOperator.execute(data, valoresTabla)

        if isinstance(left, Error):
            return left

        try:
            right = self.rightOperator.execute()
        except:
            right = self.rightOperator.execute(data, valoresTabla)

        if isinstance(right, Error):
            return right

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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                        return error
                return fechaValIzq > fechaValDer
            else:
                return Error('Semántico', 'Error de tipos en MAYOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                        return error
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq < fechaValDer
            else:
                return Error('Semántico', 'Error de tipos en MENOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq <= fechaValDer
            else:
                return Error('Semántico', 'Error de tipos en MENOR IGUAL QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq >= fechaValDer
            else:
                return Error('Semántico', 'Error de tipos en MAYOR IGUAL QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
        elif self.sign == '<>' or self.sign == '!=':
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq != fechaValDer
            elif left.type == 'string' and right.type == 'string':
                return str(left.val) != str(right.val)
            else:
                return Error('Semántico', 'Error de tipos en DIFERENTE QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq == fechaValDer
            elif left.type == 'string' and right.type == 'string':
                return str(left.val) == str(right.val)
            else:
                return Error('Semántico', 'Error de tipos en IGUAL, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)

    def __repr__(self):
        return str(self.__dict__)

    def executeInsert(self, data, valoresTabla):
        try:
            left = self.leftOperator.execute()
        except:
            left = self.leftOperator.execute(data, valoresTabla)

        if isinstance(left, Error):
            return left

        try:
            right = self.rightOperator.execute()
        except:
            right = self.rightOperator.execute(data, valoresTabla)

        if isinstance(right, Error):
            return right

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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                        return error
                return fechaValIzq > fechaValDer
            else:
                return Error('Semántico', 'Error de tipos en MAYOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                        return error
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq < fechaValDer
            else:
                return Error('Semántico', 'Error de tipos en MENOR QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq <= fechaValDer
            else:
                return Error('Semántico', 'Error de tipos en MENOR IGUAL QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq >= fechaValDer
            else:
                return Error('Semántico', 'Error de tipos en MAYOR IGUAL QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
        elif self.sign == '<>' or self.sign == '!=':
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq != fechaValDer
            elif left.type == 'string' and right.type == 'string':
                return str(left.val) != str(right.val)
            else:
                return Error('Semántico', 'Error de tipos en DIFERENTE QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
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
                except:
                    return Error('Semántico', 'Error de tipos en la comparacion de TIME.', 0, 0)
            elif (left.type == 'string' and right.type == 'date') or (right.type == 'string' and left.type == 'date'):
                try:
                    fechaI = left.val
                    fechaIzq = fechaI.replace('/', '-')
                    fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%d-%m-%Y %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq == fechaValDer
            elif left.type == 'string' and right.type == 'string':
                return str(left.val) == str(right.val)
            else:
                return Error('Semántico', 'Error de tipos en IGUAL, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)


class Between(Instruccion):

    def __init__(self, type, val1, val2):
        self.type = type
        self.val1 = val1
        self.val2 = val2

    def execute(self):
        return self

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
