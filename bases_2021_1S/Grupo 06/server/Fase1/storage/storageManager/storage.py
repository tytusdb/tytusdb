# -------------------------------
# Released under MIT License
# Copyright (c) 2020 TytusDb Team 18

from Fase1.storage.storageManager.avl import avlMode as avl
# from avl import avlMode as avl
# fro
from Fase1.storage.storageManager.b import BMode as b
# from b import BMode as b
from Fase1.storage.storageManager.bplus import BPlusMode as bplus
from Fase1.storage.storageManager.dict import DictMode as dict
from Fase1.storage.storageManager.hash import HashMode as hash
from Fase1.storage.storageManager.isam import ISAMMode as isam
from Fase1.storage.storageManager.json1 import jsonMode as json
from Fase1.storage.storageManager import Serializable as Serializable
from Fase1.storage.storageManager import blockchain as block
from Fase1.storage.storageManager import Criptografia as crypt
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
    try:
        return re.search("^[a-zA-Z][a-zA-Z0-9#@$_]*", identifier)
    except:
        return False
def dropAll():
    dict.dropAll()
    hash.__init__()
    hash._storage = hash.ListaBaseDatos.ListaBaseDatos()
    b.b = b.db.DB()
#----------------DataBase----------------#
def createDatabase(database: str, mode: str, encoding = 'utf8') -> int:
    checkData()
    if not validateIdentifier(database):
        return 1
    data = Serializable.Read('./Data/',"Data")
    if encoding not in ['ascii', 'iso-8859-1', 'utf8']:
        return 4
    if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
        return 3
    if not data.get(database.upper()):
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
            data[database.upper()] = [database,[mode],encoding, -2]
            Serializable.update('./Data', 'Data', data)
        return res
    else:
        return 2

def showDatabases():
    checkData()
    data = Serializable.Read('./Data/',"Data")
    temp = []
    temp2 = []
    temp3 = []
    for x in list(data.values()):
        temp.append(x[0])
    for x in list(data.values()):
        temp2.append(x[0])
        temp2.append(x[1][0])
        temp3.append(temp2)
        temp2 = []

    return [temp, temp3]

def alterDatabase(databaseOld, databaseNew) -> int:
    checkData()
    try:
        if not validateIdentifier(databaseNew):
            return 1
        data = Serializable.Read('./Data/',"Data")
        db = data.get(databaseOld.upper())
        if db:
            if data.get(databaseNew.upper()):
                return 3
            tablas = []
            databaseOld = db[0]
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
                del data[databaseOld.upper()]
                db[0] = databaseNew
                data[databaseNew.upper()] = db
                Serializable.update('./Data', 'Data', data)
                if len(tablas):
                    dataTable = Serializable.Read('./Data/',"DataTables")
                    dataTableRef = Serializable.Read('./Data/',"DataTablesRef")
                    for x in tablas:
                        tab = dataTable.get(databaseOld.upper()+"_"+x.upper())
                        if tab:
                            tab[0] = databaseNew
                            dataTable[databaseNew.upper()+"_"+x.upper()] = tab
                            del dataTable[databaseOld.upper()+"_"+x.upper()]
                        else:
                            dataTableRef[x.upper()+"_"+databaseNew.upper()] = dataTableRef.get(x.upper()+"_"+databaseOld.upper())
                            del dataTableRef[x.upper()+"_"+databaseOld.upper()]
                        if os.path.isfile("./Data/security/"+databaseOld+"_"+x+".json"):
                            os.rename("./Data/security/"+databaseOld+"_"+x+".json","./Data/security/"+databaseNew+"_"+x+".json")
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
        db = data.get(database.upper())
        if db:
            mode =db[1][0]
            database = db[0]
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
                del data[database.upper()]
                Serializable.update('./Data', 'Data', data)
            return res
        else:
            return 2
    except:
        return 1

