from storage.b import BMode as b_mode
from storage.bplus import BPlusMode as bplus_mode
from storage.isam import ISAMMode as isam_mode
from storage.hash import HashMode as hash_mode
from storage.avl import AVLMode as avl_mode
from storage.dict import DictMode as dict_mode
from storage.json import jsonMode as json_mode
import hashlib
from encript import *
from blockchain import *
import os
import shutil
import zlib
import pickle
# AVL: AVLMode
# B: BMode
# B+: BPlusMode
# ISAM: ISAMMode
# TablasHash: HashMode

Bases = {}
Tablas = {}

#**********************************************FASE 1****************************************************
#-------------------------------------Funciones de bases de datos----------------------------------------
def createDatabase(database, mode, encoding):
    val = 1
    if encoding != "ascii" and encoding != "iso-8859-1" and encoding != "utf8":
        val = 4
    else:
        if mode == "avl":
            # Grupo 16
            val = avl_mode.createDatabase(database)
        elif mode == "b":
            # Grupo 17
            val = b_mode.createDatabase(database)
        elif mode == "bplus":
            # Grupo 18
            val = bplus_mode.createDatabase(database)
        elif mode == "dict":
            # Auxiliar
            val = dict_mode.createDatabase(database)
        elif mode == "isam":
            # Grupo 14
            val = isam_mode.createDatabase(database)
        elif mode == "json":
            # Ingeniero
            val = json_mode.createDatabase(database)
        elif mode == "hash":
            # Grupo 15
            val = hash_mode.createDatabase(database)
        else:
            val = 3
        if val == 0:
            global Bases
            try:
                # Leemos el archivo binario de los registros de bases de datos
                fichero_lectura = open("BD_register", "rb")
                Bases = pickle.load(fichero_lectura)
                Bases.update({database: {"mode": mode, "encoding": encoding, "FK":{}}})
                # Actualizamos el archivo binario de los registros de bases de datos
                fichero_escritura = open("BD_register", "wb")
                pickle.dump(Bases, fichero_escritura)
                fichero_escritura.close()
            except:
                Bases.update({database: {"mode": mode, "encoding": encoding, "FK":{}}})
                # Actualizamos el archivo binario de los registros de bases de datos
                fichero_escritura = open("BD_register", "wb")
                pickle.dump(Bases, fichero_escritura)
                fichero_escritura.close()
    return val

def showDatabases():
    print("AVL")
    print(avl_mode.showDatabases())
    print("b")
    print(b_mode.showDatabases())
    print("b+")
    print(bplus_mode.showDatabases())
    print("dict")
    print(dict_mode.showDatabases())
    print("isam")
    print(isam_mode.showDatabases())
    print("json")
    print(json_mode.showDatabases())
    print("hash")
    print(hash_mode.showDatabases())

