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
from blockchain import blockchain
import hashlib
import re
import zlib
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
        databases.search(database).main_db = True
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
def __create_database_sp(database: str, mode: str, encoding: str) -> int:
    if encoding not in VALID_ENCODING:
        return 4
    dbs = databases.find_all(database)
    if dbs != None:
        for db in dbs:
            if db.name == database and db.mode == mode:
                # Ya existe esta base de datos alternativa
                return 0
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
    __create_database_sp(temp_db_name, mode, dbs[0].encoding)
    
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
    databases.search(temp_db_name).main_db = True
    for db in dbs:
        if __drop_database_sp(database, db.mode) != 0:
            dropDatabase(temp_db_name)
            return 1
    if alterDatabase(temp_db_name, database) != 0:
        return 1
    return 0

# Descripción:
#     Cambia el modo de almacenamiento de una tabla de una base de datos especificada
# Parámetros:
#     database:str - El nombre de la base de datos que se desea modificar
#     table:str - El nombre de la tabla que se desea modificar
#     mode:str - Es un string indicando el modo 'avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash'
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - modo incorrecto
def alterTableMode(database: str, table: str, mode: str) -> int:
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if databases.find_table(database, table) == None:
        return 3
    if mode not in MODES:
        return 4
    for db in dbs:
        tb = db.tables.search(table)
        if tb != None:
            # Revisando si la tabla ya se encuentra en una base de datos con el modo indicado
            if db.mode == mode:
                return 0
            # Se revisa si ya existe una base de datos alternativa con el modo indicado
            alt_db_exists = False
            for aux in dbs:
                if aux.name == database and aux.mode == mode and aux.encoding == db.encoding:
                    alt_db_exists = True

            # Extraer los registros de la tabla
            registers = extractTable(database, table)
            if alt_db_exists:
                # Crear tabla en esta base de datos
                if __create_table_sp(database, table, tb.columns, mode) != 0:
                    return 1
                __alter_add_pk_sp(database, table, tb.pk, mode)
                # Insertar registros
                for register in registers:
                    if __insert_sp(database, table, register, mode) != 0:
                        return 1
            else:
                # Crear base de datos y tabla e insertar las tuplas
                if __create_database_sp(database, mode, db.encoding) != 0:
                    return 1
                # Crear tabla en esta base de datos
                if __create_table_sp(database, table, tb.columns, mode) != 0:
                    return 1
                if tb.pk != []:
                    if __alter_add_pk_sp(database, table, tb.pk, mode) != 0:
                        return 1
                # Insertar registros
                for register in registers:
                    if __insert_sp(database, table, register, mode) != 0:
                        return 1
            # Eliminar tabla original
            if __drop_table_sp(database, table, db.mode) != 0:
                return 1
            if db.tables.first == None and not db.main_db:
                if __drop_database_sp(db.name, db.mode) != 0:
                    return 1
            return 0
    return 1

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
                    continue
                except:
                    alterDatabase(databaseNew, databaseOld)
            return 1
        return 0
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
                        break
                    except:
                        continue
                continue
            return 1
        return 0
    else:
        return 1

# Descripción:
#     Elimina por la base de datos con el nombre y modo indicados
# Parámetros:
#     database:str - Es el nombre de la base de datos que se desea eliminar, debe cumplir con las reglas de identificadores de SQL
#     mode:str - El modo de almacenamiento utilizado por la base de datos que se desea eliminar
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - Base de datos no existente
#     4 - Modo incorrecto
def __drop_database_sp(database: str, mode: str) -> int:
    if re.search(DB_NAME_PATTERN, database):
        dbs = databases.find_all(database)
        if dbs == []:
            return 2
        if mode not in MODES:
            return 4
        for db in dbs:
            if db.mode != mode:
                continue
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
            else:
                continue
            if code == 0:
                databases.delete_sp(db.name, db.mode)
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
#     Crea una nueva tabla en la base de datos indicada con el modo indicado
# Parámetros:
#     database:str - El nombre de la base de datos a la que se desea agregar la tabla
#     table:str - El nombre de la nueva tabla
#     numberColumns:int - La cantidad de columnas que manejará la tabla
#     mode:str - El modo de almacenamiento utilizado por la base de datos
# Valores de Retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - Base de datos inexistente
#     3 - Tabla existente
#     4 - Modo incorrecto
def __create_table_sp(database: str, table: str, numberColumns: int, mode: str) -> int:
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if mode not in MODES:
        return 4
    for db in dbs:
        if db.mode != mode:
            continue
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
        else:
            continue
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
        tb = db.tables.first
        while tb != None:
            if not tb.hidden:
                result.append(tb.name)
            tb = tb.next
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
                        continue
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
                db.tables.search(table).columns += 1
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        continue
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
                db.tables.search(table).columns -= 1
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        continue
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
#      6 - Codificación incorrecta
def insert(database: str, table: str, register: list):
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    for x in register:
        if type(x) == str and not verify_encoding(x, dbs[0].encoding):
            return 6
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
    tb = databases.find_table(database, table)
    if tb.safeMode:
        key = ""
        for pk in tb.pk:
            key += str(register[pk])
        cs = checksumDatabase(database, "SHA256")
        print(cs)
        print(tb.blockchain.new_block(key, cs))
        for x in range(5):
            try:
                Serializable.commit(databases, "lista_bases_de_datos")
                return result
            except:
                continue
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
        with open(file) as csv:
            for line in csv:
                register = line.strip().split(",")
                result += [insert(database, table, register)]
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
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if databases.find_table(database, table) == None:
        return 3
    result = 1
    for db in dbs:
        if db.tables.search(table) == None:
            continue
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
    dbs = databases.find_all(database)
    if dbs == []:
        return None
    if databases.find_table(database, table) == None:
        return None

    registers = []
    for db in dbs:
        if db.tables.search(table) == None:
            continue
        if db.mode == "avl":
            registers = avlMode.extractRangeTable(database,table,columnNumber,lower, upper)
        elif db.mode == "b":
            registers = BMode.extractRangeTable(database,table,columnNumber,lower, upper)
        elif db.mode == "bplus":
            registers = BPlusMode.extractRangeTable(database,table,columnNumber,lower, upper)
        elif db.mode == "dict":
            registers = DictMode.extractRangeTable(database,table,columnNumber,lower, upper)
        elif db.mode == "isam":
            registers = ISAMMode.extractRangeTable(database,table,columnNumber,lower, upper)
        elif db.mode == "json":
            registers = jsonMode.extractRangeTable(database,table,columnNumber,lower, upper)
        elif db.mode == "hash":
            registers = HashMode.extractRangeTable(database,table,columnNumber,lower, upper)
    return registers

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
                        continue
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
                        continue
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
        if db.mode != mode:
            continue
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
                        continue
                return 1
            break
    return result

