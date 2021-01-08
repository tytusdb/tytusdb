import os
import json as Json
import pickle
import zlib
import binascii
import sys
from cryptography.fernet import Fernet
from BlockChain.BlockChain import BlockChain

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
listBlockChain = []
uIndex = {}
isCompressed = False

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
            if value != 0:
                return value
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
            if value != 0:
                return value
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
            if value != 0:
                return value
            for i in databases:
                if database == i["name"]:
                    t = {"name": table, "nCols": nCols, "tuples": [], "safeMode": False,
                        "fk": None, "iu": None, "io": None, "indexName": None}
                    i["tables"].append(t)
                    persistence(databases)
                    return value
    return 2

def showTables(database):
    chargePersistence()
    tables = []
    changueMode(databases)
    for item in databases:
        value = item["mod"].showTables(database)
        if value:
            tables.append(value)
            break
    return tables

def extractTable(database, table):
    chargePersistence()
    # if isCompressed:
    alterDatabaseDecompress(database)
    changueMode(databases)
    for item in databases:
        value = item["mod"].extractTable(database, table)
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
            if value != 0:
                return value
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
            if value != 0:
                return value
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
            if value != 0:
                return value
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
            if value != 0:
                return value
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if table == t["name"]:
                            for tup in t["tuples"]:
                                tup["register"].pop(columnNumber)
            t["nCols"] -= 1
            persistence(databases)
            return value
    return 2

def alterAddColumn(database, table, default):
    for item in structs:
        value = item.alterAddColumn(database, table, default)
        if value != 2:
            if value != 0:
                return value
            return value
    return 2

def dropTable(database, table):
    for item in structs:
        value = item.dropTable(database, table)
        if value != 2:
            if value != 0:
                return value
            for i in databases:
                if database == i["name"]:
                    for t in i["tables"]:
                        if table == t["name"]:
                            i["tables"].remove(t)
                    persistence()
                    return value
    return 2

def insert(database, table, register):
    for item in structs:
        codificacion = codificationValidation(getCodificationMode(database),register)
        if codificacion == True:
            if insertVerifyUnique(database, table, register ):   #verifica si la tabla tiene indices unicos y si el indice unico viene en null
                value = item.insert(database, table, register)
                Unique(database,table,register)
                if value != 2:
                    if value != 0:
                        return value
                    for i in databases:
                        if database == i["name"]:
                            for t in i["tables"]:
                                if table == t["name"]:
                                    tupla = {"register": register} 
                                    t["tuples"].append(tupla)
                                    #START BlockChain
                                    i = 0
                                    while i<len(listBlockChain):
                                        if(listBlockChain[i].getName() == (str(database)+"_"+str(table))):
                                            listBlockChain[i].addNodeNoSecure(register)
                                            listBlockChain[i].generateJsonSafeMode()
                                        i += 1
                                    #END BlockChain
                                    persistence(databases)
                                    return value
            else:
                return 1
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
        # value = item.loadCSV(fileCSV, db, table)
        import csv
        try:
            with open(fileCSV, 'r') as fileCsv:
                lector = csv.reader(fileCsv, delimiter = ',')
                listaResultado = []
                for f in lector:
                    listaResultado.append(insert(db, table, f))
                return listaResultado
                # print("Operación Exitosa")
        except:
            raise

def update(database, table, register, columns):
    for item in structs:
        value = item.update(database, table, register, columns)
        # START BlockChain
        i = 0
        while i<len(listBlockChain):
            if listBlockChain[i].getName() == (str(database)+"_"+str(table)):
                j = 0
                tuplesBlockChain = listBlockChain[i].getListValues()
                tuples = extractTable("ventas", "producto")
                while j < len(tuplesBlockChain):
                    k = 0
                    newValue = ""
                    while k < len(tuples):
                        if tuples[k] not in tuplesBlockChain:
                            newValue = tuples[k]
                        k += 1
                    if tuplesBlockChain[j] not in tuples:#.getValue()
                        listBlockChain[i].alterValueNode(newValue, j)
                        listBlockChain[i].generateJsonSafeMode()
                    j += 1
                break    
            i += 1
        # END BlockChain
        if value != 2:
            if value != 0:
                return value
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
            if value != 0:
                return value
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
    chargePersistence()
    try:
        changueMode(databases)
        for db in databases:
            if db["name"] == database:
                dbCopy = db.copy()
                databases.remove(db)
                dbCopy["mod"].dropDatabase(dbCopy["name"])
                createDatabase(dbCopy["name"], mode, dbCopy["code"])
                for table in dbCopy["tables"]:
                    size = len(table["tuples"][0]["register"])
                    table["nCols"] = size
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


