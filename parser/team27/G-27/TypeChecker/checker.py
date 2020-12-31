from TypeChecker.Database_Types import DBType
from execution.symbol.typ import Type
import math

def check( tipoDato:DBType , primitivo: Type, dato, lenght):
    if primitivo == Type.INT or primitivo  == Type.DECIMAL:
        if not isinstance(dato, int) and not isinstance(dato,float):
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
            decimal, entera = math.modf(dato)
            if entera > 0 and math.log10(entera) + 1 > 131072:
                return 'El tipo DECIMAL solo admite 131072 digitos en la parte entera.'
            if decimal > 0 and math.log(decimal) + 1 > 16383:
                return 'El tipo DECIMAL solo admite 131072 digitos en la parte decimal.'
        elif tipoDato == DBType.numeric:
            decimal, entera = math.modf(dato)
            if entera > 0 and math.log10(entera) + 1 > 131072:
                return 'El tipo NUMERIC solo admite 131072 digitos en la parte entera.'
            if decimal > 0 and math.log10(decimal) + 1 > 16383:
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
        return True
    elif primitivo == Type.STRING:
        if not isinstance(dato, str):
            return 'El tipo de la columna es tipo cadena y el valor que se desea insertar'
        if tipoDato == DBType.text :
            return True
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
        data2 =''
        data1= str(dato).split(' ')
        if isinstance(data1,list):
            data2 = data1[0]
        else:
            data2 = str(dato) 
        data = data2.split('-')
        yCond = int(data[0]) <= 5874897 and int(data[0]) >= 0
        mCond = int(data[1]) <= 12 and int(data[1]) >= 1
        dCond = int(data[2]) <= 31 and int(data[2]) >= 1
        if  not (yCond and  mCond and  dCond):
            return 'La fecha indicada no cumple con el formato o sobrepasa el limite: "5874897-12-31"'
        return True
    elif primitivo == Type.TIME:
        # Limite máximo '23:59:59'
        data2 =''
        data1= str(dato).split(' ')
        if isinstance(data1,list):
            if len(data1) ==2:
                data2 = data1[1]
            else:
                data2 = data1[0]

        else:
            data2 = str(dato) 

        data = data2.split(':')
        hCond = int(data[0]) <= 23 and int(data[0]) >= 0
        mCond = int(data[1]) <= 59 and int(data[1]) >= 0
        sCond = int(data[2]) <= 59 and int(data[2]) >= 0
        if  not (hCond and  mCond and  sCond):
            return 'La hora indicada no cumple con el formato adecuado o excede una hora válida.'
        return True

def rangoNumerico(tipo, valor, inferior, superior):
    if valor < inferior or valor > superior:
        return 'El tipo de dato ' + tipo + ' solo acepta valores en el rango ['+str(inferior)+','+ str(superior) +'].' 
    else:
        return True

def getPrimitivo(tipo:DBType):
    switcher ={
        DBType.smallint:Type.INT,
        DBType.integer:Type.INT,
        DBType.bigint: Type.INT,
        DBType.decimal: Type.DECIMAL,
        DBType.numeric: Type.DECIMAL,
        DBType.real: Type.DECIMAL,
        DBType.double_precision: Type.DECIMAL,
        DBType.money: Type.DECIMAL,
        DBType.ch_varying: Type.STRING,
        DBType.varchar: Type.STRING,
        DBType.character: Type.STRING,
        DBType.char: Type.STRING,
        DBType.text: Type.STRING,
        DBType.timestamp_wtz: Type.DATE,
        DBType.timestamp_tz: Type.DATE,
        DBType.date: Type.DATE,
        DBType.time_wtz: Type.TIME,
        DBType.time_tz: Type.TIME,
        DBType.interval: Type.DATE,
        DBType.boolean: Type.BOOLEAN
    }
    return switcher.get(tipo,'El tipo de dato no coincide con ningun tipo primitivo.')
