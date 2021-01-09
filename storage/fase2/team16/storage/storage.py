# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from .Modules.database_module import DatabaseModule
from .Modules.table_module import TableModule
from .Modules.tuple_module import TupleModule

from .Modules.Complements import security as SEC
from .Modules.Complements import graph as GRP

DB = DatabaseModule()
TBL = TableModule()
TPL = TupleModule()


# region Database
def createDatabase(database: str, mode: str, encoding: str) -> int:
    return DB.createDatabase(database, mode, encoding)


def showDatabases() -> list:
    return DB.showDatabases()


def alterDatabase(databaseOld: str, databaseNew: str) -> int:
    return DB.alterDatabase(databaseOld, databaseNew)


def dropDatabase(database: str) -> int:
    return DB.dropDatabase(database)


def alterDatabaseMode(database: str, mode: str) -> int:
    return DB.alterDatabaseMode(database, mode)


def alterTableMode(database: str, table: str, mode: str) -> int:
    return DB.alterTableMode(database, table, mode)


def alterDatabaseEncoding(database: str, encoding: str) -> int:
    return DB.alterDatabaseEncoding(database, encoding)


def alterDatabaseCompress(database: str, level: int) -> int:
    return DB.alterDatabaseCompress(database, level)


def alterDatabaseDecompress(database: str) -> int:
    return DB.alterDatabaseDecompress(database)

def DBS_Safe() -> list:
    return DB.DBS_Safe()


#  endregion

# region Table
def createTable(database: str, table: str, numberColumns: int) -> int:
    return TBL.createTable(database, table, numberColumns)


def showTables(database: str) -> list:
    return TBL.showTables(database)


def extractTable(database: str, table: str) -> list:
    return TBL.extractTable(database, table)


def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    return TBL.extractRangeTable(database, table, columnNumber, lower, upper)


def alterAddPK(database: str, table: str, columns: list) -> int:
    return TBL.alterAddPK(database, table, columns)


def alterDropPK(database: str, table: str) -> int:
    return TBL.alterDropPK(database, table)


def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    return TBL.alterTable(database, tableOld, tableNew)


def alterAddColumn(database: str, table: str, default: any) -> int:
    return TBL.alterAddColumn(database, table, default)


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    return TBL.alterDropColumn(database, table, columnNumber)


def dropTable(database: str, table: str) -> int:
    return TBL.dropTable(database, table)


def alterTableAddFK(database: str, table: str, indexName: str, columns: list, tableRef: str, columnsRef: list) -> int:
    return TBL.alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef)


def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    return TBL.alterTableDropFK(database, table, indexName)


def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    return TBL.alterTableAddUnique(database, table, indexName, columns)


def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    return TBL.alterTableDropUnique(database, table, indexName)


def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    return TBL.alterTableAddIndex(database, table, indexName, columns)


def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    return TBL.alterTableDropIndex(database, table, indexName)


def alterTableCompress(database: str, table: str, level: int) -> int:
    return TBL.alterTableCompress(database, table, level)


def alterTableDecompress(database: str, table: str) -> int:
    return TBL.alterTableDecompress(database, table)


def safeModeOn(database: str, table: str) -> int:
    return TBL.safeModeOn(database, table)


def safeModeOff(database: str, table: str) -> int:
    return TBL.safeModeOff(database, table)

def TBL_Safe(database: str) -> list:
    return TBL.TBL_Safe(database)


# endregion

# region Tuple
def insert(database: str, table: str, register: list) -> int:
    return TPL.insert(database, table, register)


def loadCSV(file: str, database: str, table: str) -> list:
    return TPL.loadCSV(file, database, table)


def extractRow(database: str, table: str, columns: list) -> list:
    return TPL.extractRow(database, table, columns)


def update(database: str, table: str, register: dict, columns: list) -> int:
    return TPL.update(database, table, register, columns)


def delete(database: str, table: str, columns: list) -> int:
    return TPL.delete(database, table, columns)


def truncate(database: str, table: str) -> int:
    return TPL.truncate(database, table)


# endregion

# region Checksum
def checksumDatabase(database: str, mode: str) -> str:
    return DB.checksumDatabase(database, mode)


def checksumTable(database: str, table: str, mode: str) -> str:
    return TBL.checksumTable(database, table, mode)


# endregion

# region Security
def encrypt(backup: str, password: str) -> str:
    return SEC.encrypt(backup, password)


def decrypt(cipherBackup: str, password: str) -> str:
    return SEC.decrypt(cipherBackup, password)


# region graph
def graphDSD(database: str) -> str:
    return GRP.graphDSD(database)

def graphDF(database: str, table: str) -> str:
    return GRP.graphDF(database, table)

# endregion

def dropAll():
    return DB.dropAll()
