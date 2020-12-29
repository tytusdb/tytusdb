  
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

def showTables(database: str):
    return d.showTables(database)

def extractTable(database: str, table: str):
    return h.extractTable(database, table)

def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any):
    try:
        return h.extractRangeTable(database, table, columnNumber, lower, upper)
    except:
        return None

def alterAddPK(database: str, table: str, columns: list):
    return d.alterAddPK(database, table, columns)

def alterDropPK(database: str, table: str):
    return d.alterAddPK(database, table)
  
def alterTable(database: str, tableOld: str, tableNew: str):
    return d.alterTable(database, tableOld, tableNew)

def alterAddColumn(database: str, table: str, default: any):
    return d.alterAddColumn(database, table, default)

def alterDropColumn(database: str, table: str, columnNumber: int):
    return d.alterDropColumn(database, table, columnNumber)

def dropTable(database: str, table: str):
    return d.dropTable(database, table)

def insert(database: str, table: str, register: list):
    try:
        return h.insert(database, table, register)
    except:
        return 1     
      
def loadCSV(file: str, database: str, table: str):
    return ar.leerCSV(file, database, table)

def extractRow(database: str, table: str, columns: list):
    try:
        return h.extractRow(database, table, columns)
    except:
        return []

def update(database: str, table: str, register: dict, columns: list):
    try:
        return h.update(database, table, register, columns)
    except:
        return 1

def delete(database: str, table: str, columns: list):
    try:
        return h.delete(database, table, columns)
    except:
        return 1

def truncate(database: str, table: str):
    try: 
        return h.truncate(database, table)
    except:
        return 1

  
