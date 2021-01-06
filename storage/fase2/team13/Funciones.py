import os

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
