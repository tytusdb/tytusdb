import os
import pickle
import shutil
import zlib
import hashlib
from Blockchain import *
from cryptography.fernet import Fernet

databases = {}  # LIST WITH DIFFERENT MODES
dict_encoding = {'ascii': 1, 'iso-8859-1': 2, 'utf8': 3}
dict_modes = {'avl': 1, 'b': 2, 'bplus': 3, 'dict': 4, 'isam': 5, 'json': 6, 'hash': 7}
algoritms = ['SHA256', 'MD5']


# ---------------------------------------------------- FASE 2  ---------------------------------------------------------
# CREATE DATABASE
def createDatabase(database, mode, encoding):
    if dict_modes.get(mode) is None:
        return 3  # mode incorrect
    elif dict_encoding.get(encoding) is None:
        return 4  # encoding incorrect
    elif os.path.isfile(os.getcwd() + "\\Data\\metadata.bin"):
        dictionary = load('metadata')
        value_db = dictionary.get(database)

        if value_db:
            return 2  # Exist db
        else:
            j = checkMode(mode)
            value_return = j.createDatabase(database)
            if value_return == 1:
                return 1

            dictionary[database] = [mode, encoding, {}]
            save(dictionary, 'metadata')
            return 0
    else:
        j = checkMode(mode)
        value_return = j.createDatabase(database)
        if value_return == 1:
            return 1

        databases[database] = [mode, encoding, {}]
        save(databases, 'metadata')
        return 0

    
# ALTER DATABASEMODE
def alterDatabaseMode(database, mode):
    try:
        dictionary = load('metadata')
        value_db = dictionary.get(database)
        actual_mode = dictionary.get(database)[0]
        encoding = dictionary.get(database)[1]
        dict_tables = dictionary.get(database)[2]

        if value_db is None:
            return 2  # database doesn't exist
        elif dict_modes.get(mode) is None:
            return 4  # mode incorrect

        insertAgain(database, actual_mode, mode)
        dictionary.pop(database)
        dictionary[database] = [mode, encoding, dict_tables]
        save(dictionary, 'metadata')
        return 0
    except:
        return 1
    
    
# ALTER FOREIGN KEY
def alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef):
    try:
        if os.path.isfile(os.getcwd() + "\\Data\\FK.bin"):
            FK = load('FK')
        else:
            FK = {}
        db = load('metadata')
        if db.get(database) is not None:
            j = checkMode(db[database][0])
            tables = j.showTables(database)
            if (table in tables) and (tableRef in tables):
                if len(columns) != 0 and len(columnsRef) != 0:
                    if FK.get(indexName) is None:
                        if 'FK' not in tables:
                            j.createTable(database, 'FK', 6)
                            j.alterAddPK(database, 'FK', [1])
                        j.insert(database, 'FK', [database, indexName, table, columns, tableRef, columnsRef])
                        FK.update({indexName: [database, indexName, table, columns, tableRef, columnsRef]})
                        save(FK, 'FK')
                        return 0
                    return 1
                return 4
            return 3
        return 2
    except:
        return 1
    
    
# DROP FOREIGN KEY
def alterTableDropFK(database, table, indexName):
    try:
        if os.path.isfile(os.getcwd() + "\\Data\\FK.bin"):
            FK = load('FK')
            db = load('metadata')
            if db.get(database) is not None:
                j = checkMode(db[database][0])
                tables = j.showTables(database)
                if table in tables:
                    if FK.get(indexName) is not None:
                        j.delete(database, 'FK', [indexName])
                        FK.pop(indexName)
                        save(FK, 'FK')
                        return 0
                    return 4
                return 3
            return 2
        else:
            FK = {}
            save(FK, 'FK')
    except:
        return 1

# ALTER ADD INDEX UNIQUE
def alterTableAddUnique(database, table, indexName, columns):
    try:
        if os.path.isfile(os.getcwd() + '\\Data\\UNIQUE.bin'):
            UNIQUE = load('UNIQUE')
        else:
            UNIQUE = {}
        db = load('metadata')
        if db.get(database) is not None:
            j = checkMode(db[database][0])
            tables = j.showTables(database)
            if table in tables:
                if len(columns) != 0:
                    if UNIQUE.get(indexName) is None:
                        if 'UNIQUE' not in tables:
                            j.createTable(database, 'UNIQUE', 4)
                            j.alterAddPK(database, 'UNIQUE', [2])
                        j.insert(database, 'UNIQUE', [database, table, indexName, columns])
                        UNIQUE.update({indexName: [database, table, indexName, columns]})
                        save(UNIQUE, 'UNIQUE')
                        return 0
                    return 1
                return 4
            return 3
        return 2
    except:
        return 1

# DROP INDEX UNIQUE
def alterTableDropUnique(database, table, indexName):
    try:
        if os.path.isfile(os.getcwd() + '\\Data\\UNIQUE.bin'):
            UNIQUE = load('UNIQUE')
            db = load('metadata')
            if db.get(database) is not None:
                j = checkMode(db[database][0])
                tables = j.showTables(database)
                if table in tables:
                    if UNIQUE.get(indexName) is not None:
                        j.delete(database, 'UNIQUE', [indexName])
                        UNIQUE.pop(indexName)
                        save(UNIQUE, 'UNIQUE')
                        return 0
                    return 4
                return 3
            return 2
        else:
            UNIQUE = {}
            save(UNIQUE, 'UNIQUE')
    except:
        return 1

