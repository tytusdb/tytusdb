from cryptography.fernet import Fernet
from storage.AVLMode import avlMode as avl
from storage.BTree import BMode as b
from storage.BPlusMode import BPlusMode as bplus
from storage.HashMode.storage import HashMode as _hash
from storage.IsamMode import ISAMMode as isam
from storage.DictMode import DictMode as _dict

structs = [avl, b, bplus, _hash, isam, _dict]

def dropAll():
    avl.dropAll()
    bplus.dropAll()
    _dict.dropAll()
    return 0

def createDatabase(name, mode, code):
    try:
        if mode == 'avl':
            return avl.createDatabase(name)
        elif mode == 'b+':
            return bplus.createDatabase(name)
        elif mode == 'b':
            return b.createDatabase(name)
        elif mode == 'hash':
            return _hash.createDatabase(name)
        elif mode == 'isam':
            return isam.createDatabase(name)
        elif mode == 'dict':
            return _dict.createDatabase(name)
    except:
        return 1

def showDatabases():
    msg = "BASES DE DATOS\n"
    msg += f"\tB+: {bplus.showDatabases()}\n"
    msg += f"\tAVL: {avl.showDatabases()}\n"
    msg += f"\tB: {b.showDatabases()}\n"
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
        if value:
            return value
    return None

def extractRangeTable(database, table, columnNumber, lower, upper):
    for item in structs:
        value = item.extractRangeTable(database, table, columnNumber, lower, upper)
        if value:
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
        if item.alterTable(database, old, new) != 2:
            return value
    return 2

def alterDropColumn(database, table, columnNumber):
    for item in structs:
        value = item.alterDropColumn(database, table, columnNumber)
        if item.alterDropColumn(database, table, columnNumber) != 2:
            return value
    return 2

def insert(database, table, register):
    for item in structs:
        value = item.insert(database, table, register)
        if item.insert(database, table, register) != 2:
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

def alterDatabaseMode(database, mode):
    pass

def alterTableMode(database, table, mode):
    pass

def alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef):
    for item in structs:
        item

def alterTableDropFK(database, table, indexName):
    pass

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
