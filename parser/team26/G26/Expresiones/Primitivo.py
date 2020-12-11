import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Primitive(Instruccion):

    def __init__(self, val):
        self.val = val

    def execute(self):
        return self.val

    def __repr__(self):
        return str(self.__dict__)