def extractRow(database, table, columns):
    dbs = databases.find_all(database)
    if dbs == []:
        return []
    if databases.find_table(database, table) == None:
        return []
    result = []
    for db in dbs:
        if db.tables.search(table) == None:
            continue
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
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if databases.find_table(database, table) == None:
        return 3
    for x in register.values():
        if type(x) == str and not verify_encoding(x, dbs[0].encoding):
            return 5
    result = 1
    for db in dbs:
        if db.tables.search(table) == None:
            continue
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
    tb = databases.find_table(database, table)
    if tb.safeMode:
        key = ""
        for pk in tb.pk:
            key += str(register[pk])
        cs = checksumDatabase(database, "SHA256")
        tb.blockchain.update_block(key, cs, True)
        tb.blockchain.break_blockchain(key)
        for x in range(5):
            try:
                Serializable.commit(databases, "lista_bases_de_datos")
                return result
            except:
                continue
    return result

def truncate(database, table):
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if databases.find_table(database, table) == None:
        return 3
    result = 1
    for db in dbs:
        if db.tables.search(table) == None:
            continue
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
                        continue
                return 1
            break
    return result

# Descripción:
#     Agrega las llaves primarias a la tabla de la base de datos con el nombre y modo indicados
# Parámetros:
#     database:str - El nombre de la base de datos
#     table:str - El nombre de la tabla
#     columns:list - Una lista con los números de columna que son llaves primarias
#     mode:str - El modo de almacenamiento en el que se encuentra la base de datos a utilizar
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - Llave primaria existente
#     5 - Columnas fuera de límites
def __alter_add_pk_sp(database: str, table: str, columns: list, mode: str) -> int:
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if databases.find_table(database, table) == None:
        return 3
    for db in dbs:
        if db.mode != mode:
            continue
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
        else:
            continue
        if result != 3:
            if result == 0:
                db.tables.search(table).pk += columns
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        return result
                    except:
                        continue
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
# Descripcion:
# 	Asociada una codificación a una base de datos por completo. (UPDATE)
# Parámetro database: 
#	es el nombre de la base de datos a utilizar. Parámetro mode: es el algoritmo de hash, puede ser 'MD5' o 'SHA256'.
# Valor de retorno: 
#	0 operación exitosa,
#	1 error en la operación, 
#	2 database no existente, 
#	3 nombre de modo no existente.
def checksumDatabase(database: str, mode: str):
	try:
		list_routes = get_routes(database)
		#falta: if para ver si la db existe, abenido del get_routes
		if list_routes != []:
			#verifico existe modo
			if(mode.upper() == 'MD5'):
				m = hashlib.md5()
				print(mode)#quitar
			elif(mode.upper() == 'SHA256'):
				m = hashlib.sha256()
				print(mode)#quitar
			else:
				return 3 #nombre del modo no existe

			for direcc in list_routes:
				file = open(direcc,'rb')
				tabla = file.read() #en tipo binario
				file.close()
				m.update(tabla)
			return m.hexdigest()
		else:
			return 1 #error: la db no tiene tablas
	except:
		return 1 #error en la operacion


def checksumTable(database: str, table:str, mode: str):
	try:
		list_routes = get_route_table(database,table)
		#falta: if para ver si la db existe, obenido del get_routes
		if list_routes != None:
			#verifico existe modo
			if(mode.upper() == 'MD5'):
				m = hashlib.md5()
				print(mode)#quitar
			elif(mode.upper() == 'SHA256'):
				m = hashlib.sha256()
				print(mode)#quitar
			else:
				return 3 #nombre del modo no existe

				direcc = list_routes
				file = open(direcc,'rb')
				tabla = file.read() #en tipo binario
				file.close()
				m.update(tabla)
			return m.hexdigest()
		else:
			return 1 #error: la db no tiene tablas
	except:
		return 1 #error en la operacion

# Descripción:
#     Verifica que un texto pueda tener la codificación indicada
# Parámetros:
#     text:str - El texto que se desea verificar
#     encoding:str - El tipo de codificación que se desea utilizar
# Valores de retorno:
#     True - Si se puede codificar el texto
#     False - Si no se puede codificar el texto
def verify_encoding(text: str, encoding: str):
    if encoding in VALID_ENCODING:
        try:
            text.encode(encoding)
            return True
        except UnicodeEncodeError:
            pass
    return False

