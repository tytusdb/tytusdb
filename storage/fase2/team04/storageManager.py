# Package:      Storage Manager
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developers:   Alexis Peralta, Juan Carlos Gomez

from storage.avl import avlMode
from storage.b import BMode
from storage.bplus import BPlusMode
from storage.hash import HashMode
from storage.isam import ISAMMode
from storage.json_mode import jsonMode
from storage.dict import DictMode
from storage.b import Serializable
from DBList import DBList
import re
import codificar
from random import randint

#Para la password
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#para encriptar y desencriptar
from cryptography.fernet import Fernet

MODES = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
HEX_SYMBOLS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
VALID_ENCODING = ["utf8", "iso-8859-1", "ascii"]
DB_NAME_PATTERN = "^[a-zA-Z][a-zA-Z0-9#@$_]*"

# Obteniendo la lista general de bases de datos a partir del binario almacenado
# Si no existe el binario, se crea una nueva lista de bases de datos y se almacena
# el binario
try:
    databases = Serializable.rollback("lista_bases_de_datos")
except FileNotFoundError:
    databases = DBList()
    Serializable.commit(databases, "lista_bases_de_datos")

# Descripción:
#     Crea una nueva base de datos
# Parámetros:
#     database:str - El nombre de la nueva base de datos
#     mode:str - El modo de almacenamiento a utilizar en la base de datos
#     encoding:str - La codificación utilizada por la base de datos
# Valores de Retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - Base de datos existente
#     3 - Modo incorrecto
#     4 - Codificación incorrecta
def createDatabase(database: str, mode: str, encoding: str) -> int:
    if encoding not in VALID_ENCODING:
        return 4
    if databases.search(database) != None:
        return 2
    if mode == "avl":
        code = avlMode.createDatabase(database)
    elif mode == "b":
        code = BMode.createDatabase(database)
    elif mode == "bplus":
        code = BPlusMode.createDatabase(database)
    elif mode == "dict":
        code = DictMode.createDatabase(database)
    elif mode == "isam":
        code = ISAMMode.createDatabase(database)
    elif mode == "json":
        code = jsonMode.createDatabase(database)
    elif mode == "hash":
        code = HashMode.createDatabase(database)
    else:
        return 3
    if code == 0:
        databases.create(database, mode, encoding)
        try:
            for i in range(5):
                try:
                    Serializable.commit(databases, "lista_bases_de_datos")
                except:
                    continue
        except:
            code_drop = dropDatabase(database)
            if code_drop == 0:
                databases.delete(database)
                return 1
            else:
                for i in range(4):
                    code_drop = dropDatabase(database)
                    if code_drop == 0:
                        databases.delete(database)
                        break
                return 1
    return code

# Descripción:
#     Devuelve un nombre aleatorio que no existe entre las bases de datos
# Valores de retorno:
#     str - Un nombre no utilizado entre las bases de datos
def temp_name():
    temp_database_name = HEX_SYMBOLS[randint(10, len(HEX_SYMBOLS)-1)]
    for x in range(4):
        temp_database_name += HEX_SYMBOLS[randint(0, len(HEX_SYMBOLS)-1)]
    while databases.search(temp_database_name) != None:
        temp_database_name += HEX_SYMBOLS[randint(0, len(HEX_SYMBOLS)-1)]
    return temp_database_name

# Descripción:
#     Cambia el modo de almacenamiento de una base de datos
# Parámetros:
#     database:str - El nombre de la base de datos que se desea modificar
#     mode:str - Es un string indicando el modo 'avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash'
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     4 - modo incorrecto
def alterDatabaseMode(database: str, mode: str) -> int:
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if mode not in MODES:
        return 4
    tables = showTables(database)
    temp_db_name = temp_name()
    createDatabase(temp_db_name, mode, dbs[0].encoding)
    
    for table in tables:
        aux_table = databases.find_table(database, table)
        if createTable(temp_db_name, table, aux_table.columns) != 0:
            dropDatabase(temp_db_name)
            return 1
        if aux_table.pk != []:
            if alterAddPK(temp_db_name, table, aux_table.pk) != 0:
                dropDatabase(temp_db_name)
                return 1
        registers = extractTable(database, table)
        for register in registers:
            if insert(temp_db_name, table, register) != 0:
                dropDatabase(temp_db_name)
                return 1
    
    if dropDatabase(database) != 0:
        dropDatabase(temp_db_name)
        return 1
    if alterDatabase(temp_db_name, database) != 0:
        return 1
    return 0

