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

import os, traceback, csv, zlib
from storage.misc import serealizar as sr, ForeignKeyStr as fk_str, UniqueIndexStr as ui_str, IndexStr as i_str, \
    checksum as ch, compresion as comp, BlockChain as BC, Grafos as graph

_main_path = os.getcwd() + "\\data"


def __init__():
    global _data
    _data = []

    # database:
    # { 
    #   nombre: str,
    #   modo: str,
    #   encoding: str,
    #   tablas: list<dict>
    # }

        # tabla:
        # {
        #   nombre: str,
        #   modo: str,
        #   numero_columnas: int,
        #   pk: list,
        #   foreign_keys: ForeignKeyStr,
        #   unique_index: UniqueIndexStr,
        #   index: IndexStr
        # }

            # REGISTROS

            # foreign_key:
            # {
            #   nombre: str,
            #   table: str,
            #   tableRef: str,
            #   columns: str,
            #   columnsRef: str
            # }

            # unique_index:
            # {
            #   nombre: str,
            #   table: str,
            #   columns: str
            # }

            # index:
            # {
            #   nombre: str,
            #   table: str,
            #   columns: str
            # }


    if not os.path.isfile(_main_path + "\\" + "data"):
        sr.commit(_data, _main_path)

    else:
        _data = sr.rollback(_main_path)

    try:
        os.mkdir(_main_path + "\\SafeTables")

    except: pass

__init__()


def dropAll():
    '''Removes all the data stored

        Returns:\n
        list: successful operation
        1: an error ocurred
    
    '''

    global _data

    try:

        var=[]

        for mode in [avl, b, bplus, hash, isam, dict, json]:

            list = mode.showDatabases()

            for db in list:
                var.append(mode.dropDatabase(db))

        _data = []

        return var

    except:
        return 1


def _Guardar():
    sr.commit(_data, _main_path)


def _database(database):
    for db in _data:
        if db["nombre"].casefold() == database.casefold():
            return db

    return False


def _table(database, table):
    db = _database(database)

    if db:
        for tb in db["tablas"]:
            if tb["nombre"].casefold() == table.casefold():
                return tb

    return False


def _foreign_key(database, table, foreign_key):
    db = _database(database)

    if db:

        tb = _table(database, table)

        if tb:
            return tb["foreign_keys"].extractRow(foreign_key)

    return False


def _unique_index(database, table, unique_index):
    db = _database(database)

    if db:

        tb = _table(database, table)

        if tb:
            return tb["unique_index"].extractRow(unique_index)

    return False


def _index(database, table, index):
    db = _database(database)

    if db:

        tb = _table(database, table)

        if tb:
            return tb["index"].extractRow(index)

    return False


def _Comprobar(database, table, registro):
    '''
    METODO PARA COMPROBAR LA INTEGRIDAD DE LLAVES FORÁNEAS
    '''

    db = _database(database)

    if db:

        for fk in db["fks"]:

            if fk["table"].casefold() == table.casefold():

                for i in range(len(fk["columns"])):

                    pos=fk["columns"][i]
                    pos_r=fk["columnsRef"][i]

                    registros_r = extractTable(database, fk["tableRef"])

                    columna_r = []

                    for registro_r in registros_r:

                        columna_r.append(registro_r[pos_r])

                    if registro[pos] not in columna_r:

                        return False


        return True

    else:
        return False


def _Comprobar_unique(database, table, columns):
    '''
    METODO PARA COMPROBAR LA UNICIDAD DE DATOS
    '''

    db = _database(database)

    if db:

        tb = _table(database, table)

        if tb:


            for i in columns:

                registros = extractTable(database, table)    

                if registros:

                    columna = []

                    for registro in registros:

                        columna.append(registro[i])

                    while columna:

                        valor = columna.pop()

                        if valor in columna:
                            return False            
                
            return True   

        else:
            return False

    else:
        return False


# ===============================//=====================================
#                      ADMINISTRACION DE ALMACENAMIENTO

def createDatabase(database: str, mode: str, encoding: str) -> int:
    """Creates a database

        Parameters:\n
            database (str): name of the database
            mode (str): mode of the database
            encoding (str): encoding of the database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: database name occupied
            3: non-valid mode
            4: non-valid encoding
    """

    if not _database(database):

        val = _createDatabase(database, mode, encoding)

        if val == 0:
            _data.append({"nombre": database, "modo": mode, "encoding": encoding, "tablas": []})
            _Guardar()

        return val

    else:
        return 2


