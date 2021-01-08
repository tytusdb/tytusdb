import os
import pickle
import shutil
import zlib
from Blockchain import *

databases = {}  # LIST WITH DIFFERENT MODES
dict_encoding = {'ascii': 1, 'iso-8859-1': 2, 'utf8': 3}
dict_modes = {'avl': 1, 'b': 2, 'bplus': 3, 'dict': 4, 'isam': 5, 'json': 6, 'hash': 7}


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
                mode = dictionary.get(database)[0]
                j = checkMode(mode)
                list_tuple = j.extractTable(database, table)
                nameJson = str(database) + '-' + str(table)
                BChain = make_block_chain(list_tuple, nameJson)
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
    
    
# ---------------------------------------------- AUXILIARY FUNCTIONS  --------------------------------------------------
# SHOW DICTIONARY
def showDict(dictionary):
    print('-- DATABASES --')
    for key in dictionary:
        print(key, ":", dictionary[key])


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
    dict_tables = dictionary.get(database)[2]

    if tables:
        for name_table in tables:
            register = old_mode.extractTable(database, name_table) 
            number_columns = dict_tables.get(name_table)[0]
            new_mode.createTable(database, name_table, number_columns)

            if register:  # There are registers
                for list_register in old_mode.extractTable(database, name_table):
                    new_mode.insert(database, name_table, list_register)

        old_mode.dropDatabase(database)   
        
        

# Blockchain mode when the security mode is on
def make_block_chain(list_tuple, nameJson):
    BChain = Blockchain()
    for tuple in list_tuple:
        BChain.insertBlock(tuple, nameJson)
        graphBChain(BChain, nameJson)
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
    

# ------------------------------------------------------ FASE 1 --------------------------------------------------------
# -------------------------------------------------- Table CRUD --------------------------------------------------------

#SHOWDATABASES
def showDatabases(database):
    try:
        dictionary = load('metadata')
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.showDatabases()
        return value_return
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
        value_base = dictionary.get(nombreBase)
        if value_base:
            mode = dictionary.get(nombreBase)[0]
            j = checkMode(mode)
            j.dropDatabase(nombreBase)
            dictionary.pop(nombreBase)
            save(dictionary, 'metadata')
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
            dict_tables[table] = [numberColumns, False]
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
            return None
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.extractTable(database, table)
        
        # Decompress
        for tuple in value_return:
            newTuple = []
            for register in tuple:
                if iscompressed(register):
                    decompressed = zlib.decompress(register)
                    newTuple.append(decompressed)
                else:
                    newTuple.append(register)

            newTable.append(newTuple)
        
        return value_return
    except:
        return None
    
  
# EXTRACT RANGE TABLE
def extractRangeTable(database, table, columnNumber, lower, upper):
    try:
        newTable = []

        database = str(database)
        table = str(table)
        dictionary = load('metadata')
        value_base = dictionary.get(database)
        if not value_base:
            return None
        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.extractRangeTable(database, table, int(columnNumber), lower, upper)
        
        # Decompress
        for tuple in value_return:
            newTuple = []
            for register in tuple:
                if iscompressed(register):
                    decompressed = zlib.decompress(register)
                    newTuple.append(decompressed)
                else:
                    newTuple.append(register)

            newTable.append(newTuple)
        
        return value_return
    except:
        return None


def alterAddPK(database, table, columns):
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterAddPK(database, table, columns)
        return value_return
    except:
        return 1


def alterDropPK(database, table):
    try:
        dictionary = load('metadata')

        value_base = dictionary.get(database)
        if not value_base:
            return 2

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.alterDropPK(database, table)
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
        value_return = j.alterDropColumn(database, table, default)

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
            dict_tables.get(table)[0] = number_columns-1  # Updating number of columns

            save(dictionary, 'metadata')

        return value_return
    except:
        return 1


def dropTable(database, table) :
    try:
        dictionary = load('metadata')

        if dictionary.get(database) is None:
            return 2  # database doesn't exist

        mode = dictionary.get(database)[0]
        j = checkMode(mode)
        value_return = j.dropTable(database, table)

        if value_return == 0:
            dict_tables = dictionary.get(database)[2]
            dict_tables.pop(table)

            save(dictionary, 'metadata')
    except:
        return 1    
    
    
# INSERT
def insert(database, table, register):

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
    
        # Method to Blockchain
        if value_return == 0:
            print(j.extractRow(database, table, columns))
            dict_tables = dictionary.get(database)[2]
            tabla_info = dict_tables.get(table)

            # if the security mode is on
            if tabla_info[1] is True:
                newTuple = []

                # Generate the new Tuple
                for i in oldTuple:
                    newTuple.append(i)

                for key in register:
                    newTuple[key] = register[key]

                nameJson = str(database) + '-' + str(table)

                tabla_info[2].updateBlock(oldTuple, newTuple, nameJson)
                graphBChain(tabla_info[2], nameJson)
                save(dictionary, 'metadata')

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
