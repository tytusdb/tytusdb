# JSON Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import os 
import json


#############
# Databases #
#############

# Create a database checking their existence
def createDatabase(database: str) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if database in data:
            return 2
        else: 
            new = {database:{}}
            data.update(new)
            dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

# Rename a database name by inserting new_key and deleting old_key
def alterDatabase(databaseOld: str, databaseNew) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not databaseOld in data:
            return 2
        if databaseNew in data:
            return 3
        else:
            data[databaseNew] = data[databaseOld]
            data.pop(databaseOld)
            dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1    

# delete database by pop from dictionary
def dropDatabase(database: str) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)        
        if not database in data:
            return 2
        else:
            data.pop(database)
            dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1    

# show databases by constructing a list
def showDatabases() -> list:
    initCheck()
    databases = []
    with open('data/json/databases') as file:
        data = json.load(file)
        for d in data:
            databases.append(d);
    return databases


##########
# TABLES #
##########

# Create a table checking their existence
def createTable(database: str, table: str, numberColumns: int) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if table in data[database]:
                return 3
            else:
                new = {table:{"numberColumns":numberColumns}}
                data[database].update(new)
                dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

# show databases by constructing a list
def showTables(database: str) -> list:
    initCheck()
    tables = []
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return None
        for d in data[database]:
            tables.append(d);
    return tables

# Rename a table name by inserting new_key and deleting old_key
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not tableOld in data[database]:
                return 3
            if tableNew in data[database]:
                return 4            
            else:
                data[database][tableNew] = data[database][tableOld]
                data[database].pop(tableOld)
                dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1   

# Delete a table name by inserting new_key and deleting old_key
def dropTable(database: str, table: str) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            else:                
                data[database].pop(table)
                dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1  


#############
# UTILITIES #
#############

# Check the existence of data and json folder and databases file
# Create databases files if not exists
def initCheck():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/json'):
        os.makedirs('data/json')
    if not os.path.exists('data/json/databases'):
        data = {}
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)    

# Show the complete file of databases and tables
def showDatabasesJSON():
    initCheck()
    with open('data/json/databases') as file:
        data = json.load(file)
        print(data)
        #print(data["db1"])

# Delete all databases and tables by creating a new file
def dropAllDatabases():
    data = {}
    with open('data/json/databases', 'w') as file:
        json.dump(data, file)
