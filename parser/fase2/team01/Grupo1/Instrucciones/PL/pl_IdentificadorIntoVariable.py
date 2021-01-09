import sys
sys.path.append('../Grupo1/Instrucciones')

from instruccion import *
from Primitivo import *
from Error import *

class pl_IdentificadorIntoVariable(Instruccion):

    def __init__(self, arg0,arg1,column, variable):
        self.arg0 = arg0
        self.arg1 = arg1        

        self.column = column
        self.variable = variable

    def __repr__(self):
        return str(self.__dict__)

class pl_IdentificadorIntoStrictVariable(Instruccion):
    def __init__(self,arg0,arg1, column, variable):
        self.column = column
        self.variable = variable
        self.arg0 = arg0
        self.arg1 = arg1        



    def __repr__(self):
        return str(self.__dict__)
