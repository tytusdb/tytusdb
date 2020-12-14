import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Types(Instruccion):

    def __init__(self, type, length):
        self.type = type
        self.length = length

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class Char(Instruccion):

    def __init__(self, varying, length):
        self.varying = varying
        self.length = length

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)