def _createDatabase(database, mode, encoding) -> int:
    """Creates a database

        Parameters:\n
            database (str): name of the database
            mode (str): mode of the database
            encoding (str): encoding of the database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: database name occupied
            3: non-valid mode
            4: non-valid encoding
    """

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

    return val


def showDatabases() -> list:
    """Show stored databases

        Returns:\n
            list: successful operation
    """

    temp = []

    for db in _data:
        temp.append(db["nombre"])

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

    bd = _database(databaseOld)

    if bd:

        if not _database(databaseNew):

            mode = bd["modo"]

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
                _database(databaseOld)["nombre"] = databaseNew
                _Guardar()

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

    bd = _database(database)

    if bd:

        mode = bd["modo"]

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
            _data.remove(bd)
            _Guardar()

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

    bd = _database(database)

    if bd:
        return _createTable(database, table, numberColumns, bd["modo"])

    else:
        return 2


def _createTable(database, table, numberColumns, mode):
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

    if val == 0:
        compress = False
        level = 0
        _database(database)["tablas"].append({"nombre": table, "modo": mode, "columnas": numberColumns, "pk": [],
                                            "foreign_keys": fk_str.ForeignKeyStr(mode, database, table),
                                            "unique_index": ui_str.UniqueIndexStr(mode, database, table),
                                            "index": i_str.IndexStr(mode, database, table), "compress": compress, "level":level})
        _Guardar()

    return val


def showTables(database: str) -> list:
    """Show stored tables in a database

        Parameters:\n
            database (str): name of the database

        Returns:\n
            list: successful operation
            None: non-existent database
    """

    bd = _database(database)

    if bd:

        temp = []

        for tabla in bd["tablas"]:
            temp.append(tabla["nombre"])

        return temp

    else:
        return None


def extractTable(database: str, table: str) -> list:
    """Shows the content of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            list: successful operation
            None: non-existent database, non-existent table, an error ocurred
    """

    bd = _database(database)

    if bd:

        tb = _table(database, table)  

        if tb:

            compress = tb["compress"]

            val = _extractTable(database, table, tb["modo"])

            if compress:
                if len(val):
                    for x in val:
                        for y in x:
                            if type(y) == str:
                                i = x.index(y)
                                x[i] = zlib.decompress(bytes.fromhex(y)).decode()
            return val

        else:
            return 3

    else:
        return 2


