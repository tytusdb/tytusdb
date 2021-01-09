import sys
sys.path.append('../Grupo1/Librerias/storageManager')
sys.path.append('../Grupo1/Librerias/')
sys.path.append('../Grupo1/Instrucciones/')
sys.path.append('../Grupo1/Utils')
sys.path.append('../Grupo1')

import gramatica as g
from enum import Enum
import math
import random
import hashlib 
from jsonMode import *
import Utils.Lista as l

from tkinter import * #importando tkinter
import tkinter as TK
import Utils.TablaSimbolos as table
import Utils.Lista as l
import Librerias.storageManager.jsonMode as storage
import Librerias.storageManager.c3dGen as c3dgen
from tkinter.filedialog import askopenfilename as files
import os
import webbrowser
from Utils.fila import fila
from Error import *
import Instrucciones.DML.select as select
import json




#from storageManager import jsonMode as manager
storage.dropAll()           
datos = l.Lista({}, '')
def createDB(database: str) :
        
    instruccion = g.parse("CREATE DATABASE IF NOT EXISTS test OWNER = 'root'  MODE = 1;")
    erroresSemanticos = []
    for instr in instruccion['ast'] :
    
            if instr != None:
                result = instr.executec3d(datos)
                #print(result+'--MF')
                if isinstance(result, Error):
                    #print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    
                    print(str(result.desc))
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    print(str(instr.ImprimirTabla(result)))
                else:
                    print(str(result))


    #*********************** CREATE DB ****************************
    resultado = 10 #createDatabase(database)
    
    if resultado==0:
        print('Base de datos ' + database + ' creada correctamente')
    elif resultado==2:
        print('Error al crear la base de datos ' + database + '. El nombre ya existe')
    elif resultado==1:
        print('Ha ocurrido un error al crear la base de datos ' + database + '.')
    elif resultado==0:
        print('Error desconocido')


# READ and show databases by constructing a list
def showDB() :
    
    resultado = showDatabases()
    print(resultado)

# READ and show databases by constructing a list
def useDatabase(database: str) :   

    instruccion = g.parse("USE TEST;")
    erroresSemanticos = []
    for instr in instruccion['ast'] :
    
            if instr != None:
                result = instr.executec3d(datos)
                #print(result+'--MF')
                if isinstance(result, Error):
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    
                    print(str(result.desc))
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    print(str(instr.ImprimirTabla(result)))
                else:
                    print(str(result))

    
    print('Use ' + database)

# CREATE a table checking their existence
def createTbl(database: str, table: str, listColumns: any):
    
    cadenaE = 'CREATE TABLE ' + table.upper() + " ("
    contaCol=0
    for colIns in listColumns:
        if contaCol==0:
            cadenaE = cadenaE + colIns
        else:
            cadenaE = cadenaE + ", " + colIns
        contaCol +=1
    
    cadenaE = cadenaE + ");"

    # instruccion = g.parse('CREATE TABLE tbProducto (idproducto integer primary key, \
  	# 					 producto varchar(150), \
  	# 					 fechacreacion date, \
	# 					 estado integer);')

    instruccion = g.parse(cadenaE)

    erroresSemanticos = []
    for instr in instruccion['ast'] :
    
            if instr != None:
                result = instr.executec3d(datos)
                #print(result+'--MF')
                if isinstance(result, Error):
                    #print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    
                    print(str(result.desc))
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    print(str(instr.ImprimirTabla(result)))
                else:
                    print(str(result))



    resultado = 10 #createTable(database, table, numberColumns)

    if resultado == 1:
        print('Error(42P16): invalid_table_definition.')
    elif resultado == 2:
        print('Error(???): No existe la base de datos.')
    elif resultado == 3:
        print('Error(42P07): duplicate_table.')
    elif resultado == 0:
        print('Tabla ' + table + ' creada correctamente')


