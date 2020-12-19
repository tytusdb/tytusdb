import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Insert(Instruccion):

    def __init__(self, tableid, values = []):
        self.tableid = tableid
        self.values = values

    def execute(self):
        print(self)
        return self

    def __repr__(self):
        return str(self.__dict__)
