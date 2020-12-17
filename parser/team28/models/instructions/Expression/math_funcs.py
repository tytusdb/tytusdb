from models.instructions.shared import Instruction
from models.instructions.Expression.expression import DATA_TYPE, PrimitiveData
import math
from random import random

class Abs(Instruction):
    '''
        Valor absoluto de una columna tipo entero o de un valor.
    '''
    def __init__(self,  value) :
        self.value = value

    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.fabs(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Cbrt(Instruction):
    '''
        Raiz Cubica de un numero o una columna tipo entero.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.pow(value, 1/3))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Ceil(Instruction):
    '''
        Redondear cualquier valor decimal positivo o negativo como
        mayor que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.ceil(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Ceiling(Instruction):
    '''
        Redondear cualquier valor decimal positivo o
        negativo como mayor que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.ceil(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Degrees(Instruction):
    '''
        Se usa para devolver los valores en grados de radianes 
        como se especifica en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))
    
    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.degrees(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Div(Instruction):
    '''
        Se utiliza para devolver el cociente entero de
        una división como se especifica en el argumento.
    '''
    def __init__(self,  dividendo, divisor) :
        self.dividendo = dividendo
        self.divisor = divisor
    
    def __repr__(self):
        return str(vars(self))
    
    def execute(self, environment):
        try:
            value1 = self.dividendo.execute(environment)
            value2 = self.divisor.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, value1 // value2)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Exp(Instruction):
    '''
        La función se usa para devolver la exponenciación de
        un número como se especifica en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.exp(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Factorial(Instruction):
    '''
        Se puede utilizar la libreria Math de Python **
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.factorial(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Floor(Instruction):
    '''
        Se usa para devolver el valor después de redondear 
        cualquier valor decimal positivo o negativo 
        como más pequeño que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))
    
    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.floor(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Gcd(Instruction):
    '''
        Se puede utilizar la libreria Math de Python. 
        Maximo Comun Divisor *
    '''
    def __init__(self,  value1, value2) :
        self.value1 = value1
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value1 = self.value1.execute(environment)
            value2 = self.value2.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.gcd(value1, value2))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Ln(Instruction):
    '''
        Logaritmo natural de un numero ***
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.log(value)) #With one argument, return the natural logarithm of x (to base e).
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Log(Instruction):
    '''
        Logaritmo base 10 de un número.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.log10(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Mod(Instruction):
    '''
        La función se usa para devolver el resto de una
        división de dos números, como se especifica 
        en el argumento
    '''
    def __init__(self,  value1, value2) :
        self.value1 = value1
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value1 = self.value1.execute(environment)
            value2 = self.value2.execute(environment)

            return PrimitiveData(DATA_TYPE.NUMBER, value1%value2)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Pi(Instruction):
    '''
        Retorna el valor de la constant PI
        ***** TODO: SIN ARGUMENTOS *****
    '''
    def __init__(self) :
        pass

    def __repr__(self):
        return str(vars(self))
    
    def execute(self, environment):
        return PrimitiveData(DATA_TYPE.NUMBER,math.pi)

class Power(Instruction):
    '''
        La función se usa para devolver el valor de un 
        número elevado a la potencia de otro número, 
        proporcionado en el argumento.
    '''
    def __init__(self, base, exp) :
        self.base = base
        self.exp = exp
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value1 = self.base.execute(environment)
            value2 = self.exp.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.pow(value1, value2))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Radians(Instruction):
    '''
        La función se usa para devolver el valor en radianes 
        a partir de grados, proporcionado en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.radians(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Round(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self,  value, n_digits = 0) :
        self.value = value
        self.n_digits = n_digits
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
            try:
                value = self.value.execute(environment)
                digits = self.n_digits.execute(environment)
                if self.n_digits == 0:
                    return PrimitiveData(DATA_TYPE.NUMBER, math.trunc(value))
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, round(value, digits))
            except TypeError:
                print("Error de tipo")
                print(self)
                return
            except:
                print("FATAL ERROR, ni idea porque murio, F --- Math")

class Sign(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
            try:
                value = self.value.execute(environment)
                if value >= 0:
                    return PrimitiveData(DATA_TYPE.NUMBER, 1)
                else:
                    return PrimitiveData(DATA_TYPE.NUMBER, -1)
            except TypeError:
                print("Error de tipo")
                print(self)
                return
            except:
                print("FATAL ERROR, ni idea porque murio, F --- Math")

class Sqrt(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.sqrt(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class WithBucket(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self,  value1, value2, value3, value4) :
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            # value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, 1)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Trunc(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            value = self.value.execute(environment)
            return PrimitiveData(DATA_TYPE.NUMBER, math.trunc(value))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Random(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self) :
        pass
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            return PrimitiveData(DATA_TYPE.NUMBER, random())
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")
#TODO: PROBAR GREATEST Y LEAST
class Greatest(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, val_array) :
        self.val_array = val_array
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            array = self.val_array.execute(environment)
            return PrimitiveData(self.val_array.DATA_TYPE, max(array))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")

class Least(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self, val_array) :
        self.val_array = val_array
    
    def __repr__(self):
        return str(vars(self))

    def execute(self, environment):
        try:
            array = self.val_array.execute(environment)
            return PrimitiveData(self.val_array.DATA_TYPE, min(array))
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Math")