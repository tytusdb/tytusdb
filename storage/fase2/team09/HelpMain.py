# Copyright (c) 2020 TytusDb Team


'''
from team16 import avlMode as avl
from team17 import BMode as b
from team18 import BPlusMode as bplus
from CopyTable import *
#from DictMode import DictMode  as mdict
#from team15.storage import HashMode as thash
#from team14 import ISAMMode as isam
from storageManager import jsonMode as json 
'''
from .storage.avl.DataAccessLayer.reports import graphAVL as avltablas, graphicTables
from .storage.hash import Tabla as hashreporte
from .storage.avl import avlMode as avl
from .storage.b import BMode as b
from .storage.bplus import BPlusMode as bplus
from .storage.dict import DictMode as mdict
from .storage.hash import HashMode as mhash
from .storage.isam import ISAMMode as isam
from .storage.json import jsonMode as json 

def Grafico(arreglo,database,table):
    if arreglo == "avl":
        return  avltablas(database,table)

import os, pickle,csv
def CrearBase(modo,nombre):
    if modo == "avl":
        return avl.createDatabase(nombre)
    elif modo == "b":
        return b.createDatabase(nombre)
    elif modo== "bplus":
        return bplus.createDatabase(nombre)
    elif modo == "json":
        return json.createDatabase(nombre)
    elif modo == "hash":
        return mhash.createDatabase(nombre)
    elif modo == "dict":
        return mdict.createDatabase(nombre)
    elif modo == "isam":
        return isam.createDatabase(nombre)


def eliminainercambio(arreglo,base):
    if arreglo == "avl":
        return avl.dropDatabase(base)
    elif arreglo == "b":
        return b.dropDatabase(base)
    elif arreglo == "bplus":
        return bplus.dropDatabase(base)
    elif arreglo == "json":
        return json.dropDatabase(base)
    elif arreglo == "hash":
        return mhash.dropDatabase(base)
    elif arreglo == "dict":
        return mdict.dropDatabase(base)
    elif arreglo == "isam":
        return isam.dropDatabase(base)


def CambioNombre(Modo,nombreV,nombre):
    arreglo=[nombreV,Modo]
    if arreglo[1] == "avl":
        return avl.alterDatabase(arreglo[0],nombre)
    elif arreglo[1] == "b":
        return b.alterDatabase(arreglo[0],nombre)
    elif arreglo[1] == "bplus":
        return bplus.alterDatabase(arreglo[0],nombre)
    elif arreglo[1] == "json":
        return json.alterDatabase(arreglo[0],nombre)
    elif arreglo[1] == "hash":
        return mhash.alterDatabase(arreglo[0],nombre)
    elif arreglo[1] == "dict":
        return mdict.alterDatabase(arreglo[0],nombre)
    elif arreglo[1] == "isam":
        return isam.alterDatabase(arreglo[0],nombre)

def Creartabla(arreglo,database,nombre,columna):
    if arreglo == "avl":
        return avl.createTable(database,nombre,columna)
    elif arreglo == "b":
        return b.createTable(database,nombre,columna)
    elif arreglo == "bplus":
        return bplus.createTable(database,nombre,columna)
    elif arreglo == "json":
        return json.createTable(database,nombre,columna)
    elif arreglo == "hash":
        return mhash.createTable(database,nombre,columna)
    elif arreglo == "dict":
        return mdict.createTable(database,nombre,columna)
    elif arreglo == "isam":
        return isam.createTable(database,nombre,columna)
  


def CambiarNombreTabla(arreglo,database,tableOld,tableNew):
    if arreglo == "avl":
        return avl.alterTable(database,tableOld,tableNew)
    elif arreglo == "b":
        return b.alterTable(database,tableOld,tableNew)
    elif arreglo == "bplus":
        return bplus.alterTable(database,tableOld,tableNew)
    elif arreglo == "json":
        return json.alterTable(database,tableOld,tableNew)
    elif arreglo == "hash":
        return mhash.alterTable(database,tableOld,tableNew)
    elif arreglo == "dict":
        return mdict.alterTable(database,tableOld,tableNew)
    elif arreglo == "isam":
        return isam.alterTable(database,tableOld,tableNew)



