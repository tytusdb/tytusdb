# File:     B Mode Package
# License:  Released under MIT License
# Notice:   Copyright (c) 2020 TytusDB Team

from storage.BTree import DataBase as db
from storage.BTree import Serializable as serializar
from storage.BTree import Estructura_ArbolB as bt

b = db.DB()

try:
    b = serializar.rollback("BDD")
except:
    serializar.commit(b, "BDD")

#---------------------FUNCIONES BASES DE DATOS----------------------#


def createDatabase(database: str) -> int:
    r = b.createDatabase(database)
    serializar.commit(b, "BDD")
    return r


def showDatabases() -> list:
    return b.showDatabases()


def alterDatabase(databaseOld, databaseNew) -> int:
    r = b.alterDatabase(databaseOld, databaseNew)
    serializar.commit(b, "BDD")
    return r


def dropDatabase(database: str) -> int:
    r = b.dropDatabase(database)
    serializar.commit(b, "BDD")
    return r

# ---------------------FUNCIONES TABLAS----------------------#


def createTable(database: str, table: str, numberColumns: int) -> int:
    r = b.createTable(database, table, numberColumns)
    serializar.commit(b, "BDD")
    return r


def showTables(database: str) -> list:
    return b.showTables(database)


def extractTable(database: str, table: str) -> list:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    return b.extractTable(database, table)


def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    return b.extractRangeTable(database, table, columnNumber, lower, upper)


def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.alterAddPK(database, table, columns)
    try:
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def alterDropPK(database: str, table: str) -> int:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.alterDropPK(database, table)
    try:
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    r = b.alterTable(database, tableOld, tableNew)
    serializar.commit(b, "BDD")
    return r


def alterAddColumn(database: str, table: str, default: any) -> int:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.alterAddColumn(database, table, default)
    try:
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.alterDropColumn(database, table, columnNumber)
    try:
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def dropTable(database: str, table: str) -> int:
    r = b.dropTable(database, table)
    serializar.commit(b, "BDD")
    return r

# ---------------------FUNCIONES TUPLAS----------------------#


def insert(database: str, table: str, register: list) -> int:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.insert(database, table, register)
    try:
        serializar.commit(b.dicDB[database][table][0], database+"-"+table+"-B")
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def loadCSV(file: str, database: str, table: str) -> list:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.loadCSV(file, database, table)
    try:
        serializar.commit(b.dicDB[database][table][0], database+"-"+table+"-B")
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def extractRow(database: str, table: str, columns: list) -> list:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.extractRow(database, table, columns)
    try:
        serializar.commit(b.dicDB[database][table][0], database+"-"+table+"-B")
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.update(database, table, register, columns)
    try:
        serializar.commit(b.dicDB[database][table][0], database+"-"+table+"-B")
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def delete(database: str, table: str, columns: list) -> int:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.delete(database, table, columns)
    try:
        serializar.commit(b.dicDB[database][table][0], database+"-"+table+"-B")
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r


def truncate(database: str, table: str) -> int:
    try:
        b.dicDB[database][table][0] = serializar.rollback(
            database+"-"+table+"-B")
    except:
        pass
    r = b.truncate(database, table)
    try:
        serializar.commit(b.dicDB[database][table][0], database+"-"+table+"-B")
        b.dicDB[database][table][0] = bt.arbolB(b.grade)
        serializar.commit(b, "BDD")
    except:
        pass
    return r
