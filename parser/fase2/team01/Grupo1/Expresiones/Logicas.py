import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Utils')
sys.path.append('../Grupo1/Expresiones')

from instruccion import *
from Error import *
from Primitivo import *

class Logicas(Instruccion):

    def __init__(self, leftOperator, rightOperator, sign):
        self.leftOperator = leftOperator
        self.rightOperator = rightOperator
        self.sign = sign

    def execute(self, data, valoresTabla):
        #Execution of the arguments
        try:
            left = self.leftOperator.execute()
        except:
            left = self.leftOperator.executeInsert(data, valoresTabla)

        try:
            right = self.rightOperator.execute()
        except:
            right = self.rightOperator.executeInsert(data, valoresTabla)

        #checking returns of both arguments in case of error
        if isinstance(left, Error) :
            return left
        if isinstance(right, Error) :
            return right

        #execution of logic conditions
        if self.sign == "and" :
            return left and right
        else :
            'or'
            return left or right


    def repr(self):
        return str(self.__dict__)
