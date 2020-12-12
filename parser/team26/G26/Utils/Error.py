import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Error(Instruccion):

    def __init__(self, type, desc, line, column):
        self.type = type
        self.desc = desc
        self.line = line
        self.column = column

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)
