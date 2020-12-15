import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Show(Instruccion):

    def __init__(self, cadena, opcion = False):
        self.cadena = cadena
        self.opcion = opcion

    def execute(self):
        return self.cadena

    def __repr__(self):
        return str(self.__dict__)
