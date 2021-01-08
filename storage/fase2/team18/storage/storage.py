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
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            mode =db[1][0] 
            if mode == 'avl':
                res = avl.createTable(database, table, numberColumns)
            elif mode == 'b':
                res = b.createTable(database, table, numberColumns)
            elif mode == 'bplus':
                res = bplus.createTable(database, table, numberColumns)
            elif mode == 'dict':
                res = dict.createTable(database, table, numberColumns)
            elif mode == 'isam':
                res = isam.createTable(database, table, numberColumns)
            elif mode == 'json':
                res = json.createTable(database, table, numberColumns)
            elif mode == 'hash':
                res = hash.createTable(database, table, numberColumns)
            return res
        else:
            return 2
    except:
        return 1

def showTables(database: str) -> list:
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
            return res
        else:
            return None
    except:
        return None

def extractTable(database: str, table: str) -> list:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = None
            if 'avl' in db[1] and res == None:
                res = avl.extractTable(database, table)
            if 'b' in db[1] and res == None:
                res = b.extractTable(database, table)
            if 'bplus' in db[1] and res == None:
                res = bplus.extractTable(database, table)
            if 'dict' in db[1] and res == None:
                res = dict.extractTable(database, table)
            if 'isam' in db[1] and res == None:
                res = isam.extractTable(database, table)
            if 'json' in db[1] and res == None:
                res = json.extractTable(database, table)
            if 'hash' in db[1] and res == None:
                res = hash.extractTable(database, table)
            return res
        else:
            return None
    except:
        return None

def extractRangeTable(database: str, table: str, columnNumber: int, 
                      lower: any, upper: any) -> list:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = None
            if 'avl' in db[1] and res == None:
                res = avl.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'b' in db[1] and res == None:
                res = b.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'bplus' in db[1] and res == None:
                res = bplus.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'dict' in db[1] and res == None:
                res = dict.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'isam' in db[1] and res == None:
                res = isam.extractRangeTable(database, table, columnNumber, lower, upper)
            if 'json' in db[1] and res == None:
                res = json.extractRangeTable(database, table, lower, upper)
            if 'hash' in db[1] and res == None:
                res = hash.extractRangeTable(database, table, columnNumber, lower, upper)
            return res
        else:
            return 2
    except:
        return 1


def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.alterAddPK(database, table, columns)
            if 'b' in db[1] and res == 3:
                res = b.alterAddPK(database, table, columns)
            if 'bplus' in db[1] and res == 3:
                res = bplus.alterAddPK(database, table, columns)
            if 'dict' in db[1] and res == 3:
                res = dict.alterAddPK(database, table, columns)
            if 'isam' in db[1] and res == 3:
                res = isam.alterAddPK(database, table, columns)
            if 'json' in db[1] and res == 3:
                res = json.alterAddPK(database, table, columns)
            if 'hash' in db[1] and res == 3:
                res = hash.alterAddPK(database, table, columns)
            return res
        else:
            return 2
    except:
        return 1


