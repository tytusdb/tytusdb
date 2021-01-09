from Expresiones.Primitivo import Primitive
import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Utils')
sys.path.append('../Grupo1/Expresiones')
sys.path.append('../Grupo1/Librerias/storageManager')
sys.path.append('../Grupo1/Librerias/prettytable')

from jsonMode import *
from instruccion import *
from Error import *
from Primitivo import *
from datetime import *
from TablaSimbolos import *
from prettytable import *
from operator import itemgetter

import math
import random
import hashlib


class pl_excepcion(Instruccion):

    def __init__(self, val):
        self.val = val

    def execute(self):
        return self.notv

    def __repr__(self):
        return str(self.__dict__)

class ListaWhenExcepcion(Instruccion):
    #puede venir asterisco(*) entonces tipo == True
    #puede venir un select completo -> Tipo == False
    def __init__(self, arg0,arg1,whentipo,val):
        self.val = val
        self.whentipo = whentipo
        self.arg0 = arg0
        self.arg1 = arg1


    def execute(self, data):
        return self

    def __repr__(self):
        return str(self.__dict__)