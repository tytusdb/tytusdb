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