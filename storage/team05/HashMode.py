  
# Package:      HASH Mode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developers:   Jose Santos, Madelyn Perez, Carlos Campos and Rafael Soliz

import re
from NameStructure import ne as d 
from NameStructure import ht as h
from Archivos import archivo as ar

def createDatabase(database: str):
    return d.createDatabase(database)

def showDatabases():
    return d.showDatabases()

def alterDatabase(databaseOld, databaseNew):
    return d.alterDatabase(databaseOld, databaseNew)

def dropDatabase(database: str):
    return d.dropDatabase(database)

def createTable(database: str, table: str, numberColumns: int):
    return d.createTable(database, table, numberColumns)
