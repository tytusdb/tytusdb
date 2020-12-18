# JSON Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import os 
import json

##Create##
def TCcreateDatabase(database: str) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if database in data:
            return 2
        else: 
            new = {database:{}}
            data.update(new)
            dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

#Check if database exists
def TCSearchDatabase(database:str)->int:
    initCheck()
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if database in data:
            return 1 #existe
        else:
            return 2 #noExiste

# DELETE a database by pop from dictionary
def TCdropDatabase(database: str) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)        
        if not database in data:
            return 2
        else:
            data.pop(database)
            dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1              


# READ and show databases by constructing a list
def TCshowDatabases() -> list:
    initCheck()
    databases = []
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        for d in data:
            databases.append(d)
    return databases
    
###############
# Tables CRUD #
###############

# CREATE a table checking their existence
def TCcreateTable(database: str, table: str, Columns:list) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if table in data[database]:
                return 3
            else:
                #new ={"Type":,type,"Name":,"MaxLength":,"DefaultFlag":,"PrimaryKeyFlag":,"NullFlag":,"Constrains":[]}
                #print(Columns)
                new = {table:{}}
                data[database].update(new)
                for b in range(0,len(Columns)):
                    new2= Columns[b]
                    data[database][table].update(new2)

                dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        """dataTable = {}
        with open('data/json/'+database+'-'+table, 'w') as file:
            json.dump(dataTable, file)
        return 0"""
    else:
        return 1




# Check the existence of data and json folder and databases file
# Create databases files if not exists
def initCheck():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/json'):
        os.makedirs('data/json')
    if not os.path.exists('data/json/TypeChecker'):
        data = {}
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)    

# Show the complete file of databases and tables
def showJSON(fileName: str):
    initCheck()
    with open('data/json/'+fileName) as file:
        data = json.load(file)
        print(data)

# Delete all databases and tables by creating a new file
def dropAll():
    initCheck()
    data = {}
    with open('data/json/TypeChecker', 'w') as file:
        json.dump(data, file)

# show all collection of relational data
def showCollection():
    initCheck()
    databases = []
    tables = []
    datatables = []
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        for d in data:
            databases.append(d)
            for t in data[d]:
                tables.append(t)
                datatables.append(d+'-'+t)
    print('Databases: '+str(databases))
    print('Tables: '+str(tables))
    for d in datatables:
        registers = []
        with open('data/json/'+d) as file:
            data = json.load(file)
            for r in data:
                registers.append(r)
            print(d+' pkeys: '+str(registers))