def alterDatabaseMode(database: str, mode: str) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database.upper())
        if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
            return 4
        if db:
            tablas = []
            database = db[0]
            mod =db[1][0]
            if mod== mode:
                return 1
            
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
            data[database.upper()] = db
            Serializable.update('./Data', 'Data', data)
            return res
        else:
            return 2
    except:
        return 1

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
        tab = dataTable.get(database.upper()+"_"+x.upper())
        if tab:
            tab[1] = mode
            mod.createTable(database, x, tab[2])
            if len(tab[3]):
                mod.alterAddPK(database, x, tab[3])
        else:
            mod.createTable(database, x, dataTableRef.get(x.upper()+"_"+database.upper()))
        file = open("./data/change.csv", "w", newline='', encoding='utf-8')
        spamreader = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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
        db = data.get(database.upper())
        if db:
            database = db[0]
            res = showTables(database)
            if res:
                if len(res):
                    for x in res:
                        row = extractTable(database, x)
                        if row:
                            if len(row):
                                for l in row:
                                    for g in l:
                                        if type(g) == str:
                                            g.encode(encoding)
            db[2] == encoding
            data[database.upper()] = db
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
        db = data.get(database.upper())
        if db:
            database = db[0]
            mode =db[1][0] 
            if mode == 'avl':
                res = avl.createTable(database, table, numberColumns)
                dataTable[database.upper()+"_"+table.upper()] = [table, 'avl', numberColumns, [], db[3]]
            elif mode == 'b':
                res = b.createTable(database, table, numberColumns)
                dataTable[database.upper()+"_"+table.upper()] = [table, 'b', numberColumns, [], db[3]]
            elif mode == 'bplus':
                res = bplus.createTable(database, table, numberColumns)
                dataTable[database.upper()+"_"+table.upper()] = [table, 'bplus', numberColumns, [], db[3]]
            elif mode == 'dict':
                res = dict.createTable(database, table, numberColumns)
                dataTable[database.upper()+"_"+table.upper()] = [table, 'dict', numberColumns, [], db[3]]
            elif mode == 'isam':
                res = isam.createTable(database, table, numberColumns)
                dataTable[database.upper()+"_"+table.upper()] = [table, 'isam', numberColumns, [], db[3]]
            elif mode == 'json':
                res = json.createTable(database, table, numberColumns)
                dataTable[database.upper()+"_"+table.upper()] = [table, 'json', numberColumns, [], db[3]]
            elif mode == 'hash':
                res = hash.createTable(database, table, numberColumns)
                dataTable[database.upper()+"_"+table.upper()] = [table, 'hash', numberColumns, [], db[3]]
            if not res:
                createRefTAbles(database, 'TABLE_REF_FK_'+table, 6, mode)
                createRefTAbles(database, 'TABLE_REF_INDEXU_'+table, 4, mode)
                createRefTAbles(database, 'TABLE_REF_INDEX_'+table, 4, mode)
                dataTableRef['TABLE_REF_FK_'+table.upper()+"_"+database.upper()] = 6
                dataTableRef['TABLE_REF_INDEXU_'+table.upper()+"_"+database.upper()] = 4
                dataTableRef['TABLE_REF_INDEX_'+table.upper()+"_"+database.upper()] = 4
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
        db = data.get(database.upper())
        if db:
            database = db[0]
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
                    tab = dataTable.get(database.upper()+"_"+x.upper())
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            database = db[0]
            if tab:
                table = tab[0]
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
                ret = []
                if len(res):
                    if tab[4]!=-2:
                        import zlib
                        for tupla in res:
                            rr=[]
                            for x in tupla:
                                if type(x) == str:
                                    rr.append(zlib.decompress(bytes.fromhex(x)).decode())
                                else:
                                    rr.append(x)
                            ret.append(rr)
                if len(ret):
                    return ret
                else:
                    return res
        return None
    except:
        return None

def extractRangeTable(database: str, table: str, columnNumber: int, 
                      lower: any, upper: any) -> list:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
                ret = []
                if len(res):
                    if tab[4]!=-2:
                        import zlib
                        for tupla in res:
                            rr=[]
                            for x in tupla:
                                if type(x) == str:
                                    rr.append(zlib.decompress(bytes.fromhex(x)).decode())
                                else:
                                    rr.append(x)
                            ret.append(rr)
                if len(ret):
                    return ret
                else:
                    return res
            return 3
        else:
            return 2
    except:
        return 1

