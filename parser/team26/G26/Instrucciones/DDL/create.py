import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Create(Instruccion):

    def __init__(self, type, list):
        self.type = type
        self.list = list

    def execute(self):
        return self.type

    def __repr__(self):
        return str(self.__dict__)
