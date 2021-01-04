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

class FunctionConfig(Instruccion):

    global columnasAceptadas

    def __init__(self, parametros, fromopcional):
        self.parametros = parametros
        self.fromopcional = fromopcional


class PrintStrictParam(Instruccion):

    def __init__(self, Condiciones):
        self.Condiciones = Condiciones

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)


class ReturnParams(Instruccion):

    def __init__(self, paramReturn, paramNext, paramQuery, paramArg):
        self.paramReturn = paramReturn
        self.paramNext = paramNext
        self.paramQuery = paramQuery
        self.paramArg = paramArg

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)


class pl_execute(Instruccion):

    def __init__(self, arg1cad,arg2into, arg3strict,arg4idinto,arg5using,arg6lstexp):
        self.arg1cad = arg1cad
        self.arg2into = arg2into
        self.arg3strict = arg3strict
        self.arg4idinto = arg4idinto
        self.arg5using = arg5using
        self.arg6lstexp = arg6lstexp

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)


class pl_call(Instruccion):

    def __init__(self, argCall,argNameStoreProcedure,arglist):
        self.argCall = argCall  
        self.argNameStoreProcedure = argNameStoreProcedure
        self.arglist = arglist

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

        
