from os import name
import re
from AVL_DB import Avl as AvlDb
from AVL_Table import Avl as AvlT

DataBase = AvlDb()

def createDatabase(nameDb):
    busqueda = DataBase.buscar(str(nameDb))
    if busqueda == None:
        tabla = AvlT()
        DataBase.insertar(tabla,nameDb)
        return 0
    elif busqueda != None:
        return 2
    else: 
        return 1

def showDatabases():
    bases = DataBase.recorrido()
    lista = bases.split(' ')
    lista.pop()
    return lista

def alterDatabase(databaseOld, databaseNew):
    if re.match(r'[_]?[A-Za-z]+[_]?[_0-9]*[_]?', databaseNew):
        db = DataBase.buscar(str(databaseOld))
        db_new = DataBase.buscar(str(databaseNew))
        if db is None:
            return 2
        elif db_new is not None:
            return 3
        elif db is not None:
            db.name = databaseNew
            return 0
        else:
            return 1
    else:
        return 1
    
def dropDatabase(database):
    if CheckData():
        DataBase = Load("BD")
    try:
        if re.match(pattern, database):
            dataB = DataBase.buscar(str(database))
            if dataB is None:
                return 2
            else:
                DataBase.eliminarDB(database)
                Save(DataBase, "BD")
                return 0
        else:
            return 1
    except:
        return 1
    
def createTable(database, table, numberColumns):
    if CheckData():
        DataBase = Load("BD")
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is not None:
            tablaBuscada = dataB.avlTable.buscar(table)
            if tablaBuscada is None:
                bPlus = bPlusT(5, numberColumns)
                dataB.avlTable.insertar(bPlus, table, numberColumns)
                Save(DataBase, "BD")
                return 0
            return 3
        return 2
    except:
        return 1
    
    
def showTables(database):
    if CheckData():
        DataBase = Load("BD")
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is not None:
            tablas = dataB.avlTable.recorrido()
            if not (len(tablas) == 0):
                listaTablas = tablas.split(' ')
                listaTablas.pop()
                return listaTablas
            return tablas
        return dataB
    except:
        return None
    
def alterAddPK(database, table, columns):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(table)
        if tabla is None:
            return 3
        if not tabla.verifyListPk():
            return 4
        if not tabla.verifyColumns(columns):
            return 5
        valor = tabla.alterAddPk(columns) 
        Save(DataBase, "BD")
        return valor
    except:
        return 1
    
def alterDropPK(database, table):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(table)
        if tabla is None:
            return 3
        if tabla.verifyListPk():
            return 4
        valor = tabla.alterDropPk()
        Save(DataBase, "BD")
        return valor
    except:
        return 1
    
def alterDropColumn(database, table, columnNumber):
    if CheckData():
        DataBase = Load("BD")
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(str(table))
        if tabla is None:
            return 3
        if tabla.verifyColumnPk(columnNumber):
            return 4
        if tabla.verifyOutOfRange(columnNumber):
            return 5
        valor = tabla.bPlus.alterDropColumn(columnNumber, tabla)
        Save(DataBase, "BD")
        return valor
    except:
        return 1
    


