# -------------------------------
# Released under MIT License
# Copyright (c) 2020 TytusDb Team 18

from .avl import avlMode as avl
from .b import BMode as b
from .bplus import BPlusMode as bplus
from .dict import DictMode as dict
from .hash import HashMode as hash
from .isam import ISAMMode as isam
from .json import jsonMode as json
from . import Serializable as Serializable
from . import blockchain as block
from . import Criptografia as crypt
import hashlib
import shutil
import os
import re

#----------------Data--------------------#

def checkData():
    if not os.path.isdir("./Data"):
        os.mkdir("./Data")
    if not os.path.isfile("./Data/Data.bin"):
        dataBaseTree = {}
        Serializable.update('./Data', 'Data', dataBaseTree)
        Serializable.update('./Data', 'DataTables', dataBaseTree)
        Serializable.update('./Data', 'DataTablesRef', dataBaseTree)
    if not os.path.isdir("./Data/security"):
        os.mkdir("./Data/security")
    if not os.path.isdir("./Data/hash"):
        hash.__init__()
        hash._storage = hash.ListaBaseDatos.ListaBaseDatos()
    if not os.path.isdir("./Data/B"):
        os.mkdir("./Data/B")
        b.b = b.db.DB()

def validateIdentifier(identifier):
    # Returns true if is valid
    return re.search("^[a-zA-Z][a-zA-Z0-9#@$_]*", identifier)

def dropAll():
    dict.dropAll()
    hash.__init__()
    hash._storage = hash.ListaBaseDatos.ListaBaseDatos()
    b.b = b.db.DB()
#----------------DataBase----------------#
def createDatabase(database: str, mode: str, encoding: str) -> int:
    checkData()
    if not validateIdentifier(database):
        return 1
    data = Serializable.Read('./Data/',"Data")
    if encoding not in ['ascii', 'iso-8859-1', 'utf8']:
        return 4
    if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
        return 3
    if not data.get(database):
        if mode == 'avl':
            res = avl.createDatabase(database)
        elif mode == 'b':
            res = b.createDatabase(database)
        elif mode == 'bplus':
            res = bplus.createDatabase(database)
        elif mode == 'dict':
            res = dict.createDatabase(database)
        elif mode == 'isam':
            res = isam.createDatabase(database)
        elif mode == 'json':
            res = json.createDatabase(database)
        elif mode == 'hash':
            res = hash.createDatabase(database)
        if not res:
            data[database] = [database,[mode],encoding]
            Serializable.update('./Data', 'Data', data)
        return res
    else:
        return 2

def showDatabases() -> list:
    checkData()
    data = Serializable.Read('./Data/',"Data")
    temp = []
    for x in list(data.values()):
        temp.append(x[0])
    return temp

def alterDatabase(databaseOld, databaseNew) -> int:
    checkData()
    try:
        if not validateIdentifier(databaseNew):
            return 1
        data = Serializable.Read('./Data/',"Data")
        db = data.get(databaseOld)
        if db:
            if data.get(databaseNew):
                return 3
            tablas = []
            if 'avl' in db[1]:
                res = avl.alterDatabase(databaseOld, databaseNew)
                tablas += avl.showTables(databaseNew)
            if 'b' in db[1]:
                res = b.alterDatabase(databaseOld, databaseNew)
                tablas += b.showTables(databaseNew)
            if 'bplus'in db[1]:
                res = bplus.alterDatabase(databaseOld, databaseNew)
                tablas += bplus.showTables(databaseNew)
            if 'dict'in db[1]:
                res = dict.alterDatabase(databaseOld, databaseNew)
                tablas += dict.showTables(databaseNew)
            if 'isam'in db[1]:
                res = isam.alterDatabase(databaseOld, databaseNew)
                tablas += isam.showTables(databaseNew)
            if 'json'in db[1]:
                res = json.alterDatabase(databaseOld, databaseNew)
                tablas += json.showTables(databaseNew)
            if 'hash'in db[1]:
                res = hash.alterDatabase(databaseOld, databaseNew)
                tablas += hash.showTables(databaseNew)
            if not res:
                del data[databaseOld]
                db[0] = databaseNew
                data[databaseNew] = db
                Serializable.update('./Data', 'Data', data)
                if len(tablas):
                    dataTable = Serializable.Read('./Data/',"DataTables")
                    dataTableRef = Serializable.Read('./Data/',"DataTablesRef")
                    for x in tablas:
                        tab = dataTable.get(databaseOld+"_"+x)
                        if tab:
                            tab[0] = databaseNew
                            dataTable[databaseNew+"_"+x] = tab
                            del dataTable[databaseOld+"_"+x]
                        else:
                            dataTableRef[x+"-"+databaseNew] = dataTableRef.get(x+"-"+databaseOld)
                            del dataTableRef[x+"_"+databaseOld]
                    Serializable.update('./Data', 'DataTables', dataTable)
                    Serializable.update('./Data', 'DataTablesRef', dataTableRef)
                    Serializable.update('./Data', 'Data', data)

            return res
        else:
            return 2
    except:
        return 1

def dropDatabase(database: str) -> int: 
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            mode =db[1][0] 
            if 'avl' in db[1]:
                if mode == 'avl':
                    res = avl.dropDatabase(database)
                else:
                    avl.dropDatabase(database)
            if 'b' in db[1]:
                if mode == 'b':
                    res = b.dropDatabase(database)
                else:
                    b.dropDatabase(database)
            if 'bplus' in db[1]:
                if mode == 'bplus':
                    res = bplus.dropDatabase(database)
                else:
                    bplus.dropDatabase(database)
            if 'dict' in db[1]:
                if mode == 'dict':
                    res = dict.dropDatabase(database)
                else:
                    dict.dropDatabase(database)
            if 'isam' in db[1]:    
                if mode == 'isam':
                    res = isam.dropDatabase(database)
                else:
                    isam.dropDatabase(database)
            if 'json' in db[1]:
                if mode == 'json':
                    res = json.dropDatabase(database)
                else:
                    json.dropDatabase(database)
            if 'hash' in db[1]:
                if mode == 'hash':
                    res = hash.dropDatabase(database)
                else:
                    hash.dropDatabase(database)
            if not res:
                del data[database]
                Serializable.update('./Data', 'Data', data)
            return res
        else:
            return 2
    except:
        return 1

