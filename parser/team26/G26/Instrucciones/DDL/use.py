import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Use(Instruccion):

    def __init__(self, dbid):
        self.dbid = dbid

    def execute(self):
        return self.dbid

    def __repr__(self):
        return str(self.__dict__)