#  a table checking their existence
def insertC3D(database: str, table: str, register: list):
    #print('************ registro')   
    #print(register)

    cadenaIns = 'INSERT INTO ' + table + ' VALUES('
    contadorCampos=0
    for campoIns in register:
        if contadorCampos==0:
            if es_numero(campoIns):
                cadenaIns = cadenaIns + str(campoIns)
            else:
                fTipo = campoIns.find("NOW") 
                if fTipo >=0 :
                    cadenaIns = cadenaIns + str(campoIns) 
                else:
                    cadenaIns = cadenaIns + "'" + str(campoIns) + "'"
        else:
            if es_numero(campoIns):
                cadenaIns = cadenaIns + "," + str(campoIns)
            else:
                fTipo = campoIns.find("NOW") 
                if fTipo >=0 :
                    cadenaIns = cadenaIns + "," + str(campoIns) 
                else:
                    cadenaIns = cadenaIns + ",'" + str(campoIns) + "'"

        contadorCampos+=1;     
    cadenaIns = cadenaIns + ");"


    instruccion = g.parse(cadenaIns)
    erroresSemanticos = []
    for instr in instruccion['ast'] :
    
            if instr != None:
                result = instr.executec3d(datos)
                #print(result+'--MF')
                if isinstance(result, Error):
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    
                    print(str(result.desc))
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    print(str(instr.ImprimirTabla(result)))
                else:
                    print(str(result))

    resultado = 100 #insert(database, table, register)
    if resultado == 1:
        print('Error(42P16): invalid_table_definition.')
    elif resultado == 2:
        print('Error(???): No existe la base de datos.')
    elif resultado == 3:
        print('Error(???): No existe la tabla.')
    elif resultado == 4:
        print('Error(???): Llave primaria duplicada.')
    elif resultado == 5:
        print('Error(???): No coincide el numero de campos.')
    elif resultado == 0:
        print('Dato insertado correctamente')

def updateC3D(database: str, table: str, register: dict, columns: list):
    #print('************ registro')   
    #print(register)
    resultado = update(database, table, register, columns)
    if resultado == 1:
        print('Error(42P16): invalid_table_definition.')
    elif resultado == 2:
        print('Error(???): No existe la base de datos.')
    elif resultado == 3:
        print('Error(???): No existe la tabla.')
    elif resultado == 4:
        print('Error(???): Llave primaria no existe.')
    elif resultado == 5:
        print('Error(???): No coincide el numero de campos.')
    elif resultado == 0:
        print('Update realizado correctamente')

def selectC3D(database: str, columns: any, tablas: any, cwhere: str):
    #print('************ registro')   
    #print(register)

    cadenaE = 'SELECT '
    contCampos=0
    for i in columns:
        if contCampos==0:
            cadenaE = cadenaE + str(i)
        else:
            cadenaE = cadenaE + ', ' + str(i)
        contCampos+=1
    
    if len(tablas)>0:
        cadenaE = cadenaE + ' FROM '    
        contCampos=0
        for j in tablas:
            if contCampos==0:
                cadenaE = cadenaE + str(j)
            else:
                cadenaE = cadenaE + ', ' + str(j)
            contCampos+=1

        if len(cwhere)>0:
            cadenaE = cadenaE + ' WHERE ' + cwhere    
    cadenaE = cadenaE + ';'
    instruccion = g.parse(cadenaE)
    erroresSemanticos = []
    for instr in instruccion['ast'] :
            varValor=0
            if instr != None:
                result = instr.executec3d(datos)
                #print(result+'--MF')
                if isinstance(result, Error):                                        
                    print(str(result.desc))
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    if 'count' in result:
                        varValor =  result['count']['columnas'][0]   
                    else:
                        contResult=0
                        varColName=''
                        for colRes in result.keys():
                            varColName = colRes
                            contResult+=1
                        if contResult==1:
                            varValor = result[varColName]['columnas'][0][0]
                        else:
                            print(str(instr.ImprimirTabla(result)))

                else:                    
                    print(str(result))
    


    resultado = 100 #update(database, table, register, columns)
    if resultado == 1:
        print('Error(42P16): invalid_table_definition.')
    elif resultado == 2:
        print('Error(???): No existe la base de datos.')
    elif resultado == 3:
        print('Error(???): No existe la tabla.')
    elif resultado == 4:
        print('Error(???): Llave primaria no existe.')
    elif resultado == 5:
        print('Error(???): No coincide el numero de campos.')
    elif resultado == 0:
        print('Update realizado correctamente')

    return varValor


def existTableC3D(database: str, table: str) -> bool:       
    resultado = existTable(database,table)
    if resultado is False:
        print('La tabla no existe')
    return resultado

def es_numero(variable : any):
    try:
        float(variable)
        return True
    except :
        return False

# show databases by constructing a list
def showTables(database: str) -> list:
    resultado = showTables(database)
    print(resultado)