# Descripción:
#     Devuelve una lista con los nombres de las bases de datos
# Valores de retorno:
#     Lista de strings con los nombres de las bases de datos
#     Si ocurrió un error devuelve una lista vacía
#     Si no hay bases de datos devuelve una lista vacía
def showDatabases() -> list:
    return databases.list_databases_diff()

# Descripción:
#     Renombra la base de datos databaseOld por databaseNew
# Parámetros:
#     databaseOld:str - Nombre actual de la base de datos, debe cumplir con las reglas de identificadores de SQL
#     databaseNew:str - Nuevo nombre de la base de datos, debe cumplir con las reglas de identificadores de SQL
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - databaseOld no existente
#     3 - databaseNew existente
def alterDatabase(databaseOld: str, databaseNew: str) -> int:
    if re.search(DB_NAME_PATTERN, databaseOld) and re.search(DB_NAME_PATTERN, databaseNew):
        if databases.search(databaseNew) != None:
            return 3
        dbs = databases.find_all(databaseOld)
        if dbs == []:
            return 2
        for db in dbs:
            if db.mode == "avl":
                code = avlMode.alterDatabase(databaseOld, databaseNew)
            elif db.mode == "b":
                code = BMode.alterDatabase(databaseOld, databaseNew)
            elif db.mode == "bplus":
                code = BPlusMode.alterDatabase(databaseOld, databaseNew)
            elif db.mode == "dict":
                code = DictMode.alterDatabase(databaseOld, databaseNew)
            elif db.mode == "isam":
                code = ISAMMode.alterDatabase(databaseOld, databaseNew)
            elif db.mode == "json":
                code = jsonMode.alterDatabase(databaseOld, databaseNew)
            elif db.mode == "hash":
                code = HashMode.alterDatabase(databaseOld, databaseNew)
            if code == 0:
                db.name = databaseNew
                try:
                    Serializable.commit(databases, "lista_bases_de_datos")
                    return 0
                except:
                    db.name = databaseOld
            return 1
    else:
        return 1

# Descripción:
#     Elimina por completo la base de datos indicada en database
# Parámetros:
#     database:str - Es el nombre de la base de datos que se desea eliminar, debe cumplir con las reglas de identificadores de SQL
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - Base de datos no existente
def dropDatabase(database: str) -> int:
    if re.search(DB_NAME_PATTERN, database):
        dbs = databases.find_all(database)
        if dbs == []:
            return 2
        for db in dbs:
            if db.mode == "avl":
                code = avlMode.dropDatabase(database)
            elif db.mode == "b":
                code = BMode.dropDatabase(database)
            elif db.mode == "bplus":
                code = BPlusMode.dropDatabase(database)
            elif db.mode == "dict":
                code = DictMode.dropDatabase(database)
            elif db.mode == "isam":
                code = ISAMMode.dropDatabase(database)
            elif db.mode == "json":
                code = jsonMode.dropDatabase(database)
            elif db.mode == "hash":
                code = HashMode.dropDatabase(database)
            if code == 0:
                databases.delete(db.name)
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return 0
                    except:
                        continue
            return 1
    else:
        return 1

