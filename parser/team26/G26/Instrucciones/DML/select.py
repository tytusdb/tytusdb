from Expresiones.Primitivo import Primitive
import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')
sys.path.append('../G26/Librerias/storageManager')

from jsonMode import *
from instruccion import *
from Error import *
from Primitivo import *

import math
import random
import hashlib

class Select(Instruccion):

    global columnasAceptadas

    def __init__(self, parametros, fromopcional):
        self.parametros = parametros
        self.fromopcional = fromopcional

    def execute(self, data):
        fromData = self.fromopcional
        tablas = fromData.execute().execute()
        where = tablas.whereopcional
        directorioTablas = {}
        for tablasSeleccionadas in tablas.parametros:
            if tablasSeleccionadas.asop == None:
                directorioTablas[tablasSeleccionadas.parametros.operador.upper()] = {'fila' : None, 'alias': ''}
            else:
                directorioTablas[tablasSeleccionadas.parametros.operador.upper()] = {'fila' : None, 'alias': tablasSeleccionadas.asop.upper()}

        global columnasAceptadas
        try:
            for keys in directorioTablas.keys():
                data.tablaSimbolos[data.databaseSeleccionada]['tablas'][keys]
        except:
            return Error('Semántico', 'Error(42P01): undefined_table.', 0, 0)

        valores = []
        columnasAceptadas = {}
        for keys in directorioTablas.keys():
            valores.append(keys)
            columnasAceptadas[keys] = []
        if where == None:
            val = self.funcionPosibilidades(data, valores, [], [], directorioTablas, True)
        else:
            val = self.funcionPosibilidades(data, valores, [], [], directorioTablas, False)

        print(columnasAceptadas)
        return self

    def __repr__(self):
        return str(self.__dict__)


    def funcionPosibilidades(self, data, nombres, columna, nombreAux, ordenTablas, noWhere):
        if len(nombres) == 0:
            if noWhere:
                val = 0
                for fila in columna:
                    columnasAceptadas[nombreAux[val]].append(fila)
                    val = val + 1
                ''
            else:
                val = 0
                for fila in columna:
                    ordenTablas[nombreAux[val]]['fila'] = fila
                    val = val + 1
                result = self.fromopcional.whereopcional.operador.execute(data,ordenTablas)
                if isinstance(result, Error):
                    return result

                if result:
                    val = 0
                    for fila in columna:
                        columnasAceptadas[nombreAux[val]].append(fila)
                        val = val + 1
            return 'fin'
        nombre = nombres[0]
        nombres.remove(nombre)
        filas = extractTable(data.databaseSeleccionada, nombre)
        for fila in filas:
            s = fila
            columna.append(fila)
            nombreAux.append(nombre)
            comp = self.funcionPosibilidades(data, nombres, columna, nombreAux, ordenTablas, noWhere)
            columna.remove(s)
            nombreAux.remove(nombre)
        nombres.append(nombre)
        return 'hola'

class Casos(Instruccion):

    def __init__(self, caso,elsecase):
        self.caso = caso
        self.elsecase = elsecase

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)


class FromOpcional(Instruccion):

    def __init__(self,parametros, whereogroup):
        self.parametros = parametros
        self.whereopcional = whereogroup

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class ParametrosFromR(Instruccion):

    def __init__(self, parametros, asop):
        self.parametros = parametros
        self.asop = asop

    def execute(self,data):
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

    def execute(self,data):
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

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class QuerysSelect(Instruccion):

    def __init__(self, operador,select1,allopcional,select2):
        self.operador = operador
        self.select1 = select1
        self.allopcional = allopcional
        self.select2 = select2

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class ParametrosFrom(Instruccion):
    #true select
    #false id
    def __init__(self, parametro,tipoparametro):
        self.operador = parametro
        self.tipoparametro = tipoparametro

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class WhereOpcional(Instruccion):

    def __init__(self, condiciones,groupbyopcional):
        self.operador = condiciones
        self.groupbyopcional = groupbyopcional

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class GroupByOpcional(Instruccion):

    def __init__(self, lista,havingopcional):
        self.lista = lista
        self.havingopcional = havingopcional

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class HavingOpcional(Instruccion):

    def __init__(self, Condiciones):
        self.Condiciones = Condiciones

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)



