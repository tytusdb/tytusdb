import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Condicionales(Instruccion):

    def __init__(self, leftOperator, rightOperator, sign, extra):
        self.leftOperator = leftOperator
        self.rightOperator = rightOperator
        self.sign = sign
        self.extra = extra

    def execute(self):
        return self.sign

    def __repr__(self):
        return str(self.__dict__)

class Between(Instruccion):

    def __init__(self, type, val1, val2):
        self.type = type
        self.val1 = val1
        self.val2 = val2

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
