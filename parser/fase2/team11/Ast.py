from enum import Enum
from prettytable import PrettyTable
from datetime import date
from datetime import datetime
import math
import random
import cryptography
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from graphviz import render

from storageManager import jsonMode as jsonMode
import re

errors2 = ''
output2 =''

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
        #print('Owner: '+str(owner)+' | Mode: '+str(mode))

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

class Index:

    def __init__(self,name = '', isUnique = False, table = '', condition = '', type_ = '', columns = [], attribs = [], line = 0):
        self.name = name
        self.isUnique = isUnique
        self.table = table
        self.condition = condition
        self.type_ = type_
        self.columns = columns
        self.attribs = attribs
        self.line = line

    def toString(self):
        return self.name + ' | Unique: ' + str(self.isUnique) + ' | Table: '+ self.table + ' | Columnas: ' + str(self.columns) + ' | Atributos' + str(self.attribs) + ' | Tipo: ' + self.type_  
    
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
    def __init__(self,raiz = None,usingDB = '',ts = {},userTypes = {}, index = {},output = [],errors = [], c3d = []):
        self.raiz = raiz 
        self.usingDB = usingDB
        self.ts = ts
        self.userTypes = userTypes
        self.index = index
        self.output = output
        self.errors = errors
        self.c3d = c3d

        jsonMode.dropAll()

    def executeAST(self, nodo):
        if nodo.etiqueta == 'CREATE DATABASE':
            self.createDB(nodo)
        elif nodo.etiqueta == 'USE':
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
            #self.update(nodo)
            pass
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
        elif nodo.etiqueta == 'CREATE INDEX':
            self.procesarIndices(nodo)
        elif nodo.etiqueta == 'ALTER INDEX':
            self.modificarIndices(nodo)
        elif nodo.etiqueta == 'DROP INDEX':
            self.eliminarIndice(nodo)
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
       
##################---UPDATE---################################
    def update(self,nodo):
        #print("=============================")
        #print(self.usingDB)
        tb_id = nodo.valor
        for hijos in nodo.hijos:
            for hijos2 in hijos.hijos:
                r = jsonMode.update(self.usingDB, tb_id, hijos2.valor)
        #print(r)
        if r == 0:
            self.output.append('La tabla \"'+ tb_id+'\" de la base de datos \"' + self.usingDB + '\" ha sido actualizada con nuevos datos.')
        elif r == 1:   # Error en la operación
            self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
        elif r == 2:   # Base de datos inexistente
            self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
        elif r == 3:   # Tabla existente
            self.errors.append(Error('42P01', EType.SEMANTICO, 'undefined_table',nodo.linea))

        

##################---DELETE---################################
    def delete(self,nodo):
        a = ''
        print(self.usingDB) #BDD
        tb_id = nodo.valor # id
        for hijos in nodo.hijos:
            a = hijos.valor #condiciones
        result = jsonMode.delete(self.usingDB, tb_id, a)
        print('>>>>>>>>>>>>>>>>>>>>------',result)


##################---TRUNCATE---################################
    def truncate(self,nodo):
        tb_name=''
        for hijos in nodo.hijos:
            tb_name = hijos.valor
        result = jsonMode.truncate(self.usingDB, tb_name)