class Allopcional(Instruccion):

    def __init__(self, allopcional):
        self.allopcional = allopcional

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class Case(Instruccion):

    def __init__(self, whenCase,thenCase):
        self.whenCase = whenCase
        self.thenCase = thenCase


    def execute(self,data):
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
        return self

    def __repr__(self):
        return str(self.__dict__)

class As(Instruccion):

    def __init__(self, argumento):
        self.argumento = argumento

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class TipoRound(Instruccion):

    def __init__(self, arg1):
        self.arg1 = arg1

    def execute(self,data):
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

    def execute(self,data):
        tipo = str(self.tipofuncionTrigonometrica)
        if tipo == 'length':
            argumento = self.arg1.execute()
            if argumento.type == 'string' or argumento.type == 'ID' :
                return Primitive('integer',len(str(argumento.val)))
            else:
                error = Error('Semántico', 'Error de tipos en LENGTH, solo se aceptan valores de cadenas, se obtuvo: '+str(argumento.val), 0, 0)
                return error 
        elif tipo == 'substring' or tipo == 'substr':
            argumento = self.arg1.execute()
            argumento1 = self.arg2.execute()
            argumento2 = self.arg3.execute()
            if argumento.type == 'string' or argumento.type == 'ID' :
                return Primitive('integer',str(argumento.val)[argumento1.val:argumento2.val])
            else:
                error = Error('Semántico', 'Error de tipos en LENGTH, solo se aceptan valores de cadenas, se obtuvo: '+str(argumento.val),0,0)
                return error 
        elif tipo == 'md5':
            argumento = self.arg1.execute()
            if argumento.type == 'string' or argumento.type == 'ID' :
                return Primitive('string',hashlib.md5(str(argumento.val)).hexdigest())
            else:
                error = Error('Semántico', 'Error de tipos en MD5, solo se aceptan valores de cadenas, se obtuvo: '+str(argumento.val),0,0)
                return error 
        elif tipo == 'sha256':
            argumento = self.arg1.execute()
            if argumento.type == 'string' or argumento.type == 'ID' :
                return Primitive('string',hashlib.sha256(str(argumento.val)).hexdigest())
            else:
                error = Error('Semántico', 'Error de tipos en MD5, solo se aceptan valores de cadenas, se obtuvo: '+str(argumento.val),0,0)
                return error  
        return self

    def __repr__(self):
        return str(self.__dict__)

