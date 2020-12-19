import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')

from instruccion import *
from Error import *
from Primitivo import *

import math
import random

class Select(Instruccion):

    def __init__(self, parametros, fromopcional):
        self.parametros = parametros
        self.fromopcional = fromopcional

    def execute(self, data):
        if self.parametros != None:
            return self.parametros.execute(data)
        if self.fromopcional != None:
            #self.fromopcional.execute(data)
            ''
        return self

    def __repr__(self):
        return str(self.__dict__)


class Casos(Instruccion):

    def __init__(self, caso,elsecase):
        self.caso = caso
        self.elsecase = elsecase

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class FromOpcional(Instruccion):

    def __init__(self, parametros,whereogroup):
        self.parametros = parametros
        self.whereopcional = whereogroup

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class ParametrosFromR(Instruccion):

    def __init__(self, parametros,asop):
        self.parametros = parametros
        self.asop = asop

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class ListaDeSeleccionadosConOperador(Instruccion):
    #puede venir grastest con arg1
    #least con arg 1
    #case con arg1 y 2
    def __init__(self, operador,arg1,arg2):
        self.operador = operador
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class ListaDeSeleccionados(Instruccion):
    #puede venir asterisco(*) entonces tipo == True
    #puede venir un select completo -> Tipo == False
    def __init__(self, argumento,tipo):
        self.argumento = argumento
        self.tipo = tipo

    def execute(self, data):
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
    #true select
    #false id
    def __init__(self, parametro,tipoparametro):
        self.operador = parametro
        self.tipoparametro = tipoparametro

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

class ListaDeSeleccionadosR(Instruccion):

    def __init__(self, listaseleccionados,asopcional):
        self.listaseleccionados = listaseleccionados
        self.asopcional = asopcional


    def execute(self, data):
        return self.listaseleccionados.execute(data)
        #return self

    def __repr__(self):
        return str(self.__dict__)



class ParametrosSelect(Instruccion):
    #true si hay distinct
    #false no hay distinct
    def __init__(self, distinct, listadeseleccion):
        self.distinct = distinct
        self.listadeseleccion = listadeseleccion

    def execute(self, data):
        if self.listadeseleccion != None:
            for selection in self.listadeseleccion:
                return selection.execute(data)
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

class TipoRound(Instruccion):

    def __init__(self, arg1):
        self.arg1 = arg1

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)


