from crud_bd import CRUD_DataBase
from crud_tabla import CRUD_Tabla
from crud_tupla import CRUD_Tuplas

def createDatabase(database):
    return CRUD_DataBase().createDatabase(database)

def showDatabases():
    return CRUD_DataBase().showDatabases()

def alterDatabase(databaseOld, databaseNew):
    return CRUD_DataBase().alterDatabase(databaseOld, databaseNew)

def dropDatabase(database):
    return CRUD_DataBase().dropDatabase(database)

######################## Tablas ########################

def createTable(database, table, numberColumns):
    return CRUD_Tabla().createTable(database, table, numberColumns)

def showTables(database):
    return CRUD_Tabla().shownTables(database)

def extractTable(database, table):
    return CRUD_Tabla().extractTable(database, table)

def extractRangeTable(database, table, columnNumber, lower, upper):
    return CRUD_Tabla().extractRangeTable(database, table, columnNumber, lower, upper)

def alterAddPK(database, table, columns):
    return CRUD_Tabla().alterAddPK(database, table, columns)

def alterDropPK(database, table):
    return CRUD_Tabla().alterDropPK(database, table)

def alterTable(database, tableOld, tableNew):
    return CRUD_Tabla().alterTable(database, tableOld, tableNew)

def alterAddColumn(database, table, default):
    return CRUD_Tabla().alterAddColumn(database, table, default)

def alterDropColumn(database, table, columnNumber):
    return CRUD_Tabla().alterDropColumn(database, table, columnNumber)

def dropTable(database, table):
    return CRUD_Tabla().dropTable(database, table)

######################## Tupla ########################

def insert(database, table, register):
    return CRUD_Tabla().insert(database, table, register)

def loadCSV(file, database, table):
    return CRUD_Tabla().loadCSV(file, database, table)

def extractRow(database, table, columns):
    return CRUD_Tabla().extractRow(database, table, columns)

def update(database, table, register, columns):
    return CRUD_Tabla().update(database, table, register, columns)

def delete(database, table, columns):
    return CRUD_Tabla().delete(database, table, columns)

def truncate(database, table):
    return CRUD_Tabla().truncate(database, table)
