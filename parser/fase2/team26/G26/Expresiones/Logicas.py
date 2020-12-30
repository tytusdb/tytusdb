import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')

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
            try:
                left = self.leftOperator.executeInsert(data, valoresTabla)
            except:
                left = self.leftOperator.execute(data, valoresTabla)
            

        try:
            right = self.rightOperator.execute()
        except:
            try:
                right = self.rightOperator.executeInsert(data, valoresTabla)
            except:
                right = self.rightOperator.execute(data, valoresTabla)
            

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
