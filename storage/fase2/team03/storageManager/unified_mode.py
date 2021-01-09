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

def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    try:
        if not database.isidentifier() \
        or not tableOld.isidentifier() \
        or not tableNew.isidentifier():
            raise Exception()

        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2

        tabla = __getTable(database, tableOld)
        if tabla is False:
            return 3

        existe = __getTable(database, tableNew)
        if existe:
            return 4

        # Fase 2
        modo = tabla["mode"]

        res = 1  # esperando que la respuesta sea exitosa

        if modo == "avl":
            res = avl.alterTable(database, tableOld, tableNew)
        elif modo == "b":
            res = b.alterTable(database, tableOld, tableNew)
        elif modo == "bplus":
            res = bplus.alterTable(database, tableOld, tableNew)
        elif modo == "hash":
            res = ha.alterTable(database, tableOld, tableNew)
        elif modo == "isam":
            res = isam.alterTable(database, tableOld, tableNew)
        elif modo == "json":
            res = j.alterTable(database, tableOld, tableNew)
        elif modo == "dict":
            res = d.alterTable(database, tableOld, tableNew)

        if res == 0:  # fue satisfactoria la operacion
            # Pedir la lista de diccionarios de base de datos
            listaDB = __rollback("data")

            for db in listaDB:
                if db["nameDb"] == database:
                    for tb in db["tables"]:
                        if tb["nameTb"] == tableOld:
                            tb["foreign_keys"].alterTable(tableNew)
                            tb["unique_index"].alterTable(tableNew)
                            tb["index"].alterTable(tableNew)
                            tb["nameTb"] = tableNew
                            break

            # Se guarda la lista de base de datos ya actualizada en el archivo data
            __commit(listaDB, "data")
        
        return res
    except:
        return 1

def alterAddColumn(database: str, table: str, default: any) -> int:
    try:
        if not database.isidentifier() \
                or not table.isidentifier():
            raise Exception()

        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2

        tabla = __getTable(database, table)
        if tabla is False:
            return 3

        # Fase 2
        modo = tabla["mode"]

        res = 1

        if modo == "avl":
            res = avl.alterAddColumn(database, table, default)
        elif modo == "b":
            res = b.alterAddColumn(database, table, default)
        elif modo == "bplus":
            res = bplus.alterAddColumn(database, table, default)
        elif modo == "hash":
            res = ha.alterAddColumn(database, table, default)
        elif modo == "isam":
            res = isam.alterAddColumn(database, table, default)
        elif modo == "json":
            res = j.alterAddColumn(database, table, default)
        elif modo == "dict":
            res = d.alterAddColumn(database, table, default)

        if res == 0:
            # Pedir la lista de diccionarios de base de datos
            listaDB = __rollback("data")

            for db in listaDB:
                if db["nameDb"] == database:
                    for tb in db["tables"]:
                        if tb["nameTb"] == table:
                            columnasNew = tb["columns"] + 1
                            tb["columns"] = columnasNew
                            break

            # Se guarda la lista de base de datos ya actualizada en el archivo data
            __commit(listaDB, "data")

        return res
    except:
        return 1

def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(columnNumber, int):
            raise Exception()

        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2

        tabla = __getTable(database, table)
        if tabla is False:
            return 3

        modo = tabla["mode"]

        res = 1

        if modo == "avl":
            res = avl.alterDropColumn(database, table, columnNumber)
        elif modo == "b":
            res = b.alterDropColumn(database, table, columnNumber)
        elif modo == "bplus":
            res = bplus.alterDropColumn(database, table, columnNumber)
        elif modo == "hash":
            res = ha.alterDropColumn(database, table, columnNumber)
        elif modo == "isam":
            res = isam.alterDropColumn(database, table, columnNumber)
        elif modo == "json":
            res = j.alterDropColumn(database, table, columnNumber)
        elif modo == "dict":
            res = d.alterDropColumn(database, table, columnNumber)

        if res == 0:
            # Pedir la lista de diccionarios de base de datos
            listaDB = __rollback("data")

            for db in listaDB:
                if db["nameDb"] == database:
                    for tb in db["tables"]:
                        if tb["nameTb"] == table:
                            columnasNew = tb["columns"] - 1
                            tb["columns"] = columnasNew
                            break

            # Se guarda la lista de base de datos ya actualizada en el archivo data
            __commit(listaDB, "data")

        return res
    except:
        return 1

