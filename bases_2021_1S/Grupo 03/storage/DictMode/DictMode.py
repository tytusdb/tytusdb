# Package:      Dictionary Mode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos

import modulo_bd as bd
import modulo_table as tb
import modulo_llaves as ky
import modulo_carga as ld

def createDatabase(database: str):
    return bd.createDatabase(database)

def showDatabases():
    return bd.showDatabases()

def alterDatabase(old, new):
    return bd.alterDatabase(old, new)

def dropDatabase(database:str):
    return bd.dropDatabase(database)

'Inicio de Funciones Tabla'
def createTable(database:str, table:str, numbercolumns:int):
    return tb.createTable(database, table, numbercolumns)

def alterTable(database: str, tableOld: str, tableNew: str):
    return tb.alterTable(database, tableOld, tableNew)

def dropTable(database: str, table: str):
    return tb.dropTable(database, table)

def showTables(database:str):
    return tb.showTables(database)

'registros'
def alterAddPK(database: str, table: str, columns: list):
    return ky.alterAddPK(database, table, columns)

def alterDropPK(database: str, table: str):
    return ky.alterDropPK(database, table)

def insert(database: str, table: str, register: list):
    return ky.insert(database, table, register)

def update(database: str, table: str, register: dict, columns: list):
    return ky.update(database, table, register, columns)

def delete(database: str, table: str, columns: list):
    return ky.delete(database, table, columns)

def truncate(database: str, table: str):
    return ky.truncate(database, table)

def alterAddColumn(database: str, table: str, default: any):
    return ky.alterAddColumn(database,table, default)

def alterDropColumn(database: str, table: str, columnNumber: int):
    return ky.alterDropColumn(database, table, columnNumber)

def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any):
    return ky.extractRangeTable(database, table, columnNumber, lower, upper)

def extractTable(database: str, table: str):
    return ky.extractTable(database, table)

def extractRow(database: str, table: str, columns: list):
    return ky.extractRow(database, table, columns)

'Carga'
def loadCSV(file: str, database: str, table: str):
    return ld.loadCSV(file,database,table)

def dropAll():
    return bd.dropAll()