class FuncionBinaria(Instruccion):
    #convert tiene un tipo no un argumento
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
        # | square
        # ||  cube
        # & and
        # | or dos args
        # # <- xor
        # ~ not
        # << sl(bitwise shift left) 
        # >> sr(bitwise shift right)
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

    def execute(self, data):
        tipo = str(self.tipofuncionmatematica)
        if tipo == 'abs' : 
            'valor absoluto - FALTA IDS'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                return Primitive('float', math.fabs(argumento.val))
            else :
                error = Error('Semántico', 'Error de tipos en ABS, solo se aceptan valores numéricos, se obtuvo: '+argumento.val, 0, 0)
                return error
        elif tipo == 'cbrt' : 
            'raíz cúbica - solo numeros positivos'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = argumento.val**(1/3)
                    if isinstance(reto, int) :
                        return Primitive('integer', reto)
                    
                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en CBRT, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CBRT, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'ceil' : 
            'redondear - solo numeros positivos'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.ceil(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'ceiling' : 
            'redondear - solo numeros positivos'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.ceil(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'degrees' : 
            'radianes a grados - '
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.degrees(argumento.val)
                return Primitive('float', reto)
            else :
                error = Error('Semántico', 'Error de tipos en DEGREES, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'div' : 
            'cociente - '
            argumento = self.arg1.execute()
            argumento2 = self.arg2.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento2.type == 'float' :
                    reto = math.trunc(argumento.val / argumento2.val)
                    return Primitive('integer', reto)
                else:
                    error = Error('Semántico', 'Error de tipos en DIV, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en DIV, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'exp' : 
            'e^ argumento - '
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.exp(argumento.val)
                return Primitive('float', reto)
            else :
                error = Error('Semántico', 'Error de tipos en EXP, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'factorial' : 
            'x! - solo numeros positivos'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' :
                if argumento.val > 0 :
                    reto = math.factorial(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en FACTORIAL, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en FACTORIAL, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error
        

        elif tipo == 'floor' : 
            'redondear al menor -'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.trunc(argumento.val)
                return Primitive('integer', reto)
            else :
                error = Error('Semántico', 'Error de tipos en FLOOR, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'gcd' : 
            'MCD - '
            argumento = self.arg1.execute()
            argumento2 = self.arg2.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento2.type == 'float' :
                    if argumento.val > 0 and argumento2.val > 0 :
                        reto = math.gcd(argumento.val, argumento2.val)
                        return Primitive('integer', reto)
                    else :
                        error = Error('Semántico', 'Error de tipos en GCD, solo se aceptan valores numéricos positivos', 0, 0)
                        return error
                else:
                    error = Error('Semántico', 'Error de tipos en GCD, solo se aceptan valores numéricos, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en GCD, solo se aceptan valores numéricos, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'ln' : 
            'Ln -'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.log(argumento.val)
                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en Ln, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en Ln, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'log' : 
            'Log10 -'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.log10(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en LOG, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en LOG, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'mod' : 
            'modulo - '
            argumento = self.arg1.execute()
            argumento2 = self.arg2.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento.type == 'float' :
                    reto = math.remainder(argumento.val, argumento2.val)
                    return Primitive('integer', reto)
                else:
                    error = Error('Semántico', 'Error de tipos en MOD, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en MOD, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'pi' : 
            'PI'
            return math.pi


        elif tipo == 'power' : 
            'power - solo positivos'
            argumento = self.arg1.execute()
            argumento2 = self.arg2.execute()
            if argumento.type == 'integer' or 'float' :
                if argumento2.type == 'integer' or 'float' :
                    if argumento.val > 0 and argumento2.val > 0 :
                        reto = math.pow(argumento.val, argumento2.val)
                        if isinstance(reto, int) : return Primitive('integer', reto)
                        else : return Primitive('float', reto)
                    else :
                        error = Error('Semántico', 'Error de tipos en POWER, solo se aceptan valores numéricos positivo', 0, 0)
                        return error
                else:
                    error = Error('Semántico', 'Error de tipos en POWER, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en POWER, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'radians' : 
            'grados a radianes - '
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0:
                    reto = math.radians(argumento.val)
                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en RADIANS, solo se aceptan valores numéricos positivo', 0, 0)
                    return error
                
            else :
                error = Error('Semántico', 'Error de tipos en RADIANS, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'round' : 
            'round - redondear n decimales'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if self.arg2 == None :
                    'numero de redondeo no específicado'
                    reto = round(argumento.val)
                    return Primitive('integer', reto)
                else:
                    'numero de redondeo específicado'
                    argumento2 = self.arg2.execute()
                    if argumento2.type == 'integer' or rgumento2.type == 'float' :
                        if argumento2.val > 0 :
                            reto = round(argumento.val, argumento2.val)
                            if isinstance(reto, int): return Primitive('integer', reto)
                            else: return Primitive('float', reto)
                        else :
                            error = Error('Semántico', 'Error de tipos en ROUND, solo se aceptan valores numéricos positivo', 0, 0)
                            return error
                    else:
                        error = Error('Semántico', 'Error de tipos en ROUND, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento2.val, 0, 0)
                        return error
            else :
                error = Error('Semántico', 'Error de tipos en ROUND, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'sign' : 
            'devuelve signo - 1 o -1'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0:
                    return Primitive('integer', 1)
                else :
                    return Primitive('integer', -1)
                
            else :
                error = Error('Semántico', 'Error de tipos en SIGN, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'sqrt' : 
            'grados a radianes - '
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0:
                    reto = math.sqrt(argumento.val)
                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en SQRT, solo se aceptan valores numéricos positivo', 0, 0)
                    return error
                
            else :
                error = Error('Semántico', 'Error de tipos en SQRT, solo se aceptan valores numéricos, se obtuvo: '+argumento.val, 0, 0)
                return error


        elif tipo == 'width_bucket' : 
            'histograma - argumento1 puede ser una columna'
            argumento = self.arg1.execute()
            argumento2 = self.arg2.execute()
            argumento3 = self.arg3.execute()
            argumento4 = self.arg4.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento2.type == 'float' :
                    if argumento3.type == 'integer' or argumento3.type == 'float' :
                        if argumento4.type == 'integer' or argumento4.type == 'float' :
                            return Primitive('integer', self.widthbucket(int(argumento.val), int(argumento2.val), int(argumento3.val), int(argumento4.val)))
                            #return Primitive('integer', self.widthbucket(9, 1, 12, 4))
                        else:
                            error = Error('Semántico', 'Error de tipos en width_bucket, solo se aceptan valores numéricos', 0, 0)
                            return error
                    else:
                        error = Error('Semántico', 'Error de tipos en width_bucket, solo se aceptan valores numéricos', 0, 0)
                        return error
                else:
                    error = Error('Semántico', 'Error de tipos en width_bucket, solo se aceptan valores numéricos', 0, 0)
                    return error
            else:
                error = Error('Semántico', 'Error de tipos en width_bucket, solo se aceptan valores numéricos', 0, 0)
                return error


        elif tipo == 'trunc' : 
            'grados a radianes - '
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0:
                    reto = math.trunc(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en trunc, solo se aceptan valores numéricos positivo', 0, 0)
                    return error
                
            else :
                error = Error('Semántico', 'Error de tipos en trunc, solo se aceptan valores numéricos, se obtuvo: '+argumento.val, 0, 0)
                return error

        elif tipo == 'random' :
            'random entre 0 and 1'
            return Primitive('integer', random.randint(0,1))


        elif tipo == 'setseed' : 
            ''
        elif tipo == 'scale' : 
            ''

        return self

    def widthbucket(self, nnum, nmin, nmax, nbuckets):
        if nnum < nmin : 
            return 0
        elif nnum > nmax :
            return nbuckets+1
        else:
            bucket_width = (nmax - nmin + 1) / nbuckets
            i = nmin-1
            bucket = 1
            while i < nmax:
                if i+bucket_width > nmax:
                    #if nnum >= i or nnum <= nmax:
                        #return bucket
                    break
                else:
                    if nnum > i and  nnum <= i+bucket_width:
                        #return bucket
                        break
                i = i+bucket_width
                bucket = bucket + 1
            return bucket

    def __repr__(self):
        return str(self.__dict__)


class FuncionFecha(Instruccion):
    #2arg:
    #extract(parte y tamestap) y datepart ( argument y argument)
    def __init__(self, tipofuncionfehca, arg1,arg2):
        self.tipofuncionfehca = tipofuncionfehca
        self.arg1 = arg1
        self.arg2 = arg2
    
    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class FuncionMatematicaSimple(Instruccion):
    #puede venir:
    #Count,max,sum,avg,min
    def __init__(self, operador, argumento):
        self.argumento = argumento
        self.operador = operador

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)