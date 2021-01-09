from DataBaseLista import *
from TablasD import *
from BTree import *

Ld = ListaDOBLE()
T = TablasArboles(Ld)
def createDatabase(database : str)-> int:
    res_1 = Ld.agregarLista(database)
    return res_1
def showDatabases() -> list:
    res_2 = Ld.imprimir()
    return res_2
def alterDatabase(databaseOld, databaseNew) -> int:
    res_3 = Ld.modificarNodo(databaseOld,databaseNew)
    return res_3
def dropDatabase(database: str) -> int:
    res_4 = Ld.eliminarNodo(database)
    return res_4

def insertT(database, table, register) :
    return T.insert(database,table,register)

def loadCSV(filepath, database, table):
    return T.load(filepath, database, table)

def extractRow(database, table, columns):
    return T.extract(database, table, columns)

def update(database, table, register, columns):
    return T.UP(database, table, register, columns)

def graphB(database, table):
    return T.graphbt(database, table)

#entran las funciones 5-10 de Edgar
def alterAddPK(database: str, table: str, columns: list) -> int:
    return T.alterPK(database,table,columns)
def alterDropPK(database: str, table: str) -> int:
    return T.alterDPK(database,table)

#Tablas

def createTable(database,table,numberColumns) :
    return T.createT(database,table,numberColumns)
def showTables(database) :
    return T.showT(database)
def extractTable(database, table) :
    return T.extractT(database, table)
def extractRangeTable(database, table, columnNumber, lower, upper) :
    return T.extractRT(database, table, columnNumber, lower, upper)

#entran las funciones 5-10 de Edgar

def alterAddColumn( database, table, default) :
    return T.alterAC(database, table, default)
def alterTable(database,tableOld,tableNew) :
    return T.alterT(database,tableOld,tableNew)
def alterDropColumn(database, table, columnNumber) :
    return T.alterDC(database, table, columnNumber)
def dropTable(database,table) :
    return T.dropT(database,table)