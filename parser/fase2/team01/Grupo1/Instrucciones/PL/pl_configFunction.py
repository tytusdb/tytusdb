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

    def __init__(self, arg0,arg1,Condiciones):
        self.Condiciones = Condiciones
        self.arg0 = arg0
        self.arg1 = arg1

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)


class ReturnParams(Instruccion):

    def __init__(self, arg0,arg1,paramReturn, paramNext, paramQuery, paramArg):
        self.paramReturn = paramReturn
        self.paramNext = paramNext
        self.paramQuery = paramQuery
        self.paramArg = paramArg
        self.arg0 = arg0
        self.arg1 = arg1


    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)


class pl_execute(Instruccion):

    def __init__(self, arg0,arg1,arg1cad,arg2into, arg3strict,arg4idinto,arg5using,arg6lstexp):
        self.arg1cad = arg1cad
        self.arg2into = arg2into
        self.arg3strict = arg3strict
        self.arg4idinto = arg4idinto
        self.arg5using = arg5using
        self.arg6lstexp = arg6lstexp
        self.arg0 = arg0
        self.arg1 = arg1


    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)


class pl_call(Instruccion):

    def __init__(self,arg0,arg1, argCall,argNameStoreProcedure,arglist):
        self.argCall = argCall  
        self.argNameStoreProcedure = argNameStoreProcedure
        self.arglist = arglist
        self.arg0 = arg0
        self.arg1 = arg1


    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

        