# Descripción:
#     Asocia una codificación a una base de datos
# Parámetros:
#     database:str - El nombre de la base de datos a utilizar
#     encoding:str - El tipo de codificación a utilizar
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - Nombre de codificación no existente
def alterDatabaseEncoding(database: str, encoding: str) -> int:
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    if encoding not in VALID_ENCODING:
        return 3
    for db in dbs:
        tables = []
        aux = db.tables.first
        while aux != None:
            tables.append(aux)
            aux = aux.next
        for table in tables:
            registers = extractTable(db.name, table.name)
            for register in registers:
                for x in register:
                    if type(x) == str:
                        if not verify_encoding(x, encoding):
                            return 1
    databases.search(database).encoding = encoding
    for x in range(5):
        try:
            Serializable.commit(databases, "lista_bases_de_datos")
            return 0
        except:
            continue
    return 1

# Descripción:
#     Agrega un índice de llave foránea, creando una estructura adicional con el modo indicado para la base de datos
# Parámetros:
#     database:str - El nombre de la base de datos a utilizar
#     table:str - El nombre de la tabla a utilizar
#     indexName:str - El nombre único del índice
#     columns:list - Conjunto de índices de columnas que forman parte de la llave foránea
#     tableRef:str - El nombre de la tabla que hace referencia, donde está(n) la(s) llave(s) primarias(s)
#     columnsRef:list - El conjunto de índices de columnas que forman parte de la llave primaria
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - Cantidad no exacta entre columnas
def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
    # Comprobaciones iniciales
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    tb_local = databases.find_table(database, table)
    tb_reference = databases.find_table(database, tableRef)
    if tb_local == None or tb_reference == None:
        return 3
    if len(columns) != len(columnsRef):
        return 4
    
    for fk in tb_local.fk:
        if fk["indexName"] == indexName:
            return 1

    registers = extractTable(database, tableRef)
    if len(registers) != len(extractTable(database, table)):
        return 1

    # Obteniendo las llaves primarias de la tabla referida
    pkRef = tb_reference.pk

    # Creando la nueva estructura
    if createTable(database, indexName, len(columns) + 1) != 0:
        return 1
    
    # Definiendo las llaves primarias de la nueva estructura
    aux_pk = []
    for x in range(len(columns)):
        aux_pk.append(x)
    if alterAddPK(database, indexName, aux_pk) != 0:
        return 1

    # Insertando los registros a la nueva estructura
    for register in registers:
        aux_register = []
        for x in range(len(register)):
            if x in columnsRef:
                aux_register.append(register[x])
        reference_pk = {}
        for x in range(len(register)):
            if x in pkRef:
                reference_pk[x] = register[x]
        aux_register.append(reference_pk)
        
        if insert(database, indexName, aux_register) != 0:
            return 1

    # Agregando la información de la FK a la tabla
    tb_local.fk.append({"indexName":indexName,
                        "table":table,
                        "columns":columns,
                        "tableRef":tableRef,
                        "columnsRef":columnsRef,
                        "pkRef": pkRef})
    databases.find_table(database, indexName).hidden = True

    # Almacenando la información de la lista de bases de datos
    for x in range(5):
        try:
            Serializable.commit(databases, "lista_bases_de_datos")
            return 0
        except:
            continue
    
    return 1

# Descripción:
#     Destruye el índice tanto como metadato de la tabla como la estructura adicional creada
# Parámetros:
#     database:str - El nombre de la base de datos
#     table:str - El nombre de la tabla
#     indexName:str - El nombre único del índice
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - Nombre de índice no existente
def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    # Comprobaciones iniciales
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    tb_local = databases.find_table(database, table)
    if tb_local == None:
        return 3
    
    for x in range(len(tb_local.fk)):
        if tb_local.fk[x]["indexName"] == indexName:
            if dropTable(database, indexName) != 0:
                return 1
            tb_local.fk.pop(x)
            for x in range(5):
                try:
                    Serializable.commit(databases, "lista_bases_de_datos")
                    return 0
                except:
                    continue
    return 4

# Descripción:
#     Agrega un índice único, creando una estructura adicional con el modo indicado para la base de datos
# Parámetros:
#     database:str - El nombre de la base de datos a utilizar
#     table:str - El nombre de la tabla a utilizar
#     indexName:str - El nombre único del índice
#     columns:list - Conjunto de índices de columnas que forman parte de la llave foránea
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - indexName repetido
#     5 - No se cumple la integridad de unicidad
def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    # Comprobaciones iniciales
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    tb = databases.find_table(database, table)
    if tb == None:
        return 3
    
    for iu in tb.iu:
        if iu["indexName"] == indexName:
            return 4

    registers = extractTable(database, table)
    aux_data = [] # Usado para verificar si hay datos repetidos
    for register in registers:
        unique_index = ""
        for column in columns:
            unique_index += str(register[column])
        if unique_index in aux_data:
            return 5
        aux_data.append(unique_index)

    # Creando la nueva estructura
    if createTable(database, indexName, len(columns) + 1) != 0:
        return 1
    
    # Definiendo las llaves primarias de la nueva estructura
    aux_pk = []
    for x in range(len(columns)):
        aux_pk.append(x)
    if alterAddPK(database, indexName, aux_pk) != 0:
        return 1

    # Insertando los registros a la nueva estructura
    for register in registers:
        aux_register = []
        for x in range(len(register)):
            if x in columns:
                aux_register.append(register[x])
        reference_pk = {}
        for x in range(len(register)):
            if x in tb.pk:
                reference_pk[x] = register[x]
        aux_register.append(reference_pk)
        
        if insert(database, indexName, aux_register) != 0:
            return 1

    # Agregando la información del índice único a la tabla
    tb.iu.append({"indexName": indexName,
                  "table": table,
                  "columns": columns,
                  "pk": aux_pk})
    databases.find_table(database, indexName).hidden = True

    # Almacenando la información de la lista de bases de datos
    for x in range(5):
        try:
            Serializable.commit(databases, "lista_bases_de_datos")
            return 0
        except:
            continue
    
    return 1

