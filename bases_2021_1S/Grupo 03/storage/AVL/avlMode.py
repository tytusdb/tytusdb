# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from storage.AVL.BusinessLayer.database_module import DatabaseModule
from storage.AVL.BusinessLayer.table_module import TableModule
from storage.AVL.BusinessLayer.tuple_module import TupleModule

DB = DatabaseModule()
TBL = TableModule()
TPL = TupleModule()


# region Database
def createDatabase(database: str) -> int:
    return DB.createDatabase(database)


def showDatabases() -> list:
    return DB.showDatabases()


def alterDatabase(databaseOld: str, databaseNew: str) -> int:
    return DB.alterDatabase(databaseOld, databaseNew)


def dropDatabase(database: str) -> int:
    return DB.dropDatabase(database)


# endregion

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


def alterAddFK(database: str, table: str, references: dict) -> int:
    return TBL.alterAddFK(database, table, references)


def alterAddIndex(database: str, table: str, references: dict) -> int:
    return TBL.alterAddIndex(database, table, references)


def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    return TBL.alterTable(database, tableOld, tableNew)


def alterAddColumn(database: str, table: str, default: any) -> int:
    return TBL.alterAddColumn(database, table, default)


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    return TBL.alterDropColumn(database, table, columnNumber)


def dropTable(database: str, table: str) -> int:
    return TBL.dropTable(database, table)


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


def dropAll():
    return DB.dropAll()