# Descripción:
#     Crea una nueva tabla en la base de datos indicada
# Parámetros:
#     database:str - El nombre de la base de datos a la que se desea agregar la tabla
#     table:str - El nombre de la nueva tabla
#     numberColumns:int - La cantidad de columnas que manejará la tabla
# Valores de Retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - Base de datos inexistente
#     3 - Tabla existente
def createTable(database: str, table: str, numberColumns: int) -> int:
    db = databases.search(database)
    if db == None:
        return 2
    if table in showTables(database):
        return 3
    if db.mode == "avl":
        result = avlMode.createTable(database, table, numberColumns)
    elif db.mode == "b":
        result = BMode.createTable(database, table, numberColumns)
    elif db.mode == "bplus":
        result = BPlusMode.createTable(database, table, numberColumns)
    elif db.mode == "dict":
        result = DictMode.createTable(database, table, numberColumns)
    elif db.mode == "isam":
        result = ISAMMode.createTable(database, table, numberColumns)
    elif db.mode == "json":
        result = jsonMode.createTable(database, table, numberColumns)
    elif db.mode == "hash":
        result = HashMode.createTable(database, table, numberColumns)
    if result == 0:
        if db.tables.create(table, numberColumns) == 0:
            for x in range(5):
                try:
                    Serializable.commit(databases, "lista_bases_de_datos")
                    return result
                except:
                    continue
            return 1
    return result

# Descripción:
#     Devuelve una lista con los nombres de todas las tablas de la base de datos
# Parámetros:
#     database:str - El nombre de la base de datos cuyas tablas se desean obtener
# Valores de retorno:
#     Si existen la base de datos y las tablas devuelve una lista de nombres de tablas
#     Si existe la base de datos, pero no existen tablas devuelve una lista vacía
#     Si no existe la base de datos devuelve None
def showTables(database: str) -> list:
    dbs = databases.find_all(database)
    if dbs == []:
        return None
    result = []
    for db in dbs:
        if db.mode == "avl":
            result += avlMode.showTables(database)
        elif db.mode == "b":
            result += BMode.showTables(database)
        elif db.mode == "bplus":
            result += BPlusMode.showTables(database)
        elif db.mode == "dict":
            result += DictMode.showTables(database)
        elif db.mode == "isam":
            result += ISAMMode.showTables(database)
        elif db.mode == "json":
            result += jsonMode.showTables(database)
        elif db.mode == "hash":
            result += HashMode.showTables(database)
    return result

# Descripción:
#     Elimina la llave primaria actual en la información de la tabla, manteniendo el índice
#     actual de la estructura del árbol hasta que se invoque de nuevo el alterAddPK()
# Parámetros:
#     database:str - El nombre de la base de datos a utilizar
#     table:str - El nombre de la tabla a utilizar
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - pk no existente
def alterDropPK(database: str, table: str) -> int:
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    for db in dbs:
        if db.mode == "avl":
            result = avlMode.alterDropPK(database, table)
        elif db.mode == "b":
            result = BMode.alterDropPK(database, table)
        elif db.mode == "bplus":
            result = BPlusMode.alterDropPK(database, table)
        elif db.mode == "dict":
            result = DictMode.alterDropPK(database, table)
        elif db.mode == "isam":
            result = ISAMMode.alterDropPK(database, table)
        elif db.mode == "json":
            result = jsonMode.alterDropPK(database, table)
        elif db.mode == "hash":
            result = HashMode.alterDropPK(database, table)
        if result != 3:
            if result == 0:
                db.tables.search(table).pk = []
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        break
                return 1
            break
    return result

# Descripción:
#     Agrega una columna al final de cada registro de la tabla y base de datos especificada
# Parámetros:
#     database:str - El nombre de la base de datos a utilizar
#     table:str - El nombre de la tabla a utilizar
#     default:any - Es el valor que se establecerá en a la nueva columna para los registros existentes
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
def alterAddColumn(database: str, table: str, default: any) -> int:
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    for db in dbs:
        if db.mode == "avl":
            result = avlMode.alterAddColumn(database, table, default)
        elif db.mode == "b":
            result = BMode.alterAddColumn(database, table, default)
        elif db.mode == "bplus":
            result = BPlusMode.alterAddColumn(database, table, default)
        elif db.mode == "dict":
            result = DictMode.alterAddColumn(database, table, default)
        elif db.mode == "isam":
            result = ISAMMode.alterAddColumn(database, table, default)
        elif db.mode == "json":
            result = jsonMode.alterAddColumn(database, table, default)
        elif db.mode == "hash":
            result = HashMode.alterAddColumn(database, table, default)
        if result != 3:
            if result == 0:
                db.search(table).columns += 1
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        break
                return 1
            break
    return result