#--------------------------------------------------------------------------------------------------
# C R E A T E  T A B L E
    def crearTabla(self,nodo):
        tb_name = nodo.valor
        tb_padre = ''
        tb_parent = {}
        if len(nodo.hijos) == 2:
            tb_padre = nodo.hijos[1].valor
            if not(self.usingDB in self.ts):
                self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
                return
            db = self.ts[self.usingDB]
            if not(tb_padre in db.tables):
                self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
                return
            tb_parent = db.tables[tb_padre]
            columnas = nodo.hijos[0]
            count_cols = 0
            for c in columnas.hijos:
                if c.etiqueta == 'COLUMN':
                    count_cols += 1
            count_cols += len(tb_parent)
            result = jsonMode.createTable(self.usingDB,str(nodo.valor),count_cols)
            #Inicia la creación de Columnas
            if result == 0:     # Operación exitosa
                self.output.append('Creación de tabla \"'+tb_name+'\" exitosa.')
                c = 1
                table = {}
                for col in columnas.hijos:
                    if col.etiqueta == 'COLUMN':
                        new_col = Column(col.valor,c)
                        new_col.columnType = self.getColType(col.hijos[0])
                        for atrib in col.hijos[1].hijos:
                            if atrib.etiqueta == 'NOT NULL':
                                new_col.isNull = False
                            elif atrib.etiqueta == 'PRIMARY KEY':
                                new_col.isPrimaryKey = True
                            elif atrib.etiqueta == 'CONSTRAINT':
                                cnst = Constraint(atrib.valor,atrib.hijos[0])
                                new_col.constraint = cnst
                            elif atrib.etiqueta == 'CHECK':
                                new_col.constraint = Constraint('',atrib)
                            elif atrib.etiqueta == 'UNIQUE':
                                new_col.isUnique = True
                        #Se añade a la tabla la nueva columna
                        new_col.line = col.linea
                        table[col.valor] = new_col
                        c += 1
                    else:
                        col_name = col.hijos[0].valor
                        if col_name in table:
                            table[col_name].isPrimaryKey = True
                # Se copian las columnas del padre al hijo
                for name,col in tb_parent.items():
                    table[name] = col
                    c += 1
                # Se añade a la Base de datos la nueva Tabla
                db.tables[tb_name] = table
            elif result == 1:   # Error en la operación
                self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
            elif result == 2:   # Base de datos inexistente
                self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
            elif result == 3:   # Tabla existente
                self.errors.append(Error('42P07', EType.SEMANTICO, 'duplicate_table',nodo.linea))
            return
        #----------------------------------------------------------------------------------------------
        columnas = nodo.hijos[0]
        col_count = 0
        for h in columnas.hijos:
            if h.etiqueta == 'COLUMN':
                col_count += 1
        #Verificar que la base de dato exista o se haya seleccionado una...
        if not(self.usingDB in self.ts):
            self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
            return
        database = self.ts[self.usingDB]
        table = {}
        #--- Llamada a función nativa...
        result = jsonMode.createTable(self.usingDB,str(tb_name),col_count)
        if result == 0:     # Operación exitosa
            self.output.append('Creación de tabla \"'+tb_name+'\" exitosa.')
            c = 1
            for col in columnas.hijos:
                if col.etiqueta == 'COLUMN':
                    new_col = Column(col.valor,c)
                    new_col.columnType = self.getColType(col.hijos[0])
                    for atrib in col.hijos[1].hijos:
                        if atrib.etiqueta == 'NOT NULL':
                            new_col.isNull = False
                        elif atrib.etiqueta == 'PRIMARY KEY':
                            new_col.isPrimaryKey = True
                        elif atrib.etiqueta == 'CONSTRAINT':
                            cnst = Constraint(atrib.valor,atrib.hijos[0])
                            new_col.constraint = cnst
                        elif atrib.etiqueta == 'CHECK':
                            new_col.constraint = Constraint('',atrib)
                        elif atrib.etiqueta == 'UNIQUE':
                            new_col.isUnique = True
                    #Se añade a la tabla la nueva columna
                    new_col.line = col.linea
                    table[col.valor] = new_col
                    c += 1
                    # Se añade a la Base de datos la nueva Tabla
                    database.tables[tb_name] = table
                else:
                    col_name = col.hijos[0].valor
                    if col_name in table:
                        table[col_name].isPrimaryKey = True
        elif result == 1:   # Error en la operación
            self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
        elif result == 2:   # Base de datos inexistente
            self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
        elif result == 3:   # Tabla existente
            self.errors.append(Error('42P07', EType.SEMANTICO, 'duplicate_table',nodo.linea))

    def getColType(self,nodo_tipo) -> ColType:
        # Verificación del límite
        l = 0
        if len(nodo_tipo.hijos) == 1:
            l = nodo_tipo.hijos[0].valor        
        # Verificación del tipo
        tipo = str(nodo_tipo.valor).upper()
        if tipo == 'SMALLINT':
            return ColType(Types.SMALLINT,l)
        elif tipo == 'INTEGER':
            return ColType(Types.INTEGER,l)
        elif tipo == 'BIGINT':
            return ColType(Types.BIGINT,l)
        elif tipo == 'DECIMAL':
            return ColType(Types.DECIMAL,l)
        elif tipo == 'NUMERIC':
            return ColType(Types.NUMERIC,l)
        elif tipo == 'REAL':
            return ColType(Types.REAL,l)
        elif tipo == 'NUMERIC':
            return ColType(Types.FLOAT,l)
        elif tipo == 'INT':
            return ColType(Types.INT,l)
        elif tipo == 'DOUBLE':
            return ColType(Types.DOUBLE,l)
        elif tipo == 'MONEY':
            return ColType(Types.MONEY,l)
        elif tipo == 'VARCHAR':
            return ColType(Types.VARCHAR,l)
        elif tipo == 'CHARACTER_VARYING':
            return ColType(Types.CHARACTER_VARYING,l)
        elif tipo == 'CHARACTER':
            return ColType(Types.CHARACTER,l)
        elif tipo == 'CHAR':
            return ColType(Types.CHAR,l)
        elif tipo == 'TEXT':
            return ColType(Types.TEXT,l)
        elif tipo == 'TIMESTAMP':
            return ColType(Types.TIMESTAMP,l)
        elif tipo == 'DATE':
            return ColType(Types.DATE,l)
        elif tipo == 'TIME':
            return ColType(Types.TIME,l)
        elif tipo == 'BOOLEAN':
            return ColType(Types.BOOLEAN,l)
        elif tipo == 'INTERVAL':
            return ColType(Types.INTERVAL,l)
        else:
            return ColType(Types.ENUM,l)

    def eliminarTabla(self,nodo):
        tb_name = nodo.valor
        result = jsonMode.dropTable(self.usingDB,tb_name)
        if result == 0: # Operación exitosa
            self.output.append('Eliminación de tabla \"'+tb_name+'\" exitosa.')
            database = self.ts[self.usingDB]
            del database.tables[tb_name]
        elif result == 1: # Error en la operación
            self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
        elif result == 2: # Base de datos no existe
            self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
        elif result == 3: # Tabla no existe
            self.errors.append(Error('42P01', EType.SEMANTICO, 'undefined_table',nodo.linea))

    def crearEnum(self,nodo):
        nombre = nodo.valor
        valores = []
        for v in nodo.hijos:
            valores.append(v.valor)
        # Almacenar el tipo 
        self.userTypes[nombre] = valores


    def printOutputs(self):
        global output2
        print('\n--- SALIDAS ('+str(len(self.output))+') -----------------------------------------')
        for s in self.output:
            print(str(s))
            output2 = str(s)

    def printErrors(self):
        global errors2
        print('\n--- ERRORES ('+str(len(self.errors))+') -----------------------------------------')
        for e in self.errors:
            print(e.toString())
            errors2 = e.toString()


    def generateTSReport(self):
        now = datetime.now()
        fecha = 'Fecha: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)
        hora = 'Hora: '+str(now.hour)+':'+str(now.minute)
        header = '<html><head><br><title>REPORTE TABLA DE SIMBOLOS</title></head><body>\n<H1 ALIGN=CENTER><b><font face="Roboto" color="#1f253d">REPORTE TABLA DE SIMBOLOS</font></b></H1>\n<H4 ALIGN=CENTER><b><font face="Roboto" color="#1f253d">'+fecha+' | '+hora+'</font></b></H4>\n'
        tbhead = '<table align="center" cellpadding="20" cellspacing="0"  style="border:2px solid #1f253d">\n'
        tbhead += '<tr>\n'
        tbhead += '<td bgcolor="#2d48b5" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">DB/TABLA</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">NOMBRE COLUMNA</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="100" style="text-align:center"><font face="Roboto" color="white" size="4">TIPO</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">PRIMARY KEY</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">NULL</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">UNIQUE</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">LINEA</font></td>\n'
        tbhead += '</tr>\n'
        cont = ''
        check = '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="#83c95b" size="3">&#x2714</font></td>\n'
        notck = '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="#f04d4d" size="3">&#x2718</font></td>\n'
        # Iteración en la base de datos
        for name_db,obj_db in self.ts.items():
            # Iteración sobre las tablas de la DB
            for name_tb,table in obj_db.tables.items():
                # Iteración sobre las columnas de la tabla
                    for col_name,col in table.items():
                        cont += '<tr>\n'
                        cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+name_db+'/'+name_tb+'</font></td>\n'
                        cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+col_name+'</font></td>\n'
                        cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+col.columnType.getType()+'</font></td>\n'
                        cont += check if col.isPrimaryKey else notck
                        cont += check if col.isNull else notck
                        cont += check if col.isUnique else notck
                        cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+str(col.line)+'</font></td>\n'
                        cont += '</tr>\n'
        cont += '</table>\n<br>\n'
        # Tabla para mostrar los Indices
        cont += '<h3 ALIGN=CENTER>INDICES</h3>\n'
        cont += '<table align="center" cellpadding="20" cellspacing="0"  style="border:2px solid #1f253d">\n'
        cont += '<td bgcolor="#09ad76" width="100" style="text-align:center"><font face="Roboto" color="white" size="4">NOMBRE</font></td>\n'
        cont += '<td bgcolor="#09ad76" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">UNIQUE</font></td>\n'
        cont += '<td bgcolor="#09ad76" width="100" style="text-align:center"><font face="Roboto" color="white" size="4">TABLA</font></td>\n'
        cont += '<td bgcolor="#09ad76" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">COLUMNAS</font></td>\n'
        cont += '<td bgcolor="#09ad76" width="100" style="text-align:center"><font face="Roboto" color="white" size="4">ATRIBUTOS</font></td>\n'
        cont += '<td bgcolor="#09ad76" width="100" style="text-align:center"><font face="Roboto" color="white" size="4">CONDICION</font></td>\n'
        cont += '<td bgcolor="#09ad76" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">TIPO</font></td>\n'
        cont += '<td bgcolor="#09ad76" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">LINEA</font></td>\n'
        for e_name,e_vals in self.index.items():
            cont += '<tr>\n'
            cont += '<td bgcolor="#FFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+e_name+'</font></td>\n'
            cont += check if e_vals.isUnique else notck
            cont += '<td bgcolor="#FFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+e_vals.table+'</font></td>\n'
            cont += '<td bgcolor="#FFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+self.getStrings(e_vals.columns)+'</font></td>\n'
            cont += '<td bgcolor="#FFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+self.getStrings(e_vals.attribs)+'</font></td>\n'
            cont += '<td bgcolor="#FFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+e_vals.condition+'</font></td>\n'
            cont += '<td bgcolor="#FFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+str(e_vals.type_)+'</font></td>\n'
            cont += '<td bgcolor="#FFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+str(e_vals.line)+'</font></td>\n'
            cont += '</tr>\n'
        cont += '</table>\n<br>\n'
        # Tabla para mostrar los Enums
        cont += '<h3 ALIGN=CENTER>ENUM TYPE</h3>\n'
        cont += '<table align="center" cellpadding="20" cellspacing="0"  style="border:2px solid #1f253d">\n'
        cont += '<tr>\n'
        cont += '<td bgcolor="#e82a2a" width="200" style="text-align:center"><font face="Roboto" color="white" size="4">NOMBRE</font></td>\n'
        cont += '<td bgcolor="#e82a2a" width="660" style="text-align:center"><font face="Roboto" color="white" size="4">VALORES</font></td>\n'
        cont += '</tr>'
        for e_name,e_vals in self.userTypes.items():
            cont += '<tr>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+e_name+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+str(e_vals)+'</font></td>\n'
            cont += '</tr>\n'
        cont += '</table>\n</body>\n</HTML>\n'
        file = open("repoteTS.html", "w")
        file.write(header)
        file.write(tbhead)
        file.write(cont)
        file.close()
        
