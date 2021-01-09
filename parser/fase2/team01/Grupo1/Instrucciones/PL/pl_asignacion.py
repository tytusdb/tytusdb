import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Librerias/storageManager')
sys.path.append('../Grupo1/Utils')

from instruccion import *
from Error import *
from jsonMode import *
from TablaSimbolos import *

class pl_asignacion(Instruccion):

    def __init__(self,arg0,arg1, variable, asignaciones):
        self.variable = variable
        self.asignaciones = asignaciones
        self.arg0 = arg0
        self.arg1 = arg1


    def __repr__(self):
        return str(self.__dict__)