def dropTable(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()

        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2

        tabla = __getTable(database, table)
        if tabla is False:
            return 3

        # Fase2
        mode = tabla["mode"]

        res = 1

        if mode == "avl":
            res = avl.dropTable(database, table)
        elif mode == "b":
            res = b.dropTable(database, table)
        elif mode == "bplus":
            res = bplus.dropTable(database, table)
        elif mode == "hash":
            res = ha.dropTable(database, table)
        elif mode == "isam":
            res = isam.dropTable(database, table)
        elif mode == "json":
            res = j.dropTable(database, table)
        elif mode == "dict":
            res = d.dropTable(database, table)

        if res == 0:
            # Pedir la lista de diccionarios de base de datos
            listaDB = __rollback("data")

            #Se eliminan los registros de las estructuras correspondientes a
            #FK, indice unico, indice
            for db in listaDB:
                if db["nameDb"] == database:
                    for tb in db["tables"]:
                        if tb["nameTb"] == table:
                            tb["foreign_keys"].dropTable()
                            tb["unique_index"].dropTable()
                            tb["index"].dropTable()
                            break

            #Se elimina el diccionario correspondiente a la tabla del archivo data
            for db in listaDB:
                if db["nameDb"] == database:
                    db["tables"].remove(tabla)
                    break

            # Se guarda la lista de base de datos ya actualizada en el archivo data
            __commit(listaDB, "data")

        return res   
    except:
        return 1


##################
# Registers CRUD #
##################

def insert(database: str, table: str, register: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(register, list):
            raise Exception()        
        
        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2

        tabla = __getTable(database, table)
        if tabla is False:
            return 3

        mode = tabla["mode"]

        res = 1

        if mode == "avl":
            res = avl.insert(database, table, register)
        elif mode == "b":
            res = b.insert(database, table, register)
        elif mode == "bplus":
            res = bplus.insert(database, table, register)
        elif mode == "hash":
            res = ha.insert(database, table, register)
        elif mode == "isam":
            res = isam.insert(database, table, register)
        elif mode == "json":
            res = j.insert(database, table, register)
        elif mode == "dict":
            res = d.insert(database, table, register)

        if res == 0:
            # ************* Modificar *********************
            nombreTablaSegura = database + '-' + table
            if blockC.EsUnaTablaSegura(nombreTablaSegura):
                blockC.insertSafeTable(nombreTablaSegura, register)
            # ************* Modificar *********************
        return res      
    except:
        return 1

def loadCSV(filepath: str, database: str, table: str) -> list:
    try:
        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return []

        tabla = __getTable(database, table)
        if tabla is False:
            return []

        mode = tabla["mode"]

        res = 1

        if mode == "avl":
            res = avl.loadCSV(filepath, database, table)
        elif mode == "b":
            res = b.loadCSV(filepath, database, table)
        elif mode == "bplus":
            res = bplus.loadCSV(filepath, database, table)
        elif mode == "hash":
            res = ha.loadCSV(filepath, database, table)
        elif mode == "isam":
            res = isam.loadCSV(filepath, database, table)
        elif mode == "json":
            res = j.loadCSV(filepath, database, table)
        elif mode == "dict":
            res = d.loadCSV(filepath, database, table)

        if 0 in res:
            nombreTablaSegura = database + '-' + table
            # ************* Modificar *********************
            if blockC.EsUnaTablaSegura(nombreTablaSegura):
                blockC.insertCSV(nombreTablaSegura, filepath, res)
            # ************* Modificar *********************
        return res 
    except:
        return []

def extractRow(database: str, table: str, columns: list) -> list:
    try:
        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return []

        tabla = __getTable(database, table)
        if tabla is False:
            return []
       
        mode = tabla["mode"]

        res = 1

        if mode == "avl":
            res = avl.extractRow(database, table, columns)
        elif mode == "b":
            res = b.extractRow(database, table, columns)
        elif mode == "bplus":
            res = bplus.extractRow(database, table, columns)
        elif mode == "hash":
            res = ha.extractRow(database, table, columns)
        elif mode == "isam":
            res = isam.extractRow(database, table, columns)
        elif mode == "json":
            res = j.extractRow(database, table, columns)
        elif mode == "dict":
            res = d.extractRow(database, table, columns)

        return res
    except:
        return []

def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()        
        
        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2

        tabla = __getTable(database, table)
        if tabla is False:
            return 3

        # Fase2
        # ************* Modificar *********************
        datosAntiguos = False
        nombreTablaSegura = database + '-' + table
        if blockC.EsUnaTablaSegura(nombreTablaSegura):
            datosAntiguos = extractRow(database, table, columns)
        # ************* Modificar *********************

        mode = tabla["mode"]

        res = 1

        if mode == "avl":
            res = avl.update(database, table, register, columns)
        elif mode == "b":
            res = b.update(database, table, register, columns)
        elif mode == "bplus":
            res = bplus.update(database, table, register, columns)
        elif mode == "hash":
            res = ha.update(database, table, register, columns)
        elif mode == "isam":
            res = isam.update(database, table, register, columns)
        elif mode == "json":
            res = j.update(database, table, register, columns)
        elif mode == "dict":
            res = d.update(database, table, register, columns)

        if res == 0:
            # ************* Modificar *********************
            if datosAntiguos:
               blockC.updateSafeTable(nombreTablaSegura, datosAntiguos, extractRow(database, table, columns))
            # ************* Modificar *********************        
        return res
    except:
        return 1

def delete(database: str, table: str, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()        
        
        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2

        tabla = __getTable(database, table)
        if tabla is False:
            return 3
       
        mode = tabla["mode"]

        res = 1

        if mode == "avl":
            res = avl.delete(database, table, columns)
        elif mode == "b":
            res = b.delete(database, table, columns)
        elif mode == "bplus":
            res = bplus.delete(database, table, columns)
        elif mode == "hash":
            res = ha.delete(database, table, columns)
        elif mode == "isam":
            res = isam.delete(database, table, columns)
        elif mode == "json":
            res = j.delete(database, table, columns)
        elif mode == "dict":
            res = d.delete(database, table, columns)

        return res
    except:
        return 1

def truncate(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        
        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2

        tabla = __getTable(database, table)
        if tabla is False:
            return 3
        
        mode = tabla["mode"]

        res = 1
        
        if mode == "avl":
            res = avl.truncate(database, table)
        elif mode == "b":
            res = b.truncate(database, table)
        elif mode == "bplus":
            res = bplus.truncate(database, table)
        elif mode == "hash":
            res = ha.truncate(database, table)
        elif mode == "isam":
            res = isam.truncate(database, table)
        elif mode == "json":
            res = j.truncate(database, table)
        elif mode == "dict":
            res = d.truncate(database, table)

        return res       
    except:
        return 1


##################
#   MODE CRUD    #
##################

def alterDatabaseMode(database: str, mode: str) -> int:
    try:
        # se comprueba el modo
        modos = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
        if mode not in modos:
            return 4
        else:
            # se llama a la base de datos
            bdata = __getDatabase(database)

            if bdata:
                # se extrae el modo si es igual, se deja igual 
                if bdata["mode"] == mode:
                    return 4
                
                # se extrae un listado de tablas
                #tablas = []
                #for t in bdata.get("tables"):
                    #tablas.append(t.get("nombretb"))
                tablas = showTables(database)
                
                # se extrae el los registros de las tablas
                newdata=[]
                if len(tablas) != 0:
                    
                    for nombreTb in tablas:
                        newdata.append([nombreTb, extractTable(database, nombreTb)])                          ##### EXTRACTTABLE
                
                # se elimina la base de datos 
                dropDatabase(database)   
                # se crea la nueva base de datos en el modo respectivo                                                       ##### DROPDATABASE
                createDatabase(database , mode, bdata["encoding"])

                for t in newdata:
                    createTable(database, __getTable(database, t[0]).get("nameTb"), __getTable(database, t[0]).get("columns"))   #### _table             ##### CREATETABLE
                    alterAddPK(database , __getTable(database, t[0]).get("nameTb"), __getTable(database, t[0]).get("pk"))                      ##### ALTERADDPK

                    # INSERTAR LOS REGISTROS EN LA NUEVA ESTRUCTURA
                    for reg in newdata[1]:
                        insert(database, __getTable(database, t[0]).get("nameTb"), reg)                   ##### INSERT 
                
                return 0
            else:
                return 2           
    except:
        return 1

def alterTableMode(database: str, table: str, mode: str) -> int:
    try:
        # se comprueba el modo
        modos = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
        if mode not in modos:
            return 4
        else:
            # se llama a la base de datos
            bdata= __getDatabase(database)

            if bdata:
               
                # se extrae la tabla buscada
                #tabla =[]
                #for t in bdata.get("tables"):
                    #if t.get("nameTb") == table:
                        #tabla.append(t.get("nombretb"))
                
                # obtener diccionario de la tabla especifica
                tabla = __getTable(database, table)

                if tabla is False:
                    return 3
                
                # se extrae el modo de la tabla  si es igual, se deja igual 
                if tabla["mode"] == mode:
                    return 4
                
                # se extrae el los registros de la tabla
                newdata = extractTable(database, tabla["nameTb"])

                # se elimina la base tabla 
                dropTable(database, table)                                                       ##### DROPDATABASE
                
                # se crea la nueva tabla
                __createTable(database, table, tabla["columns"], mode)
                alterAddPK(database, tabla.get("nameTb"), tabla.get("pk"))

                # se ingresan los nuevos registros
                for reg in newdata:
                    insert(database, table, reg)
                
                # obtener diccionario de la tabla con el nuevo modo
                tabla = __getTable(database, table)

                tabla["foreign_keys"].alterTableMode(mode)
                tabla["unique_index"].alterTableMode(mode)
                tabla["index"].alterTableMode(mode)

                return 0
            else:
                return 2           
    except:
        return 1


def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
    try:
        # se llama a la base de datos
        bdata= __getDatabase(database)

        if bdata:

            # se extrae la tabla buscada y la tabla de referencia
            tablafk = __getTable(database, table)
            tablarf = __getTable(database, tableRef)

            #for t in bdata.get("tables"):
                #if t.get("nameTb") == table:
                    #tablafk  = t.get("nameTb")
                #if  t.get("nameTb") == tableRef:
                    #tablarf  = t.get("nameTb")
            
            # se comprueba la existencia de las tablas
            if len(tablafk) == 0 or len(tablarf) == 0: #tablafk != False or tablarf != False:
                return 3
            # cantidad entre columns y columnsRef
            if len(columns) != len(columnsRef):
                return 4
            # se agrega la llave foranea
            tablafk["foreign_keys"].insert([indexName, table, tableRef, columns, columnsRef])

            #Se extraen los registros actualizados de la estructura Fk
            registrosFk = tablafk["foreign_keys"].extractTable()
            #Se guardan en el archivo data
            listaDB = __rollback("data")
            for db in listaDB:
                if db["nameDb"] == database:
                    for tb in db["tables"]:
                        if tb["nameTb"] == table:
                            tb["registrosFk"] = registrosFk
                            break
                
            #Se guarda la lista de base de datos actualizada en el archivo data
            __commit(listaDB, "data")
            return 0
        else:
            return 2
    except:
        return 1

def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    try:
        # se llama a la base de datos
        bdata= __getDatabase(database)

        if bdata:

            # se extrae la tabla buscada
            tabla = __getTable(database, table)

            #for t in bdata.get("tables"):
                #if t.get("nombretb") == table:
                    #tabla  = t.get("nombretb")

            # se comprueba la existencia de las tablas
            if tabla is False :
                return 3
           
            # se busca el indexname
            ForaneKey = tabla["foreign_keys"].extractRow(indexName)
            
            if ForaneKey:
                val = tabla["foreign_keys"].delete(indexName)

                #Se extraen los registros actualizados de la estructura Fk
                registrosFk = tabla["foreign_keys"].extractTable()
                #Se guardan en el archivo data
                listaDB = __rollback("data")
                for db in listaDB:
                    if db["nameDb"] == database:
                        for tb in db["tables"]:
                            if tb["nameTb"] == table:
                                tb["registrosFk"] = registrosFk
                                break
                    
                #Se guarda la lista de base de datos actualizada en el archivo data
                __commit(listaDB, "data")
                return val   # valor esperado: 0
            else:
                return 4
        else:
            return 2
    except:
        return 1



def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        # se llama a la base de datos
        bdata = __getDatabase(database)

        if bdata:
            # se extrae la tabla buscada y la tabla de referencia
            tabla = __getTable(database, table)
            #for t in bdata.get("tables"):
                #if t.get("nombretb") == table:
                    #tabla  = t.get("nombretb")

            # se comprueba la existencia de las tablas
            if tabla is False:
                return 3
            # se agrega el indice a la clase de indices
            tabla["unique_index"].insert([indexName, table, columns])

            #Se extraen los registros actualizados de la estructura Un
            registrosUn = tabla["unique_index"].extractTable()
            #Se guardan en el archivo data
            listaDB = __rollback("data")
            for db in listaDB:
                if db["nameDb"] == database:
                    for tb in db["tables"]:
                        if tb["nameTb"] == table:
                            tb["registrosUn"] = registrosUn
                            break
                
            #Se guarda la lista de base de datos actualizada en el archivo data
            __commit(listaDB, "data")
            return 0
        else:
            return 2
    except:
        return 1

def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    try:
        # se llama a la base de datos
        bdata= __getDatabase(database)

        if bdata:
            # se extrae la tabla buscada y la tabla de referencia
            tabla = __getTable(database, table)
            #for t in bdata.get("tables"):
                #if t.get("nombretb") == table:
                    #tabla  = t.get("nombretb")

            # se comprueba la existencia de las tablas
            if tabla is False:
                return 3
            # se busca el indexname
            unique_index= tabla["unique_index"].extractRow(indexName)
            
            if unique_index:
                val = tabla["unique_index"].delete(indexName)

                #Se extraen los registros actualizados de la estructura Unique
                registrosUn = tabla["unique_index"].extractTable()
                #Se guardan en el archivo data
                listaDB = __rollback("data")
                for db in listaDB:
                    if db["nameDb"] == database:
                        for tb in db["tables"]:
                            if tb["nameTb"] == table:
                                tb["registrosUn"] = registrosUn
                                break
                    
                #Se guarda la lista de base de datos actualizada en el archivo data
                __commit(listaDB, "data")
                return val    # valor esperado: 0
            else:
                return 4
        else:
            return 2
    except:
        return 1



def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        # se llama a la base de datos
        bdata= __getDatabase(database)

        if bdata:
            # se extrae la tabla buscada 
            tabla = __getTable(database, table)

            # se comprueba la existencia de las tablas
            if tabla is False:
                return 3
            # se agrega el indice a la clase de indices
            tabla["index"].insert([indexName, table, columns])

            #Se extraen los registros actualizados de la estructura Index
            registrosIn = tabla["index"].extractTable()
            #Se guardan en el archivo data
            listaDB = __rollback("data")
            for db in listaDB:
                if db["nameDb"] == database:
                    for tb in db["tables"]:
                        if tb["nameTb"] == table:
                            tb["registrosIn"] = registrosIn
                            break
                
            #Se guarda la lista de base de datos actualizada en el archivo data
            __commit(listaDB, "data")
            return 0
        else:
            return 2
    except:
        return 1

def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    try:
        bdata= __getDatabase(database)

        if bdata:
            # se extrae la tabla buscada
            tabla = __getTable(database, table)
            
            # se comprueba la existencia de las tablas
            if tabla is False:
                return 3

            # se busca el indexname
            index= tabla["index"].extractRow(indexName)
            
            if index:
                val = tabla["index"].delete(indexName)

                #Se extraen los registros actualizados de la estructura Index
                registrosIn = tabla["index"].extractTable()
                #Se guardan en el archivo data
                listaDB = __rollback("data")
                for db in listaDB:
                    if db["nameDb"] == database:
                        for tb in db["tables"]:
                            if tb["nameTb"] == table:
                                tb["registrosIn"] = registrosIn
                                break
                    
                #Se guarda la lista de base de datos actualizada en el archivo data
                __commit(listaDB, "data")
                return val    # valor esperado: 0
            else:
                return 4
        else:
            return 2
    except:
        return 1



##################
# COMPRESS CRUD  #
##################

# auxiliar para la eliminacion de una tabla solo en la estructura
def __dropTableaux(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()

        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return 2
        
        tabla = __getTable(database, table)
        if tabla is False:
            return 3

        # Fase2
        mode = tabla["mode"]

        res = 1
        if mode == "avl":
            res = avl.dropTable(database, table)
        elif mode == "b":
            res = b.dropTable(database, table)
        elif mode == "bplus":
            res = bplus.dropTable(database, table)
        elif mode == "hash":
            res = ha.dropTable(database, table)
        elif mode == "isam":
            res = isam.dropTable(database, table)
        elif mode == "json":
            res = j.dropTable(database, table)
        elif mode == "dict":
            res = d.dropTable(database, table)
        return res
    except:
        return 1

# funcion auxiliar para crear una tabla en una estructura
def __createTableaux(database, table, numberColumns, mode):
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
        
def alterDatabaseCompress(database: str, level: int) -> int:
    try:
        # se comprueba  que "level" == 0-9
        if level  in range(10):
            # llama la base de datos
            db =  __getDatabase(database) 
            if db:
                # se extrae el listado de tablas
                l_tablas= showTables(database)
                if l_tablas:
                    # se almacena en una lista el nombre de la tabla, las columnas de las llaves primarias y sus registros:
                    data = []
                    for tb in db.get("tables"):
                        # se comprueba que el metadato de la tabla sea False (False == no compreso)
                        if tb.get("Bandera") is False:
                            data.append([tb.get("nameTb"),tb.get("pk"),extractTable(database,tb.get("nameTb")),tb.get("mode"),tb.get("columns")])
                        else:
                            data = []
                            return 1
                    # se comprueba que la data no este vacia 
                    if data:
                        # se recorre cada  arrgelo de la data [nombreTabla, llave foranea,[data],mode,columns]
                        ntable =""
                        mode = ""
                        columns = 0
                        for nreg in data:
                            new_data =[] # almacena el nuevo regigstro con datos compresos
                            ntable=nreg[0]   #nombre de la tabla 
                            pk = nreg[1]        # llaves foranas
                            mode = nreg[3]
                            columns = nreg[4]
                            # se comprime cada columna de los registros en la lista new_data:
                            contador = 0
                            for old_data in nreg[2]:
                                # se comprueba si es una llave primaria, no se comprime
                                if contador in pk:
                                    new_data.append(old_data)
                                # se comprueba que el registro sea texto
                                elif type(old_data) == str:
                                    compress = zlib.compress(old_data,level).encode("utf-8")
                                    new_data.append(compress)
                                else:
                                    new_data.append(old_data)
                                contador +=1

                            truncate(database,ntable)
                            # se elimina la tabla anterior
                            #__dropTableaux(database,ntable)
                            # se crea la tabla 
                            #__createTableaux(database,ntable,columns,mode )
                            # se inserta los nuevos registros 
                            insert(database,ntable,new_data)
                            # se cambia la bandera de compresion a TRUE
                            for tb in db.get("tables"):
                                if tb.get("nameTb")== ntable:
                                    tb["Bandera"]= True   # INCLUIR LA BANDERA DENTRO DE LOS ATRIBUTOS DEL DICCIONARIO
                                    #print("imprimiendo los registros compresos")
                                    #print(extractTable(database,ntable))
                                                                          
                        # se retorna 0
                        return 0
                    else:
                        return 1
                else:
                    return 1
            else:
                return 2
        else:
            return 3
    except:
        return 1

def alterDatabaseDecompress(database: str) -> int:
    try:
        # llama la base de datos
        db =  __getDatabase(database) 
        if db:
            # se extrae el listado de tablas
            l_tablas= showTables(database)
            if l_tablas:
                # se almacena en una lista el nombre de la tabla, las columnas de las llaves primarias y sus registros:
                data = []
                no_compress=0
                compres =0
                for tb in  db.get("tables"):
                    compres +=1
                    # se comprueba que el metadato de la tabla sea Verdadero (TRUE == compreso)
                    if tb.get("Bandera"):
                        data.append([tb.get("nameTb"),tb.get("pk"),extractTable(database,tb.get("nameTb")),tb.get("mode"),tb.get("columns")])
                        
                    else:
                        no_compress +=1
                        
                # se comprueba que todas las tablas esten compresas:
                if compres !=no_compress:
                    data = []
                    return 1
                # se comprueba que la data no este vacia 
                if data:
                    # se recorre cada  arrgelo de la data [nombreTabla, llave foranea,[data],mode,columns]
                    ntable =""
                    mode = ""
                    columns = 0
                    for nreg in data:
                        new_data =[] # almacena el nuevo regigstro con datos compresos
                        ntable=nreg[0]   #nombre de la tabla 
                        pk = nreg[1]        # llaves foranas
                        mode = nreg[3]
                        columns = nreg[4]
                        # se comprime cada columna de los registros en la lista new_data:
                        contador = 0
                        for old_data in nreg[2]:
                            # se comprueba si es una llave primaria, no se comprime
                            if contador in pk:
                                new_data.append(old_data)
                            # se comprueba que el registro sea texto
                            elif type(old_data) == bytes:
                                decompress = zlib.decompress(old_data).decode("utf-8")
                                new_data.append(decompress)
                            else:
                                new_data.append(old_data)
                            contador +=1
                        
                        truncate(database,ntable)
                        # se elimina la tabla anterior
                        #__dropTableaux(database,ntable)
                        # se crea la tabla 
                        #__createTableaux(database,ntable,columns,mode )
                        # se inserta los nuevos registros 
                        insert(database,ntable,new_data)
                        # se cambia la bandera de compresion a TRUE
                        for tb in db.get("tables"):
                            if tb.get("nameTb")== ntable:
                                tb["Bandera"]= False                # INCLUIR LA BANDERA DENTRO DE LOS ATRIBUTOS DEL DICCIONARIO 
                                #print("imprimiendo los registros compresos")
                                #print(extractTable(database,ntable))                                            
                    # se retorna 0
                    return 0
                else:
                    return 3
            else:
                return 1
        else:
            return 2
    except:
        return 1

def alterTableCompress(database: str, table: str, level: int) -> int:
    try:
        # se comprueba  que "level" == 0-9
        if level  in range(10):
            # llama la base de datos
            db =  __getDatabase(database) 
            if db:
                # se extrae el listado de tablas
                l_tablas= showTables(database)
                if l_tablas:
                    # se almacena en una lista el nombre de la tabla, las columnas de las llaves primarias y sus registros:
                    data = []
                    for tb in db.get("tables"):
                        # se busca la tabla 
                        if tb.get("nameTb")== table:
                            # se comprueba que el metadato de la tabla sea False (False == no compreso)
                            if tb.get("Bandera") is False:
                                data.append([tb.get("nameTb"),tb.get("pk"),extractTable(database,tb.get("nameTb")),tb.get("mode"),tb.get("columns")])
                                break
                            else:
                                data = []
                                return 1
                        
                    # se comprueba que la data no este vacia 
                    if data:
                        # se recorre cada  arrgelo de la data [nombreTabla, llave foranea,[data],mode,columns]
                        ntable =""
                        mode = ""
                        columns = 0
                       
                        for nreg in data:
                            new_data =[] # almacena el nuevo regigstro con datos compresos
                            ntable=nreg[0]   #nombre de la tabla 
                            pk = nreg[1]        # llaves foranas
                            mode = nreg[3]
                            columns = nreg[4]
                            # se comprime cada columna de los registros en la lista new_data:
                            contador = 0
                            for old_data in nreg[2]:
                                # se comprueba si es una llave primaria, no se comprime
                                if contador in pk:
                                    new_data.append(old_data)
                                # se comprueba que el registro sea texto
                                elif type(old_data) == str:
                                    compress = zlib.compress(old_data,level).encode("utf-8")
                                    new_data.append(compress)
                                else:
                                    new_data.append(old_data)
                                contador +=1
                            truncate(database,ntable)
                            # se elimina la tabla anterior
                            #__dropTableaux(database,ntable)
                            # se crea la tabla 
                            #__createTableaux(database,ntable,columns,mode )
                            # se inserta los nuevos registros 
                            insert(database,ntable,new_data)
                            # se cambia la bandera de compresion a TRUE
                            for tb in db.get("tables"):
                                if tb.get("nameTb")== ntable:
                                    tb["Bandera"]= True   # INCLUIR LA BANDERA DENTRO DE LOS ATRIBUTOS DEL DICCIONARIO
                                    #print("imprimiendo los registros compresos")
                                    #print(extractTable(database,ntable))
                                                                          
                        # se retorna 0
                        return 0
                    else:
                        return 3
                else:
                    return 1
            else:
                return 2
        else:
            return 4
    except:
        return 1

def alterTableDecompress(database: str, table: str) -> int:
    try:
        # llama la base de datos
        db =  __getDatabase(database) 
        if db:
            # se extrae el listado de tablas
            l_tablas= showTables(database)
            if l_tablas:
                # se almacena en una lista el nombre de la tabla, las columnas de las llaves primarias y sus registros:
                data = []
                for tb in db.get("tables"):
                        # se busca la tabla 
                        if tb.get("nameTb")== table:
                            # se comprueba que el metadato de la tabla sea True (True ==  compreso)
                            if tb.get("Bandera"):
                                data.append([tb.get("nameTb"),tb.get("pk"),extractTable(database,tb.get("nameTb")),tb.get("mode"),tb.get("columns")])
                                break
                            else:
                                return 4
               
                # se comprueba que la data no este vacia 
                if data:
                    # se recorre cada  arrgelo de la data [nombreTabla, llave foranea,[data],mode,columns]
                    ntable =""
                    mode = ""
                    columns = 0
                    
                    
                    for nreg in data:
                        new_data =[] # almacena el nuevo regigstro con datos compresos
                        ntable=nreg[0]   #nombre de la tabla 
                        pk = nreg[1]        # llaves foranas
                        mode = nreg[3]
                        columns = nreg[4]
                        # se comprime cada columna de los registros en la lista new_data:
                        contador = 0
                        for old_data in nreg[2]:
                            # se comprueba si es una llave primaria, no se comprime
                            if contador in pk:
                                new_data.append(old_data)
                            # se comprueba que el registro sea texto
                            elif type(old_data) == bytes:
                                decompress = zlib.decompress(old_data).decode("utf-8")
                                new_data.append(decompress)
                            else:
                                new_data.append(old_data)
                            contador +=1
                        truncate(database,ntable)
                        # se elimina la tabla anterior
                        #__dropTableaux(database,ntable)
                        # se crea la tabla 
                        #__createTableaux(database,ntable,columns,mode )
                        # se inserta los nuevos registros 
                        insert(database,ntable,new_data)
                        # se cambia la bandera de compresion a TRUE
                        for tb in db.get("tables"):
                            if tb.get("nameTb")== ntable:
                                tb["Bandera"]= False                # INCLUIR LA BANDERA DENTRO DE LOS ATRIBUTOS DEL DICCIONARIO 
                                #print("imprimiendo los registros compresos")
                                #print(extractTable(database,ntable))                                            
                    # se retorna 0
                    return 0
                else:
                    return 3
            else:
                return 1
        else:
            return 2
    except:
        return 1







##################
# CODIFIED CRUD  #
##################

def alterDatabaseEncoding(database: str, encoding: str) -> int:
    
    bdObtenida=__getDatabase(database) #comprueba que exista la base de datos

    if bdObtenida:
        
        codificaciones=["utf8", "ascii", "iso-8859-1"]
        #si el encoding enviado esta en la codificaciones
        if  encoding in codificaciones:
            try:
                listaDB = __rollback("data")
                for db in listaDB:
                    if db["nameDb"] == database:
                        db["encoding"]=encoding
                        break
                
                #Se guarda la nueva base de datos en el archivo data
                __commit(listaDB, "data")

                #################### ENCODING ###################

                #################### ENCODING ###################
                return 0 #operacion exitosa
            except:
                return 1 #Error en la operacion
        else:
            return 3 # La codificacion no valida
    else:
        return 2 #la BD no existe

def checksumTable(database: str, table: str, mode: str) -> str:
    if mode.upper()=="MD5":
        try:
            #Extraemos el diccionario de la base de datos respectiva
            db = __getDatabase(database)
            #si existe la BD y existe la Tabla
            if db:
                for tb in db["tables"]:
                    if tb["nameTb"]==table:

                        registros = extractTable(database, tb["nameTb"])

                        ruta=database+table
                        __commit(registros, ruta)

                        if os.path.exists(ruta+".bin"):
                            hasher=hashlib.md5()

                            with open(ruta+".bin", 'rb') as open_file:
                                content=open_file.read()
                                hasher.update(content)
                            return hasher.hexdigest() #devuelve el checksum MD5 de la tabla
                return None #No se encontro la tabla
            else:
                #si llega hasta aca es por que no encontro la BD
                return None
        #si ocurre un error al leer el archivo con el RollBack    
        except:
            return None
    elif mode.upper()=="SHA256":
        try:
            #Extraemos el diccionario de la base de datos respectiva
            db = __getDatabase(database)
            #si existe la BD y existe la Tabla
            if db:
                for tb in db["tables"]:
                    if tb["nameTb"]==table:

                        registros = extractTable(database, tb["nameTb"])

                        ruta=database+table
                        __commit(registros, ruta)
                        
                        if os.path.exists(ruta+".bin"):
                            hasher=hashlib.sha256()

                            with open(ruta+".bin", 'rb') as open_file:
                                content=open_file.read()
                                hasher.update(content)
                            return hasher.hexdigest() #devuelve el checksum MD5 de la tabla
                return None #No se encontro la tabla
            else:
                #si llega hasta aca es por que no encontro la BD
                return None
        #si ocurre un error al leer el archivo con el RollBack    
        except:
            return None
    else:
        return None #devuelve none por que no se encuentra el modo

def checksumDatabase(database: str, mode: str) -> str:
    if mode.upper()=="MD5":
        try:
            #Extraemos el diccionario de la base de datos respectiva
            db = __getDatabase(database)

            #si existe la BD
            if db:
                ruta=database
                __commit(db, ruta)
                if os.path.exists(ruta+".bin"):
                    hasher=hashlib.md5()

                    with open(ruta+".bin", 'rb') as open_file:
                        content=open_file.read()
                        hasher.update(content)
                    return hasher.hexdigest() #devuelve el checksum MD5 de la BD
            else:
                #si llega hasta aca es por que no encontro la BD
                return None
        #si ocurre un error al leer el archivo con el RollBack    
        except:
            return None
    elif mode.upper()=="SHA256":
        try:
            #Extraemos el diccionario de la base de datos respectiva
            db = __getDatabase(database)

            #si existe la BD
            if db:
                ruta=database
                __commit(db, ruta)
                if os.path.exists(ruta+".bin"):
                    hasher=hashlib.sha256()

                    with open(ruta+".bin", 'rb') as open_file:
                        content=open_file.read()
                        hasher.update(content)
                    return hasher.hexdigest() #devuelve el checksum SHA256 de la BD
            else:
                #si llega hasta aca es por que no encontro la BD
                return None
        #si ocurre un error al leer el archivo con el RollBack    
        except:
            return None
    else:
        return None #devuelve none por que no se encuentra el modo

def encrypt(backup: str, password: str) -> str:
    try:

        salida=enc.encriptMessage(backup, password)
        return salida #retorna el criptograma
    except:
        return 1    #ocurrio algun error en la encriptacion

def decrypt(cipherBackup: str, password: str) -> str:
    try:
        x=des.decryptMessage(cipherBackup, password)
        return x #se envia el criptograma desencriptado
    except:
        return 1   #ocurrio un error o clave invalida



def graphDSD(database: str) -> int:
    """Graphs a database ERD

        Pararameters:\n
            database (str): name of the database

        Returns:\n
            0: successful operation
            None: non-existent database, an error ocurred
    """
    try:

        if not database.isidentifier():
            raise Exception()

        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return None

        archivo = open('archivo.dot', 'w', encoding='utf-8')
        archivo.write('digraph structs {\n')
        archivo.write('rankdir=LR;\n')
        #archivo.write('node [shape=record];\n')

        # nodo [label="nodo"];
        print('encabezado')
        for tb in baseDatos["tables"]:
            archivo.write( '{0} [label="{0}"];\n'.format(tb["nameTb"]))

        # enlaces tabla2 -> tabla1
        print('enlaces')
        tabla1 = ''
        tabla2 = ''
        for tb in baseDatos["tables"]:
            tabla1 = tb["nameTb"]                                    
            for lista in tb["foreign_keys"].extractTable():
                tabla2 = lista[2]
                archivo.write( '{0} -> {1};\n'.format(tabla2, tabla1) )
        archivo.write("}\n")
        archivo.close()
        os.system('dot -Tpng archivo.dot -o graphDSD.png')
        os.system('graphDSD.png')
        return 0
    except:
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
    try:
        if not database.isidentifier() or not table.isidentifier():
            raise Exception()

        baseDatos = __getDatabase(database)
        if baseDatos is False:
            return None
        
        tabla = __getTable(database, table)
        if tabla is False:
            return None

        archivo = open('archivo.dot', 'w', encoding='utf-8')
        archivo.write('digraph structs {\n')
        archivo.write('rankdir=LR;')
        archivo.write('node [shape=record];\n')

        list_key = []
        list_reg = []

        for lista in tabla["unique_index"].extractTable():
            list_key.append('unique_'+str(lista[0]))
        
        primaria = 'primary'
        for pk in tabla["pk"]: 
            primaria += '_'+ str(pk)
        list_key.append(primaria)
                            # 7             -       4
        for x in range(int(tabla["columns"] - len(list_key))):
            list_reg.append("reg_"+str(x+1)) #reg_1, reg_2, reg_3

        #list_key = [primary_1, primary_2, unique_1, unique_2]
        #list_reg = [reg_1, reg_2, reg_3]
        # nodo[label=""];
        
        for x in list_key:
            archivo.write('{0} [label="{0}"];\n'.format(x))
            
        for x in list_reg:
            archivo.write('{0} [label="{0}"];\n'.format(x))
        
        # enlaces
        # pk -> reg;
        
        for x in list_key:
            for y in list_reg:
                archivo.write('{0} -> {1};\n'.format(x, y))
        archivo.write("}\n")
        archivo.close()
        os.system('dot -Tpng archivo.dot -o graphDF.png')
        os.system('graphDF.png')
        return 0
    except:
        return None

def deserializar():
    #Si el archivo binario 'data' no existe no hay nada para deserializar
    if os.path.exists("data.bin"):
        #Se activa la bandera serializado
        global deserializadoActivado
        deserializadoActivado = True

        #Deserializa el archivo binario 'data' que retorna una lista de diccionarios para las bases de datos
        diccionariosDb = __rollback("data")
        #Se recorre cada base de datos obteniendola por su ruta de archivo
        for db in diccionariosDb:
            #Capturamos el nombre de la base de datos
            nombreDb = db["nameDb"]
            #Se crea la base de datos para tenerla en memoria
            createDatabase(nombreDb, db["mode"], db["encoding"])
        
            #Se recorre cada diccionario tabla dentro de la base de datos especifica
            diccionariosTb = db["tables"]
            for tb in diccionariosTb:
                #Extraer toda la informacion del diccionario de tabla actual
                nombreTb = tb["nameTb"]
                modeTb = tb["mode"]
                columnas = tb["columns"]
                pk = tb["pk"]
                registros = tb["registros"]
                registrosFk = tb["registrosFk"]
                registrosUn = tb["registrosUn"]
                registrosIn = tb["registrosIn"]
                bandera = tb["Bandera"]


                # Pedir la lista de diccionarios de base de datos------------------------------------------
                listaDB = __rollback("data")

                #Se elimina el diccionario correspondiente a la tabla del archivo data
                for db in listaDB:
                    if db["nameDb"] == nombreDb:
                        db["tables"].remove(tb)
                        break

                # Se guarda la lista de base de datos ya actualizada en el archivo data
                __commit(listaDB, "data")
                #------------------------------------------------------------------------------------------

                #Se crea la base de datos en memoria y las instancias de Fk, Un, In
                __createTable(nombreDb, nombreTb, columnas, modeTb)
                #Se actualiza la pk
                alterAddPK(nombreDb, nombreTb, pk)

                #Se insertan los registros de la estructura
                for tupla in registros:
                    insert(nombreDb, nombreTb, tupla)
                
                #Se insertan lo registros de las llaves foraneas
                for tupla in registrosFk:
                    #[indexName, table, tableRef, columns, columnsRef]
                    alterTableAddFK(nombreDb, tupla[1], tupla[0], tupla[3], tupla[2], tupla[4])

                #Se insertan los registros de las llaves unicas
                for tupla in registrosUn:
                    #[indexName, table, columns]
                    alterTableAddUnique(nombreDb, tupla[1], tupla[0], tupla[2])
                    
                #Se insertan los registros de los indices
                for tupla in registrosIn:
                    #[indexName, table, columns]
                    alterTableAddIndex(nombreDb, tupla[1], tupla[0], tupla[2])

                # Pedir la lista de diccionarios de base de datos------------------------------------------
                listaDB = __rollback("data")

                #Se elimina el diccionario correspondiente a la tabla del archivo data
                for db in listaDB:
                    if db["nameDb"] == nombreDb:
                        for tb in db["tables"]:
                            if tb["nameTb"] == nombreTb:
                                tb["Bandera"] = bandera
                            break

                # Se guarda la lista de base de datos ya actualizada en el archivo data
                __commit(listaDB, "data")
                #------------------------------------------------------------------------------------------

        deserializadoActivado = False