# ALTER ADD INDEX
def alterTableAddIndex(database, table, indexName, columns):
    try:
        if os.path.isfile(os.getcwd() + '\\Data\\INDEX.bin'):
            INDEX = load('INDEX')
        else:
            INDEX = {}
        db = load('metadata')
        if db.get(database) is not None:
            j = checkMode(db[database][0])
            tables = j.showTables(database)
            if table in tables:
                if len(columns) != 0:
                    if INDEX.get(indexName) is None:
                        if 'INDEX' not in tables:
                            j.createTable(database, 'INDEX', 4)
                            j.alterAddPK(database, 'INDEX', [2])
                        j.insert(database, 'INDEX', [database, table, indexName, columns])
                        INDEX.update({indexName: [database, table, indexName, columns]})
                        save(INDEX, 'INDEX')
                        return 0
                    return 1
                return 4
            return 3
        return 2
    except:
        return 1

# ALTER DROP INDEX
def alterTableDropIndex(database, table, indexName):
    try:
        if os.path.isfile(os.getcwd() + '\\Data\\INDEX.bin'):
            INDEX = load('INDEX')
            db = load('metadata')
            if db.get(database) is not None:
                j = checkMode(db[database][0])
                tables = j.showTables(database)
                if table in tables:
                    if INDEX.get(indexName) is not None:
                        j.delete(database, 'INDEX', [indexName])
                        INDEX.pop(indexName)
                        save(INDEX, 'INDEX')
                        return 0
                    return 4
                return 3
            return 2
        else:
            INDEX = {}
            save(INDEX, 'INDEX')
    except:
        return 1

# ALTER ENCODING
def alterDatabaseEncoding(database, encoding):
    try:
        if dict_encoding.get(encoding) is not None:
            db = load('metadata')
            if db.get(database) is not None:
                j = checkMode(db[database][0])
                tables = j.showTables(database)
                DB = {}
                for t in tables:
                    registers = j.extractTable(database, t)
                    newRegisters = []
                    for r in registers:
                        newRegister = []
                        for c in r:
                            if isinstance(c, bytes):
                                aux = c.decode(db[database][1]).encode(encoding, 'replace')
                                if '?' in str(aux):
                                    return 1
                                newRegister.append(aux)
                            else:
                                newRegister.append(c)
                        newRegisters.append(newRegister)
                    DB.update({t: newRegisters})
                for key in DB:
                    j.truncate(database, key)
                    registers = DB[key]
                    for r in registers:
                        j.insert(database, key, r)
                db[database][1] = encoding
                save(db, 'metadata')
                return 0
            return 2
        return 3
    except:
        return 1

# CHECKSUM DATABASE
def checksumDatabase(database, mode):
    try:
        if os.path.isfile(os.getcwd() + "\\Data\\checksum.bin"):
            CHCK = load('checksum')
        else:
            CHCK = {}
        db = load('metadata')
        if db.get(database) is not None:
            j = checkMode(db[database][0])
            tables = j.showTables(database)
            if mode.upper() in algoritms:
                content = None
                if mode.upper() == 'MD5':
                    content = hashlib.md5()
                elif mode.upper() == 'SHA256':
                    content = hashlib.sha256()
                for t in tables:
                    file = open(getRouteTable(db[database][0], database, t), 'rb')
                    content.update(file.read())
                    file.close()
                    CHCK.update({database: content.hexdigest()})
                    save(CHCK, 'checksum')
                    return CHCK[database]
            return None
        return None
    except:
        return None

# CHECKSUM TABLE
def checksumTable(database, table, mode):
    try:
        if os.path.isfile(os.getcwd() + "\\Data\\checksum.bin"):
            CHCK = load('checksum')
        else:
            CHCK = {}
        db = load('metadata')
        if db.get(database) is not None:
            if mode.upper() in algoritms:
                content = None
                if mode.upper() == 'MD5':
                    content = hashlib.md5()
                elif mode.upper() == 'SHA256':
                    content = hashlib.sha256()
                file = open(getRouteTable(db[database][0], database, table), 'rb')
                content.update(file.read())
                file.close()
                CHCK.update({table: content.hexdigest()})
                save(CHCK, 'checksum')
                return CHCK[table]
            return None
        return None
    except:
        return None
    
    
# Encrypt and Decrypt
def encrypt(backup, password):
    f = Fernet(password)
    encodedMessage = backup.encode()
    encrypted = f.encrypt(encodedMessage)
    return encrypted.decode()


def decrypt(cripherBackup, password):
    f = Fernet(password)
    desencriptado = f.decrypt(cripherBackup.encode())
    return desencriptado.decode()


def generateKey():
    key = Fernet.generate_key().decode()
    return key

    
# Blockchain
def safeModeOn(database, table):
    try:
        dictionary = load('metadata')
        value_db = dictionary.get(database)

        # If db doesn't exist
        if not value_db:
            return 2

        # If tables doesn't exit
        dict_tables = dictionary.get(database)[2]
        if not dict_tables:
            return 3

        # If table info doesn't exist
        tabla_info = dict_tables.get(table)
        if not tabla_info:
            return 3

        # If modeSecurity is Off
        if tabla_info[1] is False:
            tabla_info[1] = True
            # If object Blockchain is None
            if tabla_info[2] is None:
                BChain = make_block_chain()
                tabla_info[2] = BChain
            save(dictionary, 'metadata')
            return 0
        # If modeSecurity es ON
        return 4
    except:
        return 1