def alterAddPK(database: str, table: str, columns: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        db = data.get(database.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
                    dataTable[database.upper()+"_"+table.upper()] = tab
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = db[0]
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
        db = data.get(database.upper())
        if db:
            database = db[0]
            dataTable = Serializable.Read('./Data/',"DataTables")
            tab = dataTable.get(database.upper()+"_"+table.upper())
            tabref = dataTable.get(database.upper()+"_"+tableRef.upper())
            if tab and tabref:
                table = tab[0]
                tableRef = tabref[0]
                if min(columnsRef) < 0 or min(columns) < 0 and max(columnsRef) >= tabref[2] and max(columns)>= tab[2]:
                    return 1
                mode =db[1][0]
                register = [indexName, database, table, columns, tableRef, columnsRef]
                res = registerRefTAbles(database, 'TABLE_REF_FK_'+table, register, mode)
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

def buscarcreateRefTables(database, tableref, mode, index):
    if mode == 'avl':
        res = avl.extractRow(database, tableref,[index])
    elif mode == 'b':
        res = b.extractRow(database, tableref,[index])
    elif mode == 'bplus':
        res = bplus.extractRow(database, tableref,[index])
    elif mode == 'dict':
        res = dict.extractRow(database, tableref,[index])
    elif mode == 'isam':
        res = isam.extractRow(database, tableref,[index])
    elif mode == 'json':
        res = json.extractRow(database, tableref,[index])
    elif mode == 'hash':
        res = hash.extractRow(database, tableref,[index])
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
        db = data.get(database.upper())
        if db:
            dataTable = Serializable.Read('./Data/',"DataTablesRef")
            dataTables = Serializable.Read('./Data/',"DataTables")
            tb = dataTables.get(database.upper()+"_"+table.upper())
            tab = dataTable.get('TABLE_REF_FK_'+table.upper()+"_"+database.upper())
            if tab and tb:
                database = db[0]
                table = tb[0]
                if not buscarcreateRefTables(database, 'TABLE_REF_FK_'+table, db[1][0], indexName):
                    return 4
                res = dropRefTAbles(database, 'TABLE_REF_FK_'+table, db[1][0], indexName)
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
        db = data.get(database.upper())
        if db:
            dataTable = Serializable.Read('./Data/',"DataTables")
            tab = dataTable.get(database.upper()+"_"+table.upper())
            if tab:
                if min(columns) < 0 or max(columns)>= tab[2]:
                    return 4
                database = db[0]
                table = tab[0]
                mode =db[1][0]
                register = [indexName, database, table, columns]
                res = registerRefTAbles(database, 'TABLE_REF_INDEXU_'+table, register, mode)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database.upper())
        if db:
            dataTable = Serializable.Read('./Data/',"DataTablesRef")
            dataTables = Serializable.Read('./Data/',"DataTables")
            tab = dataTable.get('TABLE_REF_FK_'+table.upper()+"_"+database.upper())
            tb = dataTables.get(database.upper()+"_"+table.upper())
            if tab and tb:
                database = db[0]
                table = tb[0]
                if not buscarcreateRefTables(database, 'TABLE_REF_INDEXU_'+table, db[1][0], indexName):
                    return 4
                res = dropRefTAbles(database, 'TABLE_REF_INDEXU_'+table, db[1][0], indexName)
                
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
        db = data.get(database.upper())
        if db:
            dataTable = Serializable.Read('./Data/',"DataTables")
            tab = dataTable.get(database.upper()+"_"+table.upper())
            if tab:
                if min(columns) < 0 or max(columns)>= tab[2]:
                    return 4
                database = db[0]
                table = tab[0]
                mode =db[1][0]
                register = [indexName, database, table, columns]
                res = registerRefTAbles(database, 'TABLE_REF_INDEX_'+table, register, mode)
                return res
            return 3
        else:
            return 2
    except:
        return 1

def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database.upper())
        if db:
            dataTable = Serializable.Read('./Data/',"DataTablesRef")
            dataTables = Serializable.Read('./Data/',"DataTables")
            tab = dataTable.get('TABLE_REF_FK_'+table.upper()+"_"+database.upper())
            tb = dataTables.get(database.upper()+"_"+table.upper())
            if tab and tb:
                database = db[0]
                table = tb[0]
                if not buscarcreateRefTables(database, 'TABLE_REF_INDEX_'+table, db[1][0], indexName):
                    return 4
                res = dropRefTAbles(database, 'TABLE_REF_INDEX_'+table, db[1][0], indexName)
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+tableOld.upper())
        if db:
            if tab:
                database = db[0]
                tableOld = tab[0]
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
                    dataTable[database.upper()+"_"+tableNew.upper()] = tab
                    del dataTable[database.upper()+"_"+tableOld.upper()]
                    if os.path.isfile("./Data/security/"+database+"_"+tableOld+".json"):
                        os.rename("./Data/security/"+database+"_"+tableOld+".json","./Data/security/"+database+"_"+tableNew+".json")
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
                if type(default) == str:
                    default.encode(db[2], 'strict')
                if tab[4]!=-2:
                    if type(default) == str:
                        import zlib
                        default = zlib.compress(default.encode(), tab[4]).hex()
                rows1 = extractTable(database, table)
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
                    rows2 = extractTable(database, table)
                    dataTable[database.upper()+"_"+table.upper()] = tab
                    Serializable.update('./Data', 'DataTables', dataTable)
                    if os.path.isfile('./Data/security/'+database+"_"+table+".json"):
                            for row in rows1:
                                index = rows1.index(row)
                                row2 = rows2[index]
                                block.blockchain().dropAddColumn(row, row2, database, table)
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
                rows1 = extractTable(database, table)
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
                        rows2 = extractTable(database, table)
                        tab[2]-=1
                        dataTable[database.upper()+"_"+table.upper()] = tab
                        Serializable.update('./Data', 'DataTables', dataTable)
                        if os.path.isfile('./Data/security/'+database+"_"+table+".json"):
                            for row in rows1:
                                index = rows1.index(row)
                                row2 = rows2[index]
                                block.blockchain().dropAddColumn(row, row2, database, table)
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
                    data[database.upper()] = db
                    del dataTable[database.upper()+"_"+table.upper()]
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
            return 4
        if db:
            if not tab:
                return 3
            database = db[0]
            table = tab[0]
            if mode == tab[1]:
                return 1
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
                file = open("./data/change.csv", "w", newline='', encoding='utf-8-sig')
                spamreader = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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
                data[database.upper()] = db
                tab[1] = mode
                dataTable[database.upper()+"_"+table.upper()] = tab
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
                res = []
                tabla = []
                import csv
                ff = open("./data/change.csv", "w", newline='', encoding='utf-8-sig')
                spamreader = csv.writer(ff, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
                ret = []
                if len(res) and tab[4]!=-2:
                    import zlib
                    for x in res:
                        if type(x) == str:
                            ret.append(zlib.decompress(bytes.fromhex(x)).decode())
                        else:
                            ret.append(x)
                if len(ret):
                    return ret
                else:
                    return res
            return None
        else:
            return None
    except:
        return None

def update(database: str, table: str, register: dict, columns: list) -> int:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
                            row2[x] = register2[x]
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
        db = data.get(database.upper())
        if db:
            database = db[0]
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
                    tab = dataTable.get(database.upper()+"_"+x.upper())
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
        db = data.get(database.upper())
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database.upper()+"_"+table.upper())
        if db:
            if tab:
                database = db[0]
                table = tab[0]
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
    db = data.get(database.upper())
    dataTable = Serializable.Read('./Data/', "DataTables")
    if type(level) != int:
        return 4
    elif (level < 0 or level > 9) and level != -1:
        return 3
    if db:
        if db[3] !=-2:
            return 1
        database = db[0]
        try:
            tablas = showTables(database)
            if tablas:
                for table in tablas:
                    tab = dataTable.get(database.upper() + "_" + table.upper())
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
                            file = open("./data/change.csv", "w", newline='', encoding='utf-8-sig')
                            spamreader = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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
        if tablas:
            for table in showTables(database):
                tab = dataTable.get(database.upper() + "_" + table.upper())
                if tab:
                    tab[4] = level
                    dataTable[database.upper()+"_"+table.upper()] = tab
        Serializable.update('./Data', 'DataTables', dataTable)
        db[3] = level
        data[database] = db
        Serializable.update('./Data', 'Data', data)
        return 0
    else:
       return 2