def alterDatabaseMode(database: str, mode: str) -> int:
    checkData()
    # try:
    data = Serializable.Read('./Data/',"Data")
    db = data.get(database)
    if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
        return 4
    if db:
        tablas = []
        mod =db[1][0]
        if mod== mode:
            return 0
        
        if mod == 'avl':
            tablas = avl.showTables(database)
            res = cambioTablas(avl, tablas, database, mode, db)
            if not res:
                avl.dropDatabase(database)
        elif mod == 'b':
            tablas = b.showTables(database)
            res = cambioTablas(b, tablas, database, mode, db)
            if not res:
                b.dropDatabase(database)
        elif mod == 'bplus':
            tablas = bplus.showTables(database)
            res = cambioTablas(bplus, tablas, database, mode, db)
            if not res:
                bplus.dropDatabase(database)
        elif mod == 'dict':
            tablas = dict.showTables(database)
            res = cambioTablas(dict, tablas, database, mode, db)
            if not res:
                dict.dropDatabase(database)
        elif mod == 'isam':
            tablas = isam.showTables(database)
            res = cambioTablas(isam, tablas, database, mode, db)
            if not res:
                isam.dropDatabase(database)
        elif mod == 'json':
            tablas = json.showTables(database)
            res = cambioTablas(json, tablas, database, mode, db)
            if not res:
                json.dropDatabase(database)
        elif mod == 'hash':
            tablas = hash.showTables(database)
            res = cambioTablas(hash, tablas, database, mode, db)
            if not res:
                hash.dropDatabase(database)
        data[database] = db
        Serializable.update('./Data', 'Data', data)
        return res
    else:
        return 2
    # except:
        # return 1

def cambioTablas(modo, tablas, database, mode, db):
    checkData()
    if mode in db:
        db[1].pop(0)
        db[1].remove(mode)
        db[1].insert(0,mode)
    else:
        db[1].pop(0)
        db[1].insert(0,mode)
        if mode == 'avl':
            avl.createDatabase(database)
            mod = avl
        elif mode == 'b':
            b.createDatabase(database)
            mod = b
        elif mode == 'bplus':
            bplus.createDatabase(database)
            mod = bplus
        elif mode == 'dict':
            dict.createDatabase(database)
            mod = dict
        elif mode == 'isam':
            isam.createDatabase(database)
            mod = isam
        elif mode == 'json':
            json.createDatabase(database)
            mod = json
        elif mode == 'hash':
            hash.createDatabase(database)
            mod = hash
    import csv
    dataTable = Serializable.Read('./Data/',"DataTables")
    dataTableRef = Serializable.Read('./Data/',"DataTablesRef")
    for x in tablas:
        tab = dataTable.get(database+"_"+x)
        if tab:
            tab[1] = mode
            mod.createTable(database, x, tab[2])
            if len(tab[3]):
                mod.alterAddPK(database, x, tab[3])
        else:
            mod.createTable(database, x, dataTableRef[x+"_"+database])
        file = open("./data/change.csv", "w", newline='', encoding='utf-8')
        spamreader = csv.writer(file)
        tipado = []
        for y in modo.extractTable(database, x):
            tipado_tupla = []
            for t in y:
                tipado_tupla.append(type(t))
            tipado.append(tipado_tupla)
            spamreader.writerow(y)
        file.close()
        mod.loadCSV("./data/change.csv", database, x, tipado)
        os.remove("./data/change.csv")
        Serializable.update('./Data', 'DataTables', dataTable)
    return 0

def alterDatabaseEncoding(database: str, encoding: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        if encoding not in ['ascii', 'iso-8859-1', 'utf8']:
            return 3
        db = data.get(database)
        if db:
            res = showTables(database)
            if len(res):
                for x in res:
                    row = extractTable(database, x)
                    if len(row):
                        for l in row:
                            for g in l:
                                if type(g) == str:
                                    g.encode(encoding)
            db[2] == encoding
            data[database] = db
            Serializable.update('./Data', 'Data', data)
            return 0
        else:
            return 2
    except:
        return 1

#----------------Table-------------------#

def createTable(database: str, table: str, numberColumns: int) -> int:
    checkData()
    try:
        if not validateIdentifier(table):
            return 1
        data = Serializable.Read('./Data/',"Data")
        dataTable = Serializable.Read('./Data/',"DataTables")
        dataTableRef = Serializable.Read('./Data/',"DataTablesRef")
        db = data.get(database)
        if db:
            mode =db[1][0] 
            if mode == 'avl':
                res = avl.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'avl', numberColumns, [], -2]
            elif mode == 'b':
                res = b.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'b', numberColumns, [], -2]
            elif mode == 'bplus':
                res = bplus.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'bplus', numberColumns, [], -2]
            elif mode == 'dict':
                res = dict.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'dict', numberColumns, [], -2]
            elif mode == 'isam':
                res = isam.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'isam', numberColumns, [], -2]
            elif mode == 'json':
                res = json.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'json', numberColumns, [], -2]
            elif mode == 'hash':
                res = hash.createTable(database, table, numberColumns)
                dataTable[database+"_"+table] = [table, 'hash', numberColumns, [], -2]
            if not res:
                createRefTAbles(database, 'Table_REF_FK_'+table, 6, mode)
                createRefTAbles(database, 'Table_REF_IndexU_'+table, 4, mode)
                createRefTAbles(database, 'Table_REF_Index_'+table, 4, mode)
                dataTableRef['Table_REF_FK_'+table+"_"+database] = 6
                dataTableRef['Table_REF_IndexU_'+table+"_"+database] = 4
                dataTableRef['Table_REF_Index_'+table+"_"+database] = 4
            Serializable.update('./Data', 'DataTables', dataTable)
            Serializable.update('./Data', 'DataTablesRef', dataTableRef)
            return res
        else:
            return 2
    except:
        return 1

