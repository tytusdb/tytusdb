import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Librerias/storageManager')
sys.path.append('../Grupo1/Utils')

from instruccion import *
from Error import *
from jsonMode import *

from TablaSimbolos import *

class pl_cadval(Instruccion):

    def __init__(self, t):
        for i in t.slice:
            self.cadval += i.value 
     
        

    def execute(self):
        return self.notv

    def __repr__(self):
        return str(self.__dict__)

class cadval(Instruccion):

    def __init__(self, t ):
        self.argIf = argIf
        self.argCondicion1 = argCondicion1
        self.argInstruccion1 = argInstruccion1
        self.argelsif = argelsif
        self.argelse = argelse
        self.arginstruccion3 = arginstruccion3

    def execute(self):
        return self.notv

    def __repr__(self):
        return str(self.__dict__)