def alterDropPK(database: str, table: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.alterDropPK(database, table)
            if 'b' in db[1] and res == 3:
                res = b.alterDropPK(database, table)
            if 'bplus' in db[1] and res == 3:
                res = bplus.alterDropPK(database, table)
            if 'dict' in db[1] and res == 3:
                res = dict.alterDropPK(database, table)
            if 'isam' in db[1] and res == 3:
                res = isam.alterDropPK(database, table)
            if 'json' in db[1] and res == 3:
                res = json.alterDropPK(database, table)
            if 'hash' in db[1] and res == 3:
                res = hash.alterDropPK(database, table)
            return res
        else:
            return 2
    except:
        return 1


def alterTableAddFK(database: str, table: str, indexName: str, 
                    columns: list,  tableRef: str, columnsRef: list) -> int:
    pass

def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    pass

def alterAddIndex(database: str, table: str, references: dict) -> int:
    pass

def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.alterTable(database, tableOld, tableNew)
            if 'b' in db[1] and res == 3:
                res = b.alterTable(database, tableOld, tableNew)
            if 'bplus' in db[1] and res == 3:
                res = bplus.alterTable(database, tableOld, tableNew)
            if 'dict' in db[1] and res == 3:
                res = dict.alterTable(database, tableOld, tableNew)
            if 'isam' in db[1] and res == 3:
                res = isam.alterTable(database, tableOld, tableNew)
            if 'json' in db[1] and res == 3:
                res = json.alterTable(database, tableOld, tableNew)
            if 'hash' in db[1] and res == 3:
                res = hash.alterTable(database, tableOld, tableNew)
            return res
        else:
            return 2
    except:
        return 1


def alterAddColumn(database: str, table: str, default: any) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.alterAddColumn(database, table, default)
            if 'b' in db[1] and res == 3:
                res = b.alterAddColumn(database, table, default)
            if 'bplus' in db[1] and res == 3:
                res = bplus.alterAddColumn(database, table, default)
            if 'dict' in db[1] and res == 3:
                res = dict.alterAddColumn(database, table, default)
            if 'isam' in db[1] and res == 3:
                res = isam.alterAddColumn(database, table, default)
            if 'json' in db[1] and res == 3:
                res = json.alterAddColumn(database, table, default)
            if 'hash' in db[1] and res == 3:
                res = hash.alterAddColumn(database, table, default)
            return res
        else:
            return 2
    except:
        return 1


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.alterDropColumn(database, table, columnNumber)
            if 'b' in db[1] and res == 3:
                res = b.alterDropColumn(database, table, columnNumber)
            if 'bplus' in db[1] and res == 3:
                res = bplus.alterDropColumn(database, table, columnNumber)
            if 'dict' in db[1] and res == 3:
                res = dict.alterDropColumn(database, table, columnNumber)
            if 'isam' in db[1] and res == 3:
                res = isam.alterDropColumn(database, table, columnNumber)
            if 'json' in db[1] and res == 3:
                res = json.alterDropColumn(database, table, columnNumber)
            if 'hash' in db[1] and res == 3:
                res = hash.alterDropColumn(database, table, columnNumber)
            return res
        else:
            return 2
    except:
        return 1


def dropTable(database: str, table: str) -> int: 
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.dropTable(database, table)
                if not len(avl.showTables(database)) and db[1][0]!='avl':
                    avl.dropDatabase(database)
                    db[1].remove('avl')
            if 'b' in db[1] and res == 3:
                res = b.dropTable(database, table)
                if not len(b.showTables(database)) and db[1][0]!='b':
                    b.dropDatabase(database)
                    db[1].remove('b')
            if 'bplus' in db[1] and res == 3:
                res = bplus.dropTable(database, table)
                if not len(bplus.showTables(database)) and db[1][0]!='bplus':
                    bplus.dropDatabase(database)
                    db[1].remove('bplus')
            if 'dict' in db[1] and res == 3:
                res = dict.dropTable(database, table)
                if not len(dict.showTables(database)) and db[1][0]!='dict':
                    dict.dropDatabase(database)
                    db[1].remove('dict')
            if 'isam' in db[1] and res == 3:
                res = isam.dropTable(database, table)
                if not len(isam.showTables(database)) and db[1][0]!='isam':
                    isam.dropDatabase(database)
                    db[1].remove('isam')
            if 'json' in db[1] and res == 3:
                res = json.dropTable(database, table)
                if not len(json.showTables(database)) and db[1][0]!='json':
                    json.dropDatabase(database)
                    db[1].remove('json')
            if 'hash' in db[1] and res == 3:
                res = hash.dropTable(database, table)
                if not len(hash.showTables(database)) and db[1][0]!='hash':
                    hash.dropDatabase(database)
                    db[1].remove('hash')
            data[database] = db
            return res
        else:
            return 2
    except:
        return 1


def alterTableMode(database: str, table: str, mode: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
            return 4
        if db:
            tuplas = None
            if mode not in db[1]:
                db[1].append(mode)
            if  'avl' in db[1] and tuplas == None:
                tuplas = avl.extractTable(database, table)
                modo = 'avl'
                avl.dropTable(database, table)
                if 'avl' != db[1][0] and tuplas!=None:
                    if not len(avl.showTables(database)):
                        avl.dropDatabase(database)
                        db[1].remove('avl')
            if  'b' in db[1] and tuplas == None:
                tuplas = b.extractTable(database, table)
                b.dropTable(database, table)
                modo = 'b'
                if 'b' != db[1][0] and tuplas!=None:
                    if not len(b.showTables(database)):
                        b.dropDatabase(database)
                        db[1].remove('b')
            if  'bplus' in db[1] and tuplas == None:
                tuplas = bplus.extractTable(database, table)
                bplus.dropTable(database, table)
                modo = 'bplus'
                if 'bplus' != db[1][0] and tuplas!=None:
                    if not len(bplus.showTables(database)):
                        bplus.dropDatabase(database)
                        db[1].remove('bplus')
            if  'dict' in db[1] and tuplas == None:
                tuplas = dict.extractTable(database, table)
                dict.dropTable(database, table)
                modo = 'dict'
                if 'dict' != db[1][0] and tuplas!=None:
                    if not len(dict.showTables(database)):
                        dict.dropDatabase(database)
                        db[1].remove('dict')
            if  'isam' in db[1] and tuplas == None:
                tuplas = isam.extractTable(database, table)
                isam.dropTable(database, table)
                modo = 'isam'
                if 'isam' != db[1][0] and tuplas!=None:
                    if not len(isam.showTables(database)):
                        isam.dropDatabase(database)
                        db[1].remove('isam')
            if  'json' in db[1] and tuplas == None:
                tuplas = json.extractTable(database, table)
                json.dropTable(database, table)
                modo = 'json'
                if 'json' != db[1][0] and tuplas!=None:
                    if not len(json.showTables(database)):
                        json.dropDatabase(database)
                        db[1].remove('json')
            if  'hash' in db[1] and tuplas == None:
                tuplas = hash.extractTable(database, table)
                hash.dropTable(database, table)
                modo = 'hash'
                if 'hash' != db[1][0] and tuplas!=None:
                    if not len(hash.showTables(database)):
                        hash.dropDatabase(database)
                        db[1].remove('hash')
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
                    
                if mode == modo:
                    return 4
                import csv
                file = open("./data/change.csv", "w", newline='', encoding='utf-8')
                spamreader = csv.writer(file)
                t=0
                if mod.showTables(database) == None:
                    mod.createDatabase(database)
                for y in tuplas:
                    if t == 0:
                        mod.createTable(database, table, len(y))
                    spamreader.writerow(y)
                    t=1
                mod.loadCSV("./data/change.csv", database, table)
                file.close()
                os.remove("./data/change.csv")
                return 0
            else:
                return 3
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
                        block.blockchain().insert(register, database, table)
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
                for x in list(register.values()):
                    if type(x)==str:
                        x.encode(db[2], "strict")
                if tab[1] == 'avl':
                    row = avl.extractRow(database, table, columns)
                    res = avl.update(database, table, register, columns)
                elif tab[1] == 'b':
                    row = b.extractRow(database, table, columns)
                    res = b.update(database, table, register, columns)
                elif tab[1] == 'bplus':
                    row = bplus.extractRow(database, table, columns)
                    res = bplus.update(database, table, register, columns)
                elif tab[1] == 'dict':
                    row = dict.extractRow(database, table, columns)
                    res = dict.update(database, table, register, columns)
                elif tab[1] == 'isam':
                    row = isam.extractRow(database, table, columns)
                    res = isam.update(database, table, register, columns)
                elif tab[1] == 'json':
                    row = json.extractRow(database, table, columns)
                    res = json.update(database, table, register, columns)
                elif tab[1] == 'hash':
                    row = hash.extractRow(database, table, columns)
                    res = hash.update(database, table, register, columns)
                if not res:
                    if os.path.isfile('./Data/security/'+database+"_"+table+".json"):
                        row2 = row[:]
                        values = list(register.values())
                        for x in list(register.keys()):
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
                if tab[1] == 'avl':
                    row = avl.extractRow(database, table, columns)
                    res = avl.delete(database, table, columns)
                elif tab[1] == 'b':
                    row = b.extractRow(database, table, columns)
                    res = b.delete(database, table, columns)
                elif tab[1] == 'bplus':
                    row = bplus.extractRow(database, table, columns)
                    res = bplus.delete(database, table, columns)
                elif tab[1] == 'dict':
                    row = dict.extractRow(database, table, columns)
                    res = dict.delete(database, table, columns)
                elif tab[1] == 'isam':
                    row = isam.extractRow(database, table, columns)
                    res = isam.delete(database, table, columns)
                elif tab[1] == 'json':
                    row = json.extractRow(database, table, columns)
                    res = json.delete(database, table, columns)
                elif tab[1] == 'hash':
                    row = hash.extractRow(database, table, columns)
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
    
#----------------Compress-------------------#

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
            alterDatabaseEncoding(database, "utf8")
            for table in showTables(database):
                tab = dataTable.get(database + "_" + table)
                if not tab:
                    return 1
                tuplas = extractTable(database, table)
                if tuplas != None:
                    truncate(database, table)
                    import zlib
                    for y in tuplas:
                        compressed_data = []
                        for item in y:
                            compressed_item = item
                            if type(item) == bytes or type(item) == bytearray:
                                compressed_item = zlib.compress(item, level)
                            elif type(item) == str:
                                compressed_item = zlib.compress(item.encode(), level)
                            compressed_data.append(compressed_item)
                        insert(database, table, compressed_data)

        except E:
            return 1
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
            alterDatabaseEncoding(database, "utf8")
            for table in showTables(database):
                tab = dataTable.get(database + "_" + table)
                if not tab:
                    return 1
                tuplas = extractTable(database, table)
                if tuplas != None:
                    truncate(database, table)
                    import zlib
                    for y in tuplas:
                        compressed_data = []
                        for item in y:
                            compressed_item = item
                            if type(item) == bytes or type(item) == bytearray:
                                compressed_item = zlib.decompress(item)
                                compressed_item = compressed_item.decode()
                            compressed_data.append(compressed_item)
                        insert(database, table, compressed_data)
        except E:
            return 1
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
        try:
            alterDatabaseEncoding(database, "utf8")
            tab = dataTable.get(database + "_" + table)
            if not tab:
                return 1
            tuplas = extractTable(database, table)
            if tuplas != None:
                truncate(database, table)
                import zlib
                for y in tuplas:
                    compressed_data = []
                    for item in y:
                        compressed_item = item
                        if type(item) == bytes or type(item) == bytearray:
                            compressed_item = zlib.compress(item, level)
                        elif type(item) == str:
                            compressed_item = zlib.compress(item.encode(), level)
                        compressed_data.append(compressed_item)
                    insert(database, table, compressed_data)
        except E:
            return 1
        return 0
    else:
        return 2

def alterTableDecompress(database, table):
    checkData()
    data = Serializable.Read('./Data/', "Data")
    db = data.get(database)
    dataTable = Serializable.Read('./Data/', "DataTables")
    if db:
        try:
            alterDatabaseEncoding(database, "utf8")
            tab = dataTable.get(database + "_" + table)
            if not tab:
                return 1
            tuplas = extractTable(database, table)
            if tuplas != None:
                truncate(database, table)
                import zlib
                for y in tuplas:
                    compressed_data = []
                    for item in y:
                        compressed_item = item
                        if type(item) == bytes or type(item) == bytearray:
                            compressed_item = zlib.decompress(item)
                            compressed_item = compressed_item.decode()
                        compressed_data.append(compressed_item)
                    insert(database, table, compressed_data)
        except E:
            return 1
        return 0
    else:
        return 2