def showTables(database: str) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = []
            if 'avl' in db[1]:
                res = res + avl.showTables(database)
            if 'b' in db[1]:
                res = res + b.showTables(database)
            if 'bplus' in db[1]:
                res = res + bplus.showTables(database)
            if 'dict' in db[1]:
                res = res + dict.showTables(database)
            if 'isam' in db[1]:
                res = res + isam.showTables(database)
            if 'json' in db[1]:
                res = res + json.showTables(database)
            if 'hash' in db[1]:
                res = res + hash.showTables(database)
            if res:
                ret = []
                dataTable = Serializable.Read('./Data/',"DataTables")
                for x in res:
                    tab = dataTable.get(database+"_"+x)
                    if tab:
                        ret.append(x)
            return ret
        else:
            return None
    except:
        return None

def extractTable(database: str, table: str) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.extractTable(database, table)
                elif tab[1] == 'b':
                    res = b.extractTable(database, table)
                elif tab[1] == 'bplus':
                    res = bplus.extractTable(database, table)
                elif tab[1] == 'dict':
                    res = dict.extractTable(database, table)
                elif tab[1] == 'isam':
                    res = isam.extractTable(database, table)
                elif tab[1] == 'json':
                    res = json.extractTable(database, table)
                elif tab[1] == 'hash':
                    res = hash.extractTable(database, table)
                if len(res) and tab[4]!=-2:
                    import zlib
                    for tupla in res:
                        for x in tupla:
                            if type(x) == str:
                                index = tupla.index(x)
                                tupla[index] = zlib.decompress(bytes.fromhex(x)).decode()
                return res
        return None
    except:
        return None

def extractRangeTable(database: str, table: str, columnNumber: int, 
                      lower: any, upper: any) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            res = None
            if tab[1] == 'avl':
                res = avl.extractRangeTable(database, table, columnNumber, lower, upper)
            elif tab[1] == 'b':
                res = b.extractRangeTable(database, table, columnNumber, lower, upper)
            elif tab[1] == 'bplus':
                res = bplus.extractRangeTable(database, table, columnNumber, lower, upper)
            elif tab[1] == 'dict':
                res = dict.extractRangeTable(database, table, columnNumber, lower, upper)
            elif tab[1] == 'isam':
                res = isam.extractRangeTable(database, table, columnNumber, lower, upper)
            elif tab[1] == 'json':
                res = json.extractRangeTable(database, table, lower, upper)
            elif tab[1] == 'hash':
                res = hash.extractRangeTable(database, table, columnNumber, lower, upper)
            if len(res) and tab[4]!=-2:
                    import zlib
                    for tupla in res:
                        for x in tupla:
                            if type(x) == str:
                                index = tupla.index(x)
                                tupla[index] = zlib.decompress(bytes.fromhex(x)).decode()
            return res
        else:
            return 2
    except:
        return 1

