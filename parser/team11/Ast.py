from enum import Enum
from prettytable import PrettyTable
from datetime import date
from datetime import datetime
import math
import random

from storageManager import jsonMode as jsonMode
import re


class Nodo:
    '''Clase que define la estructura de los nodos del AST.'''
    
    def __init__(self, etiqueta, valor, hijos = [], linea = -1, columna = -1, gramatica = ''):
        self.etiqueta = etiqueta
        self.valor = valor
        self.hijos = hijos
        self.linea = linea
        self.columna = columna
        self.gramatica = gramatica

    def toString(self):
        cadena = self.etiqueta + ',' + self.valor + ' L: ' + str(self.linea) + ' C: ' + str(self.columna)+'\n'
        for n in self.hijos:
            cadena = cadena + ' --- ' + n.toString()
        return cadena

#---------------------------------------------------------------------------------------------------------------
class EType(Enum):
    LEXICO      = 1
    SINTACTICO  = 2
    SEMANTICO   = 3

class Error:
    '''
    Clase utilizada para el manero de errores
    Atributos:
        code        - codigo de error (según errores definidos pos SQL)
        error_type  - tipo de error (EType)
        description - descripción del error
        line        - linea en la cual ocurrió
        column      - columna en la cual ocurrió
    '''
    def __init__(self,code,error_type,description = '',line = -1,column = -1):
        self.code = code
        self.error_type = error_type
        self.description = description
        self.line = line
        self.column = column
    
    def toString(self):
        return str(self.code)+'\t'+str(self.error_type.name)+'\t'+str(self.description)+'\tL: '+str(self.line)

#---------------------------------------------------------------------------------------------------------------

class Database:
    '''
    Clase que define la estructura de una base de datos
    compuesta por un diccionario de <Tablas>
    Atrbutos:
        owner  - nombre del propietario
        mode   - valor tipo entero que define el modo de la DB
        tables - diccionario de tablas [key:'...', value: {...}]
    '''
    def __init__(self,owner = '',mode = -1,tables = {}):
        self.owner = owner 
        self.mode = mode
        self.tables = {}

    def toString(self):
        return 'Owner: '+str(self.owner)+' | Mode: '+str(self.mode)+' | Tables Count: '+str(len(self.tables))

#---------------------------------------------------------------------------------------------------------------

class Constraint:
    '''
    Clase que define la Restriccion de una columna
    Atributos:
        name  -  nombre que recibe la restriccion.
        value -  nodo que contiene la porción del árbol con la condición a evaluar.  
    '''
    def __init__(self,name,value):
        self.name = name
        self.value = value

#---------------------------------------------------------------------------------------------------------------

class Types(Enum):
    SMALLINT            = 1
    INTEGER             = 2
    BIGINT              = 3
    DECIMAL             = 4
    NUMERIC             = 5
    REAL                = 6
    FLOAT               = 7
    INT                 = 8
    DOUBLE              = 9
    MONEY               = 10
    VARCHAR             = 11
    CHARACTER_VARYING   = 12
    CHARACTER           = 13
    CHAR                = 14
    TEXT                = 15
    TIMESTAMP           = 16
    DATE                = 17
    TIME                = 18
    BOOLEAN             = 19
    INTERVAL            = 20
    ENUM                = 21

class ColType:
    '''
    Clase define el tipo una columna
    Atributos:
        col_type - enum Types 
        value    - valor (int) para tipos numericos con limite o 
                   valor (string) para tipos definidos por el usuario (nombre)
    '''
    def __init__(self, col_type, value):
        self.col_type = col_type
        self.value = value
    
    def getType(self) -> str:
        if isinstance(self.value, int) and self.value > 0:
            return str(self.col_type.name) + '('+str(self.value)+')'
        elif isinstance(self.value, str):
            return str(self.col_type.name) + '('+str(self.value)+')'
        return str(self.col_type.name)
    
