# File:     storageManager
# License:  Released under MIT License
# Notice:   Copyright (c) 2020 TytusDB Team

from storage import mainMode as r
from storage import Serializable as serializar

f = r.main()

try:
    f = serializar.rollback("GOD")
except:
    serializar.commit(f, "GOD")

#---------------------FUNCIONES DE UNIFICACION DE MODOS DE ALMACENAMIENTO----------------------#

def createDatabase(database: str, mode: str, encoding: str) -> int:
    r = f.createDatabase(database, mode, encoding)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES DE ADMINISTRACION DEL MODO DE ALMACENAMIENTO----------------------#

def alterDatabaseMode(database: str, mode: str) -> int:
    r = f.alterDatabaseMode(database, mode)
    serializar.commit(f, "GOD")
    return r

def alterTableMode(database: str, table: str, mode: str) -> int:
    r =  f.alterTableMode(database, table, mode)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES DE ADMINISTRACION DE INDICES----------------------#

def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
    r = f.alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef)
    serializar.commit(f, "GOD")
    return r

def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    r = f.alterTableDropFK(database, table, indexName)
    serializar.commit(f, "GOD")
    return r

def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    r = f.alterTableAddUnique(database, table, indexName, columns)
    serializar.commit(f, "GOD")
    return r

def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    r = f.alterTableDropUnique(database, table, indexName)
    serializar.commit(f, "GOD")
    return r

def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    r = f.alterTableAddIndex(database, table, indexName, columns)
    serializar.commit(f, "GOD")
    return r

def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    r = f.alterTableDropIndex(database, table, indexName)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES DE ADMINISTRACION DE LA CODIFICACION----------------------#

def alterDatabaseEncoding(database: str, encoding: str) -> int:
    r = f.alterDatabaseEncoding(database, encoding)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES DE GENERACION DEL CHECKSUM----------------------#

def checksumDatabase(database: str, mode: str) -> str:
    r = f.checksumDatabase(database, mode)
    serializar.commit(f, "GOD")
    return r

def checksumTable(database: str, table:str, mode: str) -> str:
    r = f.checksumTable(database, table, mode)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES DE COMPRESION DE DATOS----------------------#

def alterDatabaseCompress(database: str, level: int) -> int:
    r = f.alterDatabaseCompress(database, level)
    serializar.commit(f, "GOD")
    return r

def alterDatabaseDecompress(database: str) -> int:
    r = f.alterDatabaseDecompress(database)
    serializar.commit(f, "GOD")
    return r

def alterTableCompress(database: str, table: str, level: int) -> int:
    r = f.alterTableCompress(database, table, level)
    serializar.commit(f, "GOD")
    return r

def alterTableDecompress(database: str, table: str) -> int:
    r = f.alterTableDecompress(database, table)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES DE SEGURIDAD----------------------#

def encrypt(backup: str, password: str) -> str:
    r = f.encrypt(backup, password)
    serializar.commit(f, "GOD")
    return r

def decrypt(cipherBackup: str, password: str) -> str:
    r = f.decrypt(cipherBackup, password)
    serializar.commit(f, "GOD")
    return r

def safeModeOn(database: str, table: str) -> int:
    r = f.safeModeOn(database, table)
    serializar.commit(f, "GOD")
    return r

def safeModeOff(database: str, table: str) -> int:
    r = f.safeModeOff(database, table)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES DE GRAFOS----------------------#

def graphDSD(database: str) -> str:
    r = f.graphDSD(database)
    serializar.commit(f, "GOD")
    return r

def graphDF(database: str, table: str) -> str:
    r = f.graphDF(database, table)
    serializar.commit(f, "GOD")
    return r

#---------------------FUNCIONES BASES DE DATOS (ANTIGUAS)----------------------#

def showDatabases() -> list:
    return f.showDatabases()

def alterDatabase(databaseOld, databaseNew) -> int:
    r = f.alterDatabase(databaseOld, databaseNew)
    serializar.commit(f, "GOD")
    return r

def dropDatabase(database: str) -> int:
    r = f.dropDatabase(database)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES TABLAS (ANTIGUAS)----------------------#

def createTable(database: str, table: str, numberColumns: int) -> int:
    r = f.createTable(database, table, numberColumns)
    serializar.commit(f, "GOD")
    return r

def showTables(database: str) -> list:
    return f.showTables(database)

def extractTable(database: str, table: str) -> list:
    return f.extractTable(database, table)

def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    return f.extractRangeTable(database, table, columnNumber, lower, upper)

def alterAddPK(database: str, table: str, columns: list) -> int:
    r = f.alterAddPK(database, table, columns)
    serializar.commit(f, "GOD")
    return r

def alterDropPK(database: str, table: str) -> int:
    r = f.alterDropPK(database, table)
    serializar.commit(f, "GOD")
    return r

def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    r = f.alterTable(database, tableOld, tableNew)
    serializar.commit(f, "GOD")
    return r

def alterAddColumn(database: str, table: str, default: any) -> int:
    r = f.alterAddColumn(database, table, default)
    serializar.commit(f, "GOD")
    return r

def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    r = f.alterDropColumn(database, table, columnNumber)
    serializar.commit(f, "GOD")
    return r

# ---------------------FUNCIONES TUPLAS (ANTIGUAS)----------------------#

def insert(database: str, table: str, register: list) -> int:
    r = f.insert(database, table, register)
    serializar.commit(f, "GOD")
    return r

def loadCSV(file: str, database: str, table: str) -> list:
    r = f.loadCSV(file, database, table)
    serializar.commit(f, "GOD")
    return r

def extractRow(database: str, table: str, columns: list) -> list:
    return f.extractRow(database, table, columns)

def update(database: str, table: str, register: dict, columns: list) -> int:
    r = f.update(database, table, register, columns)
    serializar.commit(f, "GOD")
    return r

def delete(database: str, table: str, columns: list) -> int:
    r = f.delete(database, table, columns)
    serializar.commit(f, "GOD")
    return r

def truncate(database: str, table: str) -> int:
    r = f.truncate(database, table)
    serializar.commit(f, "GOD")
    return r
