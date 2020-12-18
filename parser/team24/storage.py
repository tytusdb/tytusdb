# JSON Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import os 
import json


##################
# Databases CRUD #
##################

# CREATE a database checking their existence
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

# READ and show databases by constructing a list
def showDatabases() -> list:
    initCheck()
    databases = []
    with open('data/json/databases') as file:
        data = json.load(file)
        for d in data:
            databases.append(d);
    return databases

# UPDATE and rename a database name by inserting new_key and deleting old_key
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

# DELETE a database by pop from dictionary
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


###############
# Tables CRUD #
###############

# CREATE a table checking their existence
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
                new = {table:{"NCOL":numberColumns}}
                data[database].update(new)
                dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        dataTable = {}
        with open('data/json/'+database+'-'+table, 'w') as file:
            json.dump(dataTable, file)
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

# extract all register of a table
def extractTable(database: str, table: str) -> list:
    initCheck()
    rows = []
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return rows
        else: 
            if table not in data[database]:
                return rows
    with open('data/json/'+database+'-'+table) as file:
        data = json.load(file)
        for d in data:
            rows.append(data[d]);
    return rows

# extract a range registers of a table
def extractRangeTable(database: str, table: str, lower: any, upper: any) -> list:
    initCheck()
    rows = []
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return rows
        else: 
            if table not in data[database]:
                return rows
    with open('data/json/'+database+'-'+table) as file:
        data = json.load(file)
        for d in data:
            if (str(d)<=str(upper) and str(d)>=str(lower)):
                rows.append(data[d]);
    return rows

# Add a PK list to specific table and database
def alterAddPK(database: str, table: str, columns: list) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            if "PKEY" in data[database][table]:
                return 4
            else:
                maxi = max(columns)
                mini = min(columns)
                if mini>=0 and maxi<=data[database][table]["NCOL"]:
                    new = {"PKEY":columns}
                    data[database][table].update(new)                    
                    dump = True
                else:
                    return 5
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1  

# Add a PK list to specific table and database
def alterDropPK(database: str, table: str) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            if "PKEY" not in data[database][table]:
                return 4            
            else:
                data[database][table].pop("PKEY")
                dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1  


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

# add a column at the end of register with default value
def alterAddColumn(database: str, table: str, default: any) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            data[database][table]['NCOL']+=1
            dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)

        with open('data/json/'+database+'-'+table) as file:
            data = json.load(file)
            for d in data:
                data[d].append(default)
        with open('data/json/'+database+'-'+table, 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1  

# drop a column and its content (except primary key columns)
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    initCheck()
    dump = False
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            ncol = data[database][table]['NCOL']            
            pkey = data[database][table]['PKEY']
            if columnNumber in pkey:
                return 4            
            if not ncol >len(pkey):
                return 4
            if columnNumber<0 or columnNumber>ncol-1:
                return 5
            data[database][table]['NCOL']-=1
            dump = True
    if dump:
        with open('data/json/databases', 'w') as file:
            json.dump(data, file)

        with open('data/json/'+database+'-'+table) as file:
            data = json.load(file)
            for d in data:
                data[d].pop(columnNumber)
        with open('data/json/'+database+'-'+table, 'w') as file:
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

##################
# Registers CRUD #
##################

# CREATE or insert a register 
def insert(database: str, table: str, register: list) -> int:    
    initCheck()
    dump = False
    hide = False
    ncol = None
    pkey = None
    pk = ""
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else: 
            if table not in data[database]:
                return 3
            if len(register)!=data[database][table]["NCOL"]:
                return 5
            if "PKEY" not in data[database][table]:
                # hidden pk
                hide = True
            else:
                # defined pk
                pkey = data[database][table]["PKEY"]
            ncol = data[database][table]["NCOL"]
    with open('data/json/'+database+'-'+table) as file:
        data = json.load(file)
        if hide:
            pk = len(data)
        else:
            for i in pkey:
                pk += str(register[i])
            if pk in data:
                return 4
        new = {pk:register}
        data.update(new)
        dump = True
    if dump:
        with open('data/json/'+database+'-'+table, 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

# READ or load a CSV file to a table
def loadCSV(filepath: str, database: str, table: str) -> list:
    res = []
    import csv
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            res.append(insert(database,table,row))
    return res

# READ or extract a register
def extractRow(database: str, table: str, columns: list) -> list:
    initCheck()
    hide = False
    ncol = None
    pkey = None
    pk = ""
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return []
        else: 
            if table not in data[database]:
                return []
            if "PKEY" not in data[database][table]:
                # hidden pk
                hide = True
            else:
                # defined pk
                pkey = data[database][table]["PKEY"]            
    with open('data/json/'+database+'-'+table) as file:
        data = json.load(file)
        if hide:
            pk = columns[0]
        else:
            for i in pkey:
                pk += str(columns[i])
        if not pk in data:
            return []
        else:
            return data[pk]

# UPDATE a register
def update(database: str, table: str, register: dict, columns: list) -> int:
    initCheck()
    dump = False
    hide = False
    ncol = None
    pkey = None
    pk = ""
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else: 
            if table not in data[database]:
                return 3
            if "PKEY" not in data[database][table]:
                # hidden pk
                hide = True
            else:
                # defined pk
                pkey = data[database][table]["PKEY"]            
    with open('data/json/'+database+'-'+table) as file:
        data = json.load(file)
        if hide:
            pk = columns[0]
        else:
            for i in pkey:
                pk += str(columns[i])
        if not pk in data:
            return 4
        else:            
            for key in register:
                data[pk][key] = register[key]
        dump = True
    if dump:
        with open('data/json/'+database+'-'+table, 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

# DELETE a specific register
def delete(database: str, table: str, columns: list) -> int:
    initCheck()
    dump = False
    hide = False
    ncol = None
    pkey = None
    pk = ""
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else: 
            if table not in data[database]:
                return 3
            if "PKEY" not in data[database][table]:
                # hidden pk
                hide = True
            else:
                # defined pk
                pkey = data[database][table]["PKEY"]            
    with open('data/json/'+database+'-'+table) as file:
        data = json.load(file)
        if hide:
            pk = columns[0]
        else:
            for i in pkey:
                pk += str(columns[i])
        if not pk in data:
            return 4
        else:
            data.pop(pk)
        dump = True
    if dump:
        with open('data/json/'+database+'-'+table, 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1

# DELETE or truncate all registers of the table
def truncate(database: str, table: str) -> int:
    initCheck()
    dump = False
    hide = False
    ncol = None
    pkey = None
    pk = ""
    with open('data/json/databases') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else: 
            if table not in data[database]:
                return 3
        dump = True
    if dump:
        data = {}
        with open('data/json/'+database+'-'+table, 'w') as file:
            json.dump(data, file)
            return 0
    else:
        return 1

#############
# Utilities #
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
def showJSON(fileName: str):
    initCheck()
    with open('data/json/'+fileName) as file:
        data = json.load(file)
        print(data)

# Delete all databases and tables by creating a new file
def dropAll():
    initCheck()
    data = {}
    with open('data/json/databases', 'w') as file:
        json.dump(data, file)

# show all collection of relational data
def showCollection():
    initCheck()
    databases = []
    tables = []
    datatables = []
    with open('data/json/databases') as file:
        data = json.load(file)
        for d in data:
            databases.append(d);
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