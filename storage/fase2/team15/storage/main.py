# -------------------------------
# Released under MIT License
# Copyright (c) 2020 TytusDb Team


from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.dict import DictMode as dict
from storage.hash import HashMode as hash
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as json

import os
from storage import serealizar

_main_path = os.getcwd() + "\\data"


def __init__():
    global lista_general
    lista_general = []
    # Lista de  [Nombre, modo, encoding]

    if not os.path.isfile(_main_path + "\\" + "cache.bin"):
        serealizar.commit(lista_general, "cache", _main_path)

    else:
        lista_general = serealizar.rollback("cache", _main_path)

    # for db in cada carpeta, append to lista_general


__init__()


def _Buscar(nombre: str):
    for db in lista_general:

        if nombre.casefold() == db[0].casefold():
            return db

    else:
        return None


def createDatabase(database: str, mode: str, encoding: str) -> int:
    """Creates a database

        Parameters:\n
            database (str): name of the database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: database name occupied
    """

    if not _Buscar(database):

        if encoding not in ["utf8", "ascii", "iso-8859-1"]:
            return 4

        if mode == "avl":
            val = avl.createDatabase(database)

        elif mode == "b":
            val = b.createDatabase(database)

        elif mode == "bplus":
            val = bplus.createDatabase(database)

        elif mode == "hash":
            val = hash.createDatabase(database)

        elif mode == "isam":
            val = isam.createDatabase(database)

        elif mode == "json":
            val = json.createDatabase(database)

        elif mode == "dict":
            val = dict.createDatabase(database)

        else:
            return 3

        if val == 0:
            lista_general.append([database, mode, encoding])
            serealizar.commit(lista_general, "data", _main_path)

        return val

    else:
        return 2


def showDatabases() -> list:
    """Show stored databases

        Returns:\n
            list: successful operation
    """

    temp = []

    for db in lista_general:
        temp.append(db[0])

    return temp


def alterDatabase(databaseOld: str, databaseNew: str) -> int:
    """Renames a database

        Parameters:\n
            databaseOld (str): name of the target database
            databaseNew (str): new name of the target database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent target database
            3: new database name occupied
    """

    bd = _Buscar(databaseOld)

    if bd:

        if not _Buscar(databaseNew):

            mode = bd[1]

            val = -1

            if mode == "avl":
                val = avl.alterDatabase(databaseOld, databaseNew)

            elif mode == "b":
                val = b.alterDatabase(databaseOld, databaseNew)

            elif mode == "bplus":
                val = bplus.alterDatabase(databaseOld, databaseNew)

            elif mode == "hash":
                val = hash.alterDatabase(databaseOld, databaseNew)

            elif mode == "isam":
                val = isam.alterDatabase(databaseOld, databaseNew)

            elif mode == "json":
                val = json.alterDatabase(databaseOld, databaseNew)

            elif mode == "dict":
                val = dict.alterDatabase(databaseOld, databaseNew)

            if val == 0:
                posicion = lista_general.index(bd)
                bd[0] = databaseNew
                lista_general[posicion] = bd
                serealizar.commit(lista_general, "cache", _main_path)

            return val

        else:
            return 3

    else:
        return 2


def dropDatabase(database: str) -> int:
    """Deletes a database (including all of its content)

        Parameters:\n
            database (str): name of the database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.dropDatabase(database)

        elif mode == "b":
            val = b.dropDatabase(database)

        elif mode == "bplus":
            val = bplus.dropDatabase(database)

        elif mode == "hash":
            val = hash.dropDatabase(database)

        elif mode == "isam":
            val = isam.dropDatabase(database)

        elif mode == "json":
            val = json.dropDatabase(database)

        elif mode == "dict":
            val = dict.dropDatabase(database)

        if val == 0:
            lista_general.remove(bd)
            serealizar.commit(lista_general, "cache", _main_path)

        return val

    else:
        return 2


def createTable(database: str, table: str, numberColumns: int) -> int:
    """Creates a table

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            numberColumns (int): number of table columns

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: table name ocuppied
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.createTable(database, table, numberColumns)

        elif mode == "b":
            val = b.createTable(database, table, numberColumns)

        elif mode == "bplus":
            val = bplus.createTable(database, table, numberColumns)

        elif mode == "hash":
            val = hash.createTable(database, table, numberColumns)

        elif mode == "isam":
            val = isam.createTable(database, table, numberColumns)

        elif mode == "json":
            val = json.createTable(database, table, numberColumns)

        elif mode == "dict":
            val = dict.createTable(database, table, numberColumns)

        return val

    else:
        return 2