# Descripción:
#     Destruye el índice único tanto como metadato de la tabla como la estructura adicional creada
# Parámetros:
#     database:str - El nombre de la base de datos
#     table:str - El nombre de la tabla
#     indexName:str - El nombre único del índice
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - Nombre de índice no existente
def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    # Comprobaciones iniciales
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    tb_local = databases.find_table(database, table)
    if tb_local == None:
        return 3
    
    for x in range(len(tb_local.iu)):
        if tb_local.iu[x]["indexName"] == indexName:
            if dropTable(database, indexName) != 0:
                return 1
            tb_local.iu.pop(x)
            for x in range(5):
                try:
                    Serializable.commit(databases, "lista_bases_de_datos")
                    return 0
                except:
                    continue
    return 4

# Descripción:
#     Agrega un índice, creando una estructura adicional con el modo indicado para la base de datos
# Parámetros:
#     database:str - El nombre de la base de datos a utilizar
#     table:str - El nombre de la tabla a utilizar
#     indexName:str - El nombre único del índice
#     columns:list - Conjunto de índices de columnas que forman parte de la llave foránea
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - indexName repetido
def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    # Comprobaciones iniciales
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    tb = databases.find_table(database, table)
    if tb == None:
        return 3
    
    for indx in tb.indx:
        if indx["indexName"] == indexName:
            return 4

    registers = extractTable(database, table)

    # Creando la nueva estructura
    if createTable(database, indexName, len(columns) + 1) != 0:
        return 1
    
    # Definiendo las llaves primarias de la nueva estructura
    aux_pk = []
    for x in range(len(columns)):
        aux_pk.append(x)
    if alterAddPK(database, indexName, aux_pk) != 0:
        return 1

    # Insertando los registros a la nueva estructura
    for register in registers:
        aux_register = []
        for x in range(len(register)):
            if x in columns:
                aux_register.append(register[x])
        reference_pk = {}
        for x in range(len(register)):
            if x in tb.pk:
                reference_pk[x] = register[x]
        aux_register.append(reference_pk)
        insert(database, indexName, aux_register)

    # Agregando la información del índice único a la tabla
    tb.indx.append({"indexName": indexName,
                  "table": table,
                  "columns": columns,
                  "pk": aux_pk})
    databases.find_table(database, indexName).hidden = True

    # Almacenando la información de la lista de bases de datos
    for x in range(5):
        try:
            Serializable.commit(databases, "lista_bases_de_datos")
            return 0
        except:
            continue
    
    return 1

# Descripción:
#     Destruye el índice tanto como metadato de la tabla como la estructura adicional creada
# Parámetros:
#     database:str - El nombre de la base de datos
#     table:str - El nombre de la tabla
#     indexName:str - El nombre único del índice
# Valores de retorno:
#     0 - Operación exitosa
#     1 - Error en la operación
#     2 - database no existente
#     3 - table no existente
#     4 - Nombre de índice no existente
def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    # Comprobaciones iniciales
    dbs = databases.find_all(database)
    if dbs == []:
        return 2
    tb_local = databases.find_table(database, table)
    if tb_local == None:
        return 3
    
    for x in range(len(tb_local.indx)):
        if tb_local.indx[x]["indexName"] == indexName:
            if dropTable(database, indexName) != 0:
                return 1
            tb_local.indx.pop(x)
            for x in range(5):
                try:
                    Serializable.commit(databases, "lista_bases_de_datos")
                    return 0
                except:
                    continue
    return 4

# Descripcion
# Activa el modo seguro para una tabla de una base de datos.
# Parametos:
# 	Parámetro database: 
# 	nombre de la base de datos. 
# 	Parámetro table: nombre de la tabla.
# Valor de retorno:
# 	0 operación exitora, 
#	1 error en la operación, 
#	2 database inexistente, 
#	3 table inexistente, 
#	4 modo seguro existente.
def safeModeOn(database: str, table: str):
    if not os.path.isdir(".\\DataJsonBC"):
        os.makedirs(".\\DataJsonBC")
    try:
        dbs = databases.find_all(database)
        if dbs == []:
            return 2 #insexistente bd
        tb = databases.find_table(database, table)
        if tb == None:
            return 3
        if tb.safeMode == True:
            return 4
        
        for db in dbs:
            tb = db.tables.search(table)
            if tb != None:
                tb.blockchain = blockchain(db.name + "_" + tb.name)
                tb.safeMode = True
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        break
                    except:
                        continue
                with open(".\\DataJsonBC\\" + db.name + "_" + tb.name + ".json", "w") as bc:
                    bc.write('{"blocks": []}')
                break
        return 0
    except:
        return 1#error

