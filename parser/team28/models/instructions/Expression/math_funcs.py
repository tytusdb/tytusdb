
from models.instructions.DML.special_functions import *
from models.instructions.Expression.expression import *
import math
from random import randint, random

class Abs(Expression):
    '''
        Valor absoluto de una columna tipo entero o de un valor.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = 0
            print(type(self.value))
            if isinstance(self.value, UnaryOrSquareExpressions):
                value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.fabs(value.value),self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Cbrt(Expression):
    '''
        Raiz Cubica de un numero o una columna tipo entero.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.pow(value.value, 1/3), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Ceil(Expression):
    '''
        Redondear cualquier valor decimal positivo o negativo como
        mayor que el argumento.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.ceil(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Ceiling(Expression):
    '''
        Redondear cualquier valor decimal positivo o
        negativo como mayor que el argumento.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.ceil(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Degrees(Expression):
    '''
        Se usa para devolver los valores en grados de radianes 
        como se especifica en el argumento.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
        
    def __repr__(self):
        return str(vars(self))
    
    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.degrees(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Div(Expression):
    '''
        Se utiliza para devolver el cociente entero de
        una división como se especifica en el argumento.
    '''
    def __init__(self,  dividendo, divisor, type_fm,line, column) :
        self.dividendo = dividendo
        self.divisor = divisor
        self.alias = f'{type_fm}({self.dividendo.alias},{self.divisor.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))
    
    def process(self, environment):
        try:
            value1 = self.dividendo.process(environment)
            value2 = self.divisor.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, value1.value // value2.value, self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Exp(Expression):
    '''
        La función se usa para devolver la exponenciación de
        un número como se especifica en el argumento.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.exp(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Factorial(Expression):
    '''
        Se puede utilizar la libreria Math de Python **
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.factorial(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Floor(Expression):
    '''
        Se usa para devolver el valor después de redondear 
        cualquier valor decimal positivo o negativo 
        como más pequeño que el argumento.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line 
        self.column = column
    def __repr__(self):
        return str(vars(self))
    
    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.floor(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Gcd(Expression):
    '''
        Se puede utilizar la libreria Math de Python. 
        Maximo Comun Divisor *
    '''
    def __init__(self,  value1, value2,type_fm,line, column) :
        self.value1 = value1
        self.value2 = value2
        self.alias = f'{type_fm}({self.value1.alias},{self.value2.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value1 = self.value1.process(environment)
            value2 = self.value2.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.gcd(value1.value, value2.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Ln(Expression):
    '''
        Logaritmo natural de un numero ***
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, round(math.log(value.value),3), self.line, self.column) #With one argument, return the natural logarithm of x (to base e).
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Log(Expression):
    '''
        Logaritmo base 10 de un número.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, round(math.log10(value.value),3), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Mod(Expression):
    '''
        La función se usa para devolver el resto de una
        división de dos números, como se especifica 
        en el argumento
    '''
    def __init__(self,  value1, value2,type_fm,line, column) :
        self.value1 = value1
        self.value2 = value2
        self.alias = f'{type_fm}({self.value1.alias},{self.value2.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value1 = self.value1.process(environment)
            value2 = self.value2.process(environment)

            return PrimitiveData(DATA_TYPE.NUMBER, value1.value%value2.value, self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Pi(Expression):
    '''
        Retorna el valor de la constant PI
        ***** TODO: SIN ARGUMENTOS *****
    '''
    def __init__(self,type_fm,line, column) :
        self.alias = f'{type_fm}()'
        self.line = line
        self.column = column

    def __repr__(self):
        return str(vars(self))
    
    def process(self, environment):
        return PrimitiveData(DATA_TYPE.NUMBER,round(math.pi,6), self.line, self.column)

class Power(Expression):
    '''
        La función se usa para devolver el valor de un 
        número elevado a la potencia de otro número, 
        proporcionado en el argumento.
    '''
    def __init__(self, base, exp,type_fm,line, column) :
        self.base = base
        self.exp = exp
        self.alias = f'{type_fm}({self.base.alias},{self.exp.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value1 = self.base.process(environment)
            value2 = self.exp.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.pow(value1.value, value2.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Radians(Expression):
    '''
        La función se usa para devolver el valor en radianes 
        a partir de grados, proporcionado en el argumento.
    '''
    def __init__(self,  value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.radians(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Round(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self,  value, n_digits,type_fm,line, column) :
        self.value = value
        self.n_digits = n_digits
        self.alias = f'{type_fm}({self.value.alias},{self.n_digits.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
            try:
                value = self.value.process(environment)
                digits = self.n_digits.process(environment)
                if self.n_digits == 0:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.trunc(value.value), self.line, self.column)
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, round(value.value, digits.value), self.line, self.column)
            except TypeError:
                print("Error de tipo")
                print(self)
                return
            except:
                print("FATAL ERROR, ni idea porque murio, F --- Math")

class Sign(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
            try:
                value = self.value.process(environment)
                if value.value >= 0:
                    return PrimitiveData(DATA_TYPE.NUMBER, 1, self.line, self.column)
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, -1, self.line, self.column)
            except TypeError:
                print("Error de tipo")
                print(self)
                return
            except:
                print("FATAL ERROR, ni idea porque murio, F --- Math")

class Sqrt(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.sqrt(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class WithBucket(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self,  expre, min_value, max_value, index,type_fm,line, column) :
        self.expre = expre
        self.min_value = min_value
        self.max_value = max_value
        self.index = index
        self.alias = f'{type_fm}({self.expre.alias},{self.min_value.alias},{self.max_value.alias},{self.index.alias})'
        self.line = line
        self.column = column
        
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
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Trunc(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value,type_fm,line, column) :
        self.value = value
        self.alias = f'{type_fm}({self.value.alias})'
        self.line = line
        self.column = column
    
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            value = self.value.process(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.trunc(value.value), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Random(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self,type_fm,line, column) :
        self.alias = f'{type_fm}()'
        self.line = line
        self.column = column
    
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            return PrimitiveData(DATA_TYPE.NUMBER, randint(0,1), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Greatest(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, val_array,type_fm,line, column) :
        self.val_array = val_array
        self.alias = f'{type_fm}({obtain_string(self.val_array)})'
        self.line = line
        self.column = column
        
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            array = operating_list_number(self.val_array, environment)
            return PrimitiveData(DATA_TYPE.NUMBER, max(array), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")


class Least(Expression):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, val_array,type_fm,line, column) :
        self.val_array = val_array
        self.alias = f'{type_fm}({obtain_string(self.val_array)})'
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        try:
            array = operating_list_number(self.val_array, environment)
            return PrimitiveData(DATA_TYPE.NUMBER, min(array), self.line, self.column)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")