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
import shutil
import os

#----------------Data--------------------#

def checkData():
    if not os.path.isdir("./Data"):
        os.mkdir("./Data")
    if not os.path.isfile("./Data/Data.bin"):
        dataBaseTree = {}
        Serializable.update('./Data', 'Data', dataBaseTree)

def dropAll():
    dict.dropAll()
    hash.__init__()
    hash._storage = hash.ListaBaseDatos.ListaBaseDatos()
    b.b = b.db.DB()
#----------------DataBase----------------#

def createDatabase(database: str, mode: str, encoding: str) -> int:
    checkData()
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
    data = Serializable.Read('./Data/',"Data")
    temp = []
    for x in list(data.values()):
        temp.append(x[0])
    return temp

def alterDatabase(databaseOld, databaseNew) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(databaseOld)
        if db:
            if data.get(databaseNew):
                return 3
            mode =db[1][0] 
            if mode == 'avl':
                res = avl.alterDatabase(databaseOld, databaseNew)
            elif mode == 'b':
                res = b.alterDatabase(databaseOld, databaseNew)
            elif mode == 'bplus':
                res = bplus.alterDatabase(databaseOld, databaseNew)
            elif mode == 'dict':
                res = dict.alterDatabase(databaseOld, databaseNew)
            elif mode == 'isam':
                res = isam.alterDatabase(databaseOld, databaseNew)
            elif mode == 'json':
                res = json.alterDatabase(databaseOld, databaseNew)
            elif mode == 'hash':
                res = hash.alterDatabase(databaseOld, databaseNew)
            if not res:
                del data[databaseOld]
                db[0] = databaseNew
                data[databaseNew] = db
                Serializable.update('./Data', 'Data', data)
            return res
        else:
            return 2
    except:
        return 1

def dropDatabase(database: str) -> int: 
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
    # try:
    data = Serializable.Read('./Data/',"Data")
    db = data.get(database)
    if mode not in ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']:
        return 4
    if db:
        tablas = []
        mod =db[1][0] 
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
    #     return 1

def cambioTablas(modo, tablas, database, mode, db):
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
    if mod!= modo:
        import csv
        for x in tablas:
            t=0
            file = open("./data/change.csv", "w", newline='', encoding='utf-8')
            spamreader = csv.writer(file)
            for y in modo.extractTable(database, x):
                if t == 0:
                    mod.createTable(database, x, len(y))
                spamreader.writerow(y)
                t=1
            mod.loadCSV("./data/change.csv", database, x)
            file.close()
            os.remove("./data/change.csv")
        return 0
    return 4

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
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.insert(database, table, register)
            if 'b' in db[1] and res == 3:
                res = b.insert(database, table, register)
            if 'bplus' in db[1] and res == 3:
                res = bplus.insert(database, table, register)
            if 'dict' in db[1] and res == 3:
                res = dict.insert(database, table, register)
            if 'isam' in db[1] and res == 3:
                res = isam.insert(database, table, register)
            if 'json' in db[1] and res == 3:
                res = json.insert(database, table, register)
            if 'hash' in db[1] and res == 3:
                res = hash.insert(database, table, register)
            return res
        else:
            return 2
    except:
        return 1


def loadCSV(file: str, database: str, table: str) -> list:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.loadCSV(file, database, table)
            if 'b' in db[1] and res == 3:
                res = b.loadCSV(file, database, table)
            if 'bplus' in db[1] and res == 3:
                res = bplus.loadCSV(file, database, table)
            if 'dict' in db[1] and res == 3:
                res = dict.loadCSV(file, database, table)
            if 'isam' in db[1] and res == 3:
                res = isam.loadCSV(file, database, table)
            if 'json' in db[1] and res == 3:
                res = json.loadCSV(file, database, table)
            if 'hash' in db[1] and res == 3:
                res = hash.loadCSV(file, database, table)
            return res
        else:
            return 2
    except:
        return 1


def extractRow(database: str, table: str, columns: list) -> list:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.extractRow(database, table, columns)
            if 'b' in db[1] and res == 3:
                res = b.extractRow(database, table, columns)
            if 'bplus' in db[1] and res == 3:
                res = bplus.extractRow(database, table, columns)
            if 'dict' in db[1] and res == 3:
                res = dict.extractRow(database, table, columns)
            if 'isam' in db[1] and res == 3:
                res = isam.extractRow(database, table, columns)
            if 'json' in db[1] and res == 3:
                res = json.extractRow(database, table, columns)
            if 'hash' in db[1] and res == 3:
                res = hash.extractRow(database, table, columns)
            return res
        else:
            return 2
    except:
        return 1


def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.update(database, table, register, columns)
            if 'b' in db[1] and res == 3:
                res = b.update(database, table, register, columns)
            if 'bplus' in db[1] and res == 3:
                res = bplus.update(database, table, register, columns)
            if 'dict' in db[1] and res == 3:
                res = dict.update(database, table, register, columns)
            if 'isam' in db[1] and res == 3:
                res = isam.update(database, table, register, columns)
            if 'json' in db[1] and res == 3:
                res = json.update(database, table, register, columns)
            if 'hash' in db[1] and res == 3:
                res = hash.update(database, table, register, columns)
            return res
        else:
            return 2
    except:
        return 1


def delete(database: str, table: str, columns: list) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.delete(database, table, columns)
            if 'b' in db[1] and res == 3:
                res = b.delete(database, table, columns)
            if 'bplus' in db[1] and res == 3:
                res = bplus.delete(database, table, columns)
            if 'dict' in db[1] and res == 3:
                res = dict.delete(database, table, columns)
            if 'isam' in db[1] and res == 3:
                res = isam.delete(database, table, columns)
            if 'json' in db[1] and res == 3:
                res = json.delete(database, table, columns)
            if 'hash' in db[1] and res == 3:
                res = hash.delete(database, table, columns)
            return res
        else:
            return 2
    except:
        return 1


def truncate(database: str, table: str) -> int:
    try:
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        if db:
            res = 3
            if 'avl' in db[1] and res == 3:
                res = avl.truncate(database, table)
            if 'b' in db[1] and res == 3:
                res = b.truncate(database, table)
            if 'bplus' in db[1] and res == 3:
                res = bplus.truncate(database, table)
            if 'dict' in db[1] and res == 3:
                res = dict.truncate(database, table)
            if 'isam' in db[1] and res == 3:
                res = isam.truncate(database, table)
            if 'json' in db[1] and res == 3:
                res = json.truncate(database, table)
            if 'hash' in db[1] and res == 3:
                res = hash.truncate(database, table)
            return res
        else:
            return 2
    except:
        return 1
