import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Delete(Instruccion):

    def __init__(self, tableid, condiciones = []):
        self.tableid = tableid
        self.condiciones = condiciones

    def execute(self):
        return self.tableid

    def __repr__(self):
        return str(self.__dict__)
