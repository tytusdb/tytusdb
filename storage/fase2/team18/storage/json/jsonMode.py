# Package:      JSON Mode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Luis Espino

import os 
import json

path = 'data/json/'
dataPath = path + 'databases'
    
##################
# Databases CRUD #
##################

# CREATE a database checking their existence
def createDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)
        if database in data:
            return 2
        new = {database:{}}
        data.update(new)
        write(dataPath, data)
        return 0
    except:
        return 1

# READ and show databases by constructing a list
def showDatabases() -> list:
    try:
        initCheck()
        databases = []
        data = read(dataPath)
        for d in data:
            databases.append(d)
        return databases
    except:
        return []

# UPDATE and rename a database name by inserting new_key and deleting old_key
def alterDatabase(databaseOld: str, databaseNew) -> int:
    try:
        if not databaseOld.isidentifier() or not databaseNew.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)        
        if not databaseOld in data:
            return 2
        if databaseNew in data:
            return 3
        tab = showTables(databaseOld)
        data[databaseNew] = data[databaseOld]
        data.pop(databaseOld)
        write(dataPath, data)
        if len(tab):
            for x in tab:
                os.rename("./Data/json/"+databaseOld+"-"+x,"./Data/json/"+databaseNew+"-"+x)
        return 0
    except:
        return 1

# DELETE a database by pop from dictionary
def dropDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        data.pop(database)
        write(dataPath, data)
        return 0
    except:
        return 1    


###############
# Tables CRUD #
###############

# CREATE a table checking their existence
def createTable(database: str, table: str, numberColumns: int) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(numberColumns, int):
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2        
        if table in data[database]:
            return 3
        new = {table:{"NCOL":numberColumns}}
        data[database].update(new)
        write(dataPath, data)
        dataTable = {}
        write(path+database+'-'+table, dataTable)
        return 0
    except:
        return 1

# show databases by constructing a list
def showTables(database: str) -> list:
    try:
        initCheck()
        tables = []        
        data = read(dataPath)
        if not database in data:
            return None
        for d in data[database]:
            tables.append(d)
        return tables
    except:
        return []

# extract all register of a table
def extractTable(database: str, table: str) -> list:
    try:
        initCheck()
        rows = []
        data = read(dataPath)
        if not database in data:
            return None
        if table not in data[database]:
            return None
        data = read(path+database+'-'+table)
        for d in data:
            rows.append(data[d])
        return rows
    except:
        return None

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
                rows.append(data[d])
    return rows

# Add a PK list to specific table and database
def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(columns, list):
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        if not table in data[database]:
            return 3
        if "PKEY" in data[database][table]:
            return 4
        maxi = max(columns)
        mini = min(columns)
        if not (mini>=0 and maxi<data[database][table]["NCOL"]):
            return 5
        new = {"PKEY":columns}
        data[database][table].update(new)
        write(dataPath, data)
        return 0
    except:
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
    try:
        if not database.isidentifier() \
        or not tableOld.isidentifier() \
        or not tableNew.isidentifier() :
            raise Exception()        
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        if not tableOld in data[database]:
            return 3
        if tableNew in data[database]:
            return 4            
        data[database][tableNew] = data[database][tableOld]
        data[database].pop(tableOld)
        write(dataPath, data)
        os.rename("./Data/json/"+database+"-"+tableOld,"./Data/json/"+database+"-"+tableNew)
        return 0
    except:
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
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        if not table in data[database]:
            return 3
        data[database].pop(table)
        write(dataPath,data)
        return 0
    except:
        return 1  

##################
# Registers CRUD #
##################

# CREATE or insert a register 
def insert(database: str, table: str, register: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(register, list):
            raise Exception()        
        initCheck()
        hide = False
        ncol = None
        pkey = None
        pk = ""
        data = read(dataPath)
        if not database in data:
            return 2
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
        data = read(path+database+'-'+table)
        if hide:
            pk = len(data)
        else:
            for i in pkey:
                if i!=pkey[-1]:
                    pk += str(register[i])+'|'
                else:
                    pk += str(register[i])
        if pk in data:
            return 4
        new = {pk:register}
        data.update(new)
        write(path+database+'-'+table, data)
        return 0
    except:
        return 1

# READ or load a CSV file to a table
def loadCSV(filepath: str, database: str, table: str, tipado) -> list:
    try:
        res = []
        import csv
        with open(filepath, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter = ',')
            j = 0
            for row in reader:
                if tipado:
                    i=0
                    for x in row:
                        if tipado[j][i] == bool:
                            if x == 'False':
                                row[i] = bool(1)
                            else:
                                row[i] = bool(0)
                        else:
                            row[i] = tipado[j][i](x)
                        i=i+1
                    j+=1
                res.append(insert(database,table,row))
        return res
    except:
        return []

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
                if i!=pkey[-1]:
                    pk += str(columns[i])+'|'
                else:
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
                if i!=pkey[-1]:
                    pk += str(columns[i])+'|'
                else:
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
                if i!=pkey[-1]:
                    pk += str(columns[i])+'|'
                else:
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

# Read a JSON file
def read(path: str) -> dict:
    with open(path) as file:
        return json.load(file)    

# Write a JSON file
def write(path: str, data: dict):
    with open(path, 'w') as file:
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
