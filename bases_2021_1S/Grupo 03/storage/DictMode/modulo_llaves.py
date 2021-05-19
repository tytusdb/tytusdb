# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos
from singleton import alterAPK, existTable, existDB, insertRegistro, extraerRegistros, deleteRegistro, alterDPK, addColumn, dropColumn, \
    extraerRango, extraerPorColumna, updateRegistro, truncateRegistros

def alterAddPK(database: str, table: str, columns: list):
    try:
        if not existDB(database): return 2
        if not existTable(database, table): return 3
        return alterAPK(database, table,columns)
    except:
        return 1
   

def alterDropPK(database: str, table: str):
    try:
        if not existDB(database): return 2
        if not existTable(database, table): return 3
        return alterDPK(database, table)
    except:
        return 1
    

def insert(database: str, table: str, register: list):
    try:
        if not existDB(database): return 2
        if not existTable(database, table): return 3
        return insertRegistro(database, table, register)
    except:
        return 1
    

def update(database: str, table: str, register: dict, columns: list):
    try:
        if not existDB(database): return 2
        if not existTable(database, table): return 3
        return updateRegistro(database, table, register, columns)
    except:
        return 1


def delete(database: str, table: str, columns: list):
    try:
        if not existDB(database): return 2
        if not existTable(database, table): return 3
        return deleteRegistro(database, table,columns)
    except:
        return 1
    

def truncate(database: str, table: str):
    try:
        if not existDB(database): return 2
        if not existTable(database, table): return 3
        return truncateRegistros(database, table)
    except:
        return 1
    

def alterAddColumn(database: str, table: str, default: any):
    try:
        if not existDB(database): return 2
        if not existTable(database, table): return 3
        return addColumn(database, table, default)
    except:
        return 1
    

def alterDropColumn(database: str, table: str, columnNumber: int):
    try:
        if not existDB(database): return 2
        if not existTable(database, table): return 3
        return dropColumn(database, table, columnNumber)
    except:
        return 1
    

def extractTable(database: str, table: str):
    try:
        if not existDB(database): return None
        if not existTable(database, table): return None
        return extraerRegistros(database, table)
    except:
        return 1
    

def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any):
    try:
        if not existDB(database): return None
        if not existTable(database, table): return None
        return extraerRango(database, table, columnNumber, lower, upper)
    except:
        return 1
    

def extractRow(database: str, table: str, columns: list):
    try:
        if not existDB(database): return []
        if not existTable(database, table): return []
        return extraerPorColumna(database, table,columns)
    except:
        return []
    