def safeModeOff(database, table):
    try:
        dictionary = load('metadata')
        value_db = dictionary.get(database)

        # If db doesn't exist
        if not value_db:
            return 2

        # If tables doesn't exit
        dict_tables = dictionary.get(database)[2]
        if not dict_tables:
            return 3

        # If table doesn't exist
        tabla_info = dict_tables.get(table)
        if not tabla_info:
            return 3

        # If modeSecurity is ON
        if tabla_info[1] is True:
            tabla_info[1] = False
            # If object Blockchain is not None
            if tabla_info[2] is not None:
                nameJson = str(database) + '-' + str(table)
                tabla_info[2].removeFilesBlock(nameJson)
                tabla_info[2] = None
            save(dictionary, 'metadata')
            return 0
        # If modeSecurity es OFF
        return 4
    except:
        return 1

def alterDatabaseCompress(database, level):
    try:

        if level > 9 or level < 0:
            return 4

        dictionary = load('metadata')
        value_db = dictionary.get(database)
        mode = dictionary.get(database)[0]

        if value_db:
            j = checkMode(mode)
            tables = j.showTables(database)
            for table in tables:
                newTable = []
                tableEx = j.extractTable(database, table)

                for tuple in tableEx:
                    newTuple = []
                    for register in tuple:
                        if isinstance(register, bytes):
                            compressed = zlib.compress(register, level)
                            newTuple.append(compressed)
                        else:
                            newTuple.append(register)

                    newTable.append(newTuple)

                j.truncate(database, table)

                for tuple in newTable:
                    j.insert(database, table, tuple)

                save(dictionary, 'metadata')
            return 0
            # print(newTable)

        else:
            return 2
    except:
        return 1
    
def alterDatabaseDecompress(database):
    try:

        dictionary = load('metadata')
        value_db = dictionary.get(database)
        mode = dictionary.get(database)[0]

        if value_db:
            j = checkMode(mode)
            tables = j.showTables(database)
            for table in tables:
                newTable = []
                tableEx = j.extractTable(database, table)

                if tupleIsnotCompressed(tableEx):
                    return 3

                for tuple in tableEx:
                    newTuple = []
                    for register in tuple:
                        if iscompressed(register):
                            # print("Tamaño sin comprimir %d" % len(register))
                            decompressed = zlib.decompress(register)
                            # print("Tamaño comprimido %d" % len(compressed))
                            newTuple.append(decompressed)
                        else:
                            newTuple.append(register)

                    newTable.append(newTuple)

                j.truncate(database, table)

                for tuple in newTable:
                    j.insert(database, table, tuple)

                save(dictionary, 'metadata')
            return 0
            # print(newTable)

        else:
            return 2
    except:
        return 1
    
def alterTableCompress(database, table, level):
    try:

        if level > 9 or level < 0:
            return 4

        newTable = []

        dictionary = load('metadata')
        value_db = dictionary.get(database)
        mode = dictionary.get(database)[0]

        if value_db:
            j = checkMode(mode)
            tableEx = j.extractTable(database, table)
            for tuple in tableEx:
                newTuple = []
                for register in tuple:
                    if isinstance(register, bytes):
                        # print("Tamaño sin comprimir %d" % len(register))
                        compressed = zlib.compress(register, level)
                        # print("Tamaño comprimido %d" % len(compressed))
                        newTuple.append(compressed)
                    else:
                        newTuple.append(register)

                newTable.append(newTuple)

            j.truncate(database, table)

            for tuple in newTable:
                j.insert(database, table, tuple)

            save(dictionary, 'metadata')
            return 0
            # print(newTable)

        else:
            return 2
    except:
        return 1
    
def alterTableDecompress(database, table):
    try:
        newTable = []

        os.path.isfile(os.getcwd() + "\\Data\\metadata.bin")
        dictionary = load('metadata')
        value_db = dictionary.get(database)
        mode = dictionary.get(database)[0]

        if value_db:
            j = checkMode(mode)
            tableEx = j.extractTable(database, table)

            if tupleIsnotCompressed(tableEx):
                return 3

            for tuple in tableEx:
                newTuple = []
                for register in tuple:
                    if iscompressed(register):
                        # print("Tamaño sin comprimir %d" % len(register))
                        decompressed = zlib.decompress(register)
                        # print("Tamaño comprimido %d" % len(compressed))
                        newTuple.append(decompressed)
                    else:
                        newTuple.append(register)

                newTable.append(newTuple)

            j.truncate(database, table)

            for tuple in newTable:
                j.insert(database, table, tuple)

            save(dictionary, 'metadata')
            return 0
            # print(newTable)

        else:
            return 2
    except:
        return 1
    
    
# FIRST REPORT GRAPH
def graphDSD(database):
    try:
        dictionaryFK = load('FK')
        listValues = FKDatabse(dictionaryFK, database)
        dictionaryAux = {}
        counter = 0

        dictDatabases = load('metadata')
        if dictDatabases.get(database) is None:
            return None

        string = 'digraph G{\n'
        string += f'label = "DIAGRAMA DE ESTRUCTURA DE DATOS: {database}"\n'
        string += 'labelloc = \"t\"\n'
        string += 'fontsize = \"30\"\n'
        string += 'edge[ arrowhead = \"open\" ]\n'
        string += "node[shape = \"ellipse\", fillcolor = \"turquoise\", style = \"filled\", fontcolor = \"black\" ]\n"

        for element in range(0, len(listValues)):
            listElement = listValues[element]
            start = listElement[4]
            end = listElement[2]

            if dictionaryAux.get(start) is None:
                dictionaryAux[start] = [start, counter]
                counter += 1
            if dictionaryAux.get(end) is None:
                dictionaryAux[end] = [end, counter]
                counter += 1

            valuesStart = dictionaryAux.get(start)
            valuesEnd = dictionaryAux.get(end)
            string += f'node{valuesStart[1]} -> node{valuesEnd[1]}\n'

        for key in dictionaryAux:
            values = dictionaryAux.get(key)
            string += f'node{values[1]} [ label = "{values[0]}"]\n'

        string += '}'
        file = open("DSD.dot", "w")
        file.write(string)
        file.close()
        os.system("dot -Tpng DSD.dot -o DSD.png")

        return string
    except:
        return None

    
