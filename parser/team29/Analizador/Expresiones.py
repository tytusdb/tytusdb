from abc import abstractmethod
from enum import Enum
from typing import Type


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