#Descripcion:
# Desactiva el modo seguro en la tabla especificada de la base de datos.
# Parámetro database:
#	 nombre de la base de datos.
# Parámetro table: 
#	nombre de la tabla.
# Valor de retorno:
#	0 operación exitora, 
#	1 error en la operación,
#	2 database inexistente, 
#	3 table inexistente,
#	4 modo seguro no existente.
def safeModeOff(database: str, table: str):
    try:
        dbs = databases.find_all(database)
        if dbs == []:
            return 2 #insexistente bd
        tb = databases.find_table(database, table)
        if tb == None:
            return 3
        if tb.safeMode == False:
            return 4
        
        for db in dbs:
            tb = db.tables.search(table)
            if tb != None:
                tb.blockchain = None
                tb.safeMode = False
                for x in range(5):
                    try:
                        Serializable.commit(databases, "lista_bases_de_datos")
                        break
                    except:
                        continue
                os.remove(".\\DataJsonBC\\" + db.name + "_" + tb.name + ".json")
                break
        return 0
    except:
        return 1#error

# Descripcion:
# 	Asociada una codificación a una base de datos por completo. (UPDATE)
# Parámetro database: 
#	es el nombre de la base de datos a utilizar. Parámetro mode: es el algoritmo de hash, puede ser 'MD5' o 'SHA256'.
# Valor de retorno: 
#	0 operación exitosa,
#	1 error en la operación, 
#	2 database no existente, 
#	3 nombre de modo no existente.
def checksumDatabase(database: str, mode: str):
	try:
		list_routes = get_routes(database)
		#falta: if para ver si la db existe, abenido del get_routes
		if list_routes != []:
			#verifico existe modo
			if(mode.upper() == 'MD5'):
				m = hashlib.md5()
				print(mode)#quitar
			elif(mode.upper() == 'SHA256'):
				m = hashlib.sha256()
				print(mode)#quitar
			else:
				return 3 #nombre del modo no existe

			for direcc in list_routes:
				file = open(direcc,'rb')
				tabla = file.read() #en tipo binario
				file.close()
				m.update(tabla)
			return m.hexdigest()
		else:
			return 1 #error: la db no tiene tablas
	except:
		return 1 #error en la operacion


def checksumTable(database: str, table:str, mode: str):
	try:
		list_routes = get_route_table(database,table)
		#falta: if para ver si la db existe, obenido del get_routes
		if list_routes != None:
			#verifico existe modo
			if(mode.upper() == 'MD5'):
				m = hashlib.md5()
				print(mode)#quitar
			elif(mode.upper() == 'SHA256'):
				m = hashlib.sha256()
				print(mode)#quitar
			else:
				return 3 #nombre del modo no existe

				direcc = list_routes
				file = open(direcc,'rb')
				tabla = file.read() #en tipo binario
				file.close()
				m.update(tabla)
			return m.hexdigest()
		else:
			return 1 #error: la db no tiene tablas
	except:
		return 1 #error en la operacion
# Agregue compresión utilizando la biblioteca. Se debe agregar a columna tipo varchar o text de cada tabla de la base de datos. (UPDATE)
# Parámetro database: es el nombre de la base de datos que se desea modificar
# Parámetro level: es el nivel de compressión definido por la función compress de la bilbioteca zlib de Python.
# Valor de retorno: 
#0 operación exitosa, 
#1 error en la operación, 
#2 database no existente, 
#3 table no existente, 
#4 level incorrecto.
def alterDatabaseCompress(database: str, level: int):
	try:
		dbs = databases.find_all(database)
		if dbs == []:
		    return 2

		if databases.search(database).compress == True:
			return 1 #error

		if level < -1 or level > 9:
			return 4

		for db in dbs:

		    tables = []
		    aux = db.tables.first
		    while aux != None:
		        tables.append(aux)
		        aux = aux.next

		    if tables != []:

		        if db.mode == "avl":
		            for table in tables:
		            	if table.compress == False:
			            	datos =	avlMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos: #lista de registros(lista)
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == str:
				            				diccionario[x] =comprimir(e[x],level)
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = True#actualizo

		        elif db.mode == "b":
		            for table in tables:
		            	if table.compress == False:
			            	datos =	BMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == str:
				            				diccionario[x] =comprimir(e[x],level)
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = True#actualizo

		        elif db.mode == "bplus":
		            for table in tables:
		            	if table.compress == False:
			            	datos =	BPlusMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == str:
				            				diccionario[x] =comprimir(e[x],level)
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = True#actualizo

		        elif db.mode == "dict":
		            for table in tables:
		            	if table.compress == False:
			            	datos =	DictMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == str:
				            				diccionario[x] =comprimir(e[x],level)
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = True#actualizo

		        elif db.mode == "isam":
		            for table in tables:
		            	if table.compress == False:
			            	datos =	ISAMMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == str:
				            				diccionario[x] =comprimir(e[x],level)
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = True#actualizo

		        elif db.mode == "json":
		            for table in tables:
		            	if table.compress == False:
			            	datos =	jsonMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == str:
				            				diccionario[x] =comprimir(e[x],level)
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = True#actualizo

		        elif db.mode == "hash":
		            for table in tables:
		            	if table.compress == False:
			            	datos =	HashMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == str:
				            				diccionario[x] =comprimir(e[x],level)
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = True#actualizo

		databases.search(database).compress = True		            		
		return 0#exito
	except:
		return 1 #error