def showTables(database: str) -> list:
    """Show stored tables in a database

        Parameters:\n
            database (str): name of the database

        Returns:\n
            list: successful operation
            None: non-existent database
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.showTables(database)

        elif mode == "b":
            val = b.showTables(database)

        elif mode == "bplus":
            val = bplus.showTables(database)

        elif mode == "hash":
            val = hash.showTables(database)

        elif mode == "isam":
            val = isam.showTables(database)

        elif mode == "json":
            val = json.showTables(database)

        elif mode == "dict":
            val = dict.showTables(database)

        return val

    else:
        return 2


def extractTable(database: str, table: str) -> list:
    """Shows the content of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            list: successful operation
            None: non-existent database, non-existent table, an error ocurred
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.extractTable(database, table)

        elif mode == "b":
            val = b.extractTable(database, table)

        elif mode == "bplus":
            val = bplus.extractTable(database, table)

        elif mode == "hash":
            val = hash.extractTable(database, table)

        elif mode == "isam":
            val = isam.extractTable(database, table)

        elif mode == "json":
            val = json.extractTable(database, table)

        elif mode == "dict":
            val = dict.extractTable(database, table)

        return val

    else:
        return 2


def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    """Shows the content whitin a range of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columnNumber (int): PK to compare
            lower (any): lower limit of PK value
            upper (any): upper limit of PK value

        Returns:\n
            list: successful operation
            None: non-existent database, non-existent table, an error ocurred
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.extractRangeTable(database, table, columnNumber, lower, upper)

        elif mode == "b":
            val = b.extractRangeTable(database, table, columnNumber, lower, upper)

        elif mode == "bplus":
            val = bplus.extractRangeTable(database, table, columnNumber, lower, upper)

        elif mode == "hash":
            val = hash.extractRangeTable(database, table, columnNumber, lower, upper)

        elif mode == "isam":
            val = isam.extractRangeTable(database, table, columnNumber, lower, upper)

        elif mode == "json":
            val = json.extractRangeTable(database, table, columnNumber, lower, upper)

        elif mode == "dict":
            val = dict.extractRangeTable(database, table, columnNumber, lower, upper)

        return val

    else:
        return 2


def alterAddPK(database: str, table: str, columns: list) -> int:
    """Adds a PK to a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columns (list): list with PK columns

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: existent PK
            5: PK out of bounds
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.alterAddPK(database, table, columns)

        elif mode == "b":
            val = b.alterAddPK(database, table, columns)

        elif mode == "bplus":
            val = bplus.alterAddPK(database, table, columns)

        elif mode == "hash":
            val = hash.alterAddPK(database, table, columns)

        elif mode == "isam":
            val = isam.alterAddPK(database, table, columns)

        elif mode == "json":
            val = json.alterAddPK(database, table, columns)

        elif mode == "dict":
            val = dict.alterAddPK(database, table, columns)

        return val

    else:
        return 2


