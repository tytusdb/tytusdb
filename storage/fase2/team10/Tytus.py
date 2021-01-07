import os
import pickle
import zlib
import binascii
import sys
from cryptography.fernet import Fernet

# 1. UNIFICACION DE INDICES
from storage.AVLMode import avlMode as avl
from storage.BMode import BMode as b
from storage.BPlusMode import BPlusMode as bplus
from storage.HashMode.storage import HashMode as _hash
from storage.IsamMode import ISAMMode as isam
from storage.DictMode import DictMode as _dict
from storage.JsonMode import jsonMode as json
from os import path

structs = [avl, b, bplus, _hash, isam, _dict]
databases = []

def dropAll():
    avl.dropAll()
    bplus.dropAll()
    _dict.dropAll()
    json.dropAll()
    return 0

def addDatabase(name, mode, code, mod):
    database = {"mod": None, "mode": "", "name": "", "code": "", "tables": []}
    database["mod"] = mod
    database["name"] = name
    database["mode"] = mode
    database["code"] = code
    databases.append(database)
    persistence(databases)

def createDatabase(name, mode = 'avl', code = 'ASCII'):
    try:
        chargePersistence()
        if code == 'UTF8' or code == 'ASCII' or code == 'ISO-8859-1':
            if mode == 'avl':
                addDatabase(name, mode, code, avl)
                return avl.createDatabase(name)
            elif mode == 'bplus':
                addDatabase(name, mode, code, bplus)
                return bplus.createDatabase(name)
            elif mode == 'b':
                addDatabase(name, mode, code, b)
                return b.createDatabase(name)
            elif mode == 'hash':
                addDatabase(name, mode, code, _hash)
                return _hash.createDatabase(name)
            elif mode == 'isam':
                addDatabase(name, mode, code, isam)
                return isam.createDatabase(name)
            elif mode == 'dict':
                addDatabase(name, mode, code, _dict)
                return _dict.createDatabase(name)
            elif mode == 'json':
                addDatabase(name, mode, code, json)
                return json.createDatabase(name)
            else:
                return 3
        else:
            return 4
    except:
        return 1

def showDatabases():
    chargePersistence()
    msg = "BASES DE DATOS\n"
    # dbs = []
    for db in databases:
        if '_' not in db['name']:
            msg += f"\t{db['mode']}: {db['name']}\n"
    return msg

def alterDatabase(databaseOld, databaseNew):
    for item in structs:
        value = item.alterDatabase(databaseOld, databaseNew)
        if value != 2:
            for i in databases:
                if databaseOld == i["name"]:
                    i["name"] = databaseNew
                    # persistence()
                    return value
    return 2

def dropDatabase(nameDB):
    for item in structs:
        value = item.dropDatabase(nameDB)
        if value != 2:
            for i in databases:
                if nameDB == i["name"]:
                    databases.remove(i)
                    # persistence()
                    return value
    return 2

def createTable(database, table, nCols):
    for item in structs:
        value = item.createTable(database, table, nCols)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    t = {"name": table, "nCols": nCols, "tuples": [], 
                        "fk": None, "iu": None, "io": None}
                    i["tables"].append(t)
                    persistence(databases)
                    return value
    return 2

def showTables(database):
    chargePersistence()
    tables = []
    for item in databases:
        value = item["mod"].showTables(database)
        if value:
            tables.append(value)
            break
    return tables

def extractTable(database, table):
    chargePersistence()
    alterDatabaseDecompress(database)
    for item in structs:
        value = item.extractTable(database, table)
        if value is not None:
            if value != []:
                return value
    return None

def extractRangeTable(database, table, columnNumber, lower, upper):
    for item in structs:
        value = item.extractRangeTable(database, table, columnNumber, lower, upper)
        if value and value != 1:
            return value
    return []

def alterAddPK(database, table, columns):
    for item in structs:
        value = item.alterAddPK(database, table, columns)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if table == t["name"]:
                            t["pk"] = columns
                            persistence(databases)
                            return value
    return 2

def alterDropPK(database, table):
    for item in structs:
        value = item.alterDropPK(database, table)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if table == t["name"]:
                            t["pk"] = []
                            return value
    return 2

def alterTable(database, old, new):
    for item in structs:
        value = item.alterTable(database, old, new)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if old == t["name"]:
                            t["name"] = new
                        return value
    return 2

def alterDropColumn(database, table, columnNumber):
    for item in structs:
        value = item.alterDropColumn(database, table, columnNumber)
        if value != 2:
            return value
    return 2

def alterAddColumn(database, table, default):
    for item in structs:
        value = item.alterAddColumn(database, table, default)
        if value != 2:
            return value
    return 2

