from DataBaseLista import *


Ld = ListaDOBLE()
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
