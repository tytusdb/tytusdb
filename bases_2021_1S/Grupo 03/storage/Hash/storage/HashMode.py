# HASH Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team


from storage.Hash.storage import ListaBaseDatos

import os
import re
import csv

_storage = ListaBaseDatos.ListaBaseDatos()
_main_path = os.getcwd()+"\\data\\hash"
_db_name_pattern = "^[a-zA-Z][a-zA-Z0-9#@$_]*"


def __init__():

    if not os.path.isdir(os.getcwd()+"\\data"):
        os.mkdir(os.getcwd()+"\\data")

    if not os.path.isdir(os.getcwd()+"\\data\\hash"):
        os.mkdir(os.getcwd()+"\\data\\hash")

    for db in os.listdir(_main_path):
        _storage.createDatabase(db)


__init__()


def createDatabase(database: str) -> int:

    try:

        if re.search(_db_name_pattern, database):
            return _storage.createDatabase(database)

        else:
            return 1

    except:
        return 1


def showDatabases() -> list:

    return _storage.showDatabases()


def alterDatabase(databaseOld: str, databaseNew: str) -> int:

    try:

        if re.search(_db_name_pattern, databaseOld) and re.search(_db_name_pattern, databaseNew):
            return _storage.alterDatabase(databaseOld, databaseNew)

        else:
            return 1

    except:
        return 1


def dropDatabase(database: str) -> int:

    try:

        return _storage.dropDatabase(database)

    except:
        return 1


def createTable(database: str, table: str, numberColumns: int) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.createTable(table, numberColumns)

        else:
            return 2

    except:
        return 1


def showTables(database: str) -> list:

    temp = _storage.Buscar(database)

    if temp:
        return temp.showTables()

    else:
        return None


def extractTable(database: str, table: str) -> list:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.extractTable(table)

        else:
            return None

    except:
        return None


def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.extractRangeTable(table, columnNumber, lower, upper)

        else:
            return None

    except:
        return None


def alterAddPK(database: str, table: str, columns: list) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterAddPK(table, columns)

        else:
            return 2

    except:
        return 1


def alterDropPK(database: str, table: str) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterDropPK(table)

        else:
            return 2

    except:
        return 1


def alterAddFK(database: str, table: str, references: dict) -> int:

    print("codigo en proceso (FASE 2)")


def alterAddIndex(database: str, table: str, references: dict) -> int:

    print("codigo en proceso (FASE 2)")


def alterTable(database: str, tableOld: str, tableNew: str) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterTable(tableOld, tableNew)

        else:
            return 2

    except:
        return 1


def alterAddColumn(database: str, table: str, default: any) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterAddColumn(table, default)

        else:
            return 2

    except:
        return 1


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterDropColumn(table, columnNumber)

        else:
            return 2

    except:
        return 1


def dropTable(database: str, table: str) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.dropTable(table)

        else:
            return 2

    except:
        return 1


def insert(database: str, table: str, register: list) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)

            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.insertar(register)
                temp.Guardar()
                return var

            else:
                return 3

        else:
            return 2

    except:
        return 1


def loadCSV(file: str, database: str, table: str) -> list:

    try:

        archivo = open(file, "r", encoding="utf-8-sig")

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)
            nombre = temp.list_table[b[1]]

            if b[0]:

                tabla = temp.Cargar(nombre)
                registros = list(csv.reader(archivo, delimiter=","))

                valores = []
                for registro in registros:

                    for i in range(len(registro)):

                        if registro[i].isnumeric():
                            nuevo = int(registro[i])
                            registro[i] = nuevo

                    valores.append(tabla.insertar(registro))

                else:
                    temp.Guardar()
                    return valores

            else:
                return []

        else:
            return []

    except:
        return []


def extractRow(database: str, table: str, columns: list) -> list:

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)

            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.ExtraerTupla(columns)
                temp.Guardar()
                return var

            else:
                return []

        else:
            return []

    except:
        return []


def update(database: str, table: str, register: dict, columns: list) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)

            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.update(columns, register)
                temp.Guardar()
                return var

            else:
                return 3

        else:
            return 2

    except:
        return 1


def delete(database: str, table: str, columns: list) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)

            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.deleteTable(columns)
                temp.Guardar()
                return var

            else:
                return 3

        else:
            return 2

    except:
        return 1


def truncate(database: str, table: str) -> int:

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)

            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.truncate()
                temp.Guardar()
                return var

            else:
                return 3

        else:
            return 2

    except:
        return 1


def _Cargar(database, table):

    _storage.Cargar(database, table)
