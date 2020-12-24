# Package:      B+ Mode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Herberth Avila

from storageManager.BPlusServer import BPlusServer

server = BPlusServer()

##################
# Databases CRUD #
##################

# CREATE a database checking their existence
def createDatabase(database):
    try:
        if not database.isidentifier():
            raise Exception()

        existe = server.existeDB(database)
        if existe:
            return 2
        
        server.createDB(database)
        return 0
    except:
        return 1

# READ and show databases by constructing a list
def showDatabases():
    try:
        databases = []

        databases = server.showDB()
        return databases
    except:
        return []

# UPDATE and rename a database name by inserting new_key and deleting old_key
def alterDatabase(databaseOld, databaseNew):
    try:
        if not databaseOld.isidentifier() or not databaseNew.isidentifier():
            raise Exception()

        existe = server.existeDB(databaseOld)
        if existe is False:
            return 2
        
        existe = server.existeDB(databaseNew)
        if existe:
            return 3
        
        server.alterDB(databaseOld, databaseNew)
        return 0
    except:
        return 1

# DELETE a database by pop from dictionary
def dropDatabase(database):
    try:
        if not database.isidentifier():
            raise Exception()
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        server.dropDB(database)
        return 0
    except:
        return 1    

###############
# Tables CRUD #
###############

# CREATE a table checking their existence
def createTable(database, table, numberColumns):
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(numberColumns, int):
            raise Exception()

        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe:
            return 3
        
        server.createT(database, table, numberColumns)
        return 0
    except:
        return 1

# show databases by constructing a list
def showTables(database):
    try:
        if not database.isidentifier():
            raise Exception()
        
        tables = []        
        
        existe = server.existeDB(database)
        if existe is False:
            return None
        
        tables = server.showT(database)
        return tables
    except:
        return []

# extract all register of a table
def extractTable(database, table):
    try:
        rows = []
        
        existe = server.existeDB(database)
        if existe is False:
            return None
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return None
        
        rows = server.extractT(database, table)
        return rows
    except:
        return None


# extract a range registers of a table
def extractRangeTable(database, table, columnNumber, lower, upper):
    try:
        rows = []

        existe = server.existeDB(database)
        if existe is False:
            return None
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return None
        
        rows = server.extractRangeT(database, table, columnNumber, lower, upper)
        return rows
    except:
        return None

# Add a PK list to specific table and database
def alterAddPK(database, table, columns):
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(columns, list):
            raise Exception()
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.alterADDPK(database, table, columns)
    except:
        return 1  

# Add a PK list to specific table and database
def alterDropPK(database, table):
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.alterDROPPK(database, table)
    except:
        return 1

# Rename a table name by inserting new_key and deleting old_key
def alterTable(database, tableOld, tableNew):
    try:
        if not database.isidentifier() \
        or not tableOld.isidentifier() \
        or not tableNew.isidentifier() :
            raise Exception()        
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, tableOld)
        if existe is False:
            return 3
        
        existe = server.existeTabla(database, tableNew)
        if existe:
            return 4
        
        server.alterT(database, tableOld, tableNew)
        return 0
    except:
        return 1   

# add a column at the end of register with default value
def alterAddColumn(database, table, default):
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()  

        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3
        
        return server.alterAddC(database, table, default)
    except:
        return 1 

# drop a column and its content (except primary key columns)
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(columnNumber, int):
            raise Exception()  

        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.alterDropC(database, table, columnNumber)
    except:
        return 1
      
# Delete a table name by inserting new_key and deleting old_key
def dropTable(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3
        
        server.dropT(database, table)
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
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.insert(database, table, register)
    except:
        return 1

# READ or load a CSV file to a table
def loadCSV(filepath: str, database: str, table: str) -> list:
    try:
        res = []
        
        res = server.cargarCSV(filepath, database, table)
        return res
    except:
        return []

# READ or extract a register
def extractRow(database: str, table: str, columns: list) -> list:
    try:
        res = []
        
        existe = server.existeDB(database)
        if existe is False:
            return []
        existe = server.existeTabla(database, table)
        if existe is False:
            return []
        res = server.extractR(database, table, columns)
        return res
    except:
        return []

# UPDATE a register
def update(database, table, register, columns):
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()        
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.actualizarDatos(database, table, register, columns)
    except:
        return 1

# DELETE a specific register
def delete(database: str, table: str, columns: list) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier():
            raise Exception()        
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3

        return server.eliminarRegistro(database, table, columns)
    except:
        return 1

# DELETE or truncate all registers of the table
def truncate(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        
        existe = server.existeDB(database)
        if existe is False:
            return 2
        
        existe = server.existeTabla(database, table)
        if existe is False:
            return 3
        
        server.truncateT(database, table)
        return 0
    except:
        return 1