def insertVerifyUnique(database, table,tupla ):
    try:
        tabla = uIndex[database]
        indices = tabla[table]
        indiceTbl = table+indices[0]
        listaIndices = indices[1]
        uniqueIndices = [tupla[x] for x in listaIndices]
        if None in uniqueIndices:
            return False
        else:
            for estructura in structs: 
                    value = estructura.extractRow(database,indiceTbl,uniqueIndices)
                    if value[0] == uniqueIndices[0]:
                        return False
                    else:    
                        return True
            
    except: 
        return True

def Unique(database, table,  tupla):
    try:
        tabla = uIndex[database]
        indices = tabla[table]
        indiceTbl = table+indices[0]
        listaIndices = indices[1]
        uniqueIndices = [tupla[x] for x in listaIndices]
        if None in uniqueIndices:
            return True
        else:
            for estructura in structs: 
                    value = estructura.insert(database,indiceTbl,uniqueIndices)
                    if value !=2 :
                        return False
                    else:    
                        return True
            
    except: 
        return True





def alterTableaddUnique(database , table,  indexName, colums): 
    tabla = {}
    for item in structs: 
        tuplas = item.extractTable(database,table)
        if tuplas :
            if database in list(uIndex.keys()):
                tabla_dic = uIndex[database]
                if table in list(tabla_dic.keys()):
                    indice = (indexName, colums)
                    tabla_dic[table] = indice
                    uIndex[database] = tabla_dic
                else:
                    indice = (indexName , colums)
                    tabla_dic[table] = indice
                    uIndex[database] = tabla_dic
            else:
                indice = (indexName , colums)
                tabla[table] = indice
                uIndex[database] = tabla
            if item.createTable(database, table+indexName , len(colums)) != 3 and item.alterAddPK(database, table+indexName, colums)!= 4:
                for i in tuplas: 
                    unicos = [i[x] for x in colums]
                    if None in unicos:
                        return 2
                    else:
                        value = item.insert(database, table+indexName, unicos)
                        if value == 2:
                            return 2 
                    
            else: 
                return 2

# 4. ADMINISTRACION DE LA CODIFICACION
def alterDatabaseEncoding(database,encoding):
    chargePersistence()
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
    if level not in range(-1, 10):
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
                    global isCompressed
                    isCompressed = True
        return 0
    except:
        return 1

def alterDatabaseDecompress(database):
    try:
        chargePersistence()
        global isCompressed
        if not isCompressed:
            return 3
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
                return 0
    except:
        return 1

def alterTableCompress(database, table, level):
    if level not in range(-1, 9):
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
                            isCompressed = True
                        return 0
                else:
                    return 3
            else:
                return 2
    except:
        return 1

def alterTableDecompress(database, table, level):
    try:
        chargePersistence()
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

#generar el grafo reporte del block chain
def generateGraphBlockChain(database, table):
    i = 0
    fileName = str(database)+"_"+str(table)+"BC"
    while i < len(listBlockChain):
        if listBlockChain[i].getName() == (str(database)+"_"+str(table)):
            data = listBlockChain[i].generateGraph()
            with open(fileName+".dot", "w") as file:
                file.write(data)
            os.system("dot -Tpng "+fileName+".dot"+" -o "+fileName+".png")
            break
            
        else:
            print("No se encontro el Block Chain de la tabla indicada")
        i += 1  
    ### WORK BLOCKCHAIN ###