def alterAddPK(database: str, table: str, columns: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        db = data.get(database)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterAddPK(database, table, columns)
                elif tab[1] == 'b':
                    res = b.alterAddPK(database, table, columns)
                elif tab[1] == 'bplus':
                    res = bplus.alterAddPK(database, table, columns)
                elif tab[1] == 'dict':
                    res = dict.alterAddPK(database, table, columns)
                elif tab[1] == 'isam':
                    res = isam.alterAddPK(database, table, columns)
                elif tab[1] == 'json':
                    res = json.alterAddPK(database, table, columns)
                elif tab[1] == 'hash':
                    res = hash.alterAddPK(database, table, columns)
                if not res:
                    tab[3] = columns
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1

def alterDropPK(database: str, table: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterDropPK(database, table)
                elif tab[1] == 'b':
                    res = b.alterDropPK(database, table)
                elif tab[1] == 'bplus':
                    res = bplus.alterDropPK(database, table)
                elif tab[1] == 'dict':
                    res = dict.alterDropPK(database, table)
                elif tab[1] == 'isam':
                    res = isam.alterDropPK(database, table)
                elif tab[1] == 'json':
                    res = json.alterDropPK(database, table)
                elif tab[1] == 'hash':
                    res = hash.alterDropPK(database, table)
                if not res:
                    tab[3] = []
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1

def alterTableAddFK(database: str, table: str, indexName: str, 
                    columns: list,  tableRef: str, columnsRef: list) -> int:
    try:
        if len(columnsRef)!=len(columns):
            return 4
        for x in columns:
            if type(x)!=int:
                return 1
        for x in columnsRef:
            if type(x)!=int:
                return 1
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            dataTable = Serializable.Read('./Data/',"DataTables")
            if min(columnsRef) < 0 and min(columns) < 0 and max(columnsRef) >= tabref[2] and max(columns)>= tab[2]:
                return 1
            tab = dataTable.get(database+"_"+table)
            tabref = dataTable.get(database+"_"+tableRef)
            if tab and tableRef:
                mode =db[1][0]
                register = [indexName, database, table, columns, tableRef, columnsRef]
                res = registerRefTAbles(database, 'Table_REF_FK_'+table, register, mode)
                return res  
            return 3
        else:
            return 2
    except:
        return 1

def createRefTAbles(database, tableref, numberColumns, mode):
    if mode == 'avl':
        res = avl.createTable(database, tableref, numberColumns)
        res = avl.alterAddPK(database,tableref,[0])
    elif mode == 'b':
        res = b.createTable(database, tableref, numberColumns)
        res = b.alterAddPK(database,tableref,[0])
    elif mode == 'bplus':
        res = bplus.createTable(database, tableref, numberColumns)
        res = bplus.alterAddPK(database,tableref,[0])
    elif mode == 'dict':
        res = dict.createTable(database, tableref, numberColumns)
        res = dict.alterAddPK(database,tableref,[0])
    elif mode == 'isam':
        res = isam.createTable(database, tableref, numberColumns)
        res = isam.alterAddPK(database,tableref,[0])
    elif mode == 'json':
        res = json.createTable(database, tableref, numberColumns)
        res = json.alterAddPK(database,tableref,[0])
    elif mode == 'hash':
        res = hash.createTable(database, tableref, numberColumns)
        res = hash.alterAddPK(database,tableref,[0])
    return res

def registerRefTAbles(database, tableref, register, mode):
    if mode == 'avl':
        res = avl.insert(database, tableref, register)
    elif mode == 'b':
        res = b.insert(database, tableref, register)
    elif mode == 'bplus':
        res = bplus.insert(database, tableref, register)
    elif mode == 'dict':
        res = dict.insert(database, tableref, register)
    elif mode == 'isam':
        res = isam.insert(database, tableref, register)
    elif mode == 'json':
        res = json.insert(database, tableref, register)
    elif mode == 'hash':
        res = hash.insert(database, tableref, register)
    if res:
        return 1
    return res

def dropRefTAbles(database, tableref, mode, index):
    if mode == 'avl':
        res = avl.delete(database, tableref,[index])
    elif mode == 'b':
        res = b.delete(database, tableref,[index])
    elif mode == 'bplus':
        res = bplus.delete(database, tableref,[index])
    elif mode == 'dict':
        res = dict.delete(database, tableref,[index])
    elif mode == 'isam':
        res = isam.delete(database, tableref,[index])
    elif mode == 'json':
        res = json.delete(database, tableref,[index])
    elif mode == 'hash':
        res = hash.delete(database, tableref,[index])
    if res:
        return 1
    return res

def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            dataTable = Serializable.Read('./Data/',"DataTablesRef")
            tab = dataTable.get('Table_REF_FK_'+table+"_"+database)
            if tab:
                res = dropRefTAbles(database, 'Table_REF_FK_'+table, db[1][0], indexName)
                if not res:
                    del dataTable['Table_REF_FK_'+table+"_"+database]
                    Serializable.update('./Data', 'DataTablesRef', dataTable)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        for x in columns:
            if type(x)!=int:
                return 1
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            dataTable = Serializable.Read('./Data/',"DataTables")
            tab = dataTable.get(database+"_"+table)
            if min(columns) < 0 and max(columns)>= tab[2]:
                return 1
            if tab:
                mode =db[1][0]
                register = [indexName, database, table, columns]
                res = registerRefTAbles(database, 'Table_REF_IndexU_'+table, register, mode)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            dataTable = Serializable.Read('./Data/',"DataTablesRef")
            tab = dataTable.get('Table_REF_FK_'+table+"_"+database)
            if tab:
                res = dropRefTAbles(database, 'Table_REF_IndexU_'+table, db[1][0], indexName)
                if not res:
                    del dataTable['Table_REF_IndexU_'+table+"_"+database]
                    Serializable.update('./Data', 'DataTablesRef', dataTable)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        for x in columns:
            if type(x)!=int:
                return 1
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            dataTable = Serializable.Read('./Data/',"DataTables")
            tab = dataTable.get(database+"_"+table)
            if min(columns) < 0 and max(columns)>= tab[2]:
                return 1
            if tab:
                mode =db[1][0]
                register = [indexName, database, table, columns]
                res = registerRefTAbles(database, 'Table_REF_Index_'+table, register, mode)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            dataTable = Serializable.Read('./Data/',"DataTablesRef")
            tab = dataTable.get('Table_REF_FK_'+table+"_"+database)
            if tab:
                res = dropRefTAbles(database, 'Table_REF_Index_'+table, db[1][0], indexName)
                if not res:
                    del dataTable['Table_REF_Index_'+table+"_"+database]
                    Serializable.update('./Data', 'DataTablesRef', dataTable)
                return res
            return 3
        else:
            return 2
    except:
        return 1


def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    checkData()
    try:
        if not validateIdentifier(tableNew):
            return 1
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+tableOld)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'b':
                    res = b.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'bplus':
                    res = bplus.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'dict':
                    res = dict.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'isam':
                    res = isam.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'json':
                    res = json.alterTable(database, tableOld, tableNew)
                elif tab[1] == 'hash':
                    res = hash.alterTable(database, tableOld, tableNew)
                if not res:
                    tab[0]=tableNew
                    dataTable[database+"_"+tableNew] = tab
                    del dataTable[database+"_"+tableOld]
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1

def alterAddColumn(database: str, table: str, default: any) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterAddColumn(database, table, default)
                elif tab[1] == 'b':
                    res = b.alterAddColumn(database, table, default)
                elif tab[1] == 'bplus':
                    res = bplus.alterAddColumn(database, table, default)
                elif tab[1] == 'dict':
                    res = dict.alterAddColumn(database, table, default)
                elif tab[1] == 'isam':
                    res = isam.alterAddColumn(database, table, default)
                elif tab[1] == 'json':
                    res = json.alterAddColumn(database, table, default)
                elif tab[1] == 'hash':
                    res = hash.alterAddColumn(database, table, default)
                if not res:
                    tab[2]+=1
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1

def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'b':
                    res = b.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'bplus':
                    res = bplus.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'dict':
                    res = dict.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'isam':
                    res = isam.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'json':
                    res = json.alterDropColumn(database, table, columnNumber)
                elif tab[1] == 'hash':
                    res = hash.alterDropColumn(database, table, columnNumber)
                if not res:
                        tab[2]+=1
                        Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1

def dropTable(database: str, table: str) -> int: 
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                mod = None
                if tab[1] == 'avl':
                    res = avl.dropTable(database, table)
                    mod = avl
                elif tab[1] == 'b':
                    res = b.dropTable(database, table)
                    mod = b
                elif tab[1] == 'bplus':
                    res = bplus.dropTable(database, table)
                    mod = bplus
                elif tab[1] == 'dict':
                    res = dict.dropTable(database, table)
                    mod = dict
                elif tab[1] == 'isam':
                    res = isam.dropTable(database, table)
                    mod = isam
                elif tab[1] == 'json':
                    res = json.dropTable(database, table)
                    mod = json
                elif tab[1] == 'hash':
                    res = hash.dropTable(database, table)
                    mod = hash
                if not res:
                    if not len(mod.showTables(database)) and db[1][0]!=tab[1]:
                        mod.dropDatabase(database)
                        db[1].remove(tab[1])
                    data[database] = db
                    del dataTable[database+"_"+table]
                    Serializable.update('./Data', 'Data', data)
                    Serializable.update('./Data', 'DataTables', dataTable)
                return res
            else:
                return 3
        else:
            return 2
    except:
        return 1

def alterTableMode(database: str, table: str, mode: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
            return 4
        if db:
            if not tab:
                return 3
            if mode == tab[1]:
                    return 4
            tuplas = None
            if mode not in db[1]:
                db[1].append(mode)

            if  tab[1] == 'avl':
                tuplas = avl.extractTable(database, table)
                modo = avl
                avl.dropTable(database, table)

            elif  tab[1] == 'b':
                tuplas = b.extractTable(database, table)
                b.dropTable(database, table)
                modo = b

            elif  tab[1] == 'bplus':
                tuplas = bplus.extractTable(database, table)
                bplus.dropTable(database, table)
                modo = bplus

            elif  tab[1] == 'dict':
                tuplas = dict.extractTable(database, table)
                dict.dropTable(database, table)
                modo = dict

            elif  tab[1] == 'isam':
                tuplas = isam.extractTable(database, table)
                isam.dropTable(database, table)
                modo = isam

            elif  tab[1] == 'json':
                tuplas = json.extractTable(database, table)
                json.dropTable(database, table)
                modo = json

            elif  tab[1] == 'hash':
                tuplas = hash.extractTable(database, table)
                hash.dropTable(database, table)
                modo = hash

            if tab[1] != db[1][0] and tuplas!=None:
                if not len(modo.showTables(database)):
                    modo.dropDatabase(database)
                    db[1].remove(tab[1])

            if tuplas!=None:
                if mode == 'avl':
                    mod = avl
                elif mode == 'b':
                    mod = b
                elif mode == 'bplus':
                    mod = bplus
                elif mode == 'isam':
                    mod = isam
                elif mode == 'dict':
                    mod = dict
                elif mode == 'json':
                    mod = json
                elif mode == 'hash':
                    mod = hash
                import csv
                tipado = []
                file = open("./data/change.csv", "w", newline='', encoding='utf-8')
                spamreader = csv.writer(file)
                if mod.showTables(database) == None:
                    mod.createDatabase(database)
                mod.createTable(database, table, tab[2])
                for y in tuplas:
                    tipado_tupla = []
                    for t in y:
                        tipado_tupla.append(type(t))
                    tipado.append(tipado_tupla)
                    spamreader.writerow(y)
                file.close()
                if len(tab[3]):
                    mod.alterAddPK(database, table, tab[3])
                mod.loadCSV("./data/change.csv", database, table, tipado)
                os.remove("./data/change.csv")
                data[database] = db
                tab[1] = mode
                Serializable.update('./Data', 'Data', data)
                Serializable.update('./Data', 'DataTables', dataTable)
                return 0
            else:
                return 3
        else:
            return 2
    except:
        return 1        

def safeModeOn(database: str, table: str)->int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if os.path.isfile("./Data/security/"+database+"_"+table+".json"):
                    return 4
                block.blockchain().crear(database, table)
                return 0
            return 3
        return 2
    except:
        return 1

def safeModeOff(database: str, table: str)->int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if not os.path.isfile("./Data/security/"+database+"_"+table+".json"):
                    return 4
                os.remove("./Data/security/"+database+"_"+table+".json")
                return 0
            return 3
        return 2
    except:
        return 1
#----------------Tupla-------------------#
def insert(database: str, table: str, register: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                register2 = register[:]
                for x in register:
                    if type(x)==str:
                        x.encode(db[2], "strict")
                        if tab[4] != -2:
                            import zlib
                            index = register.index(x)
                            register[index] = zlib.compress(x.encode(), tab[4]).hex()  
                if tab[1] == 'avl' :
                    res = avl.insert(database, table, register)
                elif tab[1] == 'b':
                    res = b.insert(database, table, register)
                elif tab[1] == 'bplus':
                    res = bplus.insert(database, table, register)
                elif tab[1] == 'dict':
                    res = dict.insert(database, table, register)
                elif tab[1] == 'isam':
                    res = isam.insert(database, table, register)
                elif tab[1] == 'json':
                    res = json.insert(database, table, register)
                elif tab[1] == 'hash':
                    res = hash.insert(database, table, register)
                if not res:
                    if os.path.isfile("./Data/security/"+database+"_"+table+".json"):
                        block.blockchain().insert(register2, database, table)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def loadCSV(file: str, database: str, table: str) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                res = []
                tabla = []
                import csv
                ff = open("./data/change.csv", "w", newline='', encoding='utf-8')
                spamreader = csv.writer(ff)
                with open(file, 'r', encoding='utf-8-sig') as fil:
                    reader = csv.reader(fil, delimiter=',')
                    for y in reader:
                        for g in y:
                            if type(g) == str:
                                g.encode(db[2], errors='strict')
                                if tab[4] != -2:
                                    import zlib
                                    index = y.index(g)
                                    y[index] = zlib.compress(g.encode(), tab[4]).hex()  
                        spamreader.writerow(y)
                        tabla.append(y)
                    fil.close()
                    ff.close()
                file = "./data/change.csv"
                if tab[1] == 'avl':
                    res = avl.loadCSV(file, database, table, None)
                elif tab[1] == 'b':
                    res = b.loadCSV(file, database, table, None)
                elif tab[1] == 'bplus':
                    res = bplus.loadCSV(file, database, table, None)
                elif tab[1] == 'dict':
                    res = dict.loadCSV(file, database, table, None)
                elif tab[1] == 'isam':
                    res = isam.loadCSV(file, database, table, None)
                elif tab[1] == 'json':
                    res = json.loadCSV(file, database, table, None)
                elif tab[1] == 'hash':
                    res = hash.loadCSV(file, database, table, None)
                if len(tabla):
                    if os.path.isfile("./Data/security/"+database+"_"+table+".json"):
                        i=0
                        for r in res:
                            if r ==0:
                                block.blockchain().insert(tabla[i], database, table)
                        i+=1
                return res
            return []
        else:
            return []
    except:
        return []

def extractRow(database: str, table: str, columns: list) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[4] != -2:
                    import zlib
                    for x in columns:
                        if type(x) == str:
                            index = columns.index(x)
                            columns[index] = zlib.compress(x.encode(), tab[4]).hex()
                if tab[1] == 'avl':
                    res = avl.extractRow(database, table, columns)
                elif tab[1] == 'b':
                    res = b.extractRow(database, table, columns)
                elif tab[1] == 'bplus':
                    res = bplus.extractRow(database, table, columns)
                elif tab[1] == 'dict':
                    res = dict.extractRow(database, table, columns)
                elif tab[1] == 'isam':
                    res = isam.extractRow(database, table, columns)
                elif tab[1] == 'json':
                    res = json.extractRow(database, table, columns)
                elif tab[1] == 'hash':
                    res = hash.extractRow(database, table, columns)
                if len(res) and tab[4]!=-2:
                    import zlib
                    for x in res:
                        if type(x) == str:
                            index = res.index(x)
                            res[index] = zlib.decompress(bytes.fromhex(x)).decode()
                return res
            return 3
        else:
            return 2
    except:
        return 1

def update(database: str, table: str, register: dict, columns: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                register2 = {}
                register2.update(register)
                row = extractRow(database, table, columns)
                for x in list(register.values()):
                    if type(x)==str:
                        x.encode(db[2], "strict")
                if tab[4] != -2:
                    import zlib
                    for x in register.keys():
                        if type(register[x]) == str:
                            register[x] = zlib.compress(register[x].encode(), tab[4]).hex()
                if tab[1] == 'avl':
                    res = avl.update(database, table, register, columns)
                elif tab[1] == 'b':
                    res = b.update(database, table, register, columns)
                elif tab[1] == 'bplus':
                    res = bplus.update(database, table, register, columns)
                elif tab[1] == 'dict':
                    res = dict.update(database, table, register, columns)
                elif tab[1] == 'isam':
                    res = isam.update(database, table, register, columns)
                elif tab[1] == 'json':
                    res = json.update(database, table, register, columns)
                elif tab[1] == 'hash':
                    res = hash.update(database, table, register, columns)
                if not res:
                    if os.path.isfile('./Data/security/'+database+"_"+table+".json"):
                        row2 = row[:]
                        values = list(register2.values())
                        for x in list(register2.keys()):
                            row2[x] = values[x]
                        block.blockchain().CompararHash(row, row2, database, table)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def delete(database: str, table: str, columns: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                row = extractRow(database, table, columns)
                if tab[1] == 'avl':
                    res = avl.delete(database, table, columns)
                elif tab[1] == 'b':
                    res = b.delete(database, table, columns)
                elif tab[1] == 'bplus':
                    res = bplus.delete(database, table, columns)
                elif tab[1] == 'dict':
                    res = dict.delete(database, table, columns)
                elif tab[1] == 'isam':
                    res = isam.delete(database, table, columns)
                elif tab[1] == 'json':
                    res = json.delete(database, table, columns)
                elif tab[1] == 'hash':
                    res = hash.delete(database, table, columns)
                if not res:
                    if os.path.isfile('./Data/security/'+database+"_"+table+".json"):
                        block.blockchain().EliminarHash(row, database, table)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def truncate(database: str, table: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = avl.truncate(database, table)
                elif tab[1] == 'b':
                    res = b.truncate(database, table)
                elif tab[1] == 'bplus':
                    res = bplus.truncate(database, table)
                elif tab[1] == 'dict':
                    res = dict.truncate(database, table)
                elif tab[1] == 'isam':
                    res = isam.truncate(database, table)
                elif tab[1] == 'json':
                    res = json.truncate(database, table)
                elif tab[1] == 'hash':
                    res = hash.truncate(database, table)
                if not res:
                    if os.path.isfile('./Data/security/'+database+"_"+table+".json"):
                        block.blockchain().crear(database, table)
                return res
            return 3
        else:
            return 2
    except:
        return 1
#------------Nuevas Funciones-------------#

#--------------Encrypt-------------------#
def encrypt(backup:str, password: str):
    checkData()
    try:
        return crypt.encrypt(backup, password, password)
    except:
        return None

def decrypt(backup:str, password: str):
    checkData()
    try:
        return crypt.decrypt(backup, password, password)
    except:
        return None

#--------------Checksum------------------#

def checksumDatabase(database: str, mode: str) -> str:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            tables = []
            if 'avl' in db[1]:
                tables += avl.showTables(database)
            if 'b' in db[1]:
                tables += b.showTables(database)
            if 'bplus'in db[1]:
                tables += bplus.showTables(database)
            if 'dict'in db[1]:
                tables += dict.showTables(database)
            if 'isam'in db[1]:
                tables += isam.showTables(database)
            if 'json'in db[1]:
                tables += json.showTables(database)
            if 'hash'in db[1]:
                tables += hash.showTables(database)

            if len(tables):
                dataTable = Serializable.Read('./Data/',"DataTables")
                if mode == 'MD5':
                    hash_md5 = hashlib.md5()
                elif mode == 'SHA256':
                    hash_md5 = hashlib.sha256()
                else:
                    return None
                for x in tables:
                    tab = dataTable.get(database+"_"+x)
                    if tab:
                        mod = tab[1]
                    else:
                        mod = db[1][0]
                    if mod == 'avl':
                        hash_md5.update(open('./Data/avlMode/'+database+"_"+x+".tbl",'rb').read())
                    elif mod == 'b':
                        hash_md5.update(open('./Data/B/'+database+"-"+x+"-b.bin",'rb').read())
                    elif mod == 'isam':
                        hash_md5.update(open('./Data/ISAMMode/tables/'+database+x+".bin",'rb').read())
                    elif mod == 'bplus':
                        hash_md5.update(open('./Data/BPlusMode/'+database+"/"+x+"/"+x+".bin",'rb').read())
                    elif mod == 'dict':
                        hash_md5.update(open('./Data/dict/'+database+"/"+x+".bin",'rb').read())
                    elif mod == 'json':
                        hash_md5.update(open('./Data/json/'+database+"-"+x,'rb').read())
                    elif mod == 'hash':
                        hash_md5.update(open('./Data/hash/'+database+"/"+x+".bin",'rb').read())
                return hash_md5.hexdigest()
        return None
    except:
        return None

def checksumTable(database: str, table:str, mode: str) -> str:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                mod=tab[1]
                if mode == 'MD5':
                    hash_md5 = hashlib.md5()
                elif mode == 'SHA256':
                    hash_md5 = hashlib.sha256()
                else:
                    return None
                if mod == 'avl':
                    hash_md5.update(open('./Data/avlMode/'+database+"_"+table+".tbl",'rb').read())
                elif mod == 'b':
                    hash_md5.update(open('./Data/B/'+database+"-"+table+"-b.bin",'rb').read())
                elif mod == 'isam':
                    hash_md5.update(open('./Data/ISAMMode/tables/'+database+table+".bin",'rb').read())
                elif mod == 'bplus':
                    hash_md5.update(open('./Data/BPlusMode/'+database+"/"+table+"/"+table+".bin",'rb').read())
                elif mod == 'dict':
                    hash_md5.update(open('./Data/dict/'+database+"/"+table+".bin",'rb').read())
                elif mod == 'json':
                    hash_md5.update(open('./Data/json/'+database+"-"+table,"rb").read())
                elif mod == 'hash':
                    hash_md5.update(open('./Data/hash/'+database+"/"+table+".bin",'rb').read())
                return hash_md5.hexdigest()
        return None
    except:
        return None

#--------------Compress-------------------#

def alterDatabaseCompress(database, level):
    checkData()
    data = Serializable.Read('./Data/', "Data")
    db = data.get(database)
    dataTable = Serializable.Read('./Data/', "DataTables")
    if type(level) != int:
        return 4
    elif (level < 0 or level > 9) and level != -1:
        return 4
    if db:
        try:
            for table in showTables(database):
                tab = dataTable.get(database + "_" + table)
                if tab and tab[4] == -2:
                    tuplas = extractTable(database, table)
                    if tuplas != None:
                        import zlib
                        mod = None
                        if tab[1] == 'avl':
                            mod = avl
                        elif tab[1] == 'b':
                            mod = b
                        elif tab[1] == 'bplus':
                            mod = bplus
                        elif tab[1] == 'hash':
                            mod = hash
                        elif tab[1] == 'json':
                            mod = json
                        elif tab[1] == 'dict':
                            mod = dict
                        elif tab[1] == 'isam':
                            mod = isam
                        import csv
                        file = open("./data/change.csv", "w", newline='', encoding='utf-8')
                        spamreader = csv.writer(file)
                        tipado = []
                        compressed_lista = []
                        for y in tuplas:
                            compressed_data = []
                            for item in y:
                                compressed_item = item
                                if type(item) == bytes or type(item) == bytearray:
                                    compressed_item = zlib.compress(item, level).hex()
                                elif type(item) == str:
                                    compressed_item = zlib.compress(item.encode(), level).hex()
                                compressed_data.append(compressed_item)
                            compressed_lista.append(compressed_data)
                            
                        for y in compressed_lista:
                            tipado_tupla = []
                            for t in y:
                                tipado_tupla.append(type(t))
                            tipado.append(tipado_tupla)
                            spamreader.writerow(y)
                        file.close()
                        truncate(database, table)
                        mod.loadCSV("./data/change.csv", database, table, tipado)
                        os.remove("./data/change.csv")
                    
        except:
            return 1
        for table in showTables(database):
            tab = dataTable.get(database + "_" + table)
            if tab:
                tab[4] = level
                dataTable[database+"_"+table] = tab
        Serializable.update('./Data', 'DataTables', dataTable)
        return 0
    else:
       return 2

def alterDatabaseDecompress(database):
    checkData()
    data = Serializable.Read('./Data/', "Data")
    db = data.get(database)
    dataTable = Serializable.Read('./Data/', "DataTables")
    if db:
        try:
            for table in showTables(database):
                tab = dataTable.get(database + "_" + table)
                if tab and tab[4] != -2:
                    tuplas = extractTable(database, table)
                    if tuplas != None:
                        truncate(database, table)
                        import zlib
                        mod = None
                        if tab[1] == 'avl':
                            mod = avl
                        elif tab[1] == 'b':
                            mod = b
                        elif tab[1] == 'bplus':
                            mod = bplus
                        elif tab[1] == 'hash':
                            mod = hash
                        elif tab[1] == 'json':
                            mod = json
                        elif tab[1] == 'dict':
                            mod = dict
                        elif tab[1] == 'isam':
                            mod = isam
                        import csv
                        file = open("./data/change.csv", "w", newline='', encoding='utf-8')
                        spamreader = csv.writer(file)
                        tipado = []
                        compressed_lista = []
                        for y in tuplas:
                            compressed_data = []
                            for item in y:
                                compressed_item = item
                                if type(item) == str:
                                    compressed_item     = zlib.decompress(bytes.fromhex(item))
                                    compressed_item = compressed_item.decode()
                                compressed_data.append(compressed_item)
                            compressed_lista.append(compressed_data)

                        for y in compressed_lista:
                            tipado_tupla = []
                            for t in y:
                                tipado_tupla.append(type(t))
                            tipado.append(tipado_tupla)
                            spamreader.writerow(y)
                        file.close()
                        truncate(database, table)
                        mod.loadCSV("./data/change.csv", database, table, tipado)
                        os.remove("./data/change.csv")              
        except:
            return 1
        for table in showTables(database):
            tab = dataTable.get(database + "_" + table)
            if tab:
                tab[4] = -2
                dataTable[database+"_"+table] = tab
            Serializable.update('./Data', 'DataTables', dataTable)
        return 0
    else:
        return 2

def alterTableCompress(database, table, level):
    checkData()
    data = Serializable.Read('./Data/', "Data")
    db = data.get(database)
    dataTable = Serializable.Read('./Data/', "DataTables")
    if type(level) != int:
        return 4
    elif (level < 0 or level > 9) and level != -1:
        return 4
    if db:
        tab = dataTable.get(database + "_" + table)
        try:
            if tab:
                if tab[4] != -2:
                    return 3
                tuplas = extractTable(database, table)
                if tuplas != None:
                    import zlib
                    tipado = []
                    if tab[1] == 'avl':
                        mod = avl
                    elif tab[1] == 'b':
                        mod = b
                    elif tab[1] == 'bplus':
                        mod = bplus
                    elif tab[1] == 'hash':
                        mod = hash
                    elif tab[1] == 'json':
                        mod = json
                    elif tab[1] == 'dict':
                        mod = dict
                    elif tab[1] == 'isam':
                        mod = isam
                    import csv
                    file = open("./data/change.csv", "w", newline='', encoding='utf-8')
                    spamreader = csv.writer(file)
                    compress_list = []
                    for y in tuplas:
                        compressed_data = []
                        for item in y:
                            compressed_item = item
                            if type(item) == bytes or type(item) == bytearray:
                                compressed_item = zlib.compress(item, level).hex()
                            elif type(item) == str:
                                compressed_item = zlib.compress(item.encode(), level).hex()
                            compressed_data.append(compressed_item)
                        compress_list.append(compressed_data)
                    tipado = []
                    for y in compress_list:
                        tipado_tupla = []
                        for t in y:
                            tipado_tupla.append(type(t))
                        tipado.append(tipado_tupla)
                        spamreader.writerow(y)
                    file.close()
                    truncate(database, table)
                    mod.loadCSV("./data/change.csv", database, table, tipado)
                    os.remove("./data/change.csv")
            else:
                return 1
        except:
            return 1
        tab[4] = level
        dataTable[database+"_"+table] = tab 
        Serializable.update('./Data', 'DataTables', dataTable)
        return 0
    else:
        return 2

def alterTableDecompress(database, table):
    checkData()
    data = Serializable.Read('./Data/', "Data")
    db = data.get(database)
    dataTable = Serializable.Read('./Data/', "DataTables")
    if db:
        tab = dataTable.get(database + "_" + table)
        try:
            if tab:
                if tab[4] == -2:
                    return 3
                tuplas = extractTable(database, table)
                if tuplas != None:
                    truncate(database, table)
                    import zlib
                    tipado = []
                    if tab[1] == 'avl':
                        mod = avl
                    elif tab[1] == 'b':
                        mod = b
                    elif tab[1] == 'bplus':
                        mod = bplus
                    elif tab[1] == 'hash':
                        mod = hash
                    elif tab[1] == 'json':
                        mod = json
                    elif tab[1] == 'dict':
                        mod = dict
                    elif tab[1] == 'isam':
                        mod = isam
                    import csv
                    file = open("./data/change.csv", "w", newline='', encoding='utf-8')
                    spamreader = csv.writer(file)
                    decompress_list = []
                    for y in tuplas:
                        compressed_data = []
                        for item in y:
                            compressed_item = item
                            if type(item) == str:
                                compressed_item = zlib.decompress(bytes.fromhex(item)).decode()
                            compressed_data.append(compressed_item)
                        decompress_list.append(compressed_data)
                    tipado = []
                    for y in decompress_list:
                        tipado_tupla = []
                        for t in y:
                            tipado_tupla.append(type(t))
                        tipado.append(tipado_tupla)
                        spamreader.writerow(y)
                    file.close()
                    truncate(database, table)
                    mod.loadCSV("./data/change.csv", database, table, tipado)
                    os.remove("./data/change.csv")
            else:
                return 1
        except:
            return 1
        tab[4] = -2
        dataTable[database+"_"+table] = tab
        Serializable.update('./Data', 'DataTables', dataTable)
        return 0
    else:
        return 2

def graphDSD(database: str) -> str:
    checkData()
    try:
        nodos = []
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            if not os.path.isdir("./Data/Grafos/"):
                os.mkdir("./Data/Grafos/")
            f= open('./Data/Grafos/'+database+'.dot', 'w',encoding='utf-8')
            f.write("digraph dibujo{\n")
            f.write('graph [ordering="out"];')
            f.write('rankdir=TB;\n')
            f.write('node [shape = box];\n')
            mode = ExtractModeDatabase(db)
            tablas = showTables(database)
            for tab in tablas:
                rows = mode.extractTable(database,"Table_REF_FK_"+tab)
                if rows:
                    for row in rows:
                        if row[2] not in nodos:
                            f.write(row[2]+' [label = '+row[2]+',  fontsize="30", shape = box ];\n')
                            nodos.append(row[2])
                        if row[4] not in nodos:
                            f.write(row[4]+' [label = '+row[4]+',  fontsize="30", shape = box ];\n')
                            nodos.append(row[4])
                        f.write(row[4]+'->'+ row[2]+';\n')
            f.write('}')
            f.close()
            os.system('dot -Tpng ./Data/Grafos/'+database+'.dot -o tupla.png')
            os.system('tupla.png')
        return None
    except:
        return None
        

def graphDF(database: str, table: str) -> str:
    pass

def ExtractModeDatabase(data):
    if data[1][0] == 'avl':
        return avl
    elif data[1][0] == 'b':
        return b
    elif data[1][0] == 'bplus':
        return bplus
    elif data[1][0] == 'dict':
        return dict
    elif data[1][0] == 'isam':
        return isam
    elif data[1][0] == 'json':
        return json
    elif data[1][0] == 'hash':
        return hash