def alterDatabase(databaseOld, databaseNew):
    mode = None
    for i in range(7):
        mode = obtenerBase(databaseOld,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.alterDatabase(databaseOld, databaseNew)
    elif mode == "b":
        # Grupo 17
        val = b_mode.alterDatabase(databaseOld, databaseNew)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.alterDatabase(databaseOld, databaseNew)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.alterDatabase(databaseOld, databaseNew)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.alterDatabase(databaseOld, databaseNew)
    elif mode == "json":
        # Ingeniero
        val = json_mode.alterDatabase(databaseOld, databaseNew)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.alterDatabase(databaseOld, databaseNew)
    else:
        val = 3
    #-----------------Renombra la base de datos en los registros de bases de datos serializados-----------------
    if val == 0:
        global Bases
        try:
            # Leemos el archivo binario de los registros de bases de datos
            fichero_lectura = open("BD_register", "rb")
            Bases = pickle.load(fichero_lectura)
            Aux = Bases[databaseOld]
            Bases.pop(databaseOld)
            Bases.update({databaseNew: Aux})
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("BD_register", "wb")
            pickle.dump(Bases, fichero_escritura)
            fichero_escritura.close()
        except:
            Aux = Bases[databaseOld]
            Bases.pop(databaseOld)
            Bases.update({databaseNew: Aux})
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("BD_register", "wb")
            pickle.dump(Bases, fichero_escritura)
            fichero_escritura.close()
    #----------------Renombra la base de datos en los registros de tablas serializados-----------------------
        global Tablas
        try:
            # Leemos el archivo binario de los registros de tablas
            lectura = open("TB_register", "rb")
            Tablas = pickle.load(lectura)
            try:
                Aux = Tablas[databaseOld]
                Tablas.pop(databaseOld)
                Tablas.update({databaseNew:Aux})
            except:
                #Si no hay tablas creadas en esa base de datos no hay clave en el diccionario entonces no hace nada
                """"""
            # Actualizamos el archivo binario de los registros de tablas
            escritura = open("TB_register", "wb")
            pickle.dump(Tablas, escritura)
            escritura.close()
        except:
            try:
                Aux = Tablas[databaseOld]
                Tablas.pop(databaseOld)
                Tablas.update({databaseNew: Aux})
            except:
                # Si no hay tablas creadas en esa base de datos no hay clave en el diccionario entonces no hace nada
                """"""
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()

def dropDatabase(database):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.dropDatabase(database)
    elif mode == "b":
        # Grupo 17
        val = b_mode.dropDatabase(database)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.dropDatabase(database)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.dropDatabase(database)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.dropDatabase(database)
    elif mode == "json":
        # Ingeniero
        val = json_mode.dropDatabase(database)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.dropDatabase(database)
    else:
        val = 3
    if val == 0:
        global Bases
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            fichero_lectura = open("BD_register", "rb")
            Bases = pickle.load(fichero_lectura)
            Bases.pop(database)
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("BD_register", "wb")
            pickle.dump(Bases, fichero_escritura)
            fichero_escritura.close()
            try:
                # Leemos el archivo binario de los registros de tablas
                fichero_lectura = open("TB_register", "rb")
                Tablas = pickle.load(fichero_lectura)
                try:
                    Tablas.pop(database)
                except:
                    """"""
                # Actualizamos el archivo binario de los registros de tablas
                fichero_escritura = open("TB_register", "wb")
                pickle.dump(Tablas, fichero_escritura)
                fichero_escritura.close()
            except:
                try:
                    Tablas.pop(database)
                except:
                    """"""
                # Actualizamos el archivo binario de los registros de tablas
                fichero_escritura = open("TB_register", "wb")
                pickle.dump(Tablas, fichero_escritura)
                fichero_escritura.close()
        except:
            Bases.pop(database)
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("BD_register", "wb")
            pickle.dump(Bases, fichero_escritura)
            fichero_escritura.close()
            try:
                # Leemos el archivo binario de los registros de tablas
                fichero_lectura = open("TB_register", "rb")
                Tablas = pickle.load(fichero_lectura)
                try:
                    Tablas.pop(database)
                except:
                    """"""
                # Actualizamos el archivo binario de los registros de tablas
                fichero_escritura = open("TB_register", "wb")
                pickle.dump(Tablas, fichero_escritura)
                fichero_escritura.close()
            except:
                try:
                    Tablas.pop(database)
                except:
                    """"""
                    # Actualizamos el archivo binario de los registros de tablas
                    fichero_escritura = open("TB_register", "wb")
                    pickle.dump(Tablas, fichero_escritura)
                    fichero_escritura.close()
            return val
#--------------------------------------Funciones de tablas-----------------------------------------------
def createTable(database, table, numColumns):
    val = None
    mode = None
    for i in range(7):
        mode = obtenerBase(database,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.createTable(database, table, numColumns)
    elif mode == "b":
        # Grupo 17
        val = b_mode.createTable(database, table, numColumns)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.createTable(database, table, numColumns)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.createTable(database, table, numColumns)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.createTable(database, table, numColumns)
    elif mode == "json":
        # Ingeniero
        val = json_mode.createTable(database, table, numColumns)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.createTable(database, table, numColumns)
    else:
        return val
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de tablas
            lectura = open("TB_register", "rb")
            Tablas = pickle.load(lectura)
            try:
                Tablas[database].update({table: {"PK": None,"mode":mode,"safe":False,"Ncol":numColumns,"IU":{},"I":{}}})
            except:
                Tablas.update(c)
            # Actualizamos el archivo binario de los registros de tablas
            escritura = open("TB_register", "wb")
            pickle.dump(Tablas, escritura)
            escritura.close()
        except:
            try:
                Tablas[database].update({table: {"PK": None,"mode":mode,"safe":False,"Ncol":numColumns,"IU":{},"I":{}}})
            except:
                Tablas.update({database: {table: {"PK": None,"mode":mode,"safe":False,"Ncol":numColumns,"IU":{},"I":{}}}})
            # Actualizamos el archivo binario de los registros de tablas
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return val

def showTables(database):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.showTables(database)
    elif mode == "b":
        # Grupo 17
        val = b_mode.showTables(database)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.showTables(database)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.showTables(database)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.showTables(database)
    elif mode == "json":
        # Ingeniero
        val = json_mode.showTables(database)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.showTables(database)
    else:
        return val
    return val

def extractTable(database, table):
    val = None
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.extractTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.extractTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.extractTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.extractTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.extractTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.extractTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.extractTable(database, table)
    else:
        return val
    return val

def extractRangeTable(database, table, columnNumber, lower, upper):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.extractRangeTable(database, table, columnNumber, lower, upper)
    elif mode == "b":
        # Grupo 17
        val = b_mode.extractRangeTable(database, table, columnNumber, lower, upper)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.extractRangeTable(database, table, columnNumber, lower, upper)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.extractRangeTable(database, table, columnNumber, lower, upper)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.extractRangeTable(database, table, columnNumber, lower, upper)
    elif mode == "json":
        # Ingeniero
        val = json_mode.extractRangeTable(database, table, columnNumber, lower, upper)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.extractRangeTable(database, table, columnNumber, lower, upper)
    else:
        val = 3
    return val
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.extractTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.extractTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.extractTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.extractTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.extractTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.extractTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.extractTable(database, table)
    else:
        return val
    return val

def alterAddPK(database, table, columns):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.alterAddPK(database, table, columns)
    elif mode == "b":
        # Grupo 17
        val = b_mode.alterAddPK(database, table, columns)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.alterAddPK(database, table, columns)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.alterAddPK(database, table, columns)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.alterAddPK(database, table, columns)
    elif mode == "json":
        # Ingeniero
        val = json_mode.alterAddPK(database, table, columns)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.alterAddPK(database, table, columns)
    else:
        return val
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            lectura = open("TB_register", "rb")
            Tablas = pickle.load(lectura)
            Tablas[database][table]["PK"] = columns
            # Actualizamos el archivo binario de los registros de bases de datos
            escritura = open("TB_register", "wb")
            pickle.dump(Tablas, escritura)
            escritura.close()
        except:
            Tablas[database][table]["PK"] = columns
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return val

def alterDropPK(database, table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.alterDropPK(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.alterDropPK(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.alterDropPK(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.alterDropPK(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.alterDropPK(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.alterDropPK(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.alterDropPK(database, table)
    else:
        return val
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            lectura = open("TB_register", "rb")
            Tablas = pickle.load(lectura)
            Tablas[database][table]["PK"] = None
            # Actualizamos el archivo binario de los registros de bases de datos
            escritura = open("TB_register", "wb")
            pickle.dump(Tablas, escritura)
            escritura.close()
        except:
            Tablas[database][table]["PK"] = None
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return val

def alterTable(database, tableOld, tableNew):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.alterTable(database, tableOld, tableNew)
    elif mode == "b":
        # Grupo 17
        val = b_mode.alterTable(database, tableOld, tableNew)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.alterTable(database, tableOld, tableNew)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.alterTable(database, tableOld, tableNew)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.alterTable(database, tableOld, tableNew)
    elif mode == "json":
        # Ingeniero
        val = json_mode.alterTable(database, tableOld, tableNew)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.alterTable(database, tableOld, tableNew)
    else:
        return val
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de tablas
            lectura = open("TB_register", "rb")
            Tablas = pickle.load(lectura)
            Aux = Tablas[database][tableOld]
            Tablas[database].pop(tableOld)
            Tablas[database].update({tableNew: Aux})
            # Actualizamos el archivo binario de los registros de tablas
            escritura = open("TB_register", "wb")
            pickle.dump(Tablas, escritura)
            escritura.close()
        except:
            Aux = Tablas[database][tableOld]
            Tablas[database].pop(tableOld)
            Tablas[database].update({tableNew: Aux})
            # Actualizamos el archivo binario de los registros de tablas
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return 0

def alterAddColumn(database, table, default):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.alterAddColumn(database, table, default)
    elif mode == "b":
        # Grupo 17
        val = b_mode.alterAddColumn(database, table, default)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.alterAddColumn(database, table, default)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.alterAddColumn(database, table, default)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.alterAddColumn(database, table, default)
    elif mode == "json":
        # Ingeniero
        val = json_mode.alterAddColumn(database, table, default)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.alterAddColumn(database, table, default)
    else:
        return val
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            lectura = open("TB_register", "rb")
            Tablas = pickle.load(lectura)
            NumeroColumnas =Tablas[database][table]["Ncol"]
            NumeroColumnas+=1
            Tablas[database][table]["Ncol"] = NumeroColumnas
            # Actualizamos el archivo binario de los registros de bases de datos
            escritura = open("TB_register", "wb")
            pickle.dump(Tablas, escritura)
            escritura.close()
        except:
            NumeroColumnas = Tablas[database][table]["Ncol"]
            NumeroColumnas += 1
            Tablas[database][table]["Ncol"] = NumeroColumnas
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return val

def alterDropColumn(database, table, columnNumber):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.alterDropColumn(database, table, columnNumber)
    elif mode == "b":
        # Grupo 17
        val = b_mode.alterDropColumn(database, table, columnNumber)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.alterDropColumn(database, table, columnNumber)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.alterDropColumn(database, table, columnNumber)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.alterDropColumn(database, table, columnNumber)
    elif mode == "json":
        # Ingeniero
        val = json_mode.alterDropColumn(database, table, columnNumber)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.alterDropColumn(database, table, columnNumber)
    else:
        return val
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            lectura = open("TB_register", "rb")
            Tablas = pickle.load(lectura)
            NumeroColumnas =Tablas[database][table]["Ncol"]
            NumeroColumnas-=1
            Tablas[database][table]["Ncol"] = NumeroColumnas
            # Actualizamos el archivo binario de los registros de bases de datos
            escritura = open("TB_register", "wb")
            pickle.dump(Tablas, escritura)
            escritura.close()
        except:
            NumeroColumnas = Tablas[database][table]["Ncol"]
            NumeroColumnas -= 1
            Tablas[database][table]["Ncol"] = NumeroColumnas
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return val

def dropTable(database, table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.dropTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.dropTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.dropTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.dropTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.dropTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.dropTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.dropTable(database, table)
    else:
        val = 3
    if val == 0:
        global Tablas
        try:
            # Leemos el archivo binario de los registros de bases de datos
            fichero_lectura = open("TB_register", "rb")
            Tablas = pickle.load(fichero_lectura)
            Tablas[database].pop(table)
            if len(Tablas[database])==0:
                Tablas.pop(database)
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
        except:
            Tablas[database].pop(table)
            if len(Tablas[database])==0:
                Tablas.pop(database)
            # Actualizamos el archivo binario de los registros de bases de datos
            fichero_escritura = open("TB_register", "wb")
            pickle.dump(Tablas, fichero_escritura)
            fichero_escritura.close()
    return val

#--------------------------------------Funciones de tuplas-----------------------------------------------
def insert(database, table, register):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.insert(database, table, register)
    elif mode == "b":
        # Grupo 17
        val = b_mode.insert(database, table, register)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.insert(database, table, register)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.insert(database, table, register)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.insert(database, table, register)
    elif mode == "json":
        # Ingeniero
        val = json_mode.insert(database, table, register)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.insert(database, table, register)
    else:
        return val
    return val

def loadCSV(file,database,table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database,i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.loadCSV(file, database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.loadCSV(file, database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.loadCSV(file, database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.loadCSV(file, database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.loadCSV(file, database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.loadCSV(file, database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.loadCSV(file, database, table)
    else:
        val = 3
    return val

def extractRow(database, table, columns):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.extractRow(database, table, columns)
    elif mode == "b":
        # Grupo 17
        val = b_mode.extractRow(database, table, columns)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.extractRow(database, table, columns)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.extractRow(database, table, columns)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.extractRow(database, table, columns)
    elif mode == "json":
        # Ingeniero
        val = json_mode.extractRow(database, table, columns)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.extractRow(database, table, columns)
    else:
        return val
    return val

def update(database, table, register, columns):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.update(database, table, register, columns)
    elif mode == "b":
        # Grupo 17
        val = b_mode.update(database, table, register, columns)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.update(database, table, register, columns)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.update(database, table, register, columns)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.update(database, table, register, columns)
    elif mode == "json":
        # Ingeniero
        val = json_mode.update(database, table, register, columns)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.update(database, table, register, columns)
    else:
        return val
    return val

def delete(database, table, columns):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.delete(database, table, columns)
    elif mode == "b":
        # Grupo 17
        val = b_mode.delete(database, table, columns)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.delete(database, table, columns)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.delete(database, table, columns)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.delete(database, table, columns)
    elif mode == "json":
        # Ingeniero
        val = json_mode.delete(database, table, columns)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.delete(database, table, columns)
    else:
        return val
    return val

def truncate(database, table):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if mode == None:
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.truncate(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.truncate(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.truncate(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.truncate(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.truncate(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.truncate(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.truncate(database, table)
    else:
        return val
    return val

#********************************************************************************************************
#*******************************************Fase 2******************************************************
#------------------------------------------- Inciso 2 ----------------------------------------------------
def alterDatabaseMode(database, mode):
    diccionario = {"avl":0, "b":1, "bplus":2, "dict":3, "isam":4, "json":5, "hash":6}
    if mode in diccionario:
        modo_anterior = None
        for i in diccionario:
            modo_anterior = obtenerBase(database, diccionario[i])
            if modo_anterior != []:
                break
        if modo_anterior == []:
            return 2
        else:
            modo_actual = diccionario[mode]
            if modo_anterior == modo_actual:
                return 1
            else:
                temp_tablas = obtenerTablas(database, modo_anterior)
                temp_fila_tabla = []
                for tabla in temp_tablas:
                    temp_fila_tabla.append([tabla, extractTable(database, tabla)])
                dropDatabase(database)
                createDatabase(database, mode, "utf8")
                for dato in temp_fila_tabla:
                    nombre_tabla = dato[0]
                    registros = dato[1]
                    if registros != []:
                        createTable(database, nombre_tabla, len(registros[0]))
                    for registro in registros:
                        insert(database, nombre_tabla, registro)
                global Bases
                try:
                    # Leemos el archivo binario de los registros de bases de datos
                    fichero_lectura = open("BD_register", "rb")
                    Bases = pickle.load(fichero_lectura)
                    Bases[database]["mode"]=mode
                    # Actualizamos el archivo binario de los registros de bases de datos
                    fichero_escritura = open("BD_register", "wb")
                    pickle.dump(Bases, fichero_escritura)
                    fichero_escritura.close()
                except:
                    Bases[database]["mode"] = mode
                    # Actualizamos el archivo binario de los registros de bases de datos
                    fichero_escritura = open("BD_register", "wb")
                    pickle.dump(Bases, fichero_escritura)
                    fichero_escritura.close()
                return 0
    else:
        return 4

def alterTableMode(database, table, mode):
    print("alterTableMode")

#------------------------------------------- Inciso 3 ----------------------------------------------------
def alterTableAddFK(database, table, indexName, columns,  tableRef, columnsRef):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if type(mode)!=str:
        #No se encontró la base de datos
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.showTables(database)
    elif mode == "b":
        # Grupo 17
        val = b_mode.showTables(database)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.showTables(database)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.showTables(database)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.showTables(database)
    elif mode == "json":
        # Ingeniero
        val = json_mode.showTables(database)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.showTables(database)
    Existe_tabla1 = False
    Existe_tabla2 = False
    if val ==[]:
        return 3
    for i in range(len(val)):
        if val[i]==table:
            Existe_tabla1 = True
            break
    for j in range(len(val)):
        if val[j]==tableRef:
            Existe_tabla2 = True
            break
    if Existe_tabla1 == False or Existe_tabla2 == False:
        return 3
    if len(columns)!=len(columnsRef):
        return 4
    global Bases
    try:
        # Leemos el archivo binario de los registros de bases de datos
        fichero_lectura = open("BD_register", "rb")
        Bases = pickle.load(fichero_lectura)
        Bases[database]["FK"].update({indexName: [tableRef, table]})
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("BD_register", "wb")
        pickle.dump(Bases, fichero_escritura)
        fichero_escritura.close()
    except:
        Bases[database]["FK"].update({indexName: [tableRef, table]})
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("BD_register", "wb")
        pickle.dump(Bases, fichero_escritura)
        fichero_escritura.close()
    return 0

def alterTableDropFK(database, table, indexName):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if type(mode) != str:
        # No se encontró la base de datos
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.extractTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.extractTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.extractTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.extractTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.extractTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.extractTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.extractTable(database, table)
    if val == []:
        return 3
    global Bases
    try:
        # Leemos el archivo binario de los registros de bases de datos
        fichero_lectura = open("BD_register", "rb")
        Bases = pickle.load(fichero_lectura)
        try:
            Bases[database]["FK"].pop(indexName)
        except:
            return 4
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("BD_register", "wb")
        pickle.dump(Bases, fichero_escritura)
        fichero_escritura.close()
    except:
        try:
            Bases[database]["FK"].pop(indexName)
        except:
            return 4
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("BD_register", "wb")
        pickle.dump(Bases, fichero_escritura)
        fichero_escritura.close()
    return 0

def alterTableAddUnique(database, table, indexName, columns):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if type(mode) != str:
        # No se encontró la base de datos
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.showTables(database)
    elif mode == "b":
        # Grupo 17
        val = b_mode.showTables(database)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.showTables(database)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.showTables(database)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.showTables(database)
    elif mode == "json":
        # Ingeniero
        val = json_mode.showTables(database)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.showTables(database)
    Existe_tabla = False
    if val == []:
        return 3
    for i in range(len(val)):
        if val[i] == table:
            Existe_tabla = True
            break
    if Existe_tabla == False:
        return 3
    if len(columns) ==0:
        return 4
    global Tablas
    try:
        # Leemos el archivo binario de los registros de bases de datos
        fichero_lectura = open("TB_register", "rb")
        Tablas = pickle.load(fichero_lectura)
        Tablas[database][table]["IU"].update({indexName: columns})
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("BD_register", "wb")
        pickle.dump(Bases, fichero_escritura)
        fichero_escritura.close()
    except:
        Tablas[database][table]["IU"].update({indexName: columns})
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("TB_register", "wb")
        pickle.dump(Tablas, fichero_escritura)
        fichero_escritura.close()
    return 0

def alterTableDropUnique(database, table, indexName):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if type(mode) != str:
        # No se encontró la base de datos
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.extractTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.extractTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.extractTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.extractTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.extractTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.extractTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.extractTable(database, table)
    if val == []:
        return 3
    global Tablas
    try:
        # Leemos el archivo binario de los registros de bases de datos
        fichero_lectura = open("TB_register", "rb")
        Tablas = pickle.load(fichero_lectura)
        try:
            Tablas[database][table]["IU"].pop(indexName)
        except:
            return 4
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("TB_register", "wb")
        pickle.dump(Tablas, fichero_escritura)
        fichero_escritura.close()
    except:
        try:
            Tablas[database][table]["IU"].pop(indexName)
        except:
            return 4
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("TB_register", "wb")
        pickle.dump(Tablas, fichero_escritura)
        fichero_escritura.close()
    return 0

def alterTableAddIndex(database, table, indexName, columns):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if type(mode) != str:
        # No se encontró la base de datos
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.showTables(database)
    elif mode == "b":
        # Grupo 17
        val = b_mode.showTables(database)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.showTables(database)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.showTables(database)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.showTables(database)
    elif mode == "json":
        # Ingeniero
        val = json_mode.showTables(database)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.showTables(database)
    Existe_tabla = False
    if val == []:
        return 3
    for i in range(len(val)):
        if val[i] == table:
            Existe_tabla = True
            break
    if Existe_tabla == False:
        return 3
    if len(columns) ==0:
        return 4
    global Tablas
    try:
        # Leemos el archivo binario de los registros de bases de datos
        fichero_lectura = open("TB_register", "rb")
        Tablas = pickle.load(fichero_lectura)
        Tablas[database][table]["I"].update({indexName: columns})
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("TB_register", "wb")
        pickle.dump(Tablas, fichero_escritura)
        fichero_escritura.close()
    except:
        Tablas[database][table]["I"].update({indexName: columns})
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("TB_register", "wb")
        pickle.dump(Tablas, fichero_escritura)
        fichero_escritura.close()
    return 0

def alterTableDropIndex(database, table, indexName):
    mode = None
    for i in range(7):
        mode = obtenerBase(database, i)
        if mode == []:
            continue
        else:
            if mode == 0:
                mode = "avl"
            elif mode == 1:
                mode = "b"
            elif mode == 2:
                mode = "bplus"
            elif mode == 3:
                mode = "dict"
            elif mode == 4:
                mode = "isam"
            elif mode == 5:
                mode = "json"
            elif mode == 6:
                mode = "hash"
            break
    if type(mode) != str:
        # No se encontró la base de datos
        return 2
    if mode == "avl":
        # Grupo 16
        val = avl_mode.extractTable(database, table)
    elif mode == "b":
        # Grupo 17
        val = b_mode.extractTable(database, table)
    elif mode == "bplus":
        # Grupo 18
        val = bplus_mode.extractTable(database, table)
    elif mode == "dict":
        # Auxiliar
        val = dict_mode.extractTable(database, table)
    elif mode == "isam":
        # Grupo 14
        val = isam_mode.extractTable(database, table)
    elif mode == "json":
        # Ingeniero
        val = json_mode.extractTable(database, table)
    elif mode == "hash":
        # Grupo 15
        val = hash_mode.extractTable(database, table)
    if val == []:
        return 3
    global Tablas
    try:
        # Leemos el archivo binario de los registros de bases de datos
        fichero_lectura = open("TB_register", "rb")
        Tablas = pickle.load(fichero_lectura)
        try:
            Tablas[database][table]["I"].pop(indexName)
        except:
            return 4
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("TB_register", "wb")
        pickle.dump(Tablas, fichero_escritura)
        fichero_escritura.close()
    except:
        try:
            Tablas[database][table]["I"].pop(indexName)
        except:
            return 4
        # Actualizamos el archivo binario de los registros de bases de datos
        fichero_escritura = open("TB_register", "wb")
        pickle.dump(Tablas, fichero_escritura)
        fichero_escritura.close()
    return 0

#------------------------------------------- Inciso 5 ----------------------------------------------------
def checksumDatabase(database, mode):
    import hashlib
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if mode.lower() == "sha256":
                hash = hashlib.sha256()
            elif mode.lower() == "md5":
                hash = hashlib.md5()
            else:
                return None
            try:
                hash.update(database.encode("UTF-8"))
            except:
                return None
            break
    tables = obtenerTablas(database, var)
    try:
        if tables == []:
            return None
        else:
            contenido = ""
            for i in range(len(tables)):
                contenidoTabla = obtenerContenidoTabla(database, tables[i], var)
                hash.update(tables[i].encode("UTF-8"))
                contenido += contenidoTabla
            contenido = contenido.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace(",", "")
        hash.update(contenido.encode("UTF-8"))
    except:
        return None
    return hash.hexdigest()

def obtenerBase(database,estructura):
    val = []
    if estructura == 0:
        val = avl_mode.showDatabases()
    elif estructura == 1:
        val = b_mode.showDatabases()
    elif estructura == 2:
        val = bplus_mode.showDatabases()
    elif estructura == 3:
        val = dict_mode.showDatabases()
    elif estructura == 4:
        val = isam_mode.showDatabases()
    elif estructura == 5:
        val = json_mode.showDatabases()
    elif estructura == 6:
        val = hash_mode.showDatabases()
    if val == []:
        return val
    else:
        for i in range(len(val)):
            if val[i].lower()==database.lower():
                return estructura
    return []

def obtenerContenidoTabla(database, table, estructura):
    val = []
    if estructura == 0:
        val = avl_mode.extractTable(database,table)
    elif estructura == 1:
        val = b_mode.extractTable(database,table)
    elif estructura == 2:
        val = bplus_mode.extractTable(database,table)
    elif estructura == 3:
        val = dict_mode.extractTable(database,table)
    elif estructura == 4:
        val = isam_mode.extractTable(database,table.lower())
    elif estructura == 5:
        val = json_mode.extractTable(database,table)
    elif estructura == 6:
        val = hash_mode.extractTable(database,table)
    if val == [] or type(val)==int:
        return ""
    contenido = ""
    for i in range(len(val)):
        contenido+=str(val[i])
    return contenido

def obtenerTablas(database, estructura):
    val = []
    if estructura == 0:
        val = avl_mode.showTables(database)
    elif estructura == 1:
        val = b_mode.showTables(database)
    elif estructura == 2:
        val = bplus_mode.showTables(database)
    elif estructura == 3:
        val = dict_mode.showTables(database)
    elif estructura == 4:
        val = isam_mode.showTables(database)
    elif estructura == 5:
        val = json_mode.showTables(database)
    elif estructura == 6:
        val = hash_mode.showTables(database)
    return val

def checksumTable(database, table, mode):
    import hashlib
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if mode.lower() == "sha256":
                hash = hashlib.sha256()
            elif mode.lower() == "md5":
                hash = hashlib.md5()
            else:
                return None
            break
    try:
        contenido = ""
        contenidoTabla = obtenerContenidoTabla(database, table, var)
        hash.update(table.encode("UTF-8"))
        contenido += contenidoTabla
        contenido = contenido.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace(",", "")
        hash.update(contenido.encode("UTF-8"))
    except:
        return None
    return hash.hexdigest()

#------------------------------------------- Inciso 6 ---------------------------------------------------
def alterDatabaseCompress(database, level):
    if level < 0 or level > 9:
        return 4
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 3
    tables = obtenerTablas(database, var)
    if tables == []:
        return None
    else:
        try:
            for i in range(len(tables)):
                contenidoTabla = extractTable(database, tables[i])
                #print(contenidoTabla)
                for j in range(len(contenidoTabla)):
                    tupla = contenidoTabla[j]
                    for k in range(len(tupla)):
                        if type(tupla[k]) == str:
                            tupla[k] = zlib.compress(tupla[k].encode(), level)
                    contenidoTabla[j] = tupla
                truncate(database, tables[i])
                for registro in contenidoTabla:
                    insert(database, tables[i], registro)
            return 0
        except:
            return 1

def alterDatabaseDecompress(database):
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 3
    tables = obtenerTablas(database, var)
    if tables == []:
        return None
    else:
        try:
            comprimido = False
            for i in range(len(tables)):
                contenidoTabla = extractTable(database, tables[i])
                for j in range(len(contenidoTabla)):
                    tupla = contenidoTabla[j]
                    for k in range(len(tupla)):
                        if type(tupla[k]) == str or type(tupla[k]) == int or type(tupla[k]) == float or type(tupla[k]) == bool:
                            continue
                        else:
                            valor = zlib.decompress(tupla[k])
                            tupla[k] = valor.decode()
                            comprimido = True
                    contenidoTabla[j] = tupla
                if comprimido == True:
                    truncate(database, tables[i])
                    for registro in contenidoTabla:
                        insert(database, tables[i], registro)
                else:
                    return 3
            return 0
        except:
            return 1

def alterTableCompress(database, table, level):
    if level < 0 or level > 9:
        return 4
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 3
    tabla = extractTable(database,table)
    if tabla == 3:
        return None
    else:
        try:
            for i in range(len(tabla)):
                tupla = tabla[i]
                for j in range(len(tupla)):
                    if type(tupla[j]) == str:
                        tupla[j] = zlib.compress(tupla[j].encode(), level)
                tabla[i] = tupla
            truncate(database, table)
            for registro in tabla:
                insert(database, table, registro)
            return 0
        except:
            return 1

def alterTableDecompress(database, table):
    var = None
    for i in range(7):
        var = obtenerBase(database, i)
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 3
    tabla = extractTable(database,table)
    if tabla == []:
        return None
    else:
        comprimido = False
        try:
            for i in range(len(tabla)):
                tupla = tabla[i]
                for j in range(len(tupla)):
                    if type(tupla[j]) == str or type(tupla[j]) == int or type(tupla[j]) == float or type(tupla[j]) == bool:
                        continue
                    else:
                        valor = zlib.decompress(tupla[j])
                        tupla[j] = valor.decode()
                        comprimido = True
                tabla[i] = tupla
            if comprimido == True:
                truncate(database, table)
                for registro in tabla:
                    insert(database, table, registro)
                return 0
            else:
                return 3
        except:
            return 1

def alterDatabaseEncoding(database,encoding):
    print("ejcutando")
    var = None
    mode = None
    tables = None
    mode_name = None
    if encoding == "ascii" or encoding == "utf8" or encoding == "iso-8859-1":
        pass
    else:
        return 3
    for i in range(7):
        var = obtenerBase(database, i)
        mode = i
        if var == []:
            continue
        else:
            if var >= 0 and var <= 6:
                break
            else:
                return 2
    if mode == 0 :
        mode_name = "avl"
        tables = avl_mode.showTables(database)
    elif mode == 1 :
        mode_name = "b"
        tables = b_mode.showTables(database)
    elif mode == 2 :
        mode_name = "bplus"
        tables = bplus_mode.showTables(database)
    elif mode == 3:
        mode_name = "dict"
        tables == dict_mode.showTables(database)
    elif mode == 4:
        mode_name = "isam"
        tables == isam_mode.showTables(database)
    elif mode == 5 :
        mode_name = "json"
        tables == json_mode.showTables(database)
    elif mode == 6:
        mode_name = "hash"
        tables == hash_mode.showTables(database)
    if tables is None:
        dropDatabase(database)
        createDatabase(database,mode_name)
    else:
            try:
                for i in range(len(tables)):
                    contenidoTabla = extractTable(database,tables[i])
                    for j in range(len(contenidoTabla)):
                        tupla = contenidoTabla[j]
                        for k in range(len(tupla)):
                            if type(tupla[k])==str:
                                tupla[k] = gen_convert(tupla[k],encoding)
                        contenidoTabla[j] = tupla
                        truncate(database,tables[i])
                        for register in contenidoTabla:
                            insert(database,tables[i],register)
                return 0

            except:
                return 1
#------------------------------------------- Inciso 7 ---------------------------------------------------
def make_Blockchain(lista_tuples,nameJson):
    block = blockchain()
    for tuple in lista_tuples:
        block.insertBlock(tuple,nameJson)
    return block

def safeModeOn(database,table):
    try:
        var = None
        mode = None
        tables = None
        mode_name = None
        for i in range(7):
            var = obtenerBase(database, i)
            mode = i
            if var == []:
                continue
            else:
                if var >= 0 and var <= 6:
                    break
                else:
                    return 2
        if mode == 0:
            mode_name = "avl"
            tables = avl_mode.showTables(database)
        elif mode == 1:
            mode_name = "b"
            tables = b_mode.showTables(database)
        elif mode == 2:
            mode_name = "bplus"
            tables = bplus_mode.showTables(database)
        elif mode == 3:
            mode_name = "dict"
            tables == dict_mode.showTables(database)
        elif mode == 4:
            mode_name = "isam"
            tables == isam_mode.showTables(database)
        elif mode == 5:
            mode_name = "json"
            tables == json_mode.showTables(database)
        elif mode == 6:
            mode_name = "hash"
            tables == hash_mode.showTables(database)

        dict_tables_ = open("TB_register","rb")
        dictionary = pickle.load(dict_tables_)
        dict_tables = dictionary.get(database)[1]
        table_info = dict_tables.get(table)
        if table_info[2] is False:
            table_info[2] = True
            if table_info[2] is not None:
                list_tuple = extractTable(database, table)
                nameJson = str(database) + '-' + str(table)
                BChain = make_Blockchain(list_tuple, nameJson)
                table_info[2] = BChain
    except:
        return 0

def safeModeOff(database, table):
    try:
        var = None
        mode = None
        tables = None
        mode_name = None
        for i in range(7):
            var = obtenerBase(database, i)
            mode = i
            if var == []:
                continue
            else:
                if var >= 0 and var <= 6:
                    break
                else:
                    return 2
        if mode == 0:
            mode_name = "avl"
            tables = avl_mode.showTables(database)
        elif mode == 1:
            mode_name = "b"
            tables = b_mode.showTables(database)
        elif mode == 2:
            mode_name = "bplus"
            tables = bplus_mode.showTables(database)
        elif mode == 3:
            mode_name = "dict"
            tables == dict_mode.showTables(database)
        elif mode == 4:
            mode_name = "isam"
            tables == isam_mode.showTables(database)
        elif mode == 5:
            mode_name = "json"
            tables == json_mode.showTables(database)
        elif mode == 6:
            mode_name = "hash"
            tables == hash_mode.showTables(database)

        dict_tables_ = open("TB_register", "rb")
        dictionary = pickle.load(dict_tables_)

        dict_tables = dictionary.get(database)[1]
        table_info = dict_tables.get(table)
        if table_info[2] is True:
            table_info[2] = False
            if table_info[2] is not None:

                name_JSON =str(database)+'-'+str(table)
                table_info[2].removeFilesBlock(name_JSON)
                table_info[2]=None
                return 0
    except:
        return 0
#------------------------------------------- Inciso 8 ---------------------------------------------------
def graphDSD(database):
    global Bases
    try:
        # Leemos el archivo binario de los registros de bases de datos
        fichero_lectura = open("BD_register", "rb")
        Bases = pickle.load(fichero_lectura)
        Base = Bases[database]["FK"]
        grafo = "digraph grafico1 {\n"
        grafo += "rankdir = LR\n"
        for clave in Base:
            valor = Base[clave]
            grafo+="\t"+str(valor[0]).replace(" ","")+'[label="'+str(valor[0])+'"shape=box]\n'
            grafo += "\t"+str(valor[1]).replace(" ", "") + '[label="' + str(valor[1]) + '"shape=box]\n'
            grafo+="\t"+str(valor[0]).replace(" ", "")+"->"+str(valor[1]).replace(" ", "")+"\n"
        grafo+="}"
        return grafo
    except:
        return None

def graphDF(database, table):
    global Tablas
    # Leemos el archivo binario de los registros de bases de datos y tablas
    fichero_lecturaTablas = open("TB_register", "rb")
    Tablas = pickle.load(fichero_lecturaTablas)
    Tabla = Tablas[database][table]
    ncols = Tabla["Ncol"]
    pk = Tabla["PK"]
    cols = []
    rest=[]
    grafo = "digraph grafico1 {\n"
    grafo += "rankdir = LR\n"
    for i in range(ncols):
        grafo += "\t" + str(i) + '[label=' + str(i) + 'shape=box]\n'
        cols.append(i)
    for i in range(len(cols)):
        agrega = True
        for j in range(len(pk)):
            if cols[i] == pk[j]:
                agrega = False
        if agrega == True:
            rest.append(cols[i])
    for i in range(len(pk)):
        for j in range(len(rest)):
            grafo += "\t" + str(pk[i]) + "->" + str(rest[j]) + "\n"
    grafo += "}"
    return grafo
    try:
        print("")
    except:
        return None