# Descripción:
#     Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias
# Parámetros:
#     database:str - El nombre de la base de datos a utilizar
#     table:str - El nombre de la tabla a utilizar
#     columnNumber:int - El número de la columna a eliminar
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existe
#     3 - table no existe
#     4 - Llave no puede eliminarse o tabla quedarse sin columnas
#     5 - Columna fuera de límites
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    for db in dbs:
        if db.mode == "avl":
            result = avlMode.alterDropColumn(database, table, columnNumber)
        elif db.mode == "b":
            result = BMode.alterDropColumn(database, table, columnNumber)
        elif db.mode == "bplus":
            result = BPlusMode.alterDropColumn(database, table, columnNumber)
        elif db.mode == "dict":
            result = DictMode.alterDropColumn(database, table, columnNumber)
        elif db.mode == "isam":
            result = ISAMMode.alterDropColumn(database, table, columnNumber)
        elif db.mode == "json":
            result = jsonMode.alterDropColumn(database, table, columnNumber)
        elif db.mode == "hash":
            result = HashMode.alterDropColumn(database, table, columnNumber)
        if result != 3:
            if result == 0:
                db.search(table).columns -= 1
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        break
                return 1
            break
    return result

# Descripción:
#      Inserta un registro en la estructura de datos asociada a la tabla y la base de datos
# Parámetros:
#      database:str - El nombre de la base de datos a utilizar
#      table:str - El nombre de la tabla a utilizar
#      register:list - Es una lista de elementos que represent un registro
# Valores de retorno:
#      0 - Operación exitosa
#      1 - Error en la operación
#      2 - database no existente
#      3 - table no existente
#      4 - Llave primaria duplicada
#      5 - Columnas fuera de límites
def insert(database: str, table: str, register: list):
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    for db in dbs:
        if db.mode == "avl":
            result = avlMode.insert(database, table, register)
        elif db.mode == "b":
            result = BMode.insert(database, table, register)
        elif db.mode == "bplus":
            result = BPlusMode.insert(database, table, register)
        elif db.mode == "dict":
            result = DictMode.insert(database, table, register)
        elif db.mode == "isam":
            result = ISAMMode.insert(database, table, register)
        elif db.mode == "json":
            result = jsonMode.insert(database, table, register)
        elif db.mode == "hash":
            result = HashMode.insert(database, table, register)
        if result != 3:
            break
    return result

# Descripción:
#      Inserta un registro en la estructura de datos asociada a la tabla y la base de datos con el modo indicado
# Parámetros:
#      database:str - El nombre de la base de datos a utilizar
#      table:str - El nombre de la tabla a utilizar
#      register:list - Es una lista de elementos que represent un registro
#      mode:str - El modo de la base de datos en la que se desea insertar
# Valores de retorno:
#      0 - Operación exitosa
#      1 - Error en la operación
#      2 - database no existente
#      3 - table no existente
#      4 - Llave primaria duplicada
#      5 - Columnas fuera de límites
#      6 - Modo incorrecto
def __insert_sp(database: str, table: str, register: list, mode: str):
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    tb = databases.find_table(database, table)
    if tb == None:
        return 3
    if len(register) != tb.columns:
        return 5
    if mode not in MODES:
        return 6
    for db in dbs:
        if db.mode != mode:
            continue
        if db.mode == "avl":
            result = avlMode.insert(database, table, register)
        elif db.mode == "b":
            result = BMode.insert(database, table, register)
        elif db.mode == "bplus":
            result = BPlusMode.insert(database, table, register)
        elif db.mode == "dict":
            result = DictMode.insert(database, table, register)
        elif db.mode == "isam":
            result = ISAMMode.insert(database, table, register)
        elif db.mode == "json":
            result = jsonMode.insert(database, table, register)
        elif db.mode == "hash":
            result = HashMode.insert(database, table, register)
        else:
            continue
        if result != 3:
            break
    return result

