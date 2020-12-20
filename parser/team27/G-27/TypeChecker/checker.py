import sys
sys.path.append('../tytus/parser/team27/G-27/TypeChecker')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from DBType import *
from typ import *
import math

def check( tipoDato:DBType, primitivo: Type, dato, lenght):
    if primitivo == Type.INT or primitivo  == Type.DECIMAL:
        if not isinstance(dato, int):
            return 'El tipo de la columna es numérico y el dato ingresado no coincide.'
        if tipoDato == DBType.smallint:
            #-32768 to +32767
            return rangoNumerico('SMALLINT', dato, -32768, 32767)
        elif tipoDato == DBType.integer:
            #-2147483648 to +2147483647
            return rangoNumerico('INTEGER',dato,-2147483648, 2147483647)
        elif tipoDato == DBType.bigint:
            #-9223372036854775808 to +9223372036854775807
            return rangoNumerico('BIGINT',dato,-9223372036854775808, 9223372036854775807)
        elif tipoDato == DBType.decimal:
            entera, decimal = math.modf(dato)
            if math.log10(entera) + 1 > 131072:
                return 'El tipo DECIMAL solo admite 131072 digitos en la parte entera.'
            if math.log(decimal) + 1 > 16383:
                return 'El tipo DECIMAL solo admite 131072 digitos en la parte decimal.'
        elif tipoDato == DBType.numeric:
            entera, decimal = math.modf(dato)
            if math.log10(entera) + 1 > 131072:
                return 'El tipo NUMERIC solo admite 131072 digitos en la parte entera.'
            if math.log(decimal) + 1 > 16383:
                return 'El tipo NUMERIC solo admite 131072 digitos en la parte decimal.'                    
        elif tipoDato == DBType.real:
            entera, decimal = math.modf(dato)
            if math.log(decimal) + 1 > 6:
                return 'El tipo REAL solo admite 6 digitos en la parte decimal.'
        elif tipoDato == DBType.double_precision:
            entera, decimal = math.modf(dato)
            if math.log(decimal) + 1 > 15:
                return 'El tipo DOUBLE solo admite 15 digitos en la parte decimal.'        
        elif tipoDato == DBType.money:
            #-92233720368547758.08 to +92233720368547758.07
            return rangoNumerico('MONEY', dato, -92233720368547758.08, 92233720368547758.07)
        else:
            return 'El tipo de dato asignado en la columna no es numérico.'
    elif primitivo == Type.STRING:
        if not isinstance(dato, str):
            return 'El tipo de la columna es tipo cadena y el valor que se desea insertar'
        if len(dato) > lenght:
            return 'El dato a insertar cuenta con más de ' + str(lenght) + ' carácteres.'
        return True
    elif primitivo == Type.NULL:
        return True
    elif primitivo == Type.BOOLEAN:
        if not isinstance(dato, bool):
            return 'El dato que se desea ingresar no corresponde a un dato booleano.'
        return True
    elif primitivo == Type.DATE:
        # Limite máximo '5874897-12-31'
        data = dato.split('-')
        yCond = data[0] <= 5874897 and data[0] >= 0
        mCond = data[1] <= 12 and data[1] >= 1
        dCond = data[2] <= 31 and data[2] >= 1
        if  not (yCond and  mCond and  dCond):
            return 'La fecha indicada no cumple con el formato o sobrepasa el limite: "5874897-12-31"'
        return True
    elif primitivo == Type.TIME:
        # Limite máximo '5874897-12-31'
        data = dato.split('-')
        hCond = data[0] <= 23 and data[0] >= 0
        mCond = data[1] <= 59 and data[1] >= 0
        sCond = data[2] <= 59 and data[2] >= 0
        if  not (hCond and  mCond and  sCond):
            return 'La hora indicada no cumple con el formato adecuado o excede una hora válida.'
        return True

def rangoNumerico(tipo, valor, inferior, superior):
    if valor < inferior or valor > superior:
        return 'El tipo de dato ' + tipo + ' solo acepta valores en el rango ['+str(inferior)+','+ str(superior) +'].' 
    else:
        return True