# SECOND REPORT GRAPH
def graphDF(database, table):
    try:
        dictUnique = load('UNIQUE')
        dictDatabases = load('metadata')
        dictPK = load('PK')
        dictTables = dictDatabases.get(database)[2]
        numberColumns = dictTables.get(table)[0]
        values = databaseTableIndex(dictPK, database, table)
        listPK = values[2]

        listIndex = databaseTableIndex(dictUnique, database, table)
        print('LISTA DE INDICES: ', listIndex)

        counter = 0
        dictIndexUnique = {}
        dictNormalIndex = {}
        dictAuxPK = {}
        rank = ''

        if listIndex is None:
            dictDatabases = load('metadata')
            dictPK = load('PK')
            dictTables = dictDatabases.get(database)[2]
            numberColumns = dictTables.get(table)[0]
            values = databaseTableIndex(dictPK, database, table)
            listPK = values[2]

            counter = 0
            dictNormalIndex = {}
            dictAuxPK = {}
            rank = ''

            labelTable = concatenateColumns(table, None, numberColumns, listPK)

            string = 'digraph G{\n'
            string += f'label = "DIAGRAMA DE DEPENDENCIA:\\n {database} - {table}"\n'
            string += 'labelloc = \"t\"\n'
            string += 'fontsize = \"30\"\n'
            string += 'edge[ arrowhead = \"open\" ]\n'
            string += "node[shape = \"ellipse\", fillcolor = \"olivedrab2\", style = \"filled\", fontcolor = \"black\" ]\n"
            # TABLE GRAPHVIZ
            string += f'node9898 [ shape = "box", label= "{labelTable}", width=1, height=1.5 ]\n'
            string += "node[shape = \"ellipse\", fillcolor = \"turquoise\", style = \"filled\", fontcolor = \"black\" ]\n"

            rank += '{ rank = same; '
            # LIST PK
            for i in listPK:
                string += f'node{counter} [ label = "{i}_PK" ]\n'
                dictAuxPK[i] = counter
                rank += f'node{counter}; '
                counter += 1
            rank += '}\n'
            string += rank

            rank = ''
            rank += '{ rank = same; '
            for i in range(0, numberColumns):
                pk = dictAuxPK.get(i)
                if pk is None:
                    string += f'node{counter} [ label = "{i}"]\n'
                    dictNormalIndex[i] = counter
                    rank += f'node{counter}; '
                    counter += 1
            rank += '}\n'
            string += rank

            # PK -> NORMAL INDEX
            for keyPK in dictAuxPK:
                for keyNormal in dictNormalIndex:
                    string += f'node{dictAuxPK[keyPK]} -> node{dictNormalIndex[keyNormal]} [ color = "orangered1" ]\n'

            string += '}'

            file = open("DF.dot", "w")
            file.write(string)
            file.close()
            os.system("dot -Tpng DF.dot -o DF.png")

            return string

        else:
            labelTable = concatenateColumns(table, listIndex[3], numberColumns, listPK)

            string = 'digraph G{\n'
            string += f'label = "DIAGRAMA DE DEPENDENCIA:\\n {database} - {table}"\n'
            string += 'labelloc = \"t\"\n'
            string += 'fontsize = \"30\"\n'
            string += 'edge[ arrowhead = \"open\" ]\n'
            string += "node[shape = \"ellipse\", fillcolor = \"olivedrab2\", style = \"filled\", fontcolor = \"black\" ]\n"
            # TABLE GRAPHVIZ
            string += f'node9898 [ shape = "box", label= "{labelTable}", width=1, height=1.5 ]\n'
            string += "node[shape = \"ellipse\", fillcolor = \"turquoise\", style = \"filled\", fontcolor = \"black\" ]\n"

            rank += '{ rank = same; '
            # LIST PK
            for i in listPK:
                string += f'node{counter} [ label = "{i}_PK" ]\n'
                dictAuxPK[i] = counter
                rank += f'node{counter}; '
                counter += 1
            rank += '}\n'
            string += rank

            rank = ''
            rank += '{ rank = same; '
            # INDEX NODES UNIQUE
            for i in listIndex[3]:
                string += f'node{counter} [ label = "{i}_IU" ]\n'
                dictIndexUnique[i] = counter
                rank += f'node{counter}; '
                counter += 1
            rank += '}\n'
            string += rank

            rank = ''
            rank += '{ rank = same; '
            for i in range(0, numberColumns):
                index = dictIndexUnique.get(i)
                pk = dictAuxPK.get(i)
                if index is None and pk is None:
                    string += f'node{counter} [ label = "{i}"]\n'
                    dictNormalIndex[i] = counter
                    rank += f'node{counter}; '
                    counter += 1
            rank += '}\n'
            string += rank

            # CONECTIONS
            # PK -> INDEX UNIQUE
            for keyPK in dictAuxPK:
                for keyUnique in dictIndexUnique:
                    string += f'node{dictAuxPK[keyPK]} -> node{dictIndexUnique[keyUnique]} [ color = "orangered1" ]\n'

            # PK -> NORMAL INDEX
            for keyPK in dictAuxPK:
                for keyNormal in dictNormalIndex:
                    string += f'node{dictAuxPK[keyPK]} -> node{dictNormalIndex[keyNormal]} [ color = "orangered1" ]\n'

            # INDEX UNIQUE -> NORMAL INDEX
            for keyUnique in dictIndexUnique:
                for keyNormal in dictNormalIndex:
                    string += f'node{dictIndexUnique[keyUnique]} -> node{dictNormalIndex[keyNormal]}[ color = "indigo" ]\n'

            string += '}'

            file = open("DF.dot", "w")
            file.write(string)
            file.close()
            os.system("dot -Tpng DF.dot -o DF.png")

            return string
    except:
        return None
    
    
