
from parserT28.models.instructions.shared import ObjectReference
from parserT28.models.instructions.DML.special_functions import *
from parserT28.models.instructions.Expression.expression import *
import math
from random import randint, random


class Abs(Expression):
    '''
        Valor absoluto de una columna tipo entero o de un valor.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            print(type(self.value))

            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [fabs(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [fabs(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.fabs(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Abs"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = abs({temp.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para ABS"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Cbrt(Expression):
    '''
        Raiz Cubica de un numero o una columna tipo entero.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            print(type(self.value))
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [pow(columns, 1/3) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [pow(columns, 1/3) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.pow(value.value, 1/3), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para CBRT"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            tempDIV = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{tempDIV} = 1 / 3")

            temp = self.value.compile(environment)
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = pow({temp.value}, {tempDIV}) # CBRT()")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para CBRT"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Ceil(Expression):
    '''
        Redondear cualquier valor decimal positivo o negativo como
        mayor que el argumento.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            print(type(self.value))
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [ceil(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [ceil(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.ceil(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Ceil"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = ceil({temp.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Ceil"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Ceiling(Expression):
    '''
        Redondear cualquier valor decimal positivo o
        negativo como mayor que el argumento.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [ceil(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [ceil(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.ceil(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Ceiling"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = ceil({temp.value})  # CEILING()")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Ceiling"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Degrees(Expression):
    '''
        Se usa para devolver los valores en grados de radianes
        como se especifica en el argumento.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [degrees(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [degrees(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.degrees(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Degrees"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = degrees({temp.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Degrees"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Div(Expression):
    '''
        Se utiliza para devolver el cociente entero de
        una división como se especifica en el argumento.
    '''

    def __init__(self,  dividendo, divisor, type_fm, line, column):
        self.dividendo = dividendo
        self.divisor = divisor
        self.alias = f'{type_fm}({self.dividendo.alias},{self.divisor.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value1 = 0
            value2 = 0
            print(type(self.dividendo))
            print(type(self.divisor))
            if isinstance(self.dividendo, ObjectReference):
                value1 = self.dividendo.process(environment)
                value2 = self.divisor.process(environment)
                lista1 = []
                result = [columns // value2.value for columns in value1[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif isinstance(self.divisor, ObjectReference):
                value1 = self.dividendo.process(environment)
                value2 = self.divisor.process(environment)
                lista1 = []
                result = [value1.value // columns for columns in value2[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value1 = self.dividendo.process(environment)
                value2 = self.divisor.process(environment)
                if isinstance(value1, list):
                    lista1 = []
                    result = [columns // value2.value for columns in value1[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                elif isinstance(value2, list):
                    lista1 = []
                    result = [value1.value // columns for columns in value2[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, value1.value // value2.value, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Div"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp1 = self.dividendo.compile(environment)
            temp2 = self.divisor.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = {temp1.value} // {temp2.value}  # DIV()")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Div"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Exp(Expression):
    '''
        La función se usa para devolver la exponenciación de
        un número como se especifica en el argumento.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [exp(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [exp(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.exp(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Exp"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = exp({temp.value}) # EXP()")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Exp"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Factorial(Expression):
    '''
        Se puede utilizar la libreria Math de Python **
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [factorial(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [factorial(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.factorial(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Factorial"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = factorial({temp.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)

        except TypeError:
            desc = "Tipo de dato invalido para Factorial"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Floor(Expression):
    '''
        Se usa para devolver el valor después de redondear
        cualquier valor decimal positivo o negativo
        como más pequeño que el argumento.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            print(type(self.value))
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [floor(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [floor(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.floor(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Floor"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = floor({temp.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Floor"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Gcd(Expression):
    '''
        Se puede utilizar la libreria Math de Python.
        Maximo Comun Divisor *
    '''

    def __init__(self,  value1, value2, type_fm, line, column):
        self.value1 = value1
        self.value2 = value2
        self.alias = f'{type_fm}({self.value1.alias},{self.value2.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value1 = 0
            value2 = 0
            print(type(self.value1))
            print(type(self.value2))
            if isinstance(self.value1, ObjectReference):
                value1 = self.value1.process(environment)
                value2 = self.value2.process(environment)
                lista1 = []
                result = [gcd(columns, value2.value) for columns in value1[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif isinstance(self.value2, ObjectReference):
                value1 = self.value1.process(environment)
                value2 = self.value2.process(environment)
                lista1 = []
                result = [gcd(value1.value, columns) for columns in value2[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value1 = self.value1.process(environment)
                value2 = self.value2.process(environment)
                if isinstance(value1, list):
                    lista1 = []
                    result = [gcd(columns, value2.value)
                              for columns in value1[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                elif isinstance(value2, list):
                    lista1 = []
                    result = [gcd(value1.value, columns)
                              for columns in value2[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.gcd(value1.value, value2.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Gcd"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp1 = self.value1.compile(environment)
            temp2 = self.value2.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = gcd({temp1.value}, {temp2.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para GCD"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Ln(Expression):
    '''
        Logaritmo natural de un numero ***
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [log(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [log(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    # With one argument, return the natural logarithm of x (to base e).
                    return PrimitiveData(DATA_TYPE.NUMBER, round(math.log(value.value), 3), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Ln"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = log({temp.value})  # LN()")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Ln"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Log(Expression):
    '''
        Logaritmo base 10 de un número.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [log10(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [log10(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, round(math.log10(value.value), 3), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Log"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = log10({temp.value}) # LOG()")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Log"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Mod(Expression):
    '''
        La función se usa para devolver el resto de una
        división de dos números, como se especifica
        en el argumento
    '''

    def __init__(self,  value1, value2, type_fm, line, column):
        self.value1 = value1
        self.value2 = value2
        self.alias = f'{type_fm}({self.value1.alias},{self.value2.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value1 = 0
            value2 = 0
            if isinstance(self.value1, ObjectReference):
                value1 = self.value1.process(environment)
                value2 = self.value2.process(environment)
                lista1 = []
                result = [(columns) % value2.value for columns in value1[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif isinstance(self.value2, ObjectReference):
                value1 = self.value1.process(environment)
                value2 = self.value2.process(environment)
                lista1 = []
                result = [(value1.value) % columns for columns in value2[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value1 = self.value1.process(environment)
                value2 = self.value2.process(environment)
                if isinstance(value1, list):
                    lista1 = []
                    result = [(columns) %
                              value2.value for columns in value1[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                elif isinstance(value2, list):
                    lista1 = []
                    result = [(value1.value) %
                              columns for columns in value2[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, value1.value % value2.value, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Mod"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp1 = self.value1.compile(environment)
            temp2 = self.value2.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = {temp1.value} % {temp2.value} # MOD()")
            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Mod"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Pi(Expression):
    '''
        Retorna el valor de la constant PI
        ***** TODO: SIN ARGUMENTOS *****
    '''

    def __init__(self, type_fm, line, column):
        self.alias = f'{type_fm}()'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            return PrimitiveData(DATA_TYPE.NUMBER, round(math.pi, 6), self.line, self.column)
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
            return

    def compile(self, environment):
        try:
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = {round(math.pi, 6)} # PI()")
            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
            return


class Power(Expression):
    '''
        La función se usa para devolver el valor de un
        número elevado a la potencia de otro número,
        proporcionado en el argumento.
    '''

    def __init__(self, base, exp, type_fm, line, column):
        self.base = base
        self.exp = exp
        self.alias = f'{type_fm}({self.base.alias},{self.exp.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value1 = 0
            value2 = 0
            if isinstance(self.base, ObjectReference):
                value1 = self.base.process(environment)
                value2 = self.exp.process(environment)
                lista1 = []
                result = [pow(columns, value2.value) for columns in value1[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            elif isinstance(self.exp, ObjectReference):
                value1 = self.base.process(environment)
                value2 = self.exp.process(environment)
                lista1 = []
                result = [pow(value1.value, columns) for columns in value2[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value1 = self.base.process(environment)
                value2 = self.exp.process(environment)
                if isinstance(value1, list):
                    lista1 = []
                    result = [pow(columns, value2.value)
                              for columns in value1[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                elif isinstance(value2, list):
                    lista1 = []
                    result = [pow(value1.value, columns)
                              for columns in value2[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.pow(value1.value, value2.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Power"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp1 = self.base.compile(environment)
            temp2 = self.exp.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = pow({temp1.value}, {temp2.value}) # POWER()")
            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Power"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Radians(Expression):
    '''
        La función se usa para devolver el valor en radianes
        a partir de grados, proporcionado en el argumento.
    '''

    def __init__(self,  value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [radians(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(self.value, list):
                    lista1 = []
                    result = [radians(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.radians(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Radians"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = radians({temp.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Radians"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Round(Expression):
    '''
        La función se usa para devolver el valor después de
        redondear un número hasta un decimal específico,
        proporcionado en el argumento.
    '''

    def __init__(self,  value, n_digits, type_fm, line, column):
        self.value = value
        self.n_digits = n_digits
        self.alias = f'{type_fm}({self.value.alias},{self.n_digits.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            digits = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                digits = self.n_digits.process(environment)
                lista1 = []
                if digits.value == 0:
                    result = [trunc(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    result = [round(columns, digits.value)
                              for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
            else:
                value = self.value.process(environment)
                digits = self.n_digits.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    if digits.value == 0:
                        result = [trunc(columns) for columns in value[0]]
                        lista1.append(result)
                        lista1.append(self.alias)
                        return lista1
                    else:
                        result = [round(columns, digits.value)
                                  for columns in value[0]]
                        lista1.append(result)
                        lista1.append(self.alias)
                        return lista1
                else:
                    if digits.value == 0:
                        return PrimitiveData(DATA_TYPE.NUMBER, math.trunc(value.value), self.line, self.column)
                    else:
                        return PrimitiveData(DATA_TYPE.NUMBER, round(value.value, digits.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Round"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp1 = self.value.compile(environment)
            temp2 = self.n_digits.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = round({temp1.value}, {temp2.value})")
            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)

        except TypeError:
            desc = "Tipo de dato invalido para Round"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Sign(Expression):
    '''
        La función se usa para devolver el valor después de
        redondear un número hasta un decimal específico,
        proporcionado en el argumento.
    '''

    def __init__(self, value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                lista1 = []
                value = self.value.process(environment)
                result = [1 if columns > 0 else -1 for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    value = self.value.process(environment)
                    result = [1 if columns > 0 else -1 for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    if value.value >= 0:
                        return PrimitiveData(DATA_TYPE.NUMBER, 1, self.line, self.column)
                    else:
                        return PrimitiveData(DATA_TYPE.NUMBER, -1, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Sign"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            value = self.value.process(0)
            temp = self.value.compile(environment)
            temporal = ThreeAddressCode().newTemp()

            if value.value >= 0:
                ThreeAddressCode().addCode(
                    f"{temporal} = {1} # SIGN({temp.value})")
                return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
            else:
                ThreeAddressCode().addCode(
                    f"{temporal} = {-1} # SIGN({temp.value})")
                return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Sign"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Sqrt(Expression):
    '''
        La función se usa para devolver el valor después de
        redondear un número hasta un decimal específico,
        proporcionado en el argumento.
    '''

    def __init__(self, value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [sqrt(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [sqrt(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.sqrt(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Sqrt"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = sqrt({temp.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Sqrt"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class WithBucket(Expression):
    '''
        La función se usa para devolver el valor después de
        redondear un número hasta un decimal específico,
        proporcionado en el argumento.
    '''

    def __init__(self,  expre, min_value, max_value, index, type_fm, line, column):
        self.expre = expre
        self.min_value = min_value
        self.max_value = max_value
        self.index = index
        self.alias = f'{type_fm}({self.expre.alias},{self.min_value.alias},{self.max_value.alias},{self.index.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            expr1 = self.expre.process(environment)
            min_value = self.min_value.process(environment)
            max_value = self.max_value.process(environment)
            index = self.index.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, width_bucket_func(expr1.value, min_value.value, max_value.value, index.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para WithBucket"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            expr1 = self.expre.process(0)
            temp1 = self.expre.compile(environment)
            min_value = self.min_value.process(0)
            temp2 = self.min_value.compile(environment)
            max_value = self.max_value.process(0)
            temp3 = self.max_value.compile(environment)
            index = self.index.process(0)
            temp4 = self.index.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            tac = f"{temporal} = {width_bucket_func(expr1.value, min_value.value, max_value.value, index.value)} "
            tac += f"# WIDTH_BUCKET({temp1.value}, {temp2.value},  {temp3.value},  {temp4.value})"
            ThreeAddressCode().addCode(tac)
            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)

        except TypeError:
            desc = "Tipo de dato invalido para WithBucket"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Trunc(Expression):
    '''
        La función se usa para devolver el valor después de
        redondear un número hasta un decimal específico,
        proporcionado en el argumento.
    '''

    def __init__(self, value, type_fm, line, column):
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            if isinstance(self.value, ObjectReference):
                value = self.value.process(environment)
                lista1 = []
                result = [trunc(columns) for columns in value[0]]
                lista1.append(result)
                lista1.append(self.alias)
                return lista1
            else:
                value = self.value.process(environment)
                if isinstance(value, list):
                    lista1 = []
                    result = [trunc(columns) for columns in value[0]]
                    lista1.append(result)
                    lista1.append(self.alias)
                    return lista1
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.trunc(value.value), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Trunc"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temp = self.value.compile(environment)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = trunc({temp.value})")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Trunc"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Random(Expression):
    '''
        La función se usa para devolver el valor después de
        redondear un número hasta un decimal específico,
        proporcionado en el argumento.
    '''

    def __init__(self, type_fm, line, column):
        self.alias = f'{type_fm}()'
        self.line = line
        self.column = column
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            return PrimitiveData(DATA_TYPE.NUMBER, randint(0, 1), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Random"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = {randint(0, 1)} # RANDOM()")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Random"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Greatest(Expression):  # TODO IMPLEMENTAR COMPILE
    '''
        La función se usa para devolver el valor después de
        redondear un número hasta un decimal específico,
        proporcionado en el argumento.
    '''

    def __init__(self, val_array, type_fm, line, column):
        self.val_array = val_array
        self.alias = f'{type_fm}({obtain_string(self.val_array)})'
        self.line = line
        self.column = column
        self._tac = ""

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            array = operating_list_number(self.val_array, environment)
            return PrimitiveData(DATA_TYPE.NUMBER, max(array), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Greatest"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            tempList = []
            array = []

            for tac in self.val_array:
                tmpInstr = tac.compile(environment)
                array.append(tac.process(0).value)

                if isinstance(tmpInstr.value, int) or isinstance(tmpInstr.value, float):
                    temporal = ThreeAddressCode().newTemp()
                    ThreeAddressCode().addCode(
                        f"{temporal} = {tmpInstr.value}")
                    tmpInstr.value = temporal
                tempList.append(tmpInstr.value)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = {tempList[array.index(max(array))]} # GREATEST {tempList}")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Greatest"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Least(Expression):  # TODO IMPLEMENTAR COMPILE
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''

    def __init__(self, val_array, type_fm, line, column):
        self.val_array = val_array
        self.alias = f'{type_fm}({obtain_string(self.val_array)})'
        self.line = line
        self.column = column
        self._tac = ""

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            array = operating_list_number(self.val_array, environment)
            return PrimitiveData(DATA_TYPE.NUMBER, min(array), self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Least"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, environment):
        try:
            tempList = []
            array = []

            for tac in self.val_array:
                tmpInstr = tac.compile(environment)
                array.append(tac.process(0).value)

                if isinstance(tmpInstr.value, int) or isinstance(tmpInstr.value, float):
                    temporal = ThreeAddressCode().newTemp()
                    ThreeAddressCode().addCode(
                        f"{temporal} = {tmpInstr.value}")
                    tmpInstr.value = temporal
                tempList.append(tmpInstr.value)

            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = {tempList[array.index(min(array))]} # LEAST {tempList}")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Tipo de dato invalido para Least"
            ErrorController().add(37, 'Execution', desc, self.line, self.column)
            return
        except:
            desc = "FATAL ERROR --- MathFuncs"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