def ExtraerTabla(arreglo,database,table):
    if arreglo == "avl":
        return avl.extractTable(database,table)
    elif arreglo == "b":
        return b.extractTable(database,table)
    elif arreglo == "bplus":
        return bplus.extractTable(database,table)
    elif arreglo == "json":
        return json.extractTable(database,table)
    elif arreglo == "hash":
        return mhash.extractTable(database,table)
    elif arreglo == "dict":
        return mdict.extractTable(database,table)
    elif arreglo == "isam":
        return isam.extractTable(database,table)



def ExtraerRangoTabla(arreglo,database,table,columnNumber,lower,upper):
    if arreglo == "avl":
        return avl.extractRangeTable(database,table,columnNumber,lower,upper)
    elif arreglo == "b":
        return b.extractRangeTable(database,table,columnNumber,lower,upper)
    elif arreglo == "bplus":
        return bplus.extractRangeTable(database,table,columnNumber,lower,upper)
    elif arreglo == "json":
        return json.extractRangeTable(database,table,columnNumber,lower,upper)
    elif arreglo == "hash":
        return mhash.extractRangeTable(database,table,columnNumber,lower,upper)
    elif arreglo == "dict":
        return mdict.extractRangeTable(database,table,columnNumber,lower,upper)
    elif arreglo == "isam":
        return isam.extractRangeTable(database,table,columnNumber,lower,upper)




def AgregarPK(arreglo,database,table,columns):
    if arreglo == "avl":
        return avl.alterAddPK(database,table,columns)
    elif arreglo == "b":
        return b.alterAddPK(database,table,columns)
    elif arreglo == "bplus":
        return bplus.alterAddPK(database,table,columns)
    elif arreglo == "json":
        return json.alterAddPK(database,table,columns)
    elif arreglo == "hash":
        return mhash.alterAddPK(database,table,columns)
    elif arreglo == "dict":
        return mdict.alterAddPK(database,table,columns)
    elif arreglo == "isam":
        return isam.alterAddPK(database,table,columns)



def EliminarPK(arreglo,database,table):
    if arreglo == "avl":
        return avl.alterDropPK(database,table)
    elif arreglo == "b":
        return b.alterDropPK(database,table)
    elif arreglo == "bplus":
        return bplus.alterDropPK(database,table)
    elif arreglo == "json":
        return json.alterDropPK(database,table)
    elif arreglo == "hash":
        return mhash.alterDropPK(database,table)
    elif arreglo == "dict":
        return mdict.alterDropPK(database,table)
    elif arreglo == "isam":
        return isam.alterDropPK(database,table)



def AgregarColumna(arreglo,database,table,default):
    if arreglo == "avl":
        return avl.alterAddColumn(database,table,default)
    elif arreglo == "b":
        return b.alterAddColumn(database,table,default)
    elif arreglo == "bplus":
        return bplus.alterAddColumn(database,table,default)
    elif arreglo == "json":
        return json.alterAddColumn(database,table,default)
    elif arreglo == "hash":
        return mhash.alterAddColumn(database,table,default)
    elif arreglo == "dict":
        return mdict.alterAddColumn(database,table,default)
    elif arreglo == "isam":
        return isam.alterAddColumn(database,table,default)



def EliminarColumna(arreglo,database,table,default):
    if arreglo == "avl":
        return avl.alterDropColumn(database,table,default)
    elif arreglo == "b":
        return b.alterDropColumn(database,table,default)
    elif arreglo == "bplus":
        return bplus.alterDropColumn(database,table,default)
    elif arreglo == "json":
        return json.alterDropColumn(database,table,default)
    elif arreglo == "hash":
        return mhash.alterDropColumn(database,table,default)
    elif arreglo == "dict":
        return mdict.alterDropColumn(database,table,default)
    elif arreglo == "isam":
        return isam.alterDropColumn(database,table,default)