def alterDatabaseDecompress(database):
    checkData()
    data = Serializable.Read('./Data/', "Data")
    db = data.get(database.upper())
    dataTable = Serializable.Read('./Data/', "DataTables")
    if db:
        database = db[0]
        try:
            tablas = showTables(database)
            if tablas:
                for table in tablas:
                    tab = dataTable.get(database.upper() + "_" + table.upper())
                    if tab:
                        if db[3] == -2:
                            return 3
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
                            file = open("./data/change.csv", "w", newline='', encoding='utf-8-sig')
                            spamreader = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            tipado = []
                            for y in tuplas:
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
        if tablas:
            for table in showTables(database):
                tab = dataTable.get(database.upper() + "_" + table.upper())
                if tab:
                    tab[4] = -2
                    dataTable[database.upper()+"_"+table.upper()] = tab
                Serializable.update('./Data', 'DataTables', dataTable)
        db[3] = -2
        data[database.upper()] = db
        Serializable.update('./Data', 'Data', data)
        return 0
    else:
        return 2

def alterTableCompress(database, table, level):
    checkData()
    data = Serializable.Read('./Data/', "Data")
    db = data.get(database.upper())
    dataTable = Serializable.Read('./Data/', "DataTables")
    if type(level) != int:
        return 4
    elif (level < 0 or level > 9) and level != -1:
        return 4
    if db:
        tab = dataTable.get(database.upper() + "_" + table.upper())
        try:
            if tab:
                database = db[0]
                table = tab[0]
                if tab[4] != -2:
                    return 1
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
                    file = open("./data/change.csv", "w", newline='', encoding='utf-8-sig')
                    spamreader = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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
                return 3
        except:
            return 1
        tab[4] = level
        dataTable[database.upper()+"_"+table.upper()] = tab 
        Serializable.update('./Data', 'DataTables', dataTable)
        return 0
    else:
        return 2