#-----------------------------------------------------------------------------------------------------
    # I N S E R T  -  I N T O

    def insertarDatos(self,nodo):
        tb_name = nodo.valor
        if not(self.usingDB in self.ts):
            self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
            return
        # Recuperar la base de datos
        db_obj = self.ts[self.usingDB]
        # Recuperar la tabla
        if not(tb_name in db_obj.tables):
            self.errors.append(Error('42P01', EType.SEMANTICO, 'undefined_table',nodo.linea))
            return
        # tb_obj = db_obj.tables[tb_name]
        # Lista de tipos de las columnas de la tabla
        # tbcoltypelist = self.getColsTypeList(tb_obj)
        # Obtener lista de tipos entrante
        valores = []
        for p in nodo.hijos:
            if p.hijos[0].etiqueta == 'NOW()':
                now = datetime.now()
                print(str(now))
                valores.append(str(now))
            elif p.hijos[0].etiqueta == 'MD5':
                nmd = p.hijos[0].hijos[0]
                md5 = nmd.valor
                msg = md5.encode()
                #-------------------------------
                salt = b'salt_'
                kdf = PBKDF2HMAC(
                    algorithm=hashes.MD5(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend()
                )
                key = base64.urlsafe_b64encode(kdf.derive(msg))  # Can only use kdf once
                #-------------------------------
                f = Fernet(key)
                enc = f.encrypt(msg)
                enc = enc.decode("utf-8")
                #print(enc)
                valores.append(enc)
            else:    
                valores.append(p.hijos[0].valor)
        result = jsonMode.insert(self.usingDB,tb_name,valores)
        if result == 0: # Operación Exitosa
            self.output.append('Registros en \"'+tb_name+'\" ingresados correctamente.')
        elif result == 1: # Error en la operación
            self.errors.append(Error('XX000', EType.SEMANTICO, 'internal_error',nodo.linea))
        elif result == 2: # Base de datos no existente
            self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
        elif result == 3: # Tabla no existente
            self.errors.append(Error('42P01', EType.SEMANTICO, 'undefined_table',nodo.linea))
        elif result == 4: # Llave primaria duplicada
            self.errors.append(Error('-----', EType.SEMANTICO, 'duplicate_pk',nodo.linea))
        elif result == 5: # Columnas fuera de límits
            self.errors.append(Error('54011', EType.SEMANTICO, 'too_many_columns',nodo.linea))
    
    def getColsTypeList(self,tabla):
        tipos = []
        for c in tabla:
            tipos.append(tabla[c].columnType)
        return tipos

    def erroresHTML(self):
        now = datetime.now()
        fecha = 'Fecha: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)
        hora = 'Hora: '+str(now.hour)+':'+str(now.minute)
        header = '<html><head><br><title>REPORTE DE ERRORES</title></head><body>\n<H1 ALIGN=CENTER><b><font face="Roboto" color="#1f253d">REPORTE DE ERRORES</font></b></H1>\n<H4 ALIGN=CENTER><b><font face="Roboto" color="#1f253d">'+fecha+' | '+hora+'</font></b></H4>\n'
        tbhead = '<table align="center" cellpadding="20" cellspacing="0"  style="border:2px solid #1f253d">\n'
        tbhead += '<tr>\n'
        tbhead += '<td bgcolor="#2d48b5" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">CODIGO</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="150" style="text-align:center"><font face="Roboto" color="white" size="4">TIPO DE ERROR</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="100" style="text-align:center"><font face="Roboto" color="white" size="4">DESCRIPCION</font></td>\n'
        tbhead += '<td bgcolor="#2d48b5" width="50" style="text-align:center"><font face="Roboto" color="white" size="4">LINEA</font></td>\n'
        tbhead += '</tr>\n'
        cont = ''
        template = open("Errores.html", "w")

        for e in self.errors:
            print(e.toString())

        for comp in self.errors:
            # Iteración sobre las tablas de la DB
            cont += '<tr>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+comp.code+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+str(comp.error_type.name)+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+comp.description+'</font></td>\n'
            cont += '<td bgcolor="#FFFFFF" style="text-align:center"><font face="Roboto" color="gray" size="3">'+str(comp.line)+'</font></td>\n'
            cont += '</tr>\n'
        template.write(header)
        template.write(tbhead)
        template.write(cont)
        template.write("</table> \n</body> \n</html>")
        template.close()
        
#------------------------------------------------------------------------------------------------------
# I N D I C E S
 
    def procesarIndices(self,nodo):
        # Obtener el nombre de la columna
        name = nodo.hijos[0].valor
        indx = Index(name)
        columns = []
        attribs = []
        if 'UNIQUE' in nodo.hijos[0].etiqueta:
            indx.isUnique = True
        indx.table = nodo.hijos[1].valor
        if len(nodo.hijos) == 3:
            if nodo.hijos[2].valor != '':
                columns.append(nodo.hijos[2].valor)
            else:
                n = nodo.hijos[2].hijos
                for h in n:
                    if h.etiqueta == 'ID' or h.etiqueta == 'Columna':
                        columns.append(h.valor)
                    else:
                        attribs.append(h.etiqueta+' '+h.valor)
        elif len(nodo.hijos) == 4:
            if nodo.hijos[2].etiqueta == 'USING HASH':
                attribs.append('USING HASH')
                columns.append(nodo.hijos[3].valor)
            elif nodo.hijos[3].etiqueta == 'WHERE':
                columns.append(nodo.hijos[2].valor)
                indx.condition = self.getWhereCondition(nodo.hijos[3])
            elif nodo.hijos[3].etiqueta == 'OPCLASS':
                columns.append(nodo.hijos[2].valor)
                indx.type_ = nodo.hijos[3].valor  
        indx.columns = columns
        indx.attribs = attribs    
        indx.line = nodo.linea
        self.index[name] = indx
        self.output.append('Indice \"'+name+'\" creado exitosamente.')

    def getWhereCondition(self,nodo) -> str:
        return self.getAsString(nodo.hijos[0])

    def getAsString(self, nodo) -> str:
        st = ''
        op = self.scapeCharacters(nodo.valor)
        if len(nodo.hijos) == 0:
            st += nodo.valor + ' '
        elif len(nodo.hijos) == 1:
            st += self.getAsString(nodo.hijos[0]) + ' '
        else:
            st += self.getAsString(nodo.hijos[0]) + ' '
            st += op + ' '
            st += self.getAsString(nodo.hijos[1]) + ' '
        return st
    
    def scapeCharacters(self,op) -> str:
        if '\>' == op:
            return '&#60;'
        elif '\<' == op:
            return '&#62;'
        elif '\=' == op:
            return '='
        else:
            return op

# A L T E R  I N D E X   
    def modificarIndices(self,nodo):
        database = None
        if self.usingDB in self.ts:
            database = self.ts[self.usingDB]
        else:
            self.errors.append(Error('-----', EType.SEMANTICO, 'database_non_exist',nodo.linea))
            return
        index_name = nodo.hijos[0].valor
        # Verificar si el indice existe
        if index_name in self.index:
            # Obtener el indice
            indice = self.index[index_name]
            # Obtener la tabla
            tb_name = indice.table
            # Verificar que la tabla exista
            if tb_name in database.tables:
                table = database.tables[tb_name]
                if nodo.hijos[2].etiqueta == 'ENTERO':
                    i = int(nodo.hijos[2].valor)
                    for e_name,e_val in table.items():
                        if e_val.index == i:
                            # Cambiar nombre
                            for x in range(len(indice.columns)):
                                if nodo.hijos[1].valor == indice.columns[x]:
                                    indice.columns[x] = e_name
                                    self.output.append('Se ha modificado el indice \"'+index_name+'\" exitosamente.')
                                    return
                            self.errors.append(Error('-----',EType.SEMANTICO,'Error al modificar Indice \"'+index_name+'\" no se encontro la tabla \"'+e_name+'\".'))
                            return
                else:
                    n = str(nodo.hijos[2].valor)
                    for e_name,e_val in table.items():
                        if e_name == n:
                            for x in range(len(indice.columns)):
                                if nodo.hijos[1].valor == indice.columns[x]:
                                    indice.columns[x] = e_name
                                    self.output.append('Se ha modificado el indice \"'+index_name+'\" exitosamente.')
                                    return
                            self.errors.append(Error('-----',EType.SEMANTICO,'Error al modificar Indice \"'+index_name+'\" no se encontro la columna \"'+e_name+'\".'))
                            return
            else:
                self.errors.append(Error('42P01', EType.SEMANTICO, 'undefined_table',nodo.linea))

# D R O P  I N D E X
    def eliminarIndice(self,nodo):
        name = nodo.valor
        if name in self.index:
            del self.index[name]
            self.output('Eliminación del indice \"'+name+'\" exitosa.')
        else:
            self.errors.append(Error('-----',EType.SEMANTICO,'index_non_exist',nodo.linea))


######################################## Ejecucion de Querys #########################################

    def Select(self, nodo):

        if len(nodo.hijos) == 1:
            self.querySimple(nodo.hijos[0])
        elif len(nodo.hijos) > 1:
            self.queryCompleta(nodo)
    

    def queryCompleta(self, nodo):
        tablas = []
        distinct = None
        Asterisco = None
        Rows = None
        Where = None
        Groupby = None
        Orderby = None 

        for nodo in nodo.hijos:
            if nodo.etiqueta == 'DISTINC':
                distinct = nodo
            elif nodo.etiqueta == 'ASTERISCO':
                Asterisco = nodo
            elif nodo.etiqueta == 'ROWS':
                Rows = nodo
            elif nodo.etiqueta == 'FROM':
                if self.getTablas(nodo, tablas)  == -1: 
                    return           
            elif nodo.etiqueta == 'WHERE':
                Where = nodo
            elif nodo.etiqueta == 'GROUPBY':
                Groupby = nodo
            elif nodo.etiqueta == 'ORDERBY':
                Orderby = nodo
        
        if Asterisco and not Rows and not distinct and not Where and not Groupby and not Orderby:
            if len(tablas) == 1:
                db = self.ts[self.usingDB]
                tb = db.tables[tablas[0]['Tabla']]
                names = []
                self.getfieldnames(tb, names)
                x = PrettyTable()
                x.field_names = names
                x.add_rows(tablas[0]['Tuplas'])
                self.output.append(x.get_string())

        elif not Asterisco and Rows and not distinct and not Where and not Groupby and not Orderby:
            if len(tablas) == 1:
                db = self.ts[self.usingDB]
                tb = db.tables[tablas[0]['Tabla']]
                names = []
                index = []
                if self.getnamesIndex(tb, index, names, Rows) == -1:
                    return
                
                tupla = tablas[0]['Tuplas']
                rows = []
                for tup in tupla:
                    a = []
                    for i in index:
                        a.append(tup[i])
                    rows.append(a)

                x = PrettyTable()
                x.field_names = names
                x.add_rows(rows)
                self.output.append(x.get_string())
        
        elif Asterisco and not Rows and not distinct and Where and not Groupby and not Orderby:
            if len(tablas) == 1:
                db = self.ts[self.usingDB]
                tb = db.tables[tablas[0]['Tabla']]
                names = []
                self.getfieldnames(tb, names)
                resultado = []
                for tup in tablas[0]['Tuplas']:
                    if self.expresion_logica(Where.hijos[0], tup, names, tablas):
                        resultado.append(tup)

                x = PrettyTable()
                x.field_names = names
                x.add_rows(resultado)
                self.output.append(x.get_string())

        elif not Asterisco and Rows and not distinct and Where and not Groupby and not Orderby:
            if len(tablas) == 1:
                db = self.ts[self.usingDB]
                tb = db.tables[tablas[0]['Tabla']]
                names = []
                self.getfieldnames(tb, names)
                resultado = []
                for tup in tablas[0]['Tuplas']:
                    if self.expresion_logica(Where.hijos[0], tup, names, tablas):
                        resultado.append(tup)
 
                names1 = []
                index = []
                if self.getnamesIndex(tb, index, names1, Rows) == -1:
                    return
                
                rows = []
                for tup in resultado:
                    a = []
                    for i in index:
                        a.append(tup[i])
                    rows.append(a)

                x = PrettyTable()
                x.field_names = names1
                x.add_rows(rows)
                self.output.append(x.get_string())


    def getfieldnames(self, tb, names,):
        for col in tb:
            names.append(col)

    def getnamesIndex(self, tb, index, names, rows):
        for nodo in rows.hijos:
            ban = 0
            if nodo.etiqueta == 'ID':
                for col, val in tb.items():
                    if nodo.valor == col:
                        ban = 1
                        index.append(val.index)
                        if len(nodo.hijos) > 0:
                            names.append(nodo.hijos[0].valor)
                        else :
                            names.append(nodo.valor)
                        break
                if ban == 0:
                    self.errors.append(Error('42703', EType.SEMANTICO, 'No existe la columna '+str(nodo.valor), nodo.linea))
                    return -1
        return 1

    def getTablas(self, instr, tablas):
        for nodo in instr.hijos:
           if nodo.etiqueta == 'Tabla':
                hijos = {}
                hijos['Tabla'] = nodo.valor
                if len(nodo.hijos) > 0:
                   hijos['As'] = nodo.hijos[0].valor
                registros = jsonMode.extractTable(self.usingDB, nodo.valor)
                if registros == None:
                    self.errors.append(Error('42P01', EType.SEMANTICO, 'No existe la relacion '+str(nodo.valor), nodo.linea))
                    return -1
                hijos['Tuplas'] = registros
                tablas.append(hijos)
                return 1

    def querySimple(self, nodo):
        names = []
        resultados = []
        for hijo in nodo.hijos:
            if hijo.etiqueta == 'EXTRACT':
                if len(hijo.hijos) == 3:
                   names.append(hijo.hijos[2].valor)
                else:
                    names.append(hijo.valor)
                self.resolverExtract(hijo, resultados)
            elif hijo.etiqueta == 'DATE PART':
                if len(hijo.hijos) == 3:
                   names.append(hijo.hijos[2].valor)
                else:
                    names.append(hijo.valor)
                self.resolverDatepart(hijo, resultados)
            elif hijo.etiqueta == 'CURRENT_DATE':
                if len(hijo.hijos) == 1:
                    names.append(hijo.hijos[0].valor)
                else:
                    names.append(hijo.etiqueta)
                self.resolverCurrentDate(resultados)
            elif hijo.etiqueta == 'CURRENT_TIME':
                if len(hijo.hijos) == 1:
                    names.append(hijo.hijos[0].valor)
                else:
                    names.append(hijo.etiqueta)
                self.resolverCurrentTime(resultados)
            elif hijo.etiqueta == 'TIMESTAMP':
                if len(hijo.hijos) == 1:
                    names.append(hijo.hijos[0].valor)
                else:
                    names.append(hijo.etiqueta)
                self.resolverTimestampNow(resultados)
            elif hijo.etiqueta == 'NOW':
                self.resolverTimestampNow(resultados)
            elif hijo.etiqueta == 'Matematica':
                if len(hijo.hijos) == 1 or len(hijo.hijos) == 0:
                    names.append(hijo.valor)
                elif len(hijo.hijos) == 2:
                    if hijo.hijos[1].etiqueta == 'Alias':
                        names.append(hijo.hijos[1].valor)
                    else :
                       names.append(hijo.valor) 
                elif len(hijo.hijos) == 3:
                    names.append(hijo.hijos[2].valor)
                self.resolverFuncionMatematica(hijo, resultados)
            elif hijo.etiqueta == 'Trigonometrica':
                if len(hijo.hijos) == 2:
                    names.append(hijo.hijos[1].valor)
                else: 
                    names.append(hijo.valor)
                self.resolverFuncionTrigonometrica(hijo, resultados) 

        x = PrettyTable()
        x.field_names = names
        x.add_rows([resultados])
        self.output.append(x.get_string())

    def resolverExtract(self, nodo, resultados):
        try:
            valfecha, valtiempo = nodo.hijos[1].valor.split(' ')
            fecha = valfecha.split('-')
            tiempo = valtiempo.split(':')

            if nodo.hijos[0].etiqueta == 'YEAR':
                resultados.append(str(fecha[0]))
            elif nodo.hijos[0].etiqueta == 'MONTH': 
                resultados.append(str(fecha[1]))
            elif nodo.hijos[0].etiqueta == 'DAY': 
                resultados.append(str(fecha[2]))
            elif nodo.hijos[0].etiqueta == 'HOUR': 
                resultados.append(str(tiempo[0])) 
            elif nodo.hijos[0].etiqueta == 'MINUTE': 
                resultados.append(str(tiempo[1])) 
            elif nodo.hijos[0].etiqueta == 'SECOND': 
                resultados.append(str(tiempo[2])) 
        except:
            self.errors.append(Error('22008', EType.SEMANTICO, 'El valor de hora/fecha esta fuera de rango '+str(nodo.hijos[1].valor), nodo.linea))
        
        
    def resolverDatepart(self, nodo, resultados):
        try:
            datos = nodo.hijos[1].valor.split(' ')
            cont = 0
            for dt in datos:
                if nodo.hijos[0].valor == dt:
                    resultados.append(datos[cont-1])
                    return
                cont = cont + 1

            self.errors.append(Error('22008', EType.SEMANTICO, 'El valor de hora/fecha esta fuera de rango '+str(nodo.hijos[1].valor), nodo.linea))
        except:
            self.errors.append(Error('22008', EType.SEMANTICO, 'El valor de hora/fecha esta fuera de rango '+str(nodo.hijos[1].valor), nodo.linea))
        

    def resolverCurrentDate(self, resultados):
        today = date.today()
        resultados.append(str(today))
    
    def resolverCurrentTime(self, resultados):
        now = datetime.now()
        time = now.time()
        resultados.append(str(time))

    def resolverTimestampNow(self,  resultados):
        now = datetime.now()
        resultados.append(str(now))

    def resolverFuncionMatematica(self, nodo, resultado):
        if nodo.valor.lower()  == 'degrees':
            a = math.degrees(self.expresion_aritmetica(nodo.hijos[0], [], [], []))
            resultado.append(a)
        elif nodo.valor.lower() == 'div':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            b = self.expresion_aritmetica(nodo.hijos[1], [], [], [])
            c = math.floor(a / b)
            resultado.append(c)
        elif nodo.valor.lower() == 'exp':
            a = math.exp(self.expresion_aritmetica(nodo.hijos[0], [], [], []))
            resultado.append(a)
        elif nodo.valor.lower() == 'factorial':
            a = math.factorial(self.expresion_aritmetica(nodo.hijos[0], [], [], []))
            resultado.append(a)
        elif nodo.valor.lower() == 'floor':
            a = math.floor(self.expresion_aritmetica(nodo.hijos[0], [], [], []))
            resultado.append(a)
        elif nodo.valor.lower() == 'gcd':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            b = self.expresion_aritmetica(nodo.hijos[1], [], [], [])
            c = math.gcd(a , b)
            resultado.append(c)
        elif nodo.valor.lower() == 'ln':
            a = math.log(self.expresion_aritmetica(nodo.hijos[0], [], [], []))
            resultado.append(a)
        elif nodo.valor.lower() == 'log':
            a = math.log10(self.expresion_aritmetica(nodo.hijos[0], [], [], []))
            resultado.append(a)
        elif nodo.valor.lower() == 'mod':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            b = self.expresion_aritmetica(nodo.hijos[1], [], [], [])
            resultado.append(a%b)
        elif nodo.valor.lower() == 'pi':
            resultado.append(math.pi)
        elif nodo.valor.lower() == 'power':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            b = self.expresion_aritmetica(nodo.hijos[1], [], [], [])
            c = math.pow(a , b)
            resultado.append(c)
        elif nodo.valor.lower() == 'radians':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.radians(a)
            resultado.append(c)
        elif nodo.valor.lower() == 'round':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = round(a)
            resultado.append(c)
        elif nodo.valor.lower() == 'sign':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            if a < 0:
                resultado.append(-1)
            else:
                resultado.append(1)
        elif nodo.valor.lower() == 'sqrt':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.sqrt(a)
            resultado.append(c)
        elif nodo.valor.lower() == 'width_bucket':
            nd = nodo.hijos[0]
            a = self.expresion_aritmetica(nd.hijos[0], [], [], [])
            b = self.expresion_aritmetica(nd.hijos[1], [], [], [])
            c = self.expresion_aritmetica(nd.hijos[2], [], [], [])
            d = self.expresion_aritmetica(nd.hijos[3], [], [], [])
            e = d
            cont = 0
            for i in range(b, c+1):
                if i == d:
                    cont +=1
                    d = d+e
                    if a <= i:
                        break
            resultado.append(cont)    
        elif nodo.valor.lower() == 'trunc':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.trunc(a)
            resultado.append(c)
        elif nodo.valor.lower() == 'random':
            c = random.random()
            resultado.append(c)
        elif nodo.valor.lower() == 'abs': 
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.fabs(a)
            resultado.append(c)
        elif nodo.valor.lower() == 'cbrt':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = a ** (1/3)
            resultado.append(c)
        elif nodo.valor.lower() == 'ceil':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.ceil(a)
            resultado.append(c)
        elif nodo.valor.lower() == 'ceiling':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.ceil(a)
            resultado.append(c)

    def resolverFuncionTrigonometrica(self, nodo, resultado):
        if nodo.valor.lower()  == 'acos':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.acos(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'asin':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.asin(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'atan':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.atan(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'cos':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.cos(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'sin':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.sin(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'tan':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.tan(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'sinh':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.sinh(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'cosh':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.cosh(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'tanh':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.tanh(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'asinh':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.asinh(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'acosh':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            c = math.acosh(a)
            resultado.append(c)
        elif nodo.valor.lower()  == 'atanh':
            a = self.expresion_aritmetica(nodo.hijos[0], [], [], [])
            print(a)
            c = math.atanh(a)
            resultado.append(c)

 #########################################  expresiones ###################################################
    def expresion_logica(self, nodo, tupla, names, tablas) -> bool:
        if nodo.etiqueta == 'OPLOG':
            exp1 = self.expresion_logica(nodo.hijos[0], tupla, names, tablas)
            exp2 = self.expresion_logica(nodo.hijos[1], tupla, names, tablas)
            if nodo.valor.lower() == 'and':
                return exp1 and exp2
            elif nodo.valor.lower() == 'or':
                return exp1 or exp2
        
        if nodo.etiqueta == 'OPREL':
            return self.expresion_relacional(nodo, tupla, names, tablas)


    def expresion_relacional(self, nodo, tupla, names, tablas) -> bool:
        if nodo.etiqueta == 'OPREL':
            exp1 = self.expresion_aritmetica(nodo.hijos[0], tupla, names, tablas)
            exp2 = self.expresion_aritmetica(nodo.hijos[1], tupla, names, tablas)
            if nodo.valor.replace('\\', '') == '<':
                return exp1 < exp2
            elif nodo.valor.replace('\\', '') == '>':
                return exp1 > exp2
            elif nodo.valor.replace('\\', '') == '<=':
                return exp1 <= exp2
            elif nodo.valor.replace('\\', '') == '>=':
                return exp1 >= exp2
            elif nodo.valor.replace('\\', '') == '=':
                return exp1 == exp2
            elif nodo.valor.replace('\\', '') == '<>':
                return exp1 != exp2

    def expresion_aritmetica(self, nodo, tupla, names, tablas):
        if len(nodo.hijos) <= 1:
            if nodo.etiqueta == 'ENTERO':
                return int(nodo.valor)
            elif nodo.etiqueta == 'DECIMAL':
                return float(nodo.valor)
            elif nodo.etiqueta == 'CADENA':
                return str(nodo.valor)
            elif nodo.etiqueta == 'LOGICO':
                return nodo.valor.lower() in ("yes", "true", "t", "1")
            elif nodo.etiqueta == 'NEGATIVO':
                exp1 = self.expresion_aritmetica(nodo.hijos[0], tupla, names, tablas)
                return exp1 * -1
            elif nodo.etiqueta == 'ID':
                i = 0
                for val in names:
                    if nodo.valor == val:
                        return tupla[i]
                    i += 1
                self.errors.append(Error('42703', EType.SEMANTICO, 'No existe la columna '+str(nodo.valor), nodo.linea))   
            elif nodo.etiqueta == 'AliasTabla':
                if tablas[0]['As'] == nodo.valor:
                    return self.expresion_aritmetica(nodo.hijos[0], tupla, names, tablas)
                self.errors.append(Error('42P01', EType.SEMANTICO, 'Falta una entrada para -> '+str(nodo.valor), nodo.linea))
        elif len(nodo.hijos) == 2: 
            exp1 = self.expresion_aritmetica(nodo.hijos[0], tupla, names, tablas)
            exp2 = self.expresion_aritmetica(nodo.hijos[1], tupla, names, tablas)
            if nodo.valor == '+':
                return exp1 + exp2
            elif nodo.valor == '-':
                return exp1 - exp2
            elif nodo.valor == '/':
                return exp1 / exp2
            elif nodo.valor == '*':
                return exp1 * exp2
            elif nodo.valor == '%':
                return exp1 % exp2
            elif nodo.valor == '^':
                return exp1 ** exp2

#---------------------------------------------------------------------------------------------------------
# G R A F I C A R  -  A S T
    def graficarAST(self,raiz):
        c = [1]
        file = open("ast.dot", "w")
        file.write(
                'digraph G {\n'
                + 'rankdir=TB; '
                + 'node[fillcolor=\"darkturquoise:darkslategray2\", shape=record ,fontname = \"Berlin Sans FB\" ,style = filled]  \n'
                + 'edge[arrowhead=none]; \n'
            )
        file.write(self.recorrerNodos(raiz,c))
        file.write('}\n')
        file.close()
        render('dot','svg','ast.dot')

    def recorrerNodos(self,nodo,c):
        c[0] += 1
        codigo = ""
        padre = 'nodo'+str(c[0])
        codigo = padre + '[label = \"' + nodo.etiqueta + '\\n' + str(nodo.valor) + '\"];\n'
        for hijo in nodo.hijos: 
            codigo += padre + '->' + 'nodo' + str(c[0]+1) + '\n'
            codigo += self.recorrerNodos(hijo, c)
        return codigo

#---------------------------------------------------------------------------------------------------------
#  R E P O R T E  -  G R A M A T I C A L

    def crearReporte(self,raiz) :
        file = open("ReporteEjecucion.md", "w")
        file.write('## GRUPO #11 \n'
                + '# *REPORTE GRAMATICAL DE LA EJECUCION*\n\n')
        file.write(self.recorrerAST(raiz))
        file.close()

    def recorrerAST(self,nodo):
        bnf = ""
        contador = 1
        for hijo in nodo.hijos: 
            bnf += '### Instruccion #'+str(contador)+' \n'
            bnf += '```bnf\n'
            bnf += hijo.gramatica + '\n'
            bnf += self.recorrerHijo(hijo)
            bnf += '```\n\n'
            contador += 1
        return bnf

    def recorrerHijo(self,nodo):
        bnf = ""
        for hijo in nodo.hijos: 
            if hijo.gramatica != '':
                bnf += hijo.gramatica + '\n'
            bnf += self.recorrerHijo(hijo)
        return bnf