"""
    @description 
        Activa el modo seguro para una tabla de una base de datos
    @param
        database: Nombre de la base de datos a utilizar
        table: Nombre de la tabla a utilizar
    @return 
        0: Operación exitosa
        1: Error en la operación
        2: database inexistente
        3: table inexistente
        4: Modo seguro inexistente
"""
def safeModeOn(database, table):
    try:
        for db in databases:
            #verifica si la base de datos existe
            if db.get("name") == database:
                for tb in db.get("tables"):
                    #verifica si la tabla existe
                    if tb.get("name") == table:
                        #verifica si el modo seguro esta activado
                        if tb.get("safeMode"):
                            #Modo seguro existente
                            return 4
                        tb["safeMode"] = True
                        #_________________________________________________________
                        bc = BlockChain(str(database)+"_"+str(table))
                        for tp in tb.get("tuples"):
                            bc.addNode(tp.get("register"))
                        bc.generateJsonSafeMode()
                        listBlockChain.append(bc)
                        #_________________________________________________________
                #tabel inexistente
                return 3
        #database inexistente
        return 2
    except:
        #Error en la operación
        return 1

"""
    @description
        Desactiva el modo en la tabla especificada de la base de datos
    @param
        database: Nombre de la base de datos a utilizar
        table: Nombre de la tabla a utilizar
    @return 
        0: Operación exitosa
        1: Error en la operación
        2: database inexistente
        3: table inexistente
        4: modo seguro no inexistente
"""
def safeModeOff(database, table):
    try:
        for db in databases:
            #verifica si la base de datos existe
            if db.get("name") == database:
                for tb in db.get("tables"):
                    #verifica si la tabla existe
                    if tb.get("name") == table:
                        #verifica si el modo seguro esta activado
                        if tb.get("safeMode"):
                            tb["safeMode"] = False
                            os.remove('BlockChain\\'+str(database)+'_'+str(table)+'.json')
                            return 0
                        #Modo seguro no existente
                        return 4
                #tabel inexistente
                return 3
        #database inexistente
        return 2
    except:
        #Error en la operación
        return 1

# PERSISTENCIA DE DATOS
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
        # print("bases de datos cargadas")

def changueMode(database, isPersistence = False):
    for i in database:
        if i["mod"] == 'avl':
            i["mod"] = avl
        elif i["mod"] == 'b':
            i["mod"] = b
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
            
"""
    @description
        Agrega un índice, creando una estructura adicional con el 
        modo indicado para la base de datos.
    @param
        database: Nombre de la base de datos a utilizar.
        table: Nombre de la tabla donde están las llaves foráneas.
        indexName: Nombre único del índice manejado como metadato de la 
                   tabla para ubicarlo fácilmente.
        columns: Conjunto de índices de columnas que forman parte de la 
                 llave foránea, mínimo debe ser una columna.
    @return
        0: Operación exitosa
        1: Error en la operación
        2: database no existente
        3: table no existente
        4: ???
"""
def alterTableAddIndex(database, table, indexName, columns):
    try:
        for i in databases:
            #verifica si la base de datos existe
            if i.get("name") == database:
                #obtiene el tipo de almacenamiento en base al modo de la DB
                modeStorage = None
                if i.get("mode") == "b":
                    modeStorage = b
                elif i.get("mode") == "avl":
                    modeStorage = avl
                elif i.get("mode") == "bplus":
                    modeStorage = avl
                elif i.get("mode") == "_hash":
                    modeStorage = _hash
                elif i.get("mode") == "isam":
                    modeStorage = isam
                elif i.get("mode") == "_dict":
                    modeStorage = _dict
                elif i.get("mode") == "json":
                    modeStorage = json
                tuples = modeStorage.extractTable(database, table)
                for j in i.get("tables"):
                    #verifica si la tabla existe en la base de datos indicada
                    if j.get("name") == table:
                        j["indexName"] = indexName
                        modeStorage.createTable(database, (table+indexName), len(columns))
                        for tp in tuples:
                            listaData = []
                            for col in columns:
                                listaData.append(tp[col]) 
                            modeStorage.insert(database, (table+indexName), listaData)
                        return 0
                #Tabla no existente
                return 3
        #Base de datos no existente
        return 2
    except Exception as e:
        #Error en la operación
        return 1
