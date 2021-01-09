import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Librerias/storageManager')
sys.path.append('../Grupo1/Utils')

from instruccion import *
from Error import *
from jsonMode import *

from TablaSimbolos import *

class IFNOTFOUND(Instruccion):

    def __init__(self, val):
        self.val = val

    def execute(self):
        return self.notv

    def __repr__(self):
        return str(self.__dict__)


class IFELSEELSIF(Instruccion):

    def __init__(self,arg0,arg1,  argIf, argCondicion1, argInstruccion1, argelsif, argelse, arginstruccion3 ):
        self.argIf = argIf
        self.argCondicion1 = argCondicion1
        self.argInstruccion1 = argInstruccion1
        self.argelsif = argelsif
        self.argelse = argelse
        self.arginstruccion3 = arginstruccion3
        self.arg0 = arg0
        self.arg1 = arg1


    def execute(self):
        return self.notv

    def __repr__(self):
        return str(self.__dict__)



class ELSIF(Instruccion):

    def __init__(self, arg0,arg1,argelsif, argCondicion, argInstruccion):
        self.argelsif = argelsif
        self.argCondicion = argCondicion
        self.argInstruccion = argInstruccion
        self.arg0 = arg0
        self.arg1 = arg1

    def execute(self):
        return self.notv

    def __repr__(self):
        return str(self.__dict__)