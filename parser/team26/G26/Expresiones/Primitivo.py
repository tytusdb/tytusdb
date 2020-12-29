import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Primitive(Instruccion):

    def __init__(self, type, val):
        self.type = type
        self.val = val

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)