def alterDropPK(database: str, table: str) -> int:
    """Deletes PKs of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent PK
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.alterDropPK(database, table)

        elif mode == "b":
            val = b.alterDropPK(database, table)

        elif mode == "bplus":
            val = bplus.alterDropPK(database, table)

        elif mode == "hash":
            val = hash.alterDropPK(database, table)

        elif mode == "isam":
            val = isam.alterDropPK(database, table)

        elif mode == "json":
            val = json.alterDropPK(database, table)

        elif mode == "dict":
            val = dict.alterDropPK(database, table)

        return val

    else:
        return 2


def alterAddFK(database: str, table: str, references: dict) -> int:
    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.alterAddFK(database, table, references)

        elif mode == "b":
            val = b.alterAddFK(database, table, references)

        elif mode == "bplus":
            val = bplus.alterAddFK(database, table, references)

        elif mode == "hash":
            val = hash.alterAddFK(database, table, references)

        elif mode == "isam":
            val = isam.alterAddFK(database, table, references)

        elif mode == "json":
            val = json.alterAddFK(database, table, references)

        elif mode == "dict":
            val = dict.alterAddFK(database, table, references)

        return val

    else:
        return 2


def alterAddIndex(database: str, table: str, references: dict) -> int:
    """
    DOCSTRING
    """
    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.alterAddIndex(database, table, references)

        elif mode == "b":
            val = b.alterAddIndex(database, table, references)

        elif mode == "bplus":
            val = bplus.alterAddIndex(database, table, references)

        elif mode == "hash":
            val = hash.alterAddIndex(database, table, references)

        elif mode == "isam":
            val = isam.alterAddIndex(database, table, references)

        elif mode == "json":
            val = json.alterAddIndex(database, table, references)

        elif mode == "dict":
            val = dict.alterAddIndex(database, table, references)

        return val

    else:
        return 2


def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    """Renames a table in a database

        Parameters:\n
            database (str): name of the database
            tableOld (str): name of the target table
            tableNew (str): new name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent target table
            4: new table name occupied
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.alterTable(database, tableOld, tableNew)

        elif mode == "b":
            val = b.alterTable(database, tableOld, tableNew)

        elif mode == "bplus":
            val = bplus.alterTable(database, tableOld, tableNew)

        elif mode == "hash":
            val = hash.alterTable(database, tableOld, tableNew)

        elif mode == "isam":
            val = isam.alterTable(database, tableOld, tableNew)

        elif mode == "json":
            val = json.alterTable(database, tableOld, tableNew)

        elif mode == "dict":
            val = dict.alterTable(database, tableOld, tableNew)

        return val

    else:
        return 2


def alterAddColumn(database: str, table: str, default: any) -> int:
    """Appends a column to a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            default (any): default value of registers new column

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.alterAddColumn(database, table, default)

        elif mode == "b":
            val = b.alterAddColumn(database, table, default)

        elif mode == "bplus":
            val = bplus.alterAddColumn(database, table, default)

        elif mode == "hash":
            val = hash.alterAddColumn(database, table, default)

        elif mode == "isam":
            val = isam.alterAddColumn(database, table, default)

        elif mode == "json":
            val = json.alterAddColumn(database, table, default)

        elif mode == "dict":
            val = dict.alterAddColumn(database, table, default)

        return val

    else:
        return 2


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    """Deletes a column of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columnNumber (int): target column index

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: column cannot be deleted
            5: column index out of bounds
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.alterDropColumn(database, table, columnNumber)

        elif mode == "b":
            val = b.alterDropColumn(database, table, columnNumber)

        elif mode == "bplus":
            val = bplus.alterDropColumn(database, table, columnNumber)

        elif mode == "hash":
            val = hash.alterDropColumn(database, table, columnNumber)

        elif mode == "isam":
            val = isam.alterDropColumn(database, table, columnNumber)

        elif mode == "json":
            val = json.alterDropColumn(database, table, columnNumber)

        elif mode == "dict":
            val = dict.alterDropColumn(database, table, columnNumber)

        return val

    else:
        return 2


def dropTable(database: str, table: str) -> int:
    """Deletes a table in a database (including all of its content)

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.dropTable(database, table)

        elif mode == "b":
            val = b.dropTable(database, table)

        elif mode == "bplus":
            val = bplus.dropTable(database, table)

        elif mode == "hash":
            val = hash.dropTable(database, table)

        elif mode == "isam":
            val = isam.dropTable(database, table)

        elif mode == "json":
            val = json.dropTable(database, table)

        elif mode == "dict":
            val = dict.dropTable(database, table)

        return val

    else:
        return 2


def insert(database: str, table: str, register: list) -> int:
    """Inserts a register into a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            register (list): list with register values

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: PK ocuppied
            5: register out of bounds
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.insert(database, table, register)

        elif mode == "b":
            val = b.insert(database, table, register)

        elif mode == "bplus":
            val = bplus.insert(database, table, register)

        elif mode == "hash":
            val = hash.insert(database, table, register)

        elif mode == "isam":
            val = isam.insert(database, table, register)

        elif mode == "json":
            val = json.insert(database, table, register)

        elif mode == "dict":
            val = dict.insert(database, table, register)

        return val

    else:
        return 2


