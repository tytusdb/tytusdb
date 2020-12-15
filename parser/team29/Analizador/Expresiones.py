from abc import abstractmethod
from enum import Enum
from typing import Type

from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from Funciones import MathFunctions as mf
from Funciones import TrigonometricFunctions as trf

class TYPE(Enum):
    NUMBER = 1
    STRING = 2
    BOOLEAN = 3


class Expresion:
    '''
      Esta clase representa una expresión
    '''
    @abstractmethod
    def execute(self):
        pass


class ExpresionUnaria(Expresion):
    '''
      Esta clase recibe un parametro de expresion 
      para realizar operaciones unarias
    '''
    def __init__(self, exp, operador):
        self.exp = exp
        self.operador = operador
        self.lineno = 0
        self.temp = str(operador) + exp.temp

    def execute(self):
        try:
            if self.operador == '-':
                value = self.exp.execute().value * -1
            else:
                value = self.exp.execute().value
            return Primitivos("Null", value)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido")
            return Primitivos(None, None)


class ExpresionBinaria(Expresion):
    '''
      Esta clase recibe dos parametros de expresion 
      para realizar operaciones entre ellas
    '''
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.temp = exp1.temp + str(operador) + exp2.temp
        self.lineno = 0

    def execute(self):
        try:
            if self.operador == '+':
                value = self.exp1.execute().value + self.exp2.execute().value
            elif self.operador == '-':
                value = self.exp1.execute().value - self.exp2.execute().value
            elif self.operador == '*':
                value = self.exp1.execute().value * self.exp2.execute().value
            elif self.operador == '/':
                value = self.exp1.execute().value / self.exp2.execute().value
            elif self.operador == '^':
                value = self.exp1.execute().value ** self.exp2.execute().value
            elif self.operador == '%':
                value = self.exp1.execute().value % self.exp2.execute().value
            else:
                value = self.exp1.execute().value + self.exp2.execute().value
            return Primitivos("None", value)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido")
        return Primitivos(None, None)


class Primitivos(Expresion):
    '''
    Esta clase contiene los tipos primitivos 
    de datos como STRING, NUMBER, BOOLEAN
    '''
    def __init__(self, tipo, value):
        self.tipo = tipo
        self.value = value
        self.temp = str(value)
        self.lineno = 0

    def execute(self):
        return self


class NombreColumna(Expresion):
    '''
    Esta clase XD
    '''
    def __init__(self, tabla, columna):
        self.tabla = tabla
        self.columna = columna
        self.lineno = 0


class ExpresionCompBinaria(Expresion):
    '''
    Esta clase contiene las expresiones binarias de comparacion 
    que devuelven un booleano.
    '''
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.temp = exp1.temp + str(operador) + exp2.temp

    def execute(self):
        try:
            if self.operador == '<':
                value = self.exp1.execute().value < self.exp2.execute().value
            elif self.operador == '>':
                value = self.exp1.execute().value > self.exp2.execute().value
            elif self.operador == '>=':
                value = self.exp1.execute().value >= self.exp2.execute().value
            elif self.operador == '<=':
                value = self.exp1.execute().value <= self.exp2.execute().value
            elif self.operador == '!=':
                value = self.exp1.execute().value != self.exp2.execute().value
            elif self.operador == '<>':
                value = self.exp1.execute().value != self.exp2.execute().value
                '''
                TODO: Cambiar en el lexico que las palabras reservadas
                devuelvan el lexema.toUpper()
                '''
            elif self.operador == 'ISDISTINCTFROM':
                value = self.exp1.execute().value != self.exp2.execute().value
            elif self.operador == 'ISNOTDISTINCTFROM':
                value = self.exp1.execute().value == self.exp2.execute().value
            else:
                value = self.exp1.execute().value == self.exp2.execute().value
            return Primitivos(TYPE.BOOLEAN, value)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido")
            return Primitivos(None, None)


