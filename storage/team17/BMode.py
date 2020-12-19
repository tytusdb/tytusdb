from DataBase import *
b = DB()

#---------------------FUNCIONES BASES DE DATOS----------------------#

def createDatabase(database: str) -> int:
    return b.createDatabase(database)

def showDatabases() -> list:
    return b.showDatabases()

def alterDatabase(databaseOld, databaseNew) -> int:
    return b.alterDatabase(databaseOld, databaseNew)

def dropDatabase(database: str) -> int:
    return b.dropDatabase(database)

# ---------------------FUNCIONES TABLAS----------------------#

def createTable(database: str, table: str, numberColumns: int) -> int:
    return b.createTable(database, table, numberColumns)

def showTables(database: str) -> list:
    return b.showTables(database)

def extractTable(database: str, table: str) -> list:
    return b.extractTable(database, table)

def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    return b.extractRangeTable(database, table, columnNumber, lower, upper)

def alterAddPK(database: str, table: str, columns: list) -> int:
    return b.alterAddPK(database, table, columns)

def alterDropPK(database: str, table: str) -> int:
    return b.alterDropPK(database, table)

def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    return b.alterTable(database, tableOld, tableNew)

def alterAddColumn(database: str, table: str, default: any) -> int:
    return b.alterAddColumn(database, table, default)

def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    return b.alterDropColumn(database, table, columnNumber)

def dropTable(database: str, table: str) -> int:
    return b.dropTable(database, table)

# ---------------------FUNCIONES TUPLAS----------------------#

def insert(database: str, table: str, register: list) -> int:
    return b.insert(database, table, register)

def loadCSV(file: str, database: str, table: str) -> list:
    return b.loadCSV(file, database, table)

def extractRow(database: str, table: str, columns: list) -> list:
    return b.extractRow(database, table, columns)

def update(database: str, table: str, register: dict, columns: list) -> int:
    return b.update(database, table, register, columns)

def delete(database: str, table: str, columns: list) -> int:
    return b.delete(database, table, columns)

def truncate(database: str, table: str) -> int:
    return b.truncate(database, table)