def _extractTable(database: str, table: str, mode) -> list:

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            mode = tb["modo"]
            compress = tb["compress"]

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
                val = json.extractRangeTable(database, table, lower, upper)

            elif mode == "dict":
                val = dict.extractRangeTable(database, table, columnNumber, lower, upper)
            
            if compress:
                if len(val):
                    for x in val:
                        for y in x:
                            if type(y) == str:
                                i = x.index(y)
                                x[i] = zlib.decompress(bytes.fromhex(y)).decode()

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            mode = tb["modo"]

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

            if val == 0:
                _table(database, table)["pk"] = columns
                _Guardar()

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            mode = tb["modo"]

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

            if val == 0:
                _table(database, table)["pk"] = []
                _Guardar()

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, tableOld)

        if tb:

            mode = tb["modo"]

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

            if val == 0:
                for key in ["foreign_keys", "unique_index", "index"]: _table(database, tableOld)[key].alterTable(
                    tableNew)
                _table(database, tableOld)["nombre"] = tableNew
                _Guardar()

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            mode = tb["modo"]

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

            if val == 0:
                _table(database, table)["columnas"] += 1
                _Guardar()

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            mode = tb["modo"]

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

            if val == 0:
                _table(database, table)["columnas"] -= 1
                _Guardar()

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            mode = tb["modo"]

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

            if val == 0:
                for key in ["foreign_keys", "unique_index", "index"]: _table(database, table)[key].dropTable()
                _database(database)["tablas"].remove(_table(database, table))
                _Guardar()

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            encoding = bd["encoding"]	
            mode = tb["modo"]	  

            for y in register:	
                if type(y) == str:	
                    try:	
                        y.encode(encoding, "strict")	
                    except: 	
                        return 1

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

            if val == 0:
                nombreST = str(database) + '-' + str(table)
                if BC.EsUnaTablaSegura(nombreST, _main_path):
                    BC.insertSafeTable(nombreST, register, _main_path)

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)
        encoding = bd["encoding"]

        if tb:

            mode = tb["modo"]
            try:
                with open(file, 'r', encoding='utf-8-sig') as leer:
                    reader = csv.reader(leer, delimiter=',')
                    for x in reader:
                        for y in x:
                            if type(y) == str:
                                y.encode(encoding, "strict")
                    leer.close()
            except:
                return []

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

            nombreST = str(database) + '-' + str(table)

            if 0 in val:

                if BC.EsUnaTablaSegura(nombreST, _main_path):
                    BC.insertCSV(nombreST, file, _main_path, val)

            return val

        else:
            return []

    else:
        return []


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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            mode = tb["modo"]
            compress = tb["compress"]

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

            if compress:
                if len(val):
                    for x in val:
                        for y in x:
                            if type(y) == str:
                                i = x.index(y)
                                x[i] = zlib.decompress(bytes.fromhex(y)).decode()
            return val

        else:
            return []

    else:
        return []


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
    datosAntiguos = False
    nombreST = str(database) + '-' + str(table)
    if BC.EsUnaTablaSegura(nombreST, _main_path):
        datosAntiguos = extractRow(database, table, columns)

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:
            compress = tb["compress"]
            level = tb["level"]
            mode = tb["modo"]
            encoding = bd["encoding"]	

            for y in list(register.values()):	
                if type(y) == str:	
                    try:	
                        y.encode(encoding, "strict")	
                    except: 	
                        return 1
            
            if compress:
                for x in register.keys():
                    if type(register[x]) == str:
                        i = register.index(x)
                        register[i] = zlib.compress(register[i].encode(), level).hex()
                
                for x in columns:
                    if type(x) == str:
                        i = columns.index(x)
                        columns[i] =zlib.compress(x.encode(), level).hex()

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

            if val == 0:
                if datosAntiguos:
                    BC.updateSafeTable(nombreST, datosAntiguos, extractRow(database, table, columns), _main_path)

            return val

        else:
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:
            compress = tb["compress"]
            mode = tb["modo"]
            level = tb["level"]

            if compress:
                for x in columns:
                    if type(x) == str:
                        i = columns.index(x)
                        columns[i] =zlib.compress(x.encode(), level).hex()
                            
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
            return 3

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

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            mode = tb["modo"]

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
            return 3

    else:
        return 2


# ===============================//=====================================
#                     ADMINISTRACION DE MODOS

def alterDatabaseMode(database: str, mode: str) -> int:
    """Restructures a database inner structure

        Parameters:\n
            database (str): name of the database
            mode (str): new mode of the database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            4: non-valid mode
    """

    try:

        bd = _database(database)

        if bd:

            if bd["modo"] == mode or mode not in ["avl", "b", "bplus", "dict", "hash", "isam", "json"]:
                return 4

            lista_tablas = showTables(database)

            if lista_tablas:

                data = []

                for tabla in lista_tablas:

                    registros = extractTable(database, tabla)
                    
                    fk_list, ui_list, i_list = _table(database, tabla)["foreign_keys"].extractTable(), _table(database, tabla)["unique_index"].extractTable(), _table(database, tabla)["index"].extractTable()
                
                    data.append([_table(database, tabla), registros, fk_list, ui_list, i_list])

            else:
                bd["modo"] = mode
                return 0

            dropDatabase(database)
            createDatabase(database, mode, bd["encoding"])
                
            for tabla in data:

                tb = tabla[0]
                createTable(database, tb["nombre"], tb["columnas"])

                if tb["pk"]:
                    alterAddPK(database, tb["nombre"], tb["pk"])

                if tabla[1]:

                    for registro in tabla[1]:
                        insert(database, tb["nombre"], registro)
                        
                if tabla[2]:
                    for fk in tabla[2]:
                        tb["foreign_keys"].insert(fk)
                if tabla[3]:
                    for ui in tabla[3]:
                        tb["unique_index"].insert(ui)
                if tabla[4]:
                    for i in tabla[4]:
                        tb["index"].insert(i)

            return 0

        else:
            return 2

    except:
        return 1