def EliminarTabla(arreglo,database,table):
    if arreglo == "avl":
        return avl.dropTable(database,table)
    elif arreglo == "b":
        return b.dropTable(database,table)
    elif arreglo == "bplus":
        return bplus.dropTable(database,table)
    elif arreglo == "json":
        return json.dropTable(database,table)
    elif arreglo == "hash":
        return mhash.dropTable(database,table)
    elif arreglo == "dict":
        return mdict.dropTable(database,table)
    elif arreglo == "isam":
        return isam.dropTable(database,table)


def Tupla(arreglo,database,table,register):
    if arreglo == "avl":
        return avl.insert(database,table,register)
    elif arreglo == "b":
        return b.insert(database,table,register)
    elif arreglo == "bplus":
        return bplus.insert(database,table,register)
    elif arreglo == "json":
        return json.insert(database,table,register)
    elif arreglo == "hash":
        return mhash.insert(database,table,register)
    elif arreglo == "dict":
        return mdict.insert(database,table,register)
    elif arreglo == "isam":
        return isam.insert(database,table,register)



def CargandoCsvMode(arreglo,file,database,table):
    if arreglo == "avl":
        return avl.loadCSV(file,database,table)
    elif arreglo == "b":
        return b.loadCSV(file,database,table)
    elif arreglo == "bplus":
        return bplus.loadCSV(file,database,table)
    elif arreglo == "json":
        return json.loadCSV(file,database,table)
    elif arreglo == "hash":
        return mhash.loadCSV(file,database,table)
    elif arreglo == "dict":
        return mdict.loadCSV(file,database,table)
    elif arreglo == "isam":
        return isam.loadCSV(file,database,table)
 


def ExtraerFILA(arreglo,database,table,columns):
    if arreglo == "avl":
        return avl.extractRow(database,table,columns)
    elif arreglo == "b":
        return b.extractRow(database,table,columns)
    elif arreglo == "bplus":
        return bplus.extractRow(database,table,columns)
    elif arreglo == "json":
        return json.extractRow(database,table,columns)
    elif arreglo == "hash":
        return mhash.extractRow(database,table,columns)
    elif arreglo == "dict":
        return mdict.extractRow(database,table,columns)
    elif arreglo == "isam":
        return isam.extractRow(database,table,columns)
 


def actualizarupdate(arreglo,database,table,register,columns):
    if arreglo == "avl":
        return avl.update(database,table,register,columns)
    elif arreglo == "b":
        return b.update(database,table,register,columns)
    elif arreglo == "bplus":
        return bplus.update(database,table,register,columns)
    elif arreglo == "json":
        return json.update(database,table,register,columns)
    elif arreglo == "hash":
        return mhash.update(database,table,register,columns)
    elif arreglo == "dict":
        return mdict.update(database,table,register,columns)
    elif arreglo == "isam":
        return isam.update(database,table,register,columns)
 

def Deletedatos(arreglo,database,table,register):
    if arreglo == "avl":
        return avl.delete(database,table,register)
    elif arreglo == "b":
        return b.delete(database,table,register)
    elif arreglo == "bplus":
        return bplus.delete(database,table,register)
    elif arreglo == "json":
        return json.delete(database,table,register)
    elif arreglo == "hash":
        return mhash.delete(database,table,register)
    elif arreglo == "dict":
        return mdict.delete(database,table,register)
    elif arreglo == "isam":
        return isam.delete(database,table,register)



def TruncarTabla(arreglo,database,table):
    if arreglo == "avl":
        return avl.truncate(database,table)
    elif arreglo == "b":
        return b.truncate(database,table)
    elif arreglo == "bplus":
        return bplus.truncate(database,table)
    elif arreglo == "json":
        return json.truncate(database,table)
    elif arreglo == "hash":
        return mhash.truncate(database,table)
    elif arreglo == "dict":
        return mdict.truncate(database,table)
    elif arreglo == "isam":
        return isam.truncate(database,table)



