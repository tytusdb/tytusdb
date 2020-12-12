import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Logicas(Instruccion):

    def __init__(self, leftOperator, rightOperator, sign):
        self.leftOperator = leftOperator
        self.rightOperator = rightOperator
        self.sign = sign

    def execute(self):
        return self.sign

    def __repr__(self):
        return str(self.__dict__)