# ---------------------------------------------- AUXILIARY FUNCTIONS  --------------------------------------------------
# SHOW DICTIONARY
def showDict(dictionary):
    print('-- DATABASES --')
    for key in dictionary:
        print(key, ":", dictionary[key])

# ROUTES TABLES
def getRouteTable(mode, database, table):
    if mode == 'avl':
        return os.getcwd() + '\\Data\\avlMode\\' + database + '_' + table + '.tbl'
    elif mode == 'b':
        return os.getcwd() + '\\Data\\b\\' + database + '-' + table.lower() + '-b.bin'
    elif mode == 'bplus':
        return os.getcwd() + '\\Data\\BPlusMode\\' + database + '\\' + table + '\\' + table + '.bin'
    elif mode == 'dict':
        return os.getcwd() + '\\Data\\' + database + '\\' + table + '.bin'
    elif mode == 'isam':
        return os.getcwd() + '\\Data\\ISAMMode\\tables\\' + database.lower() + table.lower() + '.bin'
    elif mode == 'json':
        return os.getcwd() + '\\Data\\json\\' + database + '-' + table
    elif mode == 'hash':
        return os.getcwd() + '\\Data\\hash\\' + database + '\\' + table + '.bin'

# SHOW DICTIONARY FK
def showFK(dictionary):
    print('--FOREIGN KEYS--')
    for key in dictionary:
        print(key, ':', dictionary[key])

# SHOW DICTIONARY UNIQUE
def showUNIQUE(dictionary):
    print('--UNIQUE INDEX--')
    for key in dictionary:
        print(key, ':', dictionary[key])

# SHOW DICTIONARY INDEX
def showINDEX(dictionary):
    print('--INDEX--')
    for key in dictionary:
        print(key, ':', dictionary[key])

# SHOW DICTIONARY PK
def showPK(dictionary):
    print('--PRIMARY KEYS--')
    for key in dictionary:
        print(key, ':', dictionary[key])    

# SHOW MODE
def showMode(mode):
    j = checkMode(mode)
    print(mode, j.showDatabases())


# CHECK MODE
def checkMode(mode):
    if mode == 'avl':
        from storage.avl import avl_mode as j
        return j

    elif mode == 'b':
        from storage.b import b_mode as j
        return j

    elif mode == 'bplus':
        from storage.bplus import bplus_mode as j
        return j

    elif mode == 'dict':
        from storage.dict import dict_mode as j
        return j

    elif mode == 'isam':
        from storage.isam import isam_mode as j
        return j

    elif mode == 'json':
        from storage.json import json_mode as j
        return j

    elif mode == 'hash':
        from storage.hash import hash_mode as j
        return j
    
# If tuple is compressed
def tupleIsnotCompressed(array):
    flag = True

    for tuple in array:
        for register in tuple:
            if iscompressed(register):
                return False

    return flag

def iscompressed(data):
    result = True
    try:
        s = zlib.decompress(data)
    except:
        result = False
    return result


def insertAgain(database, mode, newMode):
    old_mode = checkMode(mode)
    new_mode = checkMode(newMode)
    new_mode.createDatabase(database)
    tables = old_mode.showTables(database)

    dictionary = load('metadata')
    dictPK = loadReturn('PK')  
    dictFK = loadReturn('FK')
    dictUNIQUE = loadReturn('UNIQUE')
    dictINDEX = loadReturn('INDEX')
    dict_tables = dictionary.get(database)[2]

    if tables:
        for name_table in tables:
            if name_table != 'FK' and name_table != 'UNIQUE' and name_table != 'INDEX':
                register = old_mode.extractTable(database, name_table)  
                number_columns = dict_tables.get(name_table)[0]
                new_mode.createTable(database, name_table, number_columns)

                # ADDING PK
                if dictPK != 1:
                    values = dictPK.get(name_table)
                    if values:
                        listPK = values[2]
                        if 'HIDDEN' not in listPK:
                            new_mode.alterAddPK(database, name_table, listPK)

                if register:  # There are registers
                    for list_register in old_mode.extractTable(database, name_table):
                        new_mode.insert(database, name_table, list_register)

            elif name_table == 'FK':
                # ADDING FK
                if dictFK != 1:
                    for key in dictFK:
                        new_mode_tables = new_mode.showTables(database)
                        values = dictFK[key]
                        if values[0] == database:
                            if 'FK' not in new_mode_tables:
                                new_mode.createTable(database, 'FK', 6)
                                new_mode.alterAddPK(database, 'FK', [1])
                            new_tuple = []
                            for i in dictFK[key]:
                                if isinstance(i, str):
                                    new_tuple.append(i.encode(dictionary[database][1]))
                                else:
                                    new_tuple.append(i)
                            new_mode.insert(database, 'FK', dictFK[key])

            elif name_table == 'UNIQUE':
                # ADDING UNIQUE
                if dictUNIQUE != 1:
                    for key in dictUNIQUE:
                        new_mode_tables = new_mode.showTables(database)
                        values = dictUNIQUE[key]
                        if values[0] == database:
                            if 'UNIQUE' not in new_mode_tables:
                                new_mode.createTable(database, 'UNIQUE', 4)
                                new_mode.alterAddPK(database, 'UNIQUE', [2])
                            new_tuple = []
                            for i in dictUNIQUE[key]:
                                if isinstance(i, str):
                                    new_tuple.append(i.encode(dictionary[database][1]))
                                else:
                                    new_tuple.append(i)
                            new_mode.insert(database, 'UNIQUE', new_tuple)

            elif name_table == 'INDEX':
                # ADDING INDEX
                if dictINDEX != 1:
                    for key in dictINDEX:
                        new_mode_tables = new_mode.showTables(database)
                        values = dictINDEX[key]
                        if values[0] == database:
                            if 'INDEX' not in new_mode_tables:
                                new_mode.createTable(database, 'INDEX', 4)
                                new_mode.alterAddPK(database, 'INDEX', [2])
                            new_tuple = []
                            for i in dictINDEX[key]:
                                if isinstance(i, str):
                                    new_tuple.append(i.encode(dictionary[database][1]))
                                else:
                                    new_tuple.append(i)
                            new_mode.insert(database, 'INDEX', new_tuple)

        old_mode.dropDatabase(database)   
        
        