class FucionTrigonometrica(Instruccion):

    def __init__(self, tipofuncionTrigonometrica, arg1,arg2):
        self.tipofuncionTrigonometrica = tipofuncionTrigonometrica
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self,data):
        tipo = str(self.tipofuncionTrigonometrica)
        if tipo == 'acos' :
            'devuelve el coseno inverso'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try :
                    result = Primitive('float',math.acos(argumento.val))
                    return result
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ACOS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error   
            else :
                error = Error('Semántico', 'Error de tipos en ACOS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'acosd' :
            'devuelve el coseno inverso en grados '
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.degrees(math.acos(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ACOSD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en ACOSD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'asin' :
            'devuelve el seno inverso'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.asin(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ASIN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en ASIN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'asind' :
            'devuelve el seno inverso en grados'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.degrees(math.asin(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ASIND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en ASIND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atan' :
            'devuelve el tangente inverso'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                try: 
                    return Primitive('float',math.atan(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ATAN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en ATAN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atand' :
            'devuelve el tangente inverso en grados'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.degrees(math.atan(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ACOS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en ATAND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atan2' :
            'devuelve el tangente inverso de una div'
            argumento =  self.arg1.execute()
            argumento2 = self.arg2.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                if argumento2.type == 'integer' or argumento2.type == 'float' : 
                    try:
                        return Primitive('float',math.atan2(argumento.val,argumento2.val))
                    except :
                        error = Error('Semántico', 'Error de DOMINIO en ATAN2, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                        return error 
                else :
                    error = Error('Semántico', 'Error de tipos en ATAN2, solo se aceptan valores numéricos, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ATAN2, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atan2d' :
            'devuelve el tangente inverso de una div en grados'
            argumento =  self.arg1.execute()
            argumento2 = self.arg2.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                if argumento2.type == 'integer' or argumento2.type == 'float' : 
                    try:
                        return Primitive('float',math.degrees(math.atan2(argumento.val,argumento2.val)))
                    except :
                        error = Error('Semántico', 'Error de DOMINIO en ATAN2D, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                        return error 
                else :
                    error = Error('Semántico', 'Error de tipos en ATAN2D, solo se aceptan valores numéricos, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ATAN2D, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cos' :
            'devuelve el coseno'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.cos(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en COS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cosd' :
            'devuelve el coseno en grados'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.degrees(math.cos(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COSD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en COSD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cot' :
            'devuelve el cotangente'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.cos(argumento.val)/math.sin(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COT, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en COT, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cotd' :
            'devuelve el cotangente en grados'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.degrees(math.cos(argumento.val)/math.sin(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COTD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en COTD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'sin' :
            'devuelve el sin'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.sin(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en SIN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en SIN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'sind' :
            'devuelve el coseno en grados'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.degrees(math.sin(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en SIND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en SIND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'tan' :
            'devuelve el tan'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.tan(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en TAN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en TAN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'tand' :
            'devuelve el tan en grados'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.degrees(math.tan(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en TAND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en TAND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'sinh' :
            'devuelve el sinh'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.sinh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en SINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en SINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cosh' :
            'devuelve el cosh'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.cosh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COSH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en COSH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'tanh' :
            'devuelve el tanh'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.tanh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en TANH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en SINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'asinh' :
            'devuelve el asinh'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.asinh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ASINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en ASINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'acosh' :
            'devuelve el asinh'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.asinh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ACOSH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en ACOSH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atanh' :
            'devuelve el atanh'
            argumento =  self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' : 
                try:
                    return Primitive('float',math.atanh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ATANH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error 
            else :
                error = Error('Semántico', 'Error de tipos en ATANH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        
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

    def execute(self,data):
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
                error = Error('Semántico', 'Error de tipos en ABS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
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
                    error = Error('Semántico', 'Error de tipos en CBRT, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CBRT, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'ceil' :
            'redondear - solo numeros positivos'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.ceil(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'ceiling' :
            'redondear - solo numeros positivos'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.ceil(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'degrees' :
            'radianes a grados - '
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.degrees(argumento.val)
                return Primitive('float', reto)
            else :
                error = Error('Semántico', 'Error de tipos en DEGREES, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en DIV, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'exp' :
            'e^ argumento - '
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.exp(argumento.val)
                return Primitive('float', reto)
            else :
                error = Error('Semántico', 'Error de tipos en EXP, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'factorial' :
            'x! - solo numeros positivos'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' :
                if argumento.val > 0 :
                    reto = math.factorial(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en FACTORIAL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en FACTORIAL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'floor' :
            'redondear al menor -'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.trunc(argumento.val)
                return Primitive('integer', reto)
            else :
                error = Error('Semántico', 'Error de tipos en FLOOR, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en GCD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'ln' :
            'Ln -'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.log(argumento.val)
                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en Ln, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en Ln, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'log' :
            'Log10 -'
            argumento = self.arg1.execute()
            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.log10(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en LOG, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en LOG, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en MOD, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en POWER, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en RADIANS, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en ROUND, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en SIGN, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en SQRT, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
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
                error = Error('Semántico', 'Error de tipos en trunc, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
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
    
    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class FuncionMatematicaSimple(Instruccion):
    #puede venir:
    #Count,max,sum,avg,min
    def __init__(self, operador, argumento):
        self.argumento = argumento
        self.operador = operador

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)