def alterTableDecompress(database, table):
    checkData()
    data = Serializable.Read('./Data/', "Data")
    db = data.get(database.upper())
    dataTable = Serializable.Read('./Data/', "DataTables")
    if db:
        tab = dataTable.get(database.upper() + "_" + table.upper())
        try:
            if tab:
                if tab[4] == -2:
                    return 4
                database = db[0]
                table = tab[0]
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
                    file = open("./data/change.csv", "w", newline='', encoding='utf-8-sig')
                    spamreader = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    tipado = []
                    for y in tuplas:
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
                return 3
        except:
            return 1
        tab[4] = -2
        dataTable[database.upper()+"_"+table.upper()] = tab
        Serializable.update('./Data', 'DataTables', dataTable)
        return 0
    else:
        return 2

def graphDSD(database: str) -> str:
    checkData()
    try:
        nodos = []
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database.upper())
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
                rows = mode.extractTable(database,"TABLE_REF_FK_"+tab)
                if rows:
                    for row in rows:
                        if row[2] not in nodos:
                            f.write(row[2]+' [label = '+row[2]+',  fontsize="30", shape = box ];\n')
                            nodos.append(row[2])
                        if row[4] not in nodos:
                            f.write(row[4]+' [label = '+row[4]+',  fontsize="30", shape = box ];\n')
                            nodos.append(row[4])
                        f.write(row[4]+'->'+ row[2]+';\n')
                else:
                    if tab not in nodos:
                        nodos.append(tab)
                        f.write(tab+' [label = '+tab+',  fontsize="30", shape = box ];\n')
            f.write('}')
            f.close()
            os.system('dot -Tpng ./Data/Grafos/'+database+'.dot -o '+database+'.png')
            return os.getcwd()+"\\Data\\Grafos\\"+database+".dot"
        return None
    except:
        return None

def graphDF(database: str, table: str) -> str:
    checkData()
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database.upper())
        if db:
            dataTable = Serializable.Read('./Data/',"DataTables")
            tab = dataTable.get(database.upper()+"_"+table.upper())
            if tab:
                database = db[0]
                table = tab[0]
                if not os.path.isdir("./Data/Grafos/"):
                    os.mkdir("./Data/Grafos/")
                f= open('./Data/Grafos/'+database+"_"+table+'_DF.dot', 'w',encoding='utf-8')
                f.write("digraph dibujo{\n")
                f.write('graph [ordering="out", ranksep = 5, nodesep = 0.5];')
                f.write('rankdir=TB;\n')
                f.write('node [shape = record];\n')
                mode = ExtractModeDatabase(db)
                rows = mode.extractTable(database,"TABLE_REF_INDEXU_"+table)
                primarias = tab[3]
                unicas = []
                normales = []
                for x in primarias:
                    f.write(str(x)+' [label = "Primary|'+str(x)+'",  fontsize="30", fillcolor = white, style = filled];\n')
                if len(rows):
                    for row in rows:
                        for x in row[3]:
                            if x not in unicas and x not in primarias:
                                f.write(str(x)+' [label = "Unique|'+str(x)+'",  fontsize="30", fillcolor = white, style = filled];\n')
                                unicas.append(x) 
                for y in range(tab[2]):
                    if y not in unicas and y not in primarias:
                        f.write(str(y)+' [label = '+str(y)+',  fontsize="30", shape = box ];\n')
                        normales.append(y)
                for p in primarias:
                    for n in normales:
                        f.write(str(p)+'->'+ str(n)+';\n')
                
                for p in unicas:
                    for n in normales:
                        f.write(str(p)+'->'+ str(n)+';\n')
                f.write('}')
                f.close()
                os.system('dot -Tpng ./Data/Grafos/'+database+"_"+table+'_DF.dot -o '+database+'_'+table+'_DF.png')
                return os.getcwd()+"\\Data\\Grafos\\"+database+"_"+table+"_DF.dot"
        return None
    except:
        return None

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
