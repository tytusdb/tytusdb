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

    def execute(self, data, valoresTabla):
        try:
            left = self.leftOperator.execute()
        except:
            left = self.leftOperator.execute(data, valoresTabla)

        if isinstance(left, Error):
            return left

        if self.rightOperator != None :
            try:
                right = self.rightOperator.execute()
            except:
                try:
                    right = self.rightOperator.execute(data, valoresTabla)
                except:
                    right = self.rightOperator.execute(data)

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
        elif self.sign == 'between' :
            if left.type == 'integer' or left.type == 'float':
                if right.type == False:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return (float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val))
                else:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return not ((float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val)) )
            elif left.type == 'string' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return not (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'date' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            try:
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except :
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                                try:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                            return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'time' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
        elif self.sign == 'not between' :
            if left.type == 'integer' or left.type == 'float':
                if right.type == False:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return not ((float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val)))
                else:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return (float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val))
            elif left.type == 'string' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return  not ((horacomparar >= horaIzq ) and (horacomparar <= horaDer ))
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else:
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'date' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            try:
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except :
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                                try:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return not((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                                except:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                    return not((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            try:
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except :
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                                try:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)

            elif left.type == 'time' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return not (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return  (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
        elif self.sign == 'isnull':
            if left.val == '' or left.val == 'null':
                return True
            else:
                return False
        elif self.sign == 'notnull':
            if left.val == '':
                return False
            elif left.val == 'null':
                return False
            else:
                return True
        elif self.sign == 'is':
            if self.rightOperator.notv == False:
                ##IS NULOS
                if self.rightOperator.val == 'null':
                    if left.val == '' or left.val == 'null':
                        return True
                    else:
                        return False
                ##IS TRUE
                if self.rightOperator.val == True:
                    if left.type == 'boolean':
                        if left.val == True:
                            return True
                        else:
                            return False
                    else :
                        error = Error('Semántico', 'Error de tipos en IS TRUE, no se puede operar ' + str(left.type), 0, 0)
                        return error
                ## IS FALSE
                if self.rightOperator.val == False:
                    if left.type == 'boolean':
                        if left.val:
                            return False
                        else:
                            return True
                    else :
                        error = Error('Semántico', 'Error de tipos en IS FALSE, no se puede operar ' + str(left.val) , 0, 0)
                        return error
                ## IS DISTINCT
                if self.rightOperator.distinct == True:
                    if self.rightOperator != None :
                        try:
                            rd = self.rightOperator.val.execute()
                        except:
                            rd = self.rightOperator.val.execute(data, valoresTabla)

                    if isinstance(right, Error):
                        return right
                    if left.val != rd.val :
                        return True
                    else:
                        return False
                ## IS UNKNOWN
                if self.rightOperator.val == 'unknown':
                    if left.type == 'boolean':
                        if left.val:
                            return False
                        else :
                            return True
            else :
                ##IS NOT NULL
                if self.rightOperator.val == 'null':
                    if left.val == '' or left.val == 'null':
                        return not True
                    else:
                        return not False
                #IS NOT TRUE
                if self.rightOperator.val == 'true':
                    if left.type == 'boolean':
                        if left.val == True:
                            return not True
                        else:
                            return not False
                    else :
                        error = Error('Semántico', 'Error de tipos en IS NOT TRUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                        return error
                ##IS NOT FALSE
                if self.rightOperator.val == 'false':
                    if left.type == 'boolean':
                        if left.val == True:
                            return not False
                        else:
                            return not True
                    else :
                        error = Error('Semántico', 'Error de tipos en IS NOT FALSE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                        return error
                ##IS DISTINCT
                if self.rightOperator.val == 'distinct':
                    if left.val != self.rightOperator.val :
                        return not True
                    else:
                        return not False
                ##ID unknown
                if self.rightOperator.val == 'unknown':
                    if left.type == 'boolean':
                        if left.val:
                            return not False
                        else :
                            return not True

    def __repr__(self):
        return str(self.__dict__)

    def executeInsert(self, data, valoresTabla):
        try:
            left = self.leftOperator.execute()
        except:
            left = self.leftOperator.execute(data, valoresTabla)

        if isinstance(left, Error):
            return left

        if self.rightOperator != None :
            try:
                right = self.rightOperator.execute()
            except:
                try:
                    right = self.rightOperator.execute(data, valoresTabla)
                except:
                    right = self.rightOperator.execute(data)

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
                    fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d %H:%M:%S')
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
                    fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d %H:%M:%S')
                    except:
                        error = Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                        return error
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d %H:%M:%S')
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
                    fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d %H:%M:%S')
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
                    fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d %H:%M:%S')
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
                    fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d %H:%M:%S')
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
                    fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d')
                except:
                    try:
                        fechaI = left.val
                        fechaIzq = fechaI.replace('/', '-')
                        fechaValIzq = datetime.strptime(fechaIzq, '%Y-%m-%d %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                try:
                    fechaD = right.val
                    fechaDer = fechaD.replace('/', '-')
                    fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d')
                except:
                    try:
                        fechaD = right.val
                        fechaDer = fechaD.replace('/', '-')
                        fechaValDer = datetime.strptime(fechaDer, '%Y-%m-%d %H:%M:%S')
                    except:
                        return Error('Semántico', 'Error de tipos en la comparacion de DATE.', 0, 0)
                return fechaValIzq == fechaValDer
            elif left.type == 'string' and right.type == 'string':
                return str(left.val) == str(right.val)
            else:
                return Error('Semántico', 'Error de tipos en IGUAL, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
        elif self.sign == 'between' :
            if left.type == 'integer' or left.type == 'float':
                if right.type == False:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return (float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val))
                else:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return not ((float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val)) )
            elif left.type == 'string' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return not (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'date' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                            return not (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'time' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return not (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
        elif self.sign == 'not between' :
            if left.type == 'integer' or left.type == 'float':
                if right.type == False:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return not ((float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val)))
                else:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return (float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val))
            elif left.type == 'string' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return  not ((horacomparar >= horaIzq ) and (horacomparar <= horaDer ))
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else:
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'date' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                            return not (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'time' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return not (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return  (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
        elif self.sign == 'isnull':
            if left.val == '' or left.val == 'null':
                return True
            else:
                return False
        elif self.sign == 'notnull':
            if left.val != '' or left.val != 'null':
                return True
            else:
                return False
        elif self.sign == 'is':
            if self.rightOperator.notv == False:
                ##IS NULOS
                if self.rightOperator.val == 'null':
                    if left.val == '' or left.val == 'null':
                        return True
                    else:
                        return False
                ##IS TRUE
                if self.rightOperator.val == True:
                    if left.type == 'boolean':
                        if left.val == True:
                            return True
                        else:
                            return False
                    else :
                        error = Error('Semántico', 'Error de tipos en IS TRUE QUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                        return error
                ## IS FALSE
                if self.rightOperator.val == False:
                    if left.type == 'boolean':
                        if left.val == True: ##esta no c aun xd
                            return False
                        else:
                            return True
                    else :
                        error = Error('Semántico', 'Error de tipos en IS FALSE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                        return error
                ## IS DISTINCT
                if self.rightOperator.val == 'distinct':
                    if left.val != self.rightOperator.val :
                        return True
                    else:
                        return False
                ## IS UNKNOWN
                if self.rightOperator.val == 'unknown':
                    if left.type == 'booleano':
                        if left.val == True :
                            return True
                        else :
                            return False
            else :
                ##IS NOT NULL
                if self.rightOperator.val == 'null':
                    if left.val == '' or left.val == 'null':
                        return not True
                    else:
                        return not False
                #IS NOT TRUE
                if self.rightOperator.val == 'true':
                    if left.type == 'boolean':
                        if left.val == True:
                            return not True
                        else:
                            return not False
                    else :
                        error = Error('Semántico', 'Error de tipos en IS NOT TRUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                        return error
                ##IS NOT FALSE
                if self.rightOperator.val == 'false':
                    if left.type == 'boolean':
                        if left.val == True:
                            return not False
                        else:
                            return not True
                    else :
                        error = Error('Semántico', 'Error de tipos en IS NOT FALSE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                        return error
                ##IS DISTINCT
                if self.rightOperator.val == 'distinct':
                    if left.val != self.rightOperator.val :
                        return not True
                    else:
                        return not False
                ##ID DISCTINCT
                if self.rightOperator.val == 'unknown':
                    if left.type == 'booleano':
                        if left.val == True :
                            return not True
                        else :
                            return not False
        elif self.sign == 'between' :
            if left.type == 'integer' or left.type == 'float':
                if right.type == False:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return (float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val))
                else:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return not ((float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val)) )
            elif left.type == 'string' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return not (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'date' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            try:
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except :
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                                try:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                            return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'time' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
        elif self.sign == 'not between' :
            if left.type == 'integer' or left.type == 'float':
                if right.type == False:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return not ((float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val)))
                else:
                    if (right.val1.type == 'integer' or right.val1.type == 'float') and (right.val2.type == 'integer' or right.val2.type == 'float') :
                        return (float(left.val) >= float(right.val1.val)) and (float(left.val) <= float(right.val2.val))
            elif left.type == 'string' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return  not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return  not ((horacomparar >= horaIzq ) and (horacomparar <= horaDer ))
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else:
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                            return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                try:
                                    horacomparar = left.val
                                    horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    try:
                                        horacomparar = str(left.val)
                                        horaIzq = str(right.val1.val)
                                        horaDer = str(right.val2.val)
                                        return (horacomparar >= horaIzq ) and (horacomparar <= horaDer )
                                    except:
                                        return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
            elif left.type == 'date' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                            try:
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except :
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                return not ((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                                try:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return not((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                                except:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                    return not((horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer ))
                            except:
                                return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d')
                            try:
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except :
                                horaIzq = right.val1.val
                                horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                horaDer = right.val2.val
                                horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            try:
                                horacomparar = left.val
                                horaValComparar = datetime.strptime(horacomparar, '%Y-%m-%d %H:%M:%S')
                                try:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                                except:
                                    horaIzq = right.val1.val
                                    horaValIzq = datetime.strptime(horaIzq, '%Y-%m-%d %H:%M:%S')
                                    horaDer = right.val2.val
                                    horaValDer = datetime.strptime(horaDer, '%Y-%m-%d %H:%M:%S')
                                    return (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                            except:
                                return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)

            elif left.type == 'time' :
                if right.type == False :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return not (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
                else :
                    if right.val1.type == 'string' and right.val2.type == 'string':
                        try:
                            horacomparar = left.val
                            horaValComparar = datetime.strptime(horacomparar, '%H:%M:%S')
                            horaIzq = right.val1.val
                            horaValIzq = datetime.strptime(horaIzq, '%H:%M:%S')
                            horaDer = right.val2.val
                            horaValDer = datetime.strptime(horaDer, '%H:%M:%S')
                            return  (horaValComparar >= horaValIzq ) and (horaValComparar <= horaValDer )
                        except:
                            return Error('Semántico', 'Error de tipos con los argumentos proporcionados. Arg1: '+str(left.val)+' Arg2: '+str(right.val1.val)+' Arg3: '+str(right.val2.val), 0, 0)
        elif self.sign == 'isnull':
            if left.val == '' or left.val == 'null':
                return True
            else:
                return False
        elif self.sign == 'notnull':
            if left.val == '':
                return False
            elif left.val == 'null':
                return False
            else:
                return True
        elif self.sign == 'is':
            if self.rightOperator.notv == False:
                ##IS NULOS
                if self.rightOperator.val == 'null':
                    if left.val == '' or left.val == 'null':
                        return True
                    else:
                        return False
                ##IS TRUE
                if self.rightOperator.val == True:
                    if left.type == 'boolean':
                        if left.val == True:
                            return True
                        else:
                            return False
                    else :
                        error = Error('Semántico', 'Error de tipos en IS TRUE, no se puede operar ' + str(left.type), 0, 0)
                        return error
                ## IS FALSE
                if self.rightOperator.val == False:
                    if left.type == 'boolean':
                        if left.val:
                            return False
                        else:
                            return True
                    else :
                        error = Error('Semántico', 'Error de tipos en IS FALSE, no se puede operar ' + str(left.val) , 0, 0)
                        return error
                ## IS DISTINCT
                if self.rightOperator.distinct == True:
                    if self.rightOperator != None :
                        try:
                            rd = self.rightOperator.val.execute()
                        except:
                            rd = self.rightOperator.val.execute(data, valoresTabla)

                    if isinstance(right, Error):
                        return right
                    if left.val != rd.val :
                        return True
                    else:
                        return False
                ## IS UNKNOWN
                if self.rightOperator.val == 'unknown':
                    if left.type == 'boolean':
                        if left.val:
                            return False
                        else :
                            return True
            else :
                ##IS NOT NULL
                if self.rightOperator.val == 'null':
                    if left.val == '' or left.val == 'null':
                        return not True
                    else:
                        return not False
                #IS NOT TRUE
                if self.rightOperator.val == 'true':
                    if left.type == 'boolean':
                        if left.val == True:
                            return not True
                        else:
                            return not False
                    else :
                        error = Error('Semántico', 'Error de tipos en IS NOT TRUE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                        return error
                ##IS NOT FALSE
                if self.rightOperator.val == 'false':
                    if left.type == 'boolean':
                        if left.val == True:
                            return not False
                        else:
                            return not True
                    else :
                        error = Error('Semántico', 'Error de tipos en IS NOT FALSE, no se puede operar ' + left.type + ' con ' + right.type, 0, 0)
                        return error
                ##IS DISTINCT
                if self.rightOperator.val == 'distinct':
                    if left.val != self.rightOperator.val :
                        return not True
                    else:
                        return not False
                ##ID unknown
                if self.rightOperator.val == 'unknown':
                    if left.type == 'boolean':
                        if left.val:
                            return not False
                        else :
                            return not True


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