# Blockchain mode when the security mode is on
def make_block_chain():
    BChain = Blockchain()
    return BChain


def graphBChain(blockchainObject, nombreImagen):
    blockchainObject.graphBlockchain(nombreImagen)
        
        
def listGraph(list_):
    string = 'digraph G{\n'
    string += 'fontsize = \"30\"\n'
    string += 'edge[ arrowhead = \"open\"\n ]'
    string += "node[shape = \"ellipse\", fillcolor = \"turquoise\", style = \"filled\", fontcolor = \"black\" ]\n"

    for i in range(0, len(list_)):
        string += f'node{hash(list_[i])*hash(list_[i])} [ label = "{list_[i]}"]\n'
        if i == len(list_)-1:
            pass
        else:
            string += f'node{hash(list_[i])*hash(list_[i])} -> node{hash(list_[i+1])*hash(list_[i+1])}\n'

    string += '}'
    file = open("List.circo", "w")
    file.write(string)
    file.close()
    os.system("circo -Tpng List.circo -o List.png")        


def concatenateStrings(list_):
    string = ''
    for i in range(0, len(list_)):
        if i == len(list_) - 1:
            string += str(list_[i])
        else:
            string += str(list_[i])+', '
    return string


def tupleGraph(list_):
    string = 'digraph G{\n'
    string += 'fontsize = \"30\"\n'
    string += 'edge[ arrowhead = \"open\"\n ]'
    string += "node[shape = \"ellipse\", fillcolor = \"turquoise\", style = \"filled\", fontcolor = \"black\" ]\n"

    for i in range(0, len(list_)):
        tuple_i = concatenateStrings(list_[i])

        string += f'node{hash(tuple_i) * hash(tuple_i)} [ label = "{tuple_i}"]\n'
        if i == len(list_)-1:
            pass
        else:
            tuple_iplus = concatenateStrings(list_[i + 1])
            string += f'node{hash(tuple_i)*hash(tuple_i)} -> node{hash(tuple_iplus)*hash(tuple_iplus)}\n'

    string += '}'
    file = open("List.circo", "w")
    file.write(string)
    file.close()
    os.system("circo -Tpng List.circo -o List.png")   
    

# FIRST REPORT GRAPH: SELECT ONLY ONE DATABASE
def FKDatabse(dictionary, database):
    listValues = []
    for key in dictionary:
        values = dictionary[key]
        if values[0] == database:
            listValues.append(values)

    return listValues


# SECOND REPORT GRAPH
def concatenateColumns(table, listIndex, numberColumns, listPK):
    string = ''
    string += f'TABLA: {table}\\n'
    if listIndex is None:
        for i in range(0, numberColumns):
            if i in listPK:
                string += f'{i}_PK\\n'
            else:
                string += f'{i}\\n'
    else:
        for i in range(0, numberColumns):
            if i in listIndex:
                string += f'{i}_IU\\n'
            elif i in listPK:
                string += f'{i}_PK\\n'
            else:
                string += f'{i}\\n'

    return string


# SELECT ONLY ONE DATABASE AND TABLE
def databaseTableIndex(dictionary, database, table):
    for key in dictionary:
        values = dictionary[key]
        if values[0] == database and values[1] == table:
            return values

# ------------------------------------------------------ FASE 1 --------------------------------------------------------
# -------------------------------------------------- Table CRUD --------------------------------------------------------

#SHOWDATABASES
def showDatabases():
    try:
        for key in dict_modes:
            print(key)
            j = checkMode(key)
            value_return = j.showDatabases()
            print(value_return)
    except:
        return []
    
    
# ALTERDATABASE
def alterDatabase(databaseOld, databaseNew):
    try:
        dictionary = load('metadata')
        value_dbO = dictionary.get(str(databaseOld))
        value_dbN = dictionary.get(str(databaseNew))
        if not value_dbO:
            return 2
        if value_dbN:
            return 3
        mode = dictionary.get(str(databaseOld))[0]
        j = checkMode(mode)
        value_return = j.alterDatabase(databaseOld, databaseNew)
        if mode == "isam" and value_return == 1:
            value_return = 0
        if value_return == 0:
            info = dictionary[str(databaseOld)]
            dictionary.pop(str(databaseOld))
            dictionary[str(databaseNew)] = info
            save(dictionary, 'metadata')
        return value_return
    except:
        return 1
    
    