# Quita la compresión de una base de datos especificada. (UPDATE)
# Parámetro:
#	 database: es el nombre de la base de datos a utilizar.
# Valor de retorno: 
#	0 operación exitosa, 
#	1 error en la operación, 
#	2 database no existente, 
#	3 no había compresión.
def alterDatabaseDecompress(database: str):
	try:

		dbs = databases.find_all(database)
		if dbs == []:
		    return 2
		if databases.search(database).compress == False:
			return 3 #error

		for db in dbs:

		    tables = []
		    aux = db.tables.first
		    while aux != None:
		        tables.append(aux)
		        aux = aux.next

		    if tables != []:

		        if db.mode == "avl":
		            for table in tables:
		            	if table.compress == True:
			            	datos =	avlMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == bytes:
				            				diccionario[x] =descomprimir(e[x])
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = False#actualizo
				            		

		        elif db.mode == "b":
		            for table in tables:
		            	if table.compress == True:
			            	datos =	BMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == bytes:
				            				diccionario[x] =descomprimir(e[x])
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = False#actualizo

		        elif db.mode == "bplus":
		            for table in tables:
		            	if table.compress == True:
			            	datos =	BPlusMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == bytes:
				            				diccionario[x] =descomprimir(e[x])
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = False#actualizo

		        elif db.mode == "dict":
		            for table in tables:
		            	if table.compress == True:
			            	datos =	DictMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == bytes:
				            				diccionario[x] =descomprimir(e[x])
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = False#actualizo

		        elif db.mode == "isam":
		            for table in tables:
		            	if table.compress == True:
			            	datos =	ISAMMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == bytes:
				            				diccionario[x] =descomprimir(e[x])
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = False#actualizo

		        elif db.mode == "json":
		            for table in tables:
		            	if table.compress == True:
			            	datos =	jsonMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == bytes:
				            				diccionario[x] =descomprimir(e[x])
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = False#actualizo

		        elif db.mode == "hash":
		            for table in tables:
		            	if table.compress == True:
			            	datos =	HashMode.extractTable(db.name,table.name)
			            	if datos != None and datos != []:
				            	for  e in datos:
				            		#lista para la primary key del registro
				            		register_pk = []
				            		#recorrer la lista con los indices de las primary keys
				            		for pk in table.pk:
				            			register_pk.append(e[pk])
				            		#Generador del diccionario con los datos comprimidos
				            		diccionario = {}
				            		for x in range(len(e)):
				            			if type(e[x]) == bytes:
				            				diccionario[x] =descomprimir(e[x])
				            		#actualizando los valores de la tabla
				            		update(db.name,table.name,diccionario,register_pk)
				            		databases.find_table(db.name,table.name).compress = False#actualizo

		databases.search(database).compress = False		            		
		return 0#exito		

	except:
		return 1 #error

# Agregue compresión  Se debe agregar a columna tipo varchar o text de cada tabla de la base de datos. De igual manera, al extraer la información se debe descomprimir
# Parametros:
# 	Parámetro database: es el nombre de la base de datos que se desea modificar
# 	Parámetro table: es el nombre de la tabla.
# 	Parámetro level: es el nivel de compressión definido por la función compress de la bilbioteca zlib de Python.
# Valor de retorno: 
#	0 operación exitosa, 
#	1 error en la operación, 
#	2 database no existente,
#	3 table no existe 
#	4 level incorrecto.
def alterTableCompress(database: str, table: str, level: int):
#	try:
		dbs = databases.find_all(database)
		if dbs == []:
		    return 2
		if databases.find_table(database,table) == None:
			return 3
		if level < -1 or level > 9:
			return 4

		for db in dbs:

			#nuevo
			tb = db.tables.search(table)
			if tb == None:
				continue

			if db.mode == "avl":
				if tb.compress == False:
					datos =	avlMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos: #lista de registros(lista)
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == str:
									diccionario[x] =comprimir(e[x],level)
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = True#actualizo			            		

			elif db.mode == "b":
				if tb.compress == False:
					datos =	BMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == str:
									diccionario[x] =comprimir(e[x],level)
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = True#actualizo

			elif db.mode == "bplus":
				if tb.compress == False:
					datos =	BPlusMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == str:
									diccionario[x] =comprimir(e[x],level)
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = True#actualizo

			elif db.mode == "dict":
				if tb.compress == False:
					datos =	DictMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == str:
									diccionario[x] =comprimir(e[x],level)
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = True#actualizo

			elif db.mode == "isam":
				if tb.compress == False:
					datos =	ISAMMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == str:
									diccionario[x] =comprimir(e[x],level)
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = True#actualizo

			elif db.mode == "json":
				if tb.compress == False:
					datos =	jsonMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == str:
									diccionario[x] =comprimir(e[x],level)
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = True#actualizo

			elif db.mode == "hash":
				if tb.compress == False:
					datos =	HashMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == str:
									diccionario[x] =comprimir(e[x],level)
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = True#actualizo

		databases.find_table(database, table).compress = True#actualizo		            		
		return 0#exito		

#	except:
#		return 1 #error