def dropTable(database, table):
    for item in structs:
        value = item.dropTable(database, table)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if table == t["name"]:
                            i["tables"].remove(t)
                    # persistence()
                    return value
    return 2

def insert(database, table, register):
    for item in structs:
        codificacion = codificationValidation(getCodificationMode(database),register)
        if codificacion == True:
            value = item.insert(database, table, register) ###AQUI CREO QUE TENGO QUE HACER ESA VALIDACION PAPUA
            if value != 2:
                for i in databases:
                    if database == i["name"]:
                        for t in i["tables"]:
                            if table == t["name"]:
                                tupla = {"register": register} 
                                t["tuples"].append(tupla)
                                persistence(databases)
                                return value
        else:
            return 1                        
    return 2

def extractRow(database, table, columns):
    chargePersistence()
    for item in structs:
        value = item.extractRow(database, table, columns)
        if value:
            return value
    return []

def loadCSV(fileCSV, db, table):
    for item in structs:
        value = item.loadCSV(fileCSV, db, table)
        if value != [] and value[0] != 2:
            # persistence()
            return value
    return value

def update(database, table, register, columns):
    for item in structs:
        value = item.update(database, table, register, columns)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if table == t["name"]:
                            for tup in t["tuples"]:
                                if tup["register"][0] == columns[0]:
                                    index = 0
                                    for key in register:
                                        index = key
                                    tup["register"][index] = register[index]
                        persistence(databases)
                        return value
    return 2

def delete(database, table, columns):
    pass
    # for item in structs:
    #     value = item.delete(database, table, columns)
    #     if value != 2:
    #         for i in databases:
    #             if database == i["name"]:
    #                 for t in i["tables"]:
    #                     if table == t["name"]:
    #                         for tup in t["tuples"]:
    #                             index = 0
    #                             for key in columns:
    #                                 index = key
    #                             tup["register"][index] = register[1]
    #                     return value
    # return 2

def truncate(database, table):
    for item in structs:
        value = item.truncate(database, table)
        if value != 2:
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if table == t["name"]:
                            t["tuples"] = []
                    # persistence()
                    return value
    return 2

# 2. ADMINISTRADOR DE MODO DE ALMACENAMIENTO
def alterDatabaseMode(database, mode):
    try:
        changueMode(databases)
        for db in databases:
            if db["name"] == database:
                dbCopy = db.copy()
                databases.remove(db)
                dbCopy["mod"].dropDatabase(dbCopy["name"])
                createDatabase(dbCopy["name"], mode, dbCopy["code"])
                for table in dbCopy["tables"]:
                    createTable(dbCopy["name"], table["name"], table["nCols"])
                    for reg in table["tuples"]:
                        insert(dbCopy["name"], table["name"], reg["register"])
                persistence(databases)
                return 0
    except:
        return 1

# 3. ADMINISTRACION DE INDICES
def alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef):
    pass

def alterTableDropFK(database, table, indexName):
    pass

# 4. ADMINISTRACION DE LA CODIFICACION
def alterDatabaseEncoding(database,encoding):
    if encoding =="ASCII" or encoding =="ISO-8859-1" or encoding =="UTF8":
        pass
    else:
        return 3
    try:
        i=0
        for db in databases:
            if db["name"] == database:
                for table in db["tables"]:
                    for tupla in table["tuples"]:
                        for register in tupla["register"]:
                            if isinstance(register, str) : 
                                codificacion = codificationValidation(encoding,register)    
                                if codificacion == True:
                                    pass
                                else:
                                    return 1     
                break                          
            i+=1   
        if i==len(databases):
            return 2
        else:
            return 0    
    except:
        return 1

def codificationValidation(codification,stringlist): ##Cristian
    if codification=="ASCII":
        try:
            for i in stringlist:
                if isinstance(i, str) : ##verifica si la validacion es para una cadena
                    i.encode('ascii')       
                else:
                    pass
            return True    
        except:
            return False    

    elif codification=="ISO-8859-1":
        try:
            for i in stringlist:
                if isinstance(i, str) : ##verifica si la validacion es para una cadena
                    i.encode('latin-1')       
                else:
                    pass
            return True    
        except:
            return False
    elif codification=="UTF8":
        try:
            for i in stringlist:
                if isinstance(i, str) : ##verifica si la validacion es para una cadena
                    i.encode('utf-8')       
                else:
                    pass
            return True    
        except:
            return False
    else:
        return 3 ##Nombre de codificacion no existente

def getCodificationMode(database):
    for i in databases:
        if database == i["name"]:
            if i["code"] == "ASCII":
                return "ASCII"
            elif i["code"] == "ISO-8859-1":
                return "ISO-8859-1"       
            elif i["code"] == "UTF8":
                return "UTF8"       
    return 2

