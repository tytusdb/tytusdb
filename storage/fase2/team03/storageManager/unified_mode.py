from storage.avl import avl_mode as avl
from storage.b import b_mode as b
from storage.bplus import bplus_mode as bplus
from storage.dict import dict_mode as d
from storage.hash import hash_mode as ha
from storage.isam import isam_mode as isam
from storage.json import json_mode as j

import pickle
import os
import zlib
import hashlib

from storageManager.server import encriptar as enc
from storageManager.server import desencriptar as des
from storageManager.server import blockChain as blockC
from storageManager import indexManager as indexM

#############
# Utilities #
#############

#Variable que valida si el deserializado esta activo
global deserializadoActivado
deserializadoActivado = False

# GUARDAR ARCHIVO
def __commit(objeto, nombre):
    file = open(nombre+".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()

# ABRIR EL ARCHIVO
def __rollback(nombre):
    file = open(nombre+".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)

def __getDatabase(database):
    if os.path.exists("data.bin"):
        listaDB = __rollback("data")

        for db in listaDB:
            if db["nameDb"].lower() == database.lower():
                # Retorna el diccionario de la base de datos
                return db

        return False
    else:
        data = []
        __commit(data, "data")
        return False

def __getTable(database, table):
    # Extraer la base de datos especificada
    dbBuscada = __getDatabase(database)

    if dbBuscada:
        for tb in dbBuscada["tables"]:
            if tb["nameTb"].lower() == table.lower():
                # Retorna el diccionario de la tabla especificada
                return tb

    return False

##################
# Databases CRUD #
##################

def createDatabase(database: str, mode: str, encoding="ascii") -> int:
    try:
        if not database.isidentifier() \
                or not mode.isidentifier() \
                or not encoding.isidentifier():
            raise Exception()

        if encoding != "utf8" and encoding != "ascii" and encoding != "iso-8859-1":
            return 4

        # Retorna el diccionario de una base de datos especifica
        dbBuscada = __getDatabase(database)
        estado = 0

        if dbBuscada is False:

            if mode == "avl":
                estado = avl.createDatabase(database)
            elif mode == "b":
                estado = b.createDatabase(database)
            elif mode == "bplus":
                estado = bplus.createDatabase(database)
            elif mode == "hash":
                estado = ha.createDatabase(database)
            elif mode == "isam":
                estado = isam.createDatabase(database)
            elif mode == "json":
                estado = j.createDatabase(database)
            elif mode == "dict":
                estado = d.createDatabase(database)
            else:
                return 3
        else:
            return 2

        if estado == 0:
            if deserializadoActivado is False:
                # Pedir la lista de diccionarios de base de datos
                listaDB = __rollback("data")
                listaDB.append({"nameDb": database, "mode": mode,
                                "encoding": encoding, "tables": []})
                # Se guarda la nueva base de datos en el archivo data
                __commit(listaDB, "data")

        return estado
    except:
        return 1

def showDatabases() -> list:
    try:
        databases = []
        listaDB = __rollback("data")

        for db in listaDB:
            databases.append(db["nameDb"])

        return databases
    except:
        return []

def alterDatabase(databaseOld: str, databaseNew: str) -> int:
    try:
        if not databaseOld.isidentifier() or not databaseNew.isidentifier():
            raise Exception()

        dbBuscada = __getDatabase(databaseOld)

        if dbBuscada is False:
            return 2

        dbNew = __getDatabase(databaseNew)
        if dbNew:
            return 3

        mode = dbBuscada["mode"]

        estado = 1

        if mode == "avl":
            estado = avl.alterDatabase(databaseOld, databaseNew)
        elif mode == "b":
            estado = b.alterDatabase(databaseOld, databaseNew)
        elif mode == "bplus":
            estado = bplus.alterDatabase(databaseOld, databaseNew)
        elif mode == "hash":
            estado = ha.alterDatabase(databaseOld, databaseNew)
        elif mode == "isam":
            estado = isam.alterDatabase(databaseOld, databaseNew)
        elif mode == "json":
            estado = j.alterDatabase(databaseOld, databaseNew)
        elif mode == "dict":
            estado = d.alterDatabase(databaseOld, databaseNew)

        if estado == 0:
            # Pedir la lista de diccionarios de base de datos
            listaDB = __rollback("data")

            for db in listaDB:
                if db["nameDb"] == databaseOld:
                    db["nameDb"] = databaseNew
                    break

            # Se guarda la base de datos ya actualizada en el archivo data
            __commit(listaDB, "data")

        return estado

    except:
        return 1

def dropDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        
        dbBuscada = __getDatabase(database)

        if dbBuscada is False:
            return 2
        
        mode = dbBuscada["mode"]

        estado = 1

        if mode == "avl":
            estado = avl.dropDatabase(database)
        elif mode == "b":
            estado = b.dropDatabase(database)
        elif mode == "bplus":
            estado = bplus.dropDatabase(database)
        elif mode == "hash":
            estado = ha.dropDatabase(database)
        elif mode == "isam":
            estado = isam.dropDatabase(database)
        elif mode == "json":
            estado = j.dropDatabase(database)
        elif mode == "dict":
            estado = d.dropDatabase(database)

        if estado == 0:
            # Pedir la lista de diccionarios de base de datos
            listaDB = __rollback("data")
            # Remover el diccionario de base de datos de la lista
            listaDB.remove(dbBuscada)

            # Se guarda la lista de base de datos ya actualizada en el archivo data
            __commit(listaDB, "data")

        return estado
    except:
        return 1 

###############
# Tables CRUD #
###############

def createTable(database: str, table: str, numberColumns: int) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(numberColumns, int):
            raise Exception()

        dbBuscada = __getDatabase(database)
        if dbBuscada is False:
            return 2
        
        tbBuscada = __getTable(database, table)
        if tbBuscada:
            return 3
        
        mode = dbBuscada["mode"]
        return __createTable(database, table, numberColumns, mode)
    except:
        return 1

def __createTable(database, table, numberColumns, mode):
    estado = 1

    if mode == "avl":
        estado = avl.createTable(database, table, numberColumns)
    elif mode == "b":
        estado = b.createTable(database, table, numberColumns)
    elif mode == "bplus":
        estado = bplus.createTable(database, table, numberColumns)
    elif mode == "hash":
        estado = ha.createTable(database, table, numberColumns)
    elif mode == "isam":
        estado = isam.createTable(database, table, numberColumns)
    elif mode == "json":
        estado = j.createTable(database, table, numberColumns)
    elif mode == "dict":
        estado = d.createTable(database, table, numberColumns)

    if estado == 0:
        # Pedir la lista de diccionarios de base de datos
        listaDB = __rollback("data")

        for db in listaDB:
            if db["nameDb"] == database:
                db["tables"].append({"nameTb": table, "mode": mode, "columns": numberColumns, "pk": [],
                                    "foreign_keys": indexM.indexManager(mode, database, table, 5, "fk"),
                                    "unique_index": indexM.indexManager(mode, database, table, 3, "un"),
                                    "index": indexM.indexManager(mode, database, table, 3, "in"),
                                    "registros": [], "registrosFk": [], "registrosUn": [], "registrosIn": [],
                                    "Bandera": False})
                break

        # Se guarda la lista de base de datos ya actualizada en el archivo data
        __commit(listaDB, "data")

    return estado

def showTables(database: str) -> list:
    try:
        if not database.isidentifier():
            raise Exception()
        
        tables = []        
        
        dbBuscada = __getDatabase(database)
        if dbBuscada is False:
            return None
        
        for tb in dbBuscada["tables"]:
            tables.append(tb["nameTb"])

        return tables
    except:
        return []

def extractTable(database: str, table: str) -> list:
    try:
        rows = []
        
        dbBuscada = __getDatabase(database)
        if dbBuscada is False:
            return None
        
        tbBuscada = __getTable(database, table)
        if tbBuscada is False:
            return None
        
        mode = tbBuscada["mode"]

        if mode == "avl":
            rows = avl.extractTable(database, table)
        elif mode == "b":
            rows = b.extractTable(database, table)
        elif mode == "bplus":
            rows = bplus.extractTable(database, table)
        elif mode == "hash":
            rows = ha.extractTable(database, table)
        elif mode == "isam":
            rows = isam.extractTable(database, table)
        elif mode == "json":
            rows = j.extractTable(database, table)
        elif mode == "dict":
            rows = d.extractTable(database, table)

        return rows
    except:
        return None

def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    try:
        rows = []

        dbBuscada = __getDatabase(database)
        if dbBuscada is False:
            return None
        
        tbBuscada = __getTable(database, table)
        if tbBuscada is False:
            return None
        
        mode = tbBuscada["mode"]

        if mode == "avl":
            rows = avl.extractRangeTable(database, table, columnNumber, lower, upper)
        elif mode == "b":
            rows = b.extractRangeTable(database, table, columnNumber, lower, upper)
        elif mode == "bplus":
            rows = bplus.extractRangeTable(database, table, columnNumber, lower, upper)
        elif mode == "hash":
            rows = ha.extractRangeTable(database, table, columnNumber, lower, upper)
        elif mode == "isam":
            rows = isam.extractRangeTable(database, table, columnNumber, lower, upper)
        elif mode == "json":
            rows = j.extractRangeTable(database, table, lower, upper)
        elif mode == "dict":
            rows = d.extractRangeTable(database, table, columnNumber, lower, upper)
        
        return rows
    except:
        return None

def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(columns, list):
            raise Exception()
        
        dbBuscada = __getDatabase(database)
        if dbBuscada is False:
            return 2
        
        tbBuscada = __getTable(database, table)
        if tbBuscada is False:
            return 3
        
        mode = tbBuscada["mode"]

        estado = 1

        if mode == "avl":
            estado = avl.alterAddPK(database, table, columns)
        elif mode == "b":
            estado = b.alterAddPK(database, table, columns)
        elif mode == "bplus":
            estado = bplus.alterAddPK(database, table, columns)
        elif mode == "hash":
            estado = ha.alterAddPK(database, table, columns)
        elif mode == "isam":
            estado = isam.alterAddPK(database, table, columns)
        elif mode == "json":
            estado = j.alterAddPK(database, table, columns)
        elif mode == "dict":
            estado = d.alterAddPK(database, table, columns)

        if estado == 0:
            if deserializadoActivado is False:
                # Pedir la lista de diccionarios de base de datos
                listaDB = __rollback("data")

                for db in listaDB:
                    if db["nameDb"] == database:
                        for tb in db["tables"]:
                            if tb["nameTb"] == table:
                                tb["pk"] = columns
                                break

                # Se guarda la lista de base de datos ya actualizada en el archivo data
                __commit(listaDB, "data")

        return estado
    except:
        return 1

def alterDropPK(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()
        
        dbBuscada = __getDatabase(database)
        if dbBuscada is False:
            return 2
        
        tbBuscada = __getTable(database, table)
        if tbBuscada is False:
            return 3
        
        mode = tbBuscada["mode"]

        estado = 1

        if mode == "avl":
            estado = avl.alterDropPK(database, table)
        elif mode == "b":
            estado = b.alterDropPK(database, table)
        elif mode == "bplus":
            estado = bplus.alterDropPK(database, table)
        elif mode == "hash":
            estado = ha.alterDropPK(database, table)
        elif mode == "isam":
            estado = isam.alterDropPK(database, table)
        elif mode == "json":
            estado = j.alterDropPK(database, table)
        elif mode == "dict":
            estado = d.alterDropPK(database, table)

        if estado == 0:
            # Pedir la lista de diccionarios de base de datos
            listaDB = __rollback("data")

            for db in listaDB:
                if db["nameDb"] == database:
                    for tb in db["tables"]:
                        if tb["nameTb"] == table:
                            tb["pk"] = []
                            break

            # Se guarda la lista de base de datos ya actualizada en el archivo data
            __commit(listaDB, "data")

        return estado
    except:
        return 1

###################################### SARAI ######################################