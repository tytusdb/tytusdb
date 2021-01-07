
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

class pl_raise(Instruccion):

    global columnasAceptadas

    def __init__(self, parametros, fromopcional):
        self.parametros = parametros
        self.fromopcional = fromopcional

    def __repr__(self):
        return str(self.__dict__)

class pl_raiseexception(Instruccion):
    def __init__(self, cadena, valor ):
        self.cadena = cadena
        self.valor = valor

    def __repr__(self):
        return str(self.__dict__)

