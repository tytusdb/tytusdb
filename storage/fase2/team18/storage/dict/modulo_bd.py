# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos
from .singleton import existDB, insertDB, alterDB, dropDB, showDB, dropAll


def createDatabase(database: str):
    try:
        if existDB(database):
            return 2
        return insertDB(database)
    except:
        return 1

def alterDatabase(databaseOld, databaseNew):
    try:
        if not existDB(databaseOld):
            return 2
        if existDB(databaseNew):
            return 3
        return alterDB(databaseOld, databaseNew)
    except:
        return 1
    

def dropDatabase(database:str):
    try:
        if not existDB(database):
            return 2
        return dropDB(database)
    except:
        return 1
    

def showDatabases():
    try:
        return showDB()
    except:
        return 1
    