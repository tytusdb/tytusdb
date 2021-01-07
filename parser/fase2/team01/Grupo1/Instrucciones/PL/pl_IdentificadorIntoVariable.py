import sys
sys.path.append('../Grupo1/Instrucciones')

from instruccion import *
from Primitivo import *
from Error import *

class pl_IdentificadorIntoVariable(Instruccion):

    def __init__(self, column, variable):
        self.column = column
        self.variable = variable

    def __repr__(self):
        return str(self.__dict__)

class pl_IdentificadorIntoStrictVariable(Instruccion):
    def __init__(self, column, variable):
        self.column = column
        self.variable = variable


    def __repr__(self):
        return str(self.__dict__)
