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

class Identificadordb(Instruccion):
    def __init__(self, id):
        self.id = id

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)