def alterTableMode(database: str, table: str, mode: str) -> int:
    """Restructures a table inner structure

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            mode (str): new mode of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-valid mode
    """

    try:

        bd = _database(database)

        if bd:

            tb = _table(database, table)

            if tb:

                if tb["modo"] == mode or mode not in ["avl", "b", "bplus", "dict", "hash", "isam", "json"]:
                    return 4

                registros = extractTable(database, table)

                fk_list, ui_list, i_list = tb["foreign_keys"].extractTable(), tb["unique_index"].extractTable(), tb["index"].extractTable()
                
                dropTable(database, table)

                _createDatabase(database, mode, bd["encoding"])
                _createTable(database, table, tb["columnas"], mode)

                alterAddPK(database, table, tb["pk"])

                tb = _table(database, table)

                for registro in registros:
                    insert(database, table, registro)

                if fk_list:
                    for fk in fk_list:
                        tb["foreign_keys"].insert(fk)
                if ui_list:
                    for ui in ui_list:
                        tb["unique_index"].insert(ui)
                if i_list:
                    for i in i_list:
                        tb["index"].insert(i)

                return 0

            else:
                return 3

        else:
            return 2

    except Exception:
        print("=" * 30)
        traceback.print_exc()
        return 1


# ===============================//=====================================
#                     ADMINISTRACION DE INDICES

def alterTableAddFK(database: str, table: str, indexName: str, columns: list, tableRef: str, columnsRef: list) -> int:
    """Adds a foreign key to a table

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table with the foreign key
            indexName (str): name of the foreign key
            columns (str): columns of the foreign key
            tableRef (str): name of the table the foreign key refers to
            columnsRef (str): columns the foreign key refers to

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-existent table, non-existent refering table
            4: columns lenght are different
            5: tables data incompatible            
    """

    bd = _database(database)

    if bd:

        tb = _table(database, table)
        tb_r = _table(database, tableRef)

        if tb and tb_r:

            if len(columns) != len(columnsRef):
                return 4

            # registros=extractTable(database, table) # Partida
            # registros_r=extractTable(database, tableRef) # Usuarios

            # for i in range(len(columns)):

            #     columna, columna_r = [], []

            #     for registro in registros:
            #         columna.append(registro[columns[i]])

            #     for registro in registros_r:
            #         columna_r.append(registro[columnsRef[i]])

            #     for valor in columna:
            #         if valor not in columna_r:
            #             return 5

            tb["foreign_keys"].insert([indexName, table, tableRef, columns, columnsRef])
            return 0

        else:
            return 3

    else:
        return 2


def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    """ Deletes a foreign key

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table with the foreign key
            indexName (str): name of the foreign key

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent foreign key
    """

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            fk = _foreign_key(database, table, indexName)

            if fk:
                return tb["foreign_keys"].delete(indexName)

            else:
                return 4

        else:
            return 3

    else:
        return 2


def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    """Adds an unique index to a table

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table with the unique index
            indexName (str): name of the unique index
            columns (str): columns of the unique index

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: duplicate value
    """

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            if not _Comprobar_unique(database, table, columns):
                return 4

            tb["unique_index"].insert([indexName, table, columns])
            return 0

        else:
            return 3

    else:
        return 2


def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    """ Deletes an unique index

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table with the unique index
            indexName (str): name of the unique index

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent unique index
    """

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            ui = _unique_index(database, table, indexName)

            if ui:
                return tb["unique_index"].delete(indexName)

            else:
                return 4

        else:
            return 3

    else:
        return 2


def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    """Adds an index to a table

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table with the index
            indexName (str): name of the index
            columns (str): columns of the index

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-existent table       
    """

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            tb["index"].insert([indexName, table, columns])
            return 0

        else:
            return 3

    else:
        return 2


def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    """ Deletes an index

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table with the index
            indexName (str): name of the index

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent index
    """

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            i = _index(database, table, indexName)

            if i:
                return tb["index"].delete(indexName)

            else:
                return 4

        else:
            return 3

    else:
        return 2


# ===============================//=====================================
#                      ADMINISTRACION DE CODIFICACION