# Descripción:
#     Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado
# Parámetros:
#     file:str - Ruta del archivo CSV a utilizar
#     database:str - El nombre de la base de datos a utilizar
#     table:str - El nombre de la tabla a utilizar
# Valores de retorno:
#     Lista con los valores enteros que devuelve el insert por cada fila del CSV
#     Si ocurrió un error o el archivo CSV no tiene filas devuelve una lista vacía
def loadCSV(file: str, database: str, table: str) -> list:
    try:
        result = []
        dbs = databases.find_all(database)
        for db in dbs:
            tb = db.tables.search(table)
            if tb == None:
                continue
            if db.mode == "avl":
                result = avlMode.loadCSV(file, database, table)
            elif db.mode == "b":
                result = BMode.loadCSV(file, database, table)
            elif db.mode == "bplus":
                result = BPlusMode.loadCSV(file, database, table)
            elif db.mode == "dict":
                result = DictMode.loadCSV(file, database, table)
            elif db.mode == "isam":
                result = ISAMMode.loadCSV(file, database, table)
            elif db.mode == "json":
                result = jsonMode.loadCSV(file, database, table)
            elif db.mode == "hash":
                result = HashMode.loadCSV(file, database, table)
        return result
    except:
        return []

# Descripción:
#     Devuelve una lista con las rutas de todos los archivos binarios relacionados a la base
#     de datos indicada
# Parámetros:
#     database:str - El nombre de la base de datos
# Valores de retorno:
#     Si existen binarios para la base de datos, un lista con todas las rutas
#     Si no existe ningún binario relacionado a la base de datos, una lista vacía
def get_routes(database: str) -> list:
    dbs = databases.find_all(database)
    if dbs == []:
        return []
    routes = []
    for db in dbs:
        if db.mode == "bplus":
            routes.append(".\\data\\BPlusMode\\{0}\\{1}.bin".format(db.name, db.name))

        tables = []
        aux = db.tables.first
        while aux != None:
            tables.append(aux)
            aux = aux.next
        
        if db.mode == "avl":
            for table in tables:
                route = ".\\data\\avlMode\\{0}_{1}.tbl".format(db.name, table.name)
                if os.path.exists(route):
                    routes.append(route)
        elif db.mode == "b":
            for table in tables:
                route = ".\\data\\b\\{0}-{1}-b.bin".format(db.name, table.name)
                if os.path.exists(route):
                    routes.append(route)
        elif db.mode == "bplus":
            for table in tables:
                route = ".\\data\\BPlusMode\\{0}\\{1}\\{2}.bin".format(db.name, table.name, table.name)
                if os.path.exists(route):
                    routes.append(route)
        elif db.mode == "dict":
            for table in tables:
                route = ".\\data\\{0}\\{1}.bin".format(db.name, table.name)
                if os.path.exists(route):
                    routes.append(route)
        elif db.mode == "isam":
            for table in tables:
                route = ".\\data\\ISAMMode\\tables\\{0}{1}.bin".format(db.name, table.name)
                if os.path.exists(route):
                    routes.append(route)
        elif db.mode == "json":
            for table in tables:
                route = ".\\data\\json\\{0}-{1}".format(db.name, table.name)
                if os.path.exists(route):
                    routes.append(route)
        elif db.mode == "hash":
            for table in tables:
                route = ".\\data\\hash\\{0}\\{1}.bin".format(db.name, table.name)
                if os.path.exists(route):
                    routes.append(route)
    return routes

