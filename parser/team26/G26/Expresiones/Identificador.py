import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Identificador(Instruccion):

    def __init__(self, table, column):
        self.column = column

    def execute(self):
        return self.val

    def __repr__(self):
        return str(self.__dict__)