#---------------------------------------------------------------------------------------------------------------

class Column:
    '''
    Clase que define los atributos de una columna
    Atributos:
        index           - indice de la columna
        columnType      - instancia de la clase <ColType>
        isPrimaryKey    - valor (bool) para indicar si una columna es llave primaria
        defaultValue    - valor por defecto para una columna
        isNull          - valor (bool) para indicar si una columna puede ser nula
        constraindValue - instancia de (Constraint) almacena la restriccion de una columna
        isUnique        - valor (bool) para indicar si los valores en la columna deben ser únicos
        line            - línea de la instrucción
    '''
    def __init__(self,name,index,columnType:ColType = None,isPrimaryKey = False,defaultValue = None,isNull = False, constraintValue = '',isUnique = False,line = 0):
        self.name = name
        self.index = index
        self.columnType = columnType
        self.isPrimaryKey = isPrimaryKey
        self.defaultValue = defaultValue
        self.isNull = isNull
        self.isUnique = isUnique
        self.line = line

    def toString(self) -> str:
        return 'Columna \"'+self.name+'\"\nTipo: '+str(self.columnType.col_type.name)+'\nPrimary Key: '+str(self.isPrimaryKey)+ '\nNull: '+str(self.isNull) + '\nUnique: '+str(self.isUnique)

#---------------------------------------------------------------------------------------------------------------

class AST:
    '''
    Clase que contendrá todo lo referente al AST
    Atributos:
        raiz      - nodo del árbol de las instrucciones
        usingDB   - almacenará el NOMBRE de la DB en en uso
        ts        - diccionario de la Tabla de Simbolos
        userTypes - diccionario para Tipo definido por el usuario (Enums)
        output    - lista de datos que se enviarán a la consola de salida
        errors    - lista que almacena objetos tipo (Error) para reporte
    '''
    def __init__(self,raiz,usingDB = '',ts = {},userTypes = {},output = [],errors = []):
        self.raiz = raiz 
        self.usingDB = usingDB
        self.ts = ts
        self.userTypes = userTypes
        self.output = output
        self.errors = errors
        jsonMode.dropAll() 

    def executeAST(self):
        for nodo in self.raiz.hijos:
            if nodo.etiqueta == 'CREATE DATABASE':
                self.createDB(nodo)
            elif nodo.etiqueta == 'USE DATABASE':
                self.useDB(nodo)
            elif nodo.etiqueta == 'REPLACE DATABASE':
                pass
            elif nodo.etiqueta == 'ALTER DATABASE':
                self.alterDB(nodo)
            elif nodo.etiqueta == 'DROP DATABASE':
                self.dropDB(nodo)
            elif nodo.etiqueta == 'CREATE TABLE':
                self.crearTabla(nodo)
            elif nodo.etiqueta == 'DROP TABLE':
                self.eliminarTabla(nodo)
            elif nodo.etiqueta == 'SHOW DATABASES':
                self.showDB(nodo)
            elif nodo.etiqueta == 'INSERT INTO':
                self.insertarDatos(nodo)
            elif nodo.etiqueta == 'UPDATE':
                self.update(nodo)
            elif nodo.etiqueta == 'CREATE ENUM':
                self.crearEnum(nodo)
            elif nodo.etiqueta == 'ALTER TABLE':
                pass
            elif nodo.etiqueta == 'DELETE':
                #self.delete()
                pass
            elif nodo.etiqueta == 'TRUNCATE':
                self.truncate(nodo)
            elif nodo.etiqueta == 'SELECT':
                self.Select(nodo)
            else:
                print('[!] Valor de etiqueta ('+nodo.etiqueta+') no corresponde, en L: '+str(nodo.linea))
