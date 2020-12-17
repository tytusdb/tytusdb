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

def alterAddPK(database: str, table: str, columns: list) -> int:
    return b.alterAddPK(database, table, columns)

def alterDropPK(database: str, table: str) -> int:
    return b.alterDropPK(database, table)

def dropTable(database: str, table: str) -> int:
    return b.dropTable(database, table)

# ---------------------FUNCIONES TUPLAS----------------------#

def insert(database: str, table: str, register: list) -> int:
    return b.insert(database, table, register)