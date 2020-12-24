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
    
#entran las funciones 5-10 de Edgar
def alterAddPK(database: str, table: str, columns: list) -> int:
    return T.alterPK(database,table,columns)
def alterDropPK(database: str, table: str) -> int:
    return T.alterDPK(database,table)