# 6. COMPRESION DE DATOS
def alterDatabaseCompress(database, level):
    if level not in range(-1, 6):
        return 4
    try:
        for db in databases:
            if db["name"] == database:
                for table in db["tables"]:
                    changueMode(databases)
                    tableCopy = table.copy()
                    table["tuples"] = []
                    db["mod"].truncate(db["name"], table["name"])
                    for tupla in tableCopy["tuples"]:
                        newRegister = []
                        for register in tupla["register"]:
                            if type(register) == str:
                                text = bytes(register, db["code"])
                                register = zlib.compress(text, level)
                            newRegister.append(register)
                        insert(db['name'], table["name"], newRegister)
        return 0
    except:
        return 1

def alterDatabaseDecompress(database):
    try:
        isCompressed = False
        for db in databases:
            if db["name"] == database:
                for table in db["tables"]:
                    changueMode(databases)
                    tableCopy = table.copy()
                    table["tuples"] = []
                    db["mod"].truncate(db["name"], table["name"])
                    for tupla in tableCopy["tuples"]:
                        newRegister = []
                        for register in tupla["register"]:
                            if type(register) == bytes:
                                text = zlib.decompress(register)
                                register = text.decode(db["code"])
                                isCompressed = True
                            newRegister.append(register)
                        insert(db['name'], table["name"], newRegister)
        if not isCompressed:
            return 3
        return 0
    except:
        return 1

def alterTableCompress(database, table, level):
    if level not in range(-1, 6):
        return 4
    try:
        for db in databases:
            if db["name"] == database:
                for t in db["tables"]:
                    changueMode(databases)
                    if t["name"] == table:
                        tableCopy = t.copy()
                        t["tuples"] = []
                        db["mod"].truncate(db["name"], t["name"])
                        for tupla in tableCopy["tuples"]:
                            newRegister = []
                            for register in tupla["register"]:
                                if type(register) == str:
                                    text = bytes(register, db["code"])
                                    register = zlib.compress(text, level)
                                newRegister.append(register)
                            insert(db['name'], t["name"], newRegister)
                        return 0
                else:
                    return 3
            else:
                return 2
    except:
        return 1

def alterTableDecompress(database, table, level):
    try:
        isCompressed = False
        for db in databases:
            if db["name"] == database:
                for table in db["tables"]:
                    if table["name"] ==  table:
                        tableCopy = table.copy()
                        table["tuples"] = []
                        db["mod"].truncate(db["name"], table["name"])
                        for tupla in tableCopy["tuples"]:
                            newRegister = []
                            for register in tupla["register"]:
                                if type(register) == bytes:
                                    text = zlib.decompress(register)
                                    register = text.decode(db["code"])
                                    isCompressed = True
                                newRegister.append(register)
                            insert(db['name'], table["name"], newRegister)
                    else:
                        return 3
            else:
                return 2
        if not isCompressed:
            return 3
        return 0
    except:
        return 1

# 7. SEGURIDAD
"""
    @description
        Encripta información.
    @param
        backup: información que se desea encriptar.
        password: llave con la que se encriptará la información.
    @return
        Información encriptada.
"""
def encrypt(backup, password):
    return Fernet(password).encrypt(backup.encode()).decode()

"""
    @description
        Descencripta información.
    @param
        cipherBackup: información que se desea descencriptar.
        password: clave con la que se desencriptará la información.
    @return
        Información descencriptada.
"""
def decrypt(cipherBackup, password):
    return Fernet(password).decrypt(cipherBackup.encode()).decode()

def persistence(databases):
    try:
        if path.exists("DB"):
            os.remove("DB")
        archivo = open("DB", "wb")
        for db in databases:
            db["mod"] = db["mode"]
        pickle.dump(databases, archivo)
        archivo.close()
        del(archivo)
    except: 
        pass

def chargePersistence():
    n = databases
    if path.isfile("DB") and len(n) == 0 and path.getsize("DB") > 0:
        archivo = open("DB" , "rb")
        data = pickle.load(archivo)
        changueMode(data, True)
        archivo.close()
        print("bases de datos cargadas")

def changueMode(database, isPersistence = False):
    for i in database:
        if i["mod"] == 'avl':
            i["mod"] = avl
        elif i["mod"] == 'b':
            i["mod"] == b
        elif i["mod"] == 'bplus':
            i["mod"] = bplus
        elif i["mod"] == 'hash':
            i["mod"] = _hash
        elif i["mod"] == 'isam':
            i["mod"] = isam
        elif i["mod"] == 'dict':
            i["mod"] = _dict
        elif i["mod"] == 'json':
            i["mod"] = json
        if isPersistence:
            databases.append(i)