def alterDatabaseEncoding(database: str, encoding: str) -> int:
    """Changes a database encoding

        Pararameters:\n
            database (str): name of the database
            encoding (str): new database encoding

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-valid encoding
    """

    bd = _database(database)

    if bd:
        if encoding not in ["utf8", "ascii", "iso-8859-1"]:
            return 3
        else:
            bd["encoding"] = encoding
            try:
                table = bd["tablas"]
                for t in table:
                    val = extractTable(database, t['nombre'])
                    if len(val):
                        for x in val:
                            for y in x:
                                if type(y) == str:
                                       y.encode(encoding, "strict")
                                       
                return 0
            except:
                return 1
    else:
        return 2


# ===============================//=====================================
#                      ADMINISTRACION DE CHECKSUM

def checksumDatabase(database: str, mode: str) -> str:
    """Generates a database checksum

        Pararameters:\n
            database (str): name of the database
            mode (str): checksum hash algorithm

        Returns:\n
            str: operation successful
            None: an error ocurred, non-existent database, non-valid checksum mode
    """

    bd = _database(database)

    if bd:

        if mode not in ["MD5", "SHA256"]:
            return None

        return ch.checksumDatabase(database,mode)

    else:
        return None


def checksumTable(database: str, table: str, mode: str) -> str:
    """Generates a table checksum

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table
            mode (str): checksum hash algorithm

        Returns:\n
            str: operation successful
            None: an error ocurred, non-existent database, non-existent table, non-valid checksum mode
    """

    bd = _database(database)

    if bd:

        tb = _table(database, table)

        if tb:

            if mode not in ["MD5", "SHA256"]:
                return None            

            return ch.checksumTable(database, table, mode)

        else:
            return None

    else:
        return None


# ===============================//=====================================
#                      ADMINISTRACION DE COMPRESION

def alterDatabaseCompress(database: str, level: int) -> int:
    """Compresses a database

        Pararameters:\n
            database (str): name of the database
            level (int): compression level

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            4: non-valid level
    """

    bd = _database(database)

    if bd:

        if level > 0 and level < 10:
            try:
                table = bd["tablas"]
                for t in table:
                    val = extractTable(database, t['nombre'])
                    truncate(database, t['nombre'])
                    if len(val):
                        for x in val:
                            for y in x:
                                if type(y) == str:
                                    try:
                                        i = x.index(y)
                                        x[i] = zlib.compress(y.encode(), level).hex()
                                    except:
                                        return 1
                            insert(database, t['nombre'], x)
                bd["compress"] = True
                bd["level"] = level

                return 0
            except:
                return 1
        else:
            return 3
    else:
        return 2


def alterDatabaseDecompress(database: str) -> int:
    """Decompresses a database

        Pararameters:\n
            database (str): name of the database

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            4: non-existent compression
    """

    bd = _database(database)

    if bd:
        com = bd["compress"]
        if com:
            try:
                table = bd["tablas"]
                for t in table:
                    val = extractTable(database, t['nombre'])
                    truncate(database, t['nombre'])
                    
                    if len(val):
                        for x in val:
                            for y in x:
                                if type(y) == str:
                                    try:
                                        i = x.index(y)
                                        x[i] = zlib.decompress(bytes.fromhex(y)).decode()
                                    except:
                                        return 1
                            insert(database, t['nombre'], x)
                bd["compress"] = False

                return 0
                
            except:
                return 1
        else:
            return 3
    else:
        return 2


def alterTableCompress(database: str, table: str, level: int) -> int:
    """Compresses a table

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table
            level (int): compression level

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-valid level
    """

    bd = _database(database)

    if bd:
        if level > 0 and level < 10:

            tb = _table(database, table)

            if tb:
                com = tb["compress"]
                tb["level"] = level

                if not com:
                    try:
                        val = _extractTable(database, tb['nombre'], tb["modo"])
                        truncate(database, tb['nombre'])
                        if len(val):
                            for x in val:
                                for y in x:
                                    if type(y) == str:
                                        try:
                                            i = x.index(y)
                                            x[i] = zlib.compress(y.encode(), level).hex()
                                        except:
                                            return 1
                                insert(database, tb['nombre'], x)
                        tb["compress"] = True
                        tb["level"] = level

                        return 0
                    except:
                        return 1
                else:
                    return 1
            else:
                return 3        
        else:
            return 4
    else:
        return 2