# Quita la compresión de una base de datos especificada. (UPDATE)
# Parámetro:
#	database: es el nombre de la base de datos a utilizar.
#	Parámetro table: es el nombre de la tabla a utilizar.
# Valor de retorno:
#	0 operación exitosa, 
#	1 error en la operación, 
#	2 database no existente, 
#	3 no había compresión.
def alterTableDecompress(database: str, table: str):
#	try:

		dbs = databases.find_all(database)
		if dbs == []:
		    return 2

		if databases.find_table(database,table).compress == False:
			return 3 #error

		for db in dbs:

			#nuevo
			tb = db.tables.search(table)
			if tb == None:
				continue


			if db.mode == "avl":
				if tb.compress == True:
					datos =	avlMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos: #lista de registros(lista)
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == bytes:
									diccionario[x] =descomprimir(e[x])
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = False#actualizo				            		

			elif db.mode == "b":
				if tb.compress == True:
					datos =	BMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == bytes:
									diccionario[x] =descomprimir(e[x])
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = False#actualizo

			elif db.mode == "bplus":
				if tb.compress == True:
					datos =	BPlusMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == bytes:
									diccionario[x] =descomprimir(e[x])
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = False#actualizo

			elif db.mode == "dict":
				if tb.compress == True:
					datos =	DictMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == bytes:
									diccionario[x] =descomprimir(e[x])
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = False#actualizo

			elif db.mode == "isam":
				if tb.compress == True:
					datos =	ISAMMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == bytes:
									diccionario[x] =descomprimir(e[x])
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = False#actualizo

			elif db.mode == "json":
				if tb.compress == True:
					datos =	jsonMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == bytes:
									diccionario[x] =descomprimir(e[x])
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = False#actualizo

			elif db.mode == "hash":
				if tb.compress == True:
					datos =	HashMode.extractTable(db.name,tb.name)
					if datos != None and datos != []:
						for  e in datos:
							#lista para la primary key del registro
							register_pk = []
							#recorrer la lista con los indices de las primary keys
							for pk in tb.pk:
								register_pk.append(e[pk])
							#Generador del diccionario con los datos comprimidos
							diccionario = {}
							for x in range(len(e)):
								if type(e[x]) == bytes:
									diccionario[x] =descomprimir(e[x])
							#actualizando los valores de la tabla
							update(db.name,tb.name,diccionario,register_pk)
							databases.find_table(db.name,tb.name).compress = False#actualizo

		databases.find_table(database, table).compress = False#actualizo	            		
		return 0#exito		

#	except:
#		return 1 #error


def comprimir(text,nivel):
	try:
		b = bytes(text, encoding="utf-8")
		comp = zlib.compress(b,nivel)#b en bytes
		return comp

	except:
		return 1#error


def descomprimir(comp):
	try:
		decomp = zlib.decompress(comp).decode()

		return decomp
	except:
		return 1#error