# Descripción:
#     Devuelve una lista con la ruta del archivo binario correspondiente a la tabla indicada
# Parámetros:
#     database:str - El nombre de la base de datos
#     table:str - El nombre de la tabla
# Valores de retorno:
#     str - La ruta del archivo binario de la tabla
#     None - Si no existe archivo binario para la tabla
def get_route_table(database: str, table: str) -> list:
    dbs = databases.find_all(database)
    if dbs == []:
        return None
    route = None
    for db in dbs:
        tb = db.tables.search(table)
        if tb == None:
            continue
        if db.mode == "avl":
            route = ".\\data\\avlMode\\{0}_{1}.tbl".format(db.name, tb.name)
        elif db.mode == "b":
            route = ".\\data\\b\\{0}-{1}-b.bin".format(db.name, tb.name)
        elif db.mode == "bplus":
            route = ".\\data\\BPlusMode\\{0}\\{1}\\{2}.bin".format(db.name, tb.name, tb.name)
        elif db.mode == "dict":
            route = ".\\data\\{0}\\{1}.bin".format(db.name, tb.name)
        elif db.mode == "isam":
            route = ".\\data\\ISAMMode\\tables\\{0}{1}.bin".format(db.name, tb.name)
        elif db.mode == "json":
            route = ".\\data\\json\\{0}-{1}".format(db.name, tb.name)
        elif db.mode == "hash":
            route = ".\\data\\hash\\{0}\\{1}.bin".format(db.name, tb.name)
    if route != None and os.path.exists(route):
        return route
    return None

def delete(database: str, table: str, columns: list):
    db = databases.search(database)
    if db == None:
        return 2
    if db.mode == "avl":
        result = avlMode.delete(database, table, columns)
    elif db.mode == "b":
        result = BMode.delete(database, table, columns)
    elif db.mode == "bplus":
        result = BPlusMode.delete(database, table, columns)
    elif db.mode == "dict":
        result = DictMode.delete(database, table, columns)
    elif db.mode == "isam":
        result = ISAMMode.delete(database, table, columns)
    elif db.mode == "json":
        result = jsonMode.delete(database, table, columns)
    elif db.mode == "hash":
        result = HashMode.delete(database, table, columns)
    return result

def extractTable(database,table):
    dbs = databases.find_all(database)
    if dbs == []:
        return None
    if databases.find_table(database, table) == None:
        return None
    result = []
    for db in dbs:
        tb = db.tables.search(table)
        if tb != None:
            if db.mode == "avl":
                result = avlMode.extractTable(database,table)
            elif db.mode == "b":
                result = BMode.extractTable(database,table)
            elif db.mode == "bplus":
                result = BPlusMode.extractTable(database,table)
            elif db.mode == "dict":
                result = DictMode.extractTable(database,table)
            elif db.mode == "isam":
                result = ISAMMode.extractTable(database,table)
            elif db.mode == "json":
                result = jsonMode.extractTable(database,table)
            elif db.mode == "hash":
                result = HashMode.extractTable(database,table)
            else:
                continue
    return result

def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    db = databases.search(database)
    if db == None:
        return None
    if db.mode == "avl":
        result = avlMode.extractRangeTable(database,table,columnNumber,lower, upper)
    elif db.mode == "b":
        result = BMode.extractRangeTable(database,table,columnNumber,lower, upper)
    elif db.mode == "bplus":
        result = BPlusMode.extractRangeTable(database,table,columnNumber,lower, upper)
    elif db.mode == "dict":
        result = DictMode.extractRangeTable(database,table,columnNumber,lower, upper)
    elif db.mode == "isam":
        result = ISAMMode.extractRangeTable(database,table,columnNumber,lower, upper)
    elif db.mode == "json":
        result = jsonMode.extractRangeTable(database,table,columnNumber,lower, upper)
    elif db.mode == "hash":
        result = HashMode.extractRangeTable(database,table,columnNumber,lower, upper)
    return result

