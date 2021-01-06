import os
import pickle
import zlib
import binascii
from cryptography.fernet import Fernet

# 1. UNIFICACION DE INDICES
from storage.AVLMode import avlMode as avl
from storage.BMode import BMode as b
from storage.BPlusMode import BPlusMode as bplus
from storage.HashMode.storage import HashMode as _hash
from storage.IsamMode import ISAMMode as isam
from storage.DictMode import DictMode as _dict
from storage.JsonMode import jsonMode as json
from os import path

structs = [avl, b, bplus, _hash, isam, _dict]
databases = []

def dropAll():
    avl.dropAll()
    bplus.dropAll()
    _dict.dropAll()
    json.dropAll()
    return 0

def addDatabase(name, mode, code, mod):
    database = {"mod": None, "mode": "", "name": "", "code": "", "tables": []}
    database["mod"] = mod
    database["name"] = name
    database["mode"] = mode
    database["code"] = code
    databases.append(database)

def createDatabase(name, mode = 'avl', code = 'ASCII'):
    try:
        if code == 'UTF8' or code == 'ASCII' or code == 'ISO-8859-1':
            if mode == 'avl':
                addDatabase(name, mode, code, avl)
                return avl.createDatabase(name)
            elif mode == 'bplus':
                addDatabase(name, mode, code, bplus)
                return bplus.createDatabase(name)
            elif mode == 'b':
                addDatabase(name, mode, code, b)
                return b.createDatabase(name)
            elif mode == 'hash':
                addDatabase(name, mode, code, _hash)
                return _hash.createDatabase(name)
            elif mode == 'isam':
                addDatabase(name, mode, code, isam)
                return isam.createDatabase(name)
            elif mode == 'dict':
                addDatabase(name, mode, code, _dict)
                return _dict.createDatabase(name)
            elif mode == 'json':
                addDatabase(name, mode, code, json)
                return json.createDatabase(name)
            else:
                return 3
        else:
            return 4
    except:
        return 1

def showDatabases():
    # return databases
    msg = "BASES DE DATOS\n"
    dbs = []
    for db in databases:
        if '_' not in db['name']:
            msg += f"\t{db['mode']}: {db['name']}\n"
    # msg += f"\tAVL: {avl.showDatabases()}\n"
    # msg += f"\tB: {b.showDatabases()}\n"
    # msg += f"\tB+: {bplus.showDatabases()}\n"
    # msg += f"\tHash: {_hash.showDatabases()}\n"
    # msg += f"\tIsam: {isam.showDatabases()}\n"
    # msg += f"\tDict: {_dict.showDatabases()}\n"
    # msg += f"\tJSON: {json.showDatabases()}\n"
    return msg

def alterDatabase(databaseOld, databaseNew):
    for item in structs:
        value = item.alterDatabase(databaseOld, databaseNew)
        if value != 2:
            return value
    return 2

def dropDatabase(nameDB):
    for item in structs:
        value = item.dropDatabase(nameDB)
        if value != 2:
            return value
    return 2

def createTable(database, table, nCols):
    for item in structs:
        value = item.createTable(database, table, nCols)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    t = {"name": table, "nCols": nCols, "tuples": [], "mode": i["mode"]}
                    i["tables"].append(t)
                    return value
    return 2

def showTables(database):
    tables = []
    for item in structs:
        value = item.showTables(database)
        if value:
            tables.append(value)
    return tables

def extractTable(database, table):
    for item in structs:
        value = item.extractTable(database, table)
        if value is not None:
            if value != []:
                return value
            else:
                return extractTable(f"{table}_{database}", table)
    return None

def extractRangeTable(database, table, columnNumber, lower, upper):
    for item in structs:
        value = item.extractRangeTable(database, table, columnNumber, lower, upper)
        if value and value != 1:
            return value
    return []

def alterAddPK(database, table, columns):
    for item in structs:
        value = item.alterAddPK(database, table, columns)
        if value != 2:
            return value
    return 2

def alterDropPK(database, table):
    for item in structs:
        value = item.alterDropPK(database, table)
        if value != 2:
            return value
    return 2

def alterTable(database, old, new):
    for item in structs:
        value = item.alterTable(database, old, new)
        if value != 2:
            return value
    return 2

def alterDropColumn(database, table, columnNumber):
    for item in structs:
        value = item.alterDropColumn(database, table, columnNumber)
        if value != 2:
            return value
    return 2

def alterAddColumn(database, table, default):
    for item in structs:
        value = item.alterAddColumn(database, table, default)
        if value != 2:
            return value
    return 2

def insert(database, table, register):
    for item in structs:
        value = item.insert(database, table, register)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if table == t["name"]:
                            tupla = {"register": register}
                            t["tuples"].append(tupla)
                            return value
    return 2

def extractRow(database, table, columns):
    for item in structs:
        value = item.extractRow(database, table, columns)
        if value:
            return value
    return []

def loadCSV(fileCSV, db, table):
    for item in structs:
        value = item.loadCSV(fileCSV, db, table)
        if value != [] and value[0] != 2:
            return value
    return value

# 2. ADMINISTRADOR DE MODO DE ALMACENAMIENTO
def alterDatabaseMode(database, mode):
    try:
        for db in databases:
            if db["name"] == database:
                dbCopy = db.copy()
                databases.remove(db)
                dbCopy["mod"].dropDatabase(dbCopy["name"])
                createDatabase(dbCopy["name"], mode, dbCopy["code"])
                for table in dbCopy["tables"]:
                    createTable(dbCopy["name"], table["name"], table["nCols"])
                    for reg in table["tuples"]:
                        insert(dbCopy["name"], table["name"], reg["register"])
                return 0
    except:
        return 1

def alterTableMode(database, table, mode):
    try:
        for db in databases:
            if db["name"] == database:
                for t in db["tables"]:
                    if table == t["name"]:
                        tableCopy = t.copy()
                        # db["tables"].remove(t)
                        db["mod"].truncate(db["name"], t["name"])
                        break
                break
        createDatabase(f"{table}_{database}", mode, 'ASCII')
        createTable(f"{table}_{database}", table, tableCopy["nCols"])
        for reg in tableCopy["tuples"]:
            insert(f"{table}_{database}", table, reg["register"])
        return 0
    except:
        return 1

# 3. ADMINISTRACION DE INDICES
def alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef):
    pass

def alterTableDropFK(database, table, indexName):
    pass

# 6. COMPRESION DE DATOS
def alterDatabaseCompress(database, level):
    for db in databases:
        if db["name"] == database:
            for table in db["tables"]:
                for tupla in table["tuples"]:
                    for register in tupla["register"]:
                        if type(register) == str:
                            text = bytes(register, 'utf-8')
                            zlib.compress(text, level)
    return 0

# 7. SEGURIDAD
"""
    @description
        Encripta información.
    @param
        backup: información que se desea encriptar.
        password: llave con la que se encriptará la información.
    @return
        Información encriptada.
"""
def encrypt(backup, password):
    return Fernet(password).encrypt(backup.encode()).decode()

"""
    @description
        Descencripta información.
    @param
        cipherBackup: información que se desea descencriptar.
        password: clave con la que se desencriptará la información.
    @return
        Información descencriptada.
"""
def decrypt(cipherBackup, password):
    return Fernet(password).decrypt(cipherBackup.encode()).decode()

# def chargePersistence():
#     try:
#         n = databases
#         if path.isfile("DB.bin") and len(n) ==0:
#             archivo = open("DB" , "rb")
#             data = pickle.load(archivo)
#             databases = data[:]
#             archivo.close
#             print("bases de datos cargadas")
#     except: 
#         pass
