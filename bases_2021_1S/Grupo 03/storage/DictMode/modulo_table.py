# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos
from singleton import existTable, existDB, insertTable, showTBS, alterTB, dropTB
from diccionario import Estructura

def createTable(database: str, table: str, numberColumns: int):
    try:
        if not existDB(database):
            return 2
        if existTable(database,table):
            return 3
        return insertTable(database, table, Estructura(numberColumns) )
    except:
        return 1
    

def alterTable(database: str, tableOld: str, tableNew: str):
    try:
        if not existDB(database):
            return 2
        if not existTable(database, tableOld):
            return 3
        if existTable(database,tableNew):
            return 4
        return alterTB(database,tableOld, tableNew)
    except:
        return 1
    

def dropTable(database: str, table: str):
    try:
        if not existDB(database):
            return 2
        if not existTable(database, table):
            return 3
        return dropTB(database, table)
    except:
        return 1
    

def showTables(database: str):
    try:
        if not existDB(database):
            return None
        return showTBS(database)
    except:
        return None
    