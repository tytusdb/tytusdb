import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Drop(Instruccion):
    #False: Drop table
    #True: Drop database
    def __init__(self, id, dropopt = False):
        self.dropopt = dropopt
        self.id = id

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)