# DROP DATABASE
def dropDatabase(database):
    try:
        nombreBase = str(database)
        dictionary = load('metadata')
        FK = load('FK')
        UNIQUE = load('UNIQUE')
        INDEX = load('INDEX')

        value_base = dictionary.get(nombreBase)
        if value_base:
            mode = dictionary.get(nombreBase)[0]
            j = checkMode(mode)
            j.dropDatabase(nombreBase)
            dictionary.pop(nombreBase)

            if FK != 1:
                for key in FK:
                    if FK[key][0] == database:
                        FK.pop(FK[key][1])

            if INDEX != 1:
                for key in INDEX:
                    if INDEX[key][0] == database:
                        INDEX.pop(INDEX[key][2])

            if UNIQUE != 1:
                for key in UNIQUE:
                    if UNIQUE[key][0] == database:
                        UNIQUE.pop(UNIQUE[key][2])

            save(dictionary, 'metadata')
            save(FK, 'FK')
            save(INDEX, 'INDEX')
            save(UNIQUE, 'UNIQUE')
            return 0
        return 2
    except:
        return 1
    

def createTable(database, table, numberColumns):
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.createTable(database, table, numberColumns)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            Bchain = None
            dict_tables[table] = [numberColumns, False, Bchain]
            save(dictionary, 'metadata')

        return value_return
    except:
        return 1


def showTables(database):
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return None  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.showTables(database)
        return value_return
    except:
        return 1
    
    
# EXTRACT TABLE
def extractTable(database, table):
    try:
        newTable = []

        database = str(database)
        table = str(table)
        dictionary = load('metadata')
        value_base = dictionary.get(database)
        if not value_base:
            return []
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.extractTable(database, table)

        # compress
        for tuple in value_return:
            newTuple = []
            for register in tuple:
                if iscompressed(register):
                    decompressed = zlib.decompress(register)
                    newTuple.append(decompressed)
                else:
                    newTuple.append(register)

            newTable.append(newTuple)

        value_return = []
        for r in newTable:
            newRegister = []
            for c in r:
                if isinstance(c, bytes):
                    newRegister.append(c.decode(dictionary[database][1]))
                else:
                    newRegister.append(c)
            value_return.append(newRegister)

        return value_return
    except:
        return []
    
  
# EXTRACT RANGE TABLE
def extractRangeTable(database, table, columnNumber, lower, upper):
    try:
        newTable = []

        database = str(database)
        table = str(table)
        dictionary = load('metadata')
        value_base = dictionary.get(database)
        if not value_base:
            return []
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        if isinstance(lower, str):
            lower = lower.encode(dictionary[database][1])
        if isinstance(upper, str):
            upper = upper.encode(dictionary[database][1])
        value_return = j.extractRangeTable(database, table, int(columnNumber), lower, upper)

        # compress
        for tuple in value_return:
            newTuple = []
            for register in tuple:
                if iscompressed(register):
                    decompressed = zlib.decompress(register)
                    newTuple.append(decompressed)
                else:
                    newTuple.append(register)

            newTable.append(newTuple)

        value_return = []
        for r in newTable:
            newRegister = []
            for c in r:
                if isinstance(c, bytes):
                    newRegister.append(c.decode(dictionary[database][1]))
                else:
                    newRegister.append(c)
            value_return.append(newRegister)

        return value_return
    except:
        return []


def alterAddPK(database, table, columns):
    try:
        if os.path.isfile(os.getcwd() + '\\Data\\PK.bin'):
            PK = load('PK')
        else:
            PK = {}
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterAddPK(database, table, columns)
        PK.update({table: [database, table, columns]})
        save(PK, 'PK')
        return value_return
    except:
        return 1


def alterDropPK(database, table):
    try:
        if os.path.isfile(os.getcwd() + '\\Data\\PK.bin'):
            PK = load('PK')
        else:
            PK = {}
        dictionary = load('metadata')

        value_base = dictionary.get(database)
        if not value_base:
            return 2

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterDropPK(database, table)
        PK.pop(table)
        save(PK, 'PK')
        return value_return
    except:
        return 2
    
    
# ALTER TABLE
def alterTable(database, tableOld, tableNew):
    try:
        database = str(database)
        tableOld = str(tableOld)
        tableNew = str(tableNew)
        dictionary = load('metadata')
        value_base = dictionary.get(database)
        if not value_base:
            return 2
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterTable(database, tableOld, tableNew)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            infoTabla = dict_tables[tableOld]
            dict_tables.pop(tableOld)
            dict_tables[tableNew] = infoTabla
            save(dictionary, 'metadata')
        return value_return
    except:
        return 1
    
    
# ALTER ADD COLUMN
def alterAddColumn(database, table, default):
    try:
        database = str(database)
        table = str(table)
        dictionary = load('metadata')

        value_base = dictionary.get(database)
        if not value_base:
            return 2

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        if isinstance(default, str):
            default = default.encode(dictionary[database][1])
        value_return = j.alterAddColumn(database, table, default)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            number_columns = dict_tables.get(table)[0]
            dict_tables.get(table)[0] = number_columns + 1
            save(dictionary, 'metadata')

        return value_return
    except:
        return 1
    
    
def alterDropColumn(database, table, columnNumber):
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterDropColumn(database, table, columnNumber)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            number_columns = dict_tables.get(table)[0]
            dict_tables.get(table)[0] = number_columns - 1  # Updating number of columns

            save(dictionary, 'metadata')

        return value_return
    except:
        return 1


