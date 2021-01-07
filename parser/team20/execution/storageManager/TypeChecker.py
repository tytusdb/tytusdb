# JSON Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import os 
import json

##Create##
def TCcreateDatabase(database: str,Mode:str) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if database in data:
            return 2
        else: 
            new = {database:{"MODE":Mode,"TYPES":{}}}
            data.update(new)
            data["USE"]=database
            dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

#Get database selected#
def TCgetDatabase()->str:
    initCheck()
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        return data["USE"]

#Get table columns in order
def TCgetTableColumns(database: str,table:str)->str:
    initCheck()
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        keys = []
        try:
            info = data[database][table]
            for key in info.keys():
                keys.append(key)
            return keys
        except:
            return table

#Set database select
def TCsetDatabase(database: str)->int:
    initCheck()
    dump= False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        data["USE"]= database
        dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 2
    return 1

#Check if database exists
def TCSearchDatabase(database:str)->int:
    initCheck()
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if database in data:
            return   data[database]["MODE"]  #existe
        else:
            return 8 #noExiste

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

def TCdropTable(database:str, table:str):
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)        
        if not database in data:
            return 2
        else:
            if not table in data[database] :
                return 3
            else:
                data[database].pop(table)
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

# UPDATE and rename a database name by inserting new_key and deleting old_key
def TCalterDatabase(databaseOld: str, databaseNew) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
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
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

###############
# Tables CRUD #
###############

# CREATE a table checking their existence
def TCcreateTable(database: str, table: str, Columns:None) -> int:
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
                data[database][table].update(Columns)

                dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0 
    else:
        return 1

def TCaddCheckTable (database: str, table: str,column:str ,value:None,op:str) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            else:
                if not column in data[database][table]:
                    return 4
                else:
                    data[database][table][column]['CHECKS'].append({'OP':op,'VALUE':value})
                    dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0 
    else:
        return 1

def TCaddPrimaryKey (database: str, table: str,column:str,value:bool) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            else:
                if not column in data[database][table]:
                    return 4
                else:
                    new={'PRIMARY':value}
                    data[database][table][column].update(new)
                    dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0 
    else:
        return 1

def TCaddUnique (database: str, table: str,column:str,value:bool) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            else:
                if not column in data[database][table]:
                    return 4
                else:
                    new={'UNIQUE':value}
                    data[database][table][column].update(new)
                    dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0 
    else:
        return 1

def TCgetToInherit(database: str, table: str) -> None:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        doc={}
        if not database in data:
            return doc
        else:
            if not table in data[database]:
                return doc
            else:
                for d in data[database][table]:
                    new= dict.copy(data[database][table][d])
                    doc.update({d:new})
                return doc

def TCalterDropPk(database:str,table:str)->int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            else:
                for i in data[database][table]:
                    if 'PRIMARY' in data[database][table][i]['CONST']:
                        data[database][table][i]['CONST'].pop('PRIMARY')
                        dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0 
    else:
        return 1

def TCaltertype(database:str,table:str,column:str,lenght:int)->int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            else:
                if not column in data[database][table]:
                    return 4
                else:
                    data[database][table][column]['CONST']['MAXLENGTH']=lenght
                    dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0 
    else:
        return 1

###############
# Tables TYPES #
###############

# CREATE a type
def TCcreateType(database: str, typeEnum: str, Values:None) -> int:
    initCheck()
    dump = False
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if typeEnum in data[database]['TYPES']:
                return 3
            else:
                print(Values)
                new = {typeEnum:{}}
                data[database]['TYPES'].update(new)
                data[database]['TYPES'][typeEnum].update(Values)
                dump = True
    if dump:
        with open('data/json/TypeChecker', 'w') as file:
            json.dump(data, file)
        return 0 
    else:
        return 1
'''def TCgetPrimarys(database:str,table:str)->str:
    initCheck()
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if database in data:
            if table in data[database][table]:
                for d in data[database][table]
                    print(data[database][table][d])
            else:
                return 1
        else:
            return 2

def TCValidateReference(database:str,table:str,column:str)->int:
    initCheck()
    with open('data/json/TypeChecker') as file:
        data = json.load(file)
        if database in data:
            if table in data[database][table]:
                if column in data[database][table][column]:
                    return 0
                else:
                    return 1 #noexists column in table
            else:
                return 2 #noexists table in database

        else:
            return 3 #noexists database'''

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