class ExpresionCompTernaria(Expresion):
    '''
    Esta clase contiene las expresiones ternarias de comparacion 
    que devuelven un booleano.
    '''
    def __init__(self, exp1, exp2, exp3, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.operador = operador
        self.temp = exp1.temp + str(operador) + exp2.temp

    def execute(self):
        try:
            if self.operador == 'BETWEEN':
                value = self.exp1.execute().value > self.exp2.execute().value and self.exp1.execute().value < self.exp3.execute().value
            elif self.operador == 'NOTBETWEEN':
                value = not (self.exp1.execute().value > self.exp2.execute().value and self.exp1.execute().value < self.exp3.execute().value)
            elif self.operador == 'BETWEENSYMMETRIC':
                t1 = self.exp1.execute().value > self.exp2.execute().value and self.exp1.execute().value < self.exp3.execute().value
                t2 = self.exp1.execute().value < self.exp2.execute().value and self.exp1.execute().value > self.exp3.execute().value
                value = t1 or t2
            else:
                value = self.exp1.execute().value > self.exp2.execute().value and self.exp1.execute().value < self.exp3.execute().value
            return Primitivos(TYPE.BOOLEAN, value)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido")
            return Primitivos(None, None)


class ExpresionCompUnaria(Expresion):
    '''
    Esta clase contiene las expresiones unarias de comparacion 
    que devuelven un booleano.
    '''
    def __init__(self, exp1, operador):
        self.exp1 = exp1
        self.operador = operador
        self.temp = exp1.temp + str(operador) 

    def execute(self):
        try:
            if self.operador == 'ISNULL':
                value = self.exp1.execute().value == None
            elif self.operador == 'NOTNULL':
                value = self.exp1.execute().value != None
            elif self.operador == 'ISTRUE':
                value = self.exp1.execute().value == True
            elif self.operador == 'ISFALSE':
                value = self.exp1.execute().value == False
            elif self.operador == 'ISUNKMOWM':
                value = self.exp1.execute().value == None
            elif self.operador == 'ISNOTNULL':
                value = self.exp1.execute().value != None
            elif self.operador == 'ISNOTTRUE':
                value = self.exp1.execute().value != True
            elif self.operador == 'ISNOTFALSE':
                value = self.exp1.execute().value != False
            elif self.operador == 'ISNOTUNKMOWM':
                value = self.exp1.execute().value != None
            else:
                value = False
            return Primitivos(TYPE.BOOLEAN, value)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido")
            return Primitivos(None, None)


class ExpresionBooleanaBinaria(Expresion):
    '''
    Esta clase contiene las expresiones booleanas binarias.
    '''
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.temp = exp1.temp + str(operador) + exp2.temp


    def execute(self):
        try:
            if self.operador == 'AND':
                value = self.exp1.execute().value and self.exp2.execute().value
            elif self.operador == 'OR':
                value = self.exp1.execute().value or self.exp2.execute().value
            else:
                value = False
            return Primitivos(TYPE.BOOLEAN, value)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido 1")
            return Primitivos(None, None)


class ExpresionBooleanaUnaria(Expresion):
    '''
    Esta clase contiene las expresiones booleanas unarias.
    '''
    def __init__(self, exp1, operador):
        self.exp1 = exp1
        self.operador = operador
        self.temp = str(operador) + exp1.temp


    def execute(self):
        try:
            if self.operador == 'NOT':
                value = not self.exp1.execute().value
            else:
                value = self.exp1.execute().value
            return Primitivos(TYPE.BOOLEAN, value)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido 2")
            return Primitivos(None, None)

#---------------------------------------------------------------------

class FunctionCall(Expresion):
    '''
    Esta clase contiene las llamadas a funciones
    '''

    def __init__(self, funcion, params):
        self.funcion = funcion
        self.params = params
        self.temp = str(funcion) + "("
        for t in params : self.temp += t.temp
        self.temp += ")"

    # TODO: Quitar los corchetes iniciales de valores
    def execute(self):
        try:
            valores = [[p.execute().value for p in self.params]]

            if self.funcion == "abs" :
                value = mf.absolute(*valores)
            elif self.funcion == "cbrt" :
                value = mf.cbrt(*valores)
            elif self.funcion == "ceil" :
                value = mf.ceil(*valores)
            elif self.funcion == "ceiling" :
                value = mf.ceiling(*valores)
            elif self.funcion == "degrees" :
                value = mf.degrees(*valores)
            elif self.funcion == "div" :
                value = mf.div(*valores)
            elif self.funcion == "exp" :
                value = mf.exp(*valores)
            elif self.funcion == "factorial" :
                value = mf.factorial(*valores)
            elif self.funcion == "floor" :
                value = mf.floor(*valores)
            elif self.funcion == "gcd" :
                value = mf.gcd(*valores)
            elif self.funcion == "lcm" :
                value = mf.lcm(*valores)
            elif self.funcion == "ln" :
                value = mf.ln(*valores)
            elif self.funcion == "log" :
                value = mf.log(*valores)
            elif self.funcion == "log10" :
                value = mf.log10(*valores)             
            elif self.funcion == "mod" :
                value = mf.mod(*valores)
            elif self.funcion == "pi":
                value = mf.pi()
            elif self.funcion == "power" :
                value = mf.pow(*valores)
            elif self.funcion == "radians" :
                value = mf.radians(*valores)
            elif self.funcion == "round" :
                value = mf.round(*valores)
            elif self.funcion == "sign" :
                value = mf.sign(*valores)
            elif self.funcion == "sqrt" :
                value = mf.sqrt(*valores)
            elif self.funcion == "trunc" :
                value = mf.truncate_col(*valores)
            elif self.funcion == "width_bucket" :
                value = mf.with_bucket(*valores)
            elif self.funcion == "random" :
                value = mf.random_()   
            elif self.funcion == "acos":
                value = trf.acos(*valores)
            elif self.funcion == "acosd":
                value = trf.acosd(*valores)
            elif self.funcion == "asin":
                value = trf.asin(*valores)
            elif self.funcion == "asind":
                value = trf.asind(*valores)
            elif self.funcion == "atan":
                value = trf.atan(*valores)
            elif self.funcion == "atand":
                value = trf.atand(*valores)
            elif self.funcion == "atan2":
                value = trf.atan2(*valores)
            elif self.funcion == "atan2d":
                value = trf.atan2d(*valores)
            elif self.funcion == "cos":
                value = trf.cos(*valores)
            elif self.funcion == "cosd":
                value = trf.cosd(*valores)
            elif self.funcion == "cot":
                value = trf.cot(*valores)
            elif self.funcion == "cotd":
                value = trf.cotd(*valores)
            elif self.funcion == "sin":
                value = trf.sin(*valores)
            elif self.funcion == "sind":
                value = trf.sind(*valores)
            elif self.funcion == "tan":
                value = trf.tan(*valores)
            elif self.funcion == "tand":
                value = trf.tand(*valores)
            elif self.funcion == "sinh":
                value = trf.sinh(*valores)
            elif self.funcion == "cosh":
                value = trf.cosh(*valores)
            elif self.funcion == "tanh":
                value = trf.tanh(*valores)
            elif self.funcion == "asinh":
                value = trf.asinh(*valores)
            elif self.funcion == "acosh":
                value = trf.acosh(*valores)
            elif self.funcion == "atanh":
                value = trf.atanh(*valores)
            else :
                value = valores[0]
            if isinstance(value, list):
                if len(value) <= 1:
                    value = value[0]
            
            return Primitivos(None, value)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido")
        return Primitivos(None, None)

        