################---CREATE DATABASE---##########################
    def createDB(self, nodo):
        name_db = ''
        owner = ''
        mode = -1

        hijo1 = ''
        hijo2 = ''
        hijo3 = ''

        for hijos in nodo.hijos:
            for hijos2 in hijos.hijos:
                for hijos3 in hijos2.hijos:
                    hijo3 = hijos3.valor
                hijo2 = hijos2.valor
            hijo1 = hijos.valor

        if nodo.valor != '':
            name_db = nodo.valor
            owner = hijo1
            mode = hijo2
        else:
            name_db = hijo1
            owner = hijo2
            mode = hijo3
        
        
        query_result = jsonMode.createDatabase(name_db)
        if query_result == 0:
            jsonMode.createDatabase(name_db)
            self.ts[name_db] = Database(owner, mode)
            self.output.append('Creación de base de datos \"'+name_db+'\" exitosa.')
        elif query_result == 1:
            self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
        elif query_result == 2:
            self.errors.append(Error('42P04', EType.SEMANTICO, 'duplicate_database',nodo.linea))
            
#################---USE DATABASE---################################
    def useDB(self,nodo):
        if nodo.valor in self.ts:
            self.usingDB = nodo.valor
            self.output.append('Usted esta ubicado en la base de datos \"'+ self.usingDB +'\".')
            # print(self.usingDB)
        else:
            # agregar el error semantico con su debido codigo -> DB no existe
            self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))

##################---DROP DATABASE---################################
    def dropDB(self, nodo):
        
        if nodo.valor in self.ts:
            result = jsonMode.dropDatabase(nodo.valor)
            del self.ts[nodo.valor]
            if result == 0:
                self.output.append('Base de datos \"'+ nodo.valor+'\" botada exitosamente.')
            elif result == 1:
                self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
            elif result == 2:   # Base de datos inexistente
                self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))


##################---ALTER DATABASE---################################
    def alterDB(self,nodo):
        databaseOld = ''
        databaseNew = ''
        owner = ''
        rename = 0

        for hijos in nodo.hijos:
            databaseNew = hijos.valor
            if hijos.etiqueta == 'RENAME TO':
                rename = 1
            else:
                owner = hijos.valor

        if nodo.valor != '':
            databaseOld = nodo.valor

        query_result = jsonMode.alterDatabase(databaseOld, databaseNew)

        if rename == 1:
            if query_result == 0:
                if databaseOld in self.ts:
                    self.ts[databaseNew] = self.ts[databaseOld]
                    del self.ts[databaseOld]
                self.output.append('La base de datos \"'+ databaseOld+'\" ha sido renombrada a \"' + databaseNew + '\".')
            elif query_result == 1:
                self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
            elif query_result == 2:   # Base de datos inexistente
                self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
            elif query_result == 3:   # Base de datos existente
                self.errors.append(Error('42P04', EType.SEMANTICO, 'duplicate_database',nodo.linea))
            
            #self.output.append(query_result)
        else:
            if query_result == 0:
                self.ts[databaseOld].owner = owner
                self.output.append('La base de datos \"'+ databaseOld+'\" ha cambiado de propietario a \"' + owner + '\".')
            elif query_result == 1:
                self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
            elif query_result == 2:   # Base de datos inexistente
                self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
            elif query_result == 3:   # Base de datos existente
                self.errors.append(Error('42P04', EType.SEMANTICO, 'duplicate_database',nodo.linea))
            

##################---SHOW DATABASE---################################
    def showDB(self,nodo):
        query_result = jsonMode.showDatabases()
        er = ''
        veces_mod = 0
        pos_mod1 = 0
        pos_mod2 = 0

        if nodo.valor == '':
            self.output.append(query_result)
        else:
            er = nodo.valor
            er = '^' + er.replace('%','.+').replace('_','(.){0,1}') + '$'
            # if pos_mod1 == 1 and veces_mod == 1:
            filtrada = []
            for base in query_result:
                if re.match(er, base):
                    filtrada.append(base)
                
            #     print("====================================")
            self.output.append(filtrada)
       