class Grafo:
    def graphDF(database: str, table: str):
        dbs = databases.find_all(database)
        if dbs == []:
            return None
        for db in dbs:
            tb = db.tables.search(table)
            if tb == None:
                continue
            if db.mode == "avl":
                primarias = tb.pk#lista PKs
                ius = []
                for iu in tb.iu:
                    for column in iu["columns"]:
                        if column not in ius:
                            ius.append(column)
                indiceUnico = ius # lista IUnicos
                texto = "digraph {" +"\n"
                "node[shape=box3d, style=filled];"+"\n"

                normal_index = []
                for x in range(tb.columns):
                    if x not in tb.pk and x not in ius:
                        normal_index.append(x)

                #datos = ISAMMode.extractTable(db.name,tb.name) #obtengo lista con registros
                if normal_index != []: #no vacia 
                    for dat in normal_index:#recorro llaves 
                        texto += str(dat) +"[fillcolor=\"#1EB3C5\" ];"+ "\n" #poner color
                        for pk in primarias:
                            texto += str(pk) + "->" + str(dat)+";"+"\n"#dependencia pks

                        for indU in indiceUnico:
                            texto += str(indU) + "->" + str(dat)+";"+"\n"#dependencias IUnicos

                texto +="}"
                with open("graphDF.dot", 'w') as f:
                    f.write(texto)#escrivo archivo
                    
                os.system("Dot -Tsvg graphDF.dot -o graphDF.svg")
                os.system("graphDF.svg")

            elif db.mode == "b":
                primarias = tb.pk#lista PKs
                ius = []
                for iu in tb.iu:
                    for column in iu["columns"]:
                        if column not in ius:
                            ius.append(column)
                indiceUnico = ius # lista IUnicos
                texto = "digraph {" +"\n"
                "node[shape=box3d, style=filled];"+"\n"

                normal_index = []
                for x in range(tb.columns):
                    if x not in tb.pk and x not in ius:
                        normal_index.append(x)

                #datos = ISAMMode.extractTable(db.name,tb.name) #obtengo lista con registros
                if normal_index != []: #no vacia 
                    for dat in normal_index:#recorro llaves 
                        texto += str(dat) +"[fillcolor=\"#1EB3C5\" ];"+ "\n" #poner color
                        for pk in primarias:
                            texto += str(pk) + "->" + str(dat)+";"+"\n"#dependencia pks

                        for indU in indiceUnico:
                            texto += str(indU) + "->" + str(dat)+";"+"\n"#dependencias IUnicos

                texto +="}"
                with open("graphDF.dot", 'w') as f:
                    f.write(texto)#escrivo archivo
                    
                os.system("Dot -Tsvg graphDF.dot -o graphDF.svg")
                os.system("graphDF.svg")
            elif db.mode == "bplus":
                primarias = tb.pk#lista PKs
                ius = []
                for iu in tb.iu:
                    for column in iu["columns"]:
                        if column not in ius:
                            ius.append(column)
                indiceUnico = ius # lista IUnicos
                texto = "digraph {" +"\n"
                "node[shape=box3d, style=filled];"+"\n"

                normal_index = []
                for x in range(tb.columns):
                    if x not in tb.pk and x not in ius:
                        normal_index.append(x)

                #datos = ISAMMode.extractTable(db.name,tb.name) #obtengo lista con registros
                if normal_index != []: #no vacia 
                    for dat in normal_index:#recorro llaves 
                        texto += str(dat) +"[fillcolor=\"#1EB3C5\" ];"+ "\n" #poner color
                        for pk in primarias:
                            texto += str(pk) + "->" + str(dat)+";"+"\n"#dependencia pks

                        for indU in indiceUnico:
                            texto += str(indU) + "->" + str(dat)+";"+"\n"#dependencias IUnicos

                texto +="}"
                with open("graphDF.dot", 'w') as f:
                    f.write(texto)#escrivo archivo
                    
                os.system("Dot -Tsvg graphDF.dot -o graphDF.svg")
                os.system("graphDF.svg")
            elif db.mode == "dict":
                primarias = tb.pk#lista PKs
                ius = []
                for iu in tb.iu:
                    for column in iu["columns"]:
                        if column not in ius:
                            ius.append(column)
                indiceUnico = ius # lista IUnicos
                texto = "digraph {" +"\n"
                "node[shape=box3d, style=filled];"+"\n"

                normal_index = []
                for x in range(tb.columns):
                    if x not in tb.pk and x not in ius:
                        normal_index.append(x)

                #datos = ISAMMode.extractTable(db.name,tb.name) #obtengo lista con registros
                if normal_index != []: #no vacia 
                    for dat in normal_index:#recorro llaves 
                        texto += str(dat) +"[fillcolor=\"#1EB3C5\" ];"+ "\n" #poner color
                        for pk in primarias:
                            texto += str(pk) + "->" + str(dat)+";"+"\n"#dependencia pks

                        for indU in indiceUnico:
                            texto += str(indU) + "->" + str(dat)+";"+"\n"#dependencias IUnicos

                texto +="}"
                with open("graphDF.dot", 'w') as f:
                    f.write(texto)#escrivo archivo
                    
                os.system("Dot -Tsvg graphDF.dot -o graphDF.svg")
                os.system("graphDF.svg")
            elif db.mode == "isam":
                primarias = tb.pk#lista PKs
                ius = []
                for iu in tb.iu:
                    for column in iu["columns"]:
                        if column not in ius:
                            ius.append(column)
                indiceUnico = ius # lista IUnicos
                texto = "digraph {" +"\n"
                "node[shape=box3d, style=filled];"+"\n"

                normal_index = []
                for x in range(tb.columns):
                    if x not in tb.pk and x not in ius:
                        normal_index.append(x)

                #datos = ISAMMode.extractTable(db.name,tb.name) #obtengo lista con registros
                if normal_index != []: #no vacia 
                    for dat in normal_index:#recorro llaves 
                        texto += str(dat) +"[fillcolor=\"#1EB3C5\" ];"+ "\n" #poner color
                        for pk in primarias:
                            texto += str(pk) + "->" + str(dat)+";"+"\n"#dependencia pks

                        for indU in indiceUnico:
                            texto += str(indU) + "->" + str(dat)+";"+"\n"#dependencias IUnicos

                texto +="}"
                with open("graphDF.dot", 'w') as f:
                    f.write(texto)#escrivo archivo
                    
                os.system("Dot -Tsvg graphDF.dot -o graphDF.svg")
                os.system("graphDF.svg")
            elif db.mode == "json":
                primarias = tb.pk#lista PKs
                ius = []
                for iu in tb.iu:
                    for column in iu["columns"]:
                        if column not in ius:
                            ius.append(column)
                indiceUnico = ius # lista IUnicos
                texto = "digraph {" +"\n"
                "node[shape=box3d, style=filled];"+"\n"

                normal_index = []
                for x in range(tb.columns):
                    if x not in tb.pk and x not in ius:
                        normal_index.append(x)

                #datos = ISAMMode.extractTable(db.name,tb.name) #obtengo lista con registros
                if normal_index != []: #no vacia 
                    for dat in normal_index:#recorro llaves 
                        texto += str(dat) +"[fillcolor=\"#1EB3C5\" ];"+ "\n" #poner color
                        for pk in primarias:
                            texto += str(pk) + "->" + str(dat)+";"+"\n"#dependencia pks

                        for indU in indiceUnico:
                            texto += str(indU) + "->" + str(dat)+";"+"\n"#dependencias IUnicos

                texto +="}"
                with open("graphDF.dot", 'w') as f:
                    f.write(texto)#escrivo archivo
                    
                os.system("Dot -Tsvg graphDF.dot -o graphDF.svg")
                os.system("graphDF.svg") 
            elif db.mode == "hash":
                primarias = tb.pk#lista PKs
                ius = []
                for iu in tb.iu:
                    for column in iu["columns"]:
                        if column not in ius:
                            ius.append(column)
                indiceUnico = ius # lista IUnicos
                texto = "digraph {" +"\n"
                "node[shape=box3d, style=filled];"+"\n"

                normal_index = []
                for x in range(tb.columns):
                    if x not in tb.pk and x not in ius:
                        normal_index.append(x)

                #datos = ISAMMode.extractTable(db.name,tb.name) #obtengo lista con registros
                if normal_index != []: #no vacia 
                    for dat in normal_index:#recorro llaves 
                        texto += str(dat) +"[fillcolor=\"#1EB3C5\" ];"+ "\n" #poner color
                        for pk in primarias:
                            texto += str(pk) + "->" + str(dat)+";"+"\n"#dependencia pks

                        for indU in indiceUnico:
                            texto += str(indU) + "->" + str(dat)+";"+"\n"#dependencias IUnicos

                texto +="}"
                with open("graphDF.dot", 'w') as f:
                    f.write(texto)#escrivo archivo
                    
                os.system("Dot -Tsvg graphDF.dot -o graphDF.svg")
                os.system("graphDF.svg") 
        if route != None and os.path.exists(route):
            return route
        return None