def dropTable(database, table):
    try:
        dictionary = load('metadata')
        FK = loadReturn('FK')
        INDEX = loadReturn('INDEX')
        UNIQUE = loadReturn('UNIQUE')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.dropTable(database, table)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            dict_tables.pop(table)

            if FK != 1:
                for key in FK:
                    values = FK[key]
                    if values[0] == database:
                        if table == values[2] or table == [4]:
                            FK.pop(values[1])
                            j.delete(database, 'FK', values[1])
                            save(FK, 'FK')

            if INDEX != 1:
                for key in INDEX:
                    values = INDEX[key]
                    if values[0] == database:
                        if table == values[1]:
                            INDEX.pop(values[2])
                            j.delete(database, 'INDEX', values[2])
                            save(INDEX, 'INDEX')

            if UNIQUE != 1:
                for key in UNIQUE:
                    values = UNIQUE[key]
                    if values[0] == database:
                        if table == values[1]:
                            UNIQUE.pop(values[2])
                            j.delete(database, 'UNIQUE', values[2])
                            save(UNIQUE, 'UNIQUE')
            save(dictionary, 'metadata')
        return value_return
    except:
        return 1   
    
    
# INSERT
def insert(database, table, register):
    try:
        if os.path.isfile(os.getcwd() + '\\Data\\PK.bin'):
            PK = load('PK')
        else:
            PK = {}

        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        newRegister = []
        for c in register:
            if isinstance(c, str):
                newRegister.append(c.encode(dictionary[database][1]))
            else:
                newRegister.append(c)
        value_return = j.insert(database, table, newRegister)
        if PK.get(table) is None:
            PK.update({table: [database, table, ['HIDDEN']]})
            save(PK, 'PK')

        # Method to Blockchain
        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            tabla_info = dict_tables.get(table)

            # if the security mode is on
            if tabla_info[1] is True:
                nameJson = str(database) + '-' + str(table)
                # The object block chain
                tabla_info[2].insertBlock(register, nameJson)
                graphBChain(tabla_info[2], nameJson)
                save(dictionary, 'metadata')
        return value_return
    except:
        return 1
    
    
# UPDATE
def update(database, table, register, columns):
    # database: str name of database
    # table: str name of table
    # register: dictionary {column: newValue}
    # columns: list [primaryKey] [primarykey1, primarykey2...]
    try:
        dictionary = load('metadata')
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        # Save the old tuple for the BChain method
        newColumns = []
        for key in columns:
            if isinstance(key, str):
                newColumns.append(key.encode(dictionary[database][1]))
            else:
                newColumns.append(key)
        oldTuple = j.extractRow(database, table, newColumns)
        for key in register:
            if isinstance(register[key], str):
                register.update({key: register[key].encode(dictionary[database][1])})
        value_return = j.update(database, table, register, newColumns)

        # ----------------------------------------------------- ISAAC --------------------------------------------------
        # Method to Blockchain
        if value_return == 0:
            print(j.extractRow(database, table, newColumns))
            dict_tables = dictionary.get(database)[2]
            tabla_info = dict_tables.get(table)

            # if the security mode is on
            if tabla_info[1] is True:
                newTuple = []

                # Generate the new Tuple
                for i in range(len(oldTuple)):
                    decodificado = oldTuple[i].decode(dictionary[database][1])
                    oldTuple[i] = decodificado
                    newTuple.append(decodificado)

                for key in register:
                    newTuple[key] = register[key].decode(dictionary[database][1])

                nameJson = str(database) + '-' + str(table)
                tabla_info[2].updateBlock(oldTuple, newTuple, nameJson)
                graphBChain(tabla_info[2], nameJson)
                save(dictionary, 'metadata')

        return value_return
    except:
        return 1
    
def loadCSV(file, database, table):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        file = open(file, 'r')
        file = file.read()
        registers = file.split('\n')
        results = []
        for r in registers:
            newRegister = []
            register = r.split(',')
            for c in register:
                if isinstance(c, str):
                    newRegister.append(c.encode(dictionary[database][1]))
                else:
                    newRegister.append(c)
            results.append(j.insert(database, table, newRegister))
        return results
    except:
        return []
  
def extractRow(database, table, columns):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        new_Columns = []
        for i in columns:
            if isinstance(i, str):
                new_Columns.append(i.encode(dictionary[database][1]))
            else:
                new_Columns.append(i)
        register = j.extractRow(database, table, new_Columns)
        newRegister = []
        for c in register:
            if isinstance(c, bytes):
                newRegister.append(c.decode(dictionary[database][1]))
            else:
                newRegister.append(c)
        return newRegister
    except:
        return []
    
def delete(database, table, columns):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        new_Columns = []
        for i in columns:
            if isinstance(i, str):
                new_Columns.append(i.encode(dictionary[database][1]))
            else:
                new_Columns.append(i)
        value_return = j.delete(database, table, new_Columns)
        return value_return
    except:
        return 1
   
def truncate(database, table):
    dictionary = load('metadata')
    try:
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.truncate(database, table)
        return value_return
    except:
        return 1
    
    
# ------------------------------------------------------- FILES --------------------------------------------------------
def save(objeto, nombre):
    file = open(nombre + ".bin", "wb")
    file.write(pickle.dumps(objeto))
    file.close()
    if os.path.isfile(os.getcwd() + "\\Data\\" + nombre + ".bin"):
        os.remove(os.getcwd() + "\\Data\\" + nombre + ".bin")
    shutil.move(os.getcwd() + "\\" + nombre + ".bin", os.getcwd() + "\\Data")


def load(nombre):
    file = open(os.getcwd() + "\\Data\\" + nombre + ".bin", "rb")
    objeto = file.read()
    file.close()
    return pickle.loads(objeto)      

def loadReturn(nombre):
    if os.path.isfile(os.getcwd() + '\\Data\\' + nombre + ".bin"):
        file = open(os.getcwd() + "\\Data\\" + nombre + ".bin", "rb")
        objeto = file.read()
        file.close()
        return pickle.loads(objeto)
    return 1