def alterTable(database, tableOld, tableNew):
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    for db in dbs:
        if db.mode == "avl":
            result = avlMode.alterTable(database,tableOld,tableNew)
        elif db.mode == "b":
            result = BMode.alterTable(database,tableOld,tableNew)
        elif db.mode == "bplus":
            result = BPlusMode.alterTable(database,tableOld,tableNew)
        elif db.mode == "dict":
            result = DictMode.alterTable(database,tableOld,tableNew)
        elif db.mode == "isam":
            result = ISAMMode.alterTable(database,tableOld,tableNew)
        elif db.mode == "json":
            result = jsonMode.alterTable(database,tableOld,tableNew)
        elif db.mode == "hash":
            result = HashMode.alterTable(database,tableOld,tableNew)
        if result != 3:
            if result == 0:
                db.tables.search(tableOld).name = tableNew
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        break
                return 1
            break
    return result

def dropTable(database,table):
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    for db in dbs:
        if db.mode == "avl":
            result = avlMode.dropTable(database, table)
        elif db.mode == "b":
            result = BMode.dropTable(database, table)
        elif db.mode == "bplus":
            result = BPlusMode.dropTable(database, table)
        elif db.mode == "dict":
            result = DictMode.dropTable(database, table)
        elif db.mode == "isam":
            result = ISAMMode.dropTable(database, table)
        elif db.mode == "json":
            result = jsonMode.dropTable(database, table)
        elif db.mode == "hash":
            result = HashMode.dropTable(database, table)
        if result != 3:
            if result == 0:
                db.tables.delete(table)
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        break
                return 1
            break
    return result

# Descripción:
#     Elimina una tabla especificada en una base de datos con el nombre y modo especificados.
# Parámetros:
#     database:str - El nombre de la base de datos que se va a utilizar
#     table:str - El nombre de la tabla que se desea eliminar
#     mode:str - El modo que debe tener la base de datos que se va a utilizar
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error durante la operación
#     2 - database no existe
#     3 - table no existe
def __drop_table_sp(database, table, mode):
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if databases.find_table(database, table) == None:
        return 3
    for db in dbs:
        if db.mode == mode == "avl":
            result = avlMode.dropTable(database, table)
        elif db.mode == mode == "b":
            result = BMode.dropTable(database, table)
        elif db.mode == mode == "bplus":
            result = BPlusMode.dropTable(database, table)
        elif db.mode == mode == "dict":
            result = DictMode.dropTable(database, table)
        elif db.mode == mode == "isam":
            result = ISAMMode.dropTable(database, table)
        elif db.mode == mode == "json":
            result = jsonMode.dropTable(database, table)
        elif db.mode == mode == "hash":
            result = HashMode.dropTable(database, table)
        else:
            continue
        if result != 3:
            if result == 0:
                db.tables.delete(table)
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        break
                return 1
            break
    return result

def extractRow(database, table, columns):
    db = databases.search(database)
    if    db == None:
        return 2
    if db.mode == "avl":
        result = avlMode.extractRow(database, table, columns)
    elif db.mode == "b":
        result = BMode.extractRow(database, table, columns)
    elif db.mode == "bplus":
        result = BPlusMode.extractRow(database, table, columns)
    elif db.mode == "dict":
        result = DictMode.extractRow(database, table, columns)
    elif db.mode == "isam":
        result = ISAMMode.extractRow(database, table, columns)
    elif db.mode == "json":
        result = jsonMode.extractRow(database, table, columns)
    elif db.mode == "hash":
        result = HashMode.extractRow(database, table, columns)
    return result

def update(database, table, register, columns):
    db = databases.search(database)
    if db == None:
        return 2
    if db.mode == "avl":
        result = avlMode.update(database, table, register, columns)
    elif db.mode == "b":
        result = BMode.update(database, table, register, columns)
    elif db.mode == "bplus":
        result = BPlusMode.update(database, table, register, columns)
    elif db.mode == "dict":
        result = DictMode.update(database, table, register, columns)
    elif db.mode == "isam":
        result = ISAMMode.update(database, table, register, columns)
    elif db.mode == "json":
        result = jsonMode.update(database, table, register, columns)
    elif db.mode == "hash":
        result = HashMode.update(database, table, register, columns)
    return result

