import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Select(Instruccion):

    def __init__(self, parametros, fromopcional):
        self.parametros = parametros
        self.fromopcional = fromopcional

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class FromOpcional(Instruccion):

    def __init__(self, parametros,asopcional,whereopcional):
        self.parametros = parametros
        self.asopcional = asopcional
        self.whereopcional = whereopcional

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class ElseOpcional(Instruccion):

    def __init__(self, elseopcional):
        self.elseopcional = elseopcional

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class QuerysSelect(Instruccion):

    def __init__(self, operador,select1,allopcional,select2):
        self.operador = operador
        self.select1 = select1
        self.allopcional = allopcional
        self.select2 = select2

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__) 

class ParametrosFrom(Instruccion):

    def __init__(self, parametro):
        self.operador = parametro

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)       

class WhereOpcional(Instruccion):

    def __init__(self, condiciones,groupbyopcional):
        self.operador = condiciones
        self.groupbyopcional = groupbyopcional

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)       

class GroupByOpcional(Instruccion):

    def __init__(self, lista,havingopcional):
        self.lista = lista
        self.havingopcional = havingopcional

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)  

class HavingOpcional(Instruccion):

    def __init__(self, Condiciones):
        self.Condiciones = Condiciones

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)      



class Allopcional(Instruccion):

    def __init__(self, allopcional):
        self.allopcional = allopcional

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class Case(Instruccion):

    def __init__(self, whenCase,thenCase):
        self.whenCase = whenCase
        self.thenCase = thenCase


    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)




class ParametrosSelect(Instruccion):

    def __init__(self, distinct, listadeseleccion):
        self.distinct = distinct
        self.listadeseleccion = listadeseleccion

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class As(Instruccion):

    def __init__(self, argumento):
        self.argumento = argumento

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class Fecha(Instruccion):

    def __init__(self, argumento):
        self.argumento = argumento

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class TipoRound(Instruccion):

    def __init__(self, arg1):
        self.arg1 = arg1

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class FuncionBinaria(Instruccion):

    def __init__(self, operador, arg1,arg2,arg3):
        self.operador = operador
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class FucionTrigonometrica(Instruccion):

    def __init__(self, tipofuncionTrigonometrica, arg1):
        self.tipofuncionTrigonometrica = tipofuncionTrigonometrica
        self.arg1 = arg1

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class OperadoresSelect(Instruccion):

    def __init__(self, tipoOperador, arg1,arg2):
        self.tipoOperador = tipoOperador
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class FuncionMatematica(Instruccion):

    def __init__(self, tipofuncionmatematica, arg1,arg2,arg3,arg4):
        self.tipofuncionmatematica = tipofuncionmatematica
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class FuncionFecha(Instruccion):

    def __init__(self, tipofuncionfehca, arg1,arg2):
        self.tipofuncionfehca = tipofuncionfehca
        self.arg1 = arg1
        self.arg2 = arg2
    
    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class FuncionMatematicaSimple(Instruccion):

    def __init__(self, operador, argumento):
        self.argumento = argumento
        self.operador = operador

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)