def loadCSV(file: str, database: str, table: str) -> list:
    """Loads a csv file and inserts its content into a table in a database

        Parameters:\n
            file (str): csv file path
            file (str): csv file path
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            list: return values of each insert
            empty list: non-existent database, non-existent table, an error occured, csv file is empty
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.loadCSV(file, database, table)

        elif mode == "b":
            val = b.loadCSV(file, database, table)

        elif mode == "bplus":
            val = bplus.loadCSV(file, database, table)

        elif mode == "hash":
            val = hash.loadCSV(file, database, table)

        elif mode == "isam":
            val = isam.loadCSV(file, database, table)

        elif mode == "json":
            val = json.loadCSV(file, database, table)

        elif mode == "dict":
            val = dict.loadCSV(file, database, table)

        return val

    else:
        return 2


def extractRow(database: str, table: str, columns: list) -> list:
    """Shows a register of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columns (list): PK of target register

        Returns:\n
            list: succesful operation
            empty list: non-existent database, non-existent table, an error ocurred
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.extractRow(database, table, columns)

        elif mode == "b":
            val = b.extractRow(database, table, columns)

        elif mode == "bplus":
            val = bplus.extractRow(database, table, columns)

        elif mode == "hash":
            val = hash.extractRow(database, table, columns)

        elif mode == "isam":
            val = isam.extractRow(database, table, columns)

        elif mode == "json":
            val = json.extractRow(database, table, columns)

        elif mode == "dict":
            val = dict.extractRow(database, table, columns)

        return val

    else:
        return 2


def update(database: str, table: str, register: dict, columns: list) -> int:
    """Updates a register into a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            register (dict): key: column number, value: new values
            columns (list): PK of target register

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent PK
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.update(database, table, register, columns)

        elif mode == "b":
            val = b.update(database, table, register, columns)

        elif mode == "bplus":
            val = bplus.update(database, table, register, columns)

        elif mode == "hash":
            val = hash.update(database, table, register, columns)

        elif mode == "isam":
            val = isam.update(database, table, register, columns)

        elif mode == "json":
            val = json.update(database, table, register, columns)

        elif mode == "dict":
            val = dict.update(database, table, register, columns)

        return val

    else:
        return 2


def delete(database: str, table: str, columns: list) -> int:
    """Deletes a register into a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columns (list): PK of target register

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent PK
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.delete(database, table, columns)

        elif mode == "b":
            val = b.delete(database, table, columns)

        elif mode == "bplus":
            val = bplus.delete(database, table, columns)

        elif mode == "hash":
            val = hash.delete(database, table, columns)

        elif mode == "isam":
            val = isam.delete(database, table, columns)

        elif mode == "json":
            val = json.delete(database, table, columns)

        elif mode == "dict":
            val = dict.delete(database, table, columns)

        return val

    else:
        return 2


def truncate(database: str, table: str) -> int:
    """Deletes the content of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
    """

    bd = _Buscar(database)

    if bd:

        mode = bd[1]

        val = -1

        if mode == "avl":
            val = avl.truncate(database, table)

        elif mode == "b":
            val = b.truncate(database, table)

        elif mode == "bplus":
            val = bplus.truncate(database, table)

        elif mode == "hash":
            val = hash.truncate(database, table)

        elif mode == "isam":
            val = isam.truncate(database, table)

        elif mode == "json":
            val = json.truncate(database, table)

        elif mode == "dict":
            val = dict.truncate(database, table)

        return val

    else:
        return 2

def alterDatabaseMode(database: str, mode: str) -> int:
    """Deletes the content of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
    """

    bd = _Buscar(database)

    if bd:

        pass

    else:
        return 2



def alterTableMode(database: str, table: str, encoding: str) -> int:
    """Deletes the content of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
    """

    bd = _Buscar(database)

    if bd:

        pass

    else:
        return 2