def alterTableDecompress(database: str, table: str) -> int:
    """Decompresses a table

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: operation successful
            1: an error ocurred
            2: non-existent database
            3: non-existent compression
    """

    bd = _database(database)

    if bd:
        tb = _table(database, table)
        
        if tb:
            com = tb["compress"]
            
            if com:
                try:
                    val = _extractTable(database, tb['nombre'], tb["modo"])
                    truncate(database, tb['nombre'])
                    
                    if len(val):
                        for x in val:
                            for y in x:
                                if type(y) == str:
                                    try:
                                        i = x.index(y)
                                        x[i] =zlib.decompress(bytes.fromhex(y)).decode()
                                    except:
                                        return 1
                            insert(database, tb['nombre'], x)
                    tb["compress"] = False
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 1
    else:
        return 2

# ===============================//=====================================
#                      ADMINISTRACION DE SEGURIDAD

def encrypt(backup: str, password: str) -> str:
    """Encrypts a database backup

        Pararameters:\n
            backup (str): name of the database backup
            password (str): encrypting password

        Returns:\n
            str: cryptogram of the encryption
            None: an error ocurred
    """

    try:
        return comp.encriptar(backup, password)

    except:
        return None


def decrypt(cipherBackup: str, password: str) -> str:
    """Encrypts a database backup

        Pararameters:\n
            cipherBackup (str): name of the database backup
            password (str): encrypting password

        Returns:\n
            str: decrypted text
            None: an error ocurred
    """

    try:
        return comp.desencriptar(cipherBackup, password)

    except:
        return None


def safeModeOn(database: str, table: str) -> int:
    """Enables safe mode for a table in a database

            Pararameters:\n
                database (str): name of the database
                table (str): name of the table

            Returns:\n
                0: successful operation
                1: an error ocurred
                2: non-existent database
                3: non-existent table
                4: existing safe mode
        """
    nombreST = str(database) + '-' + str(table)
    if not _database(database):
        return 2

    if not _table(database, table):
        return 3

    if BC.EsUnaTablaSegura(nombreST, _main_path):
        return 4

    try:
        BC.CreateBlockChain(nombreST, _main_path)
        return 0
    except:
        return 1


def safeModeOff(database: str, table: str) -> int:
    """Disables safe mode for a table in a database

            Pararameters:\n
                database (str): name of the database
                table (str): name of the table

            Returns:\n
                0: successful operation
                1: an error ocurred
                2: non-existent database
                3: non-existent table
                4: non-existent safe mode
        """

    nombreST = str(database) + '-' + str(table)

    if not _database(database):
        return 2

    if not _table(database, table):
        return 3

    if not BC.EsUnaTablaSegura(nombreST, _main_path):
        return 4

    try:
        BC.DeleteSafeTable(nombreST, _main_path)
        return 0
    except:
        return 1

        
# ===============================//=====================================
#                      GENERACIÓN DE GRAFOS

def graphTable(database: str, table: str):
    """Graphs a table inner structure

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            str: successful operation
            None: non-existent database, an error ocurred
    """

    try:

        mode = _table(database, table)["modo"]

        if mode == "avl":

            avl._Cargar(database, table)

        elif mode == "b":

            b._Cargar(database, table)

        elif mode == "bplus":

            bplus._Cargar(database, table)

        if mode == "hash":

            hash._Cargar(database, table)

        elif mode == "isam":

            isam._Cargar(database, table)

        return _main_path+"\\graph\\"+mode+".png"

    except:
        return None


def graphSafeTable(database: str, table: str) -> int:
    """Graphs a table blockchain diagram

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            str: successful operation
            None: non-existent database, an error ocurred
    """

    try:

        nombreST = str(database) + '-' + str(table)
        BC.GraphSafeTable(nombreST, _main_path)

        return _main_path+"\\graph\\BlockChain.png"

    except:
        return None


def graphDSD(database: str) -> int:
    """Graphs a database ERD

        Pararameters:\n
            database (str): name of the database

        Returns:\n
            0: successful operation
            None: non-existent database, an error ocurred
    """

    db = _database(database)

    if db:
        return graph.graphDSD(database)

    else:
        return None


def graphDF(database: str, table: str) -> int:
    """Graphs a table s functional dependencies

        Pararameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            None: non-existent database, an error ocurred
    """

    db = _database(database)

    if db:
        return graph.graphDF(database,table)

    else:
        return None