def truncate(database, table):
    db = databases.search(database)
    if db == None:
        return 2
    if db.mode == "avl":
        result = avlMode.truncate(database, table)
    elif db.mode == "b":
        result = BMode.truncate(database, table)
    elif db.mode == "bplus":
        result = BPlusMode.truncate(database, table)
    elif db.mode == "dict":
        result = DictMode.truncate(database, table)
    elif db.mode == "isam":
        result = ISAMMode.truncate(database, table)
    elif db.mode == "json":
        result = jsonMode.truncate(database, table)
    elif db.mode == "hash":
        result = HashMode.truncate(database, table)
    return result

def alterAddPK(database, table, columns):
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    for db in dbs:
        if db.mode == "avl":
            result = avlMode.alterAddPK(database, table, columns)
        elif db.mode == "b":
            result = BMode.alterAddPK(database, table, columns)
        elif db.mode == "bplus":
            result = BPlusMode.alterAddPK(database, table, columns)
        elif db.mode == "dict":
            result = DictMode.alterAddPK(database, table, columns)
        elif db.mode == "isam":
            result = ISAMMode.alterAddPK(database, table, columns)
        elif db.mode == "json":
            result = jsonMode.alterAddPK(database, table, columns)
        elif db.mode == "hash":
            result = HashMode.alterAddPK(database, table, columns)
        if result != 3:
            if result == 0:
                db.tables.search(table).pk += columns
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        break
                return 1
            break
    return result

#Descripcion:
#	Crifra el texto backup con la llave password y devuelve el criptograma. Se puede utilizar cualquier método y biblioteca. (UPDATE)
#Parámetro
#	backup: es el nombre de la base de datos a utilizar.
#Valor de retorno:
#	0 operación exitosa
#	1 error en la operación.
def encrypt(backup: str, password: str):
	try:
		if type(backup) == bytes:
			#Generar una llave con el password ingresado
			password_provided = password
			passwordB = password_provided.encode() #convertido a byte

			salt = b"\x1c(\xe8\xe0J^\xd9\x81~f\n\xc9\xe3'\xdb\xf3" # este salt = os.urandom(16)

			kdf = PBKDF2HMAC(
				algorithm=hashes.SHA256(),
				length=32,
				salt=salt,
				iterations=100000,
				backend=default_backend()
			)

			#Llave generada
			key = base64.urlsafe_b64encode(kdf.derive(passwordB))#solo se puede usar kdf una vez

			#Cifrar el mensaje
			f = Fernet(key)
			encrip = f.encrypt(backup)

			return encrip

		else:

			return None #error
	except:
		return None #error

# Descripcion:
# 	Descrifra el texto cipherBackup con la llave password y devuelve el texto plano. Se puede utilizar cualquier método y biblioteca. (UPDATE)
# Parámetros:
# 	cipherBackup: es el nombre de la base de datos a utilizar.
# Valor de retorno:
#	0 operación exitosa
#	1 error en la operación.
def decrypt(cipherBackup: str, password: str):

	try:
		#Generar una llave con el password ingresado
		password_provided = password
		passwordB = password_provided.encode() #convertido a byte

		salt = b"\x1c(\xe8\xe0J^\xd9\x81~f\n\xc9\xe3'\xdb\xf3" # este salt = os.urandom(16)

		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100000,
			backend=default_backend()
		)

		#Llave generada
		key = base64.urlsafe_b64encode(kdf.derive(passwordB))#solo se puede usar kdf una vez

		#Desencriptar el mensaje
		f2 = Fernet(key)
		desen = f2.decrypt(cipherBackup)
		#desen_str = desen.decode()
		#print("Mensaje Desencriptado:\n",desen_str)
		return desen

	except:
		return None #error

