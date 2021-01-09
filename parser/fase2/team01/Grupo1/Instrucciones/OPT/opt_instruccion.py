import sys
sys.path.append('../Grupo1/Instrucciones')

from instruccion import *
from Primitivo import *
from Error import *

class opt_instruccion(Instruccion):

    def __init__(self, arg0,arg1,column1, column2,column3,column4,column5, column6):
        self.arg0 = arg0
        self.arg1 = arg1        

        self.column1 = column1
        self.column2 = column2
        self.column3 = column3
        self.column4 = column4
        self.column5 = column5
        self.column6 = column6


    def __repr__(self):
        return str(self.__dict__)

class opt_instruccionasign(Instruccion):
    def __init__(self,arg0,arg1, column, variable):
        self.column = column
        self.variable = variable
        self.arg0 = arg0
        self.arg1 = arg1        



    def __repr__(self):
        return str(self.__dict__)