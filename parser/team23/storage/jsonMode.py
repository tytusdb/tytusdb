# JSON Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import os 
import json

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

# Create a database checking their existence
def createDatabase(database: str) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if database in data:
            return 2
        else: 
            new = {database:[]}
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