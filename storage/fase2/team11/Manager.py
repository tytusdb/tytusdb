from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bPlus
from storage.dict import DictMode as diccionario
from storage.isam import ISAMMode as isam
from storage.hash import HashMode as hash
from storage.json import jsonMode as json
from Binary import verify_string

mode_list = list()


class Mode:
    def __init__(self, name_database, mode, enconding):
        self.__name_database = name_database
        self.__mode = mode
        self.__enconding = enconding

    def set_name_database(self, name_database):
        self.__name_database = name_database

    def get_name_database(self):
        return self.__name_database

    def set_mode(self, mode):
        self.__mode = mode

    def get_mode(self):
        return self.__mode

    def set_encondig(self, encondig):
        self.__enconding = encondig

    def get_encondig(self):
        return self.__enconding


def save_mode(database, mode, encondig):
    new_mode = Mode(database, mode, encondig)
    mode_list.append(new_mode)


def exist(database: str):
    for mode in mode_list:
        if mode.get_name_database() == database:
            return True
    return False


def createDatabase(database: str, mode: str, encoding: str):
    if verify_string(database):
        if exist(database): return 2
        if encoding.lower().strip() is "ascii" or encoding.lower().strip() is "iso-8859-1" \
                or encoding.lower().strip() is "utf8":
            status = -1
            if mode.lower().strip() is "avl":
                status = avl.createDatabase(database)
            elif mode.lower().strip() is "b":
                status = b.createDatabase(database)
            elif mode.lower().strip() is "bplus":
                status = bPlus.createDatabase(database)
            elif mode.lower().strip() is "dict":
                status = diccionario.createDatabase(database)
            elif mode.lower().strip() is "isam":
                status = isam.createDatabase(database)
            elif mode.lower().strip() is "json":
                status = json.createDatabase(database)
            elif mode.lower().strip() is "hash":
                status = hash.createDatabase(database)
            else:
                return 3
            if status == 0:
                save_mode(database, mode, encoding)
            return status
        else:
            return 4
    else:
        return 1

def exist_Alter(database: str):
    indice=0
    for mode in mode_list:          
        if mode.get_name_database() == database:            
            return mode,indice
        indice+=1
    return None



def alterDatabaseMode(database: str, mode: str):
    ModeDB,indexDB = exist_Alter(database)
    mode_list.pop(indexDB)     
    createDatabase(database,mode,ModeDB.get_encondig())
    if ModeDB:
       
        oldMode = ModeDB.get_mode()
        if oldMode.lower().strip() == "avl":           
            tables=avl.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            avl.dropDatabase(database)        
        elif oldMode.lower().strip() == "b":           
            tables=b.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            b.dropDatabase(database)
        elif oldMode.lower().strip() == "bplus":           
            tables=bplus.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            bplus.dropDatabase(database)
        elif oldMode.lower().strip() == "dict":           
            tables=diccionario.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            diccionario.dropDatabase(database)
        elif oldMode.lower().strip() == "isam":           
            tables=isam.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            isam.dropDatabase(database)
        elif oldMode.lower().strip() == "hash":           
            tables=hash.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            hash.dropDatabase(database)
        elif oldMode.lower().strip() == "json":           
            tables=json.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            json.dropDatabase(database)

            
def insertAlter(database,tabla,numberColumns,mode,listaDatos):
    if mode.lower().strip() =="avl":
        avl.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            avl.insert(database,tabla,data)
    elif mode.lower().strip() =="b":
        b.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            b.insert(database,tabla,data)
    elif mode.lower().strip() =="bplus":
        bplus.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            bplus.insert(database,tabla,data)
    elif mode.lower().strip() =="dict":
        diccionario.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            diccionario.insert(database,tabla,data)
    elif mode.lower().strip() =="isam":
        isam.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            isam.insert(database,tabla,data)
    elif mode.lower().strip() =="hash":
        hash.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            hash.insert(database,tabla,data)
    elif mode.lower().strip() =="json":
        json.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            json.insert(database,tabla,data)


            
            
def get_Data(database:str,table:str,mode:str):
    if mode.lower().strip() =="avl":
        return avl.extractTable(database,table)
    elif mode.lower().strip() =="b":
        return b.extractTable(database,table)
    elif mode.lower().strip() =="bplus":
        return bplus.extractTable(database,table)
    elif mode.lower().strip() =="dict":
        return diccionario.extractTable(database,table)
    elif mode.lower().strip() =="isam":
        return isam.extractTable(database,table)
    elif mode.lower().strip() =="hash":
        return hash.extractTable(database,table)
    elif mode.lower().strip() =="json":
        return json.extractTable(database,table)
    
def alterTableMode(database: str, table: str, databaseRef: str, mode: str):
    if exist_Alter(database) and exist_Alter(databaseRef) and exist_Alter(databaseRef)[0].get_mode()==mode:
        ModeDB,indice = exist_Alter(database)
        if ModeDB:
            oldMode = ModeDB.get_mode()
            if oldMode.lower().strip() == "avl":           
                tables=avl.showTables(database)     
                for tabla in tables:
                    if tabla == table: 
                        listaDatos = get_Data(database,tabla,oldMode) # UNA LISTA VACIA NO EJECUTA EL FOR
                        numberColumns=len(listaDatos[0])
                        insertAlter(databaseRef,tabla,numberColumns,mode,listaDatos)   
                avl.dropTable(database,table)     
            elif oldMode.lower().strip() == "b":           
                tables=b.showTables(database)     
                for tabla in tables:
                    if tabla == table:      
                        listaDatos = get_Data(database,tabla,oldMode)
                        numberColumns=len(listaDatos[0])
                        insertAlter(databaseRef,tabla,numberColumns,mode,listaDatos)   
                b.dropTable(database,table)
            elif oldMode.lower().strip() == "bplus":           
                tables=bplus.showTables(database)     
                for tabla in tables:
                    if tabla == table:     
                        listaDatos = get_Data(database,tabla,oldMode)
                        numberColumns=len(listaDatos[0])
                        insertAlter(databaseRef,tabla,numberColumns,mode,listaDatos)   
                bplus.dropTable(database,table)
            elif oldMode.lower().strip() == "dict":           
                tables=diccionario.showTables(database)     
                for tabla in tables:
                    if tabla == table:
                        listaDatos = get_Data(database,tabla,oldMode)
                        numberColumns=len(listaDatos[0])
                        insertAlter(databaseRef,tabla,numberColumns,mode,listaDatos)   
                diccionario.dropTable(database,table)
            elif oldMode.lower().strip() == "isam":           
                tables=isam.showTables(database)     
                for tabla in tables:
                    if tabla == table:    
                        listaDatos = get_Data(database,tabla,oldMode)
                        numberColumns=len(listaDatos[0])
                        insertAlter(databaseRef,tabla,numberColumns,mode,listaDatos)
                isam.dropTable(database,table)
            elif oldMode.lower().strip() == "hash":           
                tables=hash.showTables(database)     
                for tabla in tables:
                    if tabla == table:      
                        listaDatos = get_Data(database,tabla,oldMode)
                        numberColumns=len(listaDatos[0])
                        insertAlter(databaseRef,tabla,numberColumns,mode,listaDatos)   
                hash.dropTable(database,table)
            elif oldMode.lower().strip() == "json":           
                tables=json.showTables(database)     
                for tabla in tables:
                    if tabla == table:      
                        listaDatos = get_Data(database,tabla,oldMode)
                        numberColumns=len(listaDatos[0])
                        insertAlter(databaseRef,tabla,numberColumns,mode,listaDatos)   
                json.dropTable(database,table)
    else:
        None
        
        
def alterDatabase(old_db, new_db):
    modeDB, indexDB = exist_Alter(old_db)
    modeDB_new, indexDB_newDB = exist_Alter(new_db)
    if modeDB and modeDB_new is None:
        mode = modeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.alterDatabase(old_db, new_db)
        elif mode.lower().strip() == "b":
            return b.alterDatabase(old_db, new_db)
        elif mode.lower().strip() == "bPlus":
            return bPlus.alterDatabase(old_db, new_db)
        elif mode.lower().strip() == "dict":
            return diccionario.alterDatabase(old_db, new_db)
        elif mode.lower().strip() == "hash":
            return hash.alterDatabase(old_db, new_db)
        elif mode.lower().strip() == "isam":
            return isam.alterDatabase(old_db, new_db)
        elif mode.lower().strip() == "json":
            return json.alterDatabase(old_db, new_db)


def dropDatabase(name_db):
    ModeDB, indexDB = exist_Alter(name_db)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.dropDatabase(name_db)
        elif mode.lower().strip() == "b":
            return b.dropDatabase(name_db)
        elif mode.lower().strip() == "bPlus":
            return bPlus.dropDatabase(name_db)
        elif mode.lower().strip() == "dict":
            return diccionario.dropDatabase(name_db)
        elif mode.lower().strip() == "hash":
            return hash.dropDatabase(name_db)
        elif mode.lower().strip() == "isam":
            return isam.dropDatabase(name_db)
        elif mode.lower().strip() == "json":
            return json.dropDatabase(name_db)


def createTable(database, name_table, number_columns):
    ModeDB, indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.createTable(database, name_table, number_columns)
        elif mode.lower().strip() == "b":
            return b.createTable(database, name_table, number_columns)
        elif mode.lower().strip() == "bPlus":
            return bPlus.createTable(database, name_table, number_columns)
        elif mode.lower().strip() == "dict":
            return diccionario.createTable(database, name_table, number_columns)
        elif mode.lower().strip() == "hash":
            return hash.createTable(database, name_table, number_columns)
        elif mode.lower().strip() == "isam":
            return isam.createTable(database, name_table, number_columns)
        elif mode.lower().strip() == "json":
            return json.createTable(database, name_table, number_columns)
        
        
 def showTables(database):
    ModeDB, indexDB = exist_Alter(database)

    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.showTables(database)
        elif mode.lower().strip() == "b":
            return b.showTables(database)
        elif mode.lower().strip() == "bplus":
            return bplus.showTables(database)
        elif mode.lower().strip() == "dict":
            return diccionario.showTables(database)
        elif mode.lower().strip() == "hash":
            return hash.showTables(database)
        elif mode.lower().strip() == "isam":
            return isam.showTables(database)
        elif mode.lower().strip() == "json":
            return json.showTables(database)


def extractTable(database, name_table):
    ModeDB, indexDB = exist_Alter(database)

    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.extractTable(database, name_table)
        elif mode.lower().strip() == "b":
            return b.extractTable(database, name_table)
        elif mode.lower().strip() == "bplus":
            return bplus.extractTable(database, name_table)
        elif mode.lower().strip() == "dict":
            return diccionario.extractTable(database, name_table)
        elif mode.lower().strip() == "hash":
            return hash.extractTable(database, name_table)
        elif mode.lower().strip() == "isam":
            return isam.extractTable(database, name_table)
        elif mode.lower().strip() == "json":
            return json.extractTable(database, name_table)


def extractRangeTable(database, name_table, number_column, lower, upper):
    ModeDB, indexDB = exist_Alter(database)

    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.extractRangeTable(database, name_table, number_column, lower, upper)
        elif mode.lower().strip() == "b":
            return b.extractRangeTable(database, name_table, number_column, lower, upper)
        elif mode.lower().strip() == "bplus":
            return bplus.extractRangeTable(database, name_table, number_column, lower, upper)
        elif mode.lower().strip() == "dict":
            return diccionario.extractRangeTable(database, name_table, number_column, lower, upper)
        elif mode.lower().strip() == "hash":
            return hash.extractRangeTable(database, name_table, number_column, lower, upper)
        elif mode.lower().strip() == "isam":
            return isam.extractRangeTable(database, name_table, number_column, lower, upper)
        elif mode.lower().strip() == "json":
            return json.extractRangeTable(database, name_table, number_column, lower, upper)

def alterAddPK(database, name_table, columns):
    ModeDB, indexDB = exist_Alter(database)

    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.alterAddPK(database, name_table, columns)
        elif mode.lower().strip() == "b":
            return b.alterAddPK(database, name_table, columns)
        elif mode.lower().strip() == "bplus":
            return bplus.alterAddPK(database, name_table, columns)
        elif mode.lower().strip() == "dict":
            return diccionario.alterAddPK(database, name_table, columns)
        elif mode.lower().strip() == "hash":
            return hash.alterAddPK(database, name_table, columns)
        elif mode.lower().strip() == "isam":
            return isam.alterAddPK(database, name_table, columns)
        elif mode.lower().strip() == "json":
            return json.alterAddPK(database, name_table, columns)

def alterDropPK(database, name_table):
    ModeDB, indexDB = exist_Alter(database)

    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.alterDropPK(database, name_table)
        elif mode.lower().strip() == "b":
            return b.alterDropPK(database, name_table)
        elif mode.lower().strip() == "bplus":
            return bplus.alterDropPK(database, name_table)
        elif mode.lower().strip() == "dict":
            return diccionario.alterDropPK(database, name_table)
        elif mode.lower().strip() == "hash":
            return hash.alterDropPK(database, name_table)
        elif mode.lower().strip() == "isam":
            return isam.alterDropPK(database, name_table)
        elif mode.lower().strip() == "json":
            return json.alterDropPK(database, name_table)

def alterTable(database, old_table, new_table):
    ModeDB,indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.alterTable(database, old_table, new_table)
        elif mode.lower().strip() == "b":
            return b.alterTable(database, old_table, new_table)
        elif mode.lower().strip() == "bplus":
            return bplus.alterTable(database, old_table, new_table)
        elif mode.lower().strip() == "dict":
            return diccionario.alterTable(database, old_table, new_table)
        elif mode.lower().strip() == "hash":
            return hash.alterTable(database, old_table, new_table)
        elif mode.lower().strip() == "isam":
            return isam.alterTable(database, old_table, new_table)
        elif mode.lower().strip() == "json":
            return json.alterTable(database, old_table, new_table)


def alterAddColumn(database, name_table, default):
    ModeDB,indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.alterAddColumn(database, name_table, default)
        elif mode.lower().strip() == "b":
            return b.alterAddColumn(database, name_table, default)
        elif mode.lower().strip() == "bplus":
            return bplus.alterAddColumn(database, name_table, default)
        elif mode.lower().strip() == "dict":
            return diccionario.alterAddColumn(database, name_table, default)
        elif mode.lower().strip() == "hash":
            return hash.alterAddColumn(database, name_table, default)
        elif mode.lower().strip() == "isam":
            return isam.alterAddColumn(database, name_table, default)
        elif mode.lower().strip() == "json":
            return json.alterAddColumn(database, name_table, default)


def alterDropColumn(database, name_table, number_column):
    ModeDB,indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.alterDropColumn(database, name_table, number_column)
        elif mode.lower().strip() == "b":
            return b.alterDropColumn(database, name_table, number_column)
        elif mode.lower().strip() == "bplus":
            return bplus.alterDropColumn(database, name_table, number_column)
        elif mode.lower().strip() == "dict":
            return diccionario.alterDropColumn(database, name_table, number_column)
        elif mode.lower().strip() == "hash":
            return hash.alterDropColumn(database, name_table, number_column)
        elif mode.lower().strip() == "isam":
            return isam.alterDropColumn(database, name_table, number_column)
        elif mode.lower().strip() == "json":
            return json.alterDropColumn(database, name_table, number_column)


def dropTable(database, name_table):
    ModeDB,indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.dropTable(database, name_table)
        elif mode.lower().strip() == "b":
            return b.dropTable(database, name_table)
        elif mode.lower().strip() == "bplus":
            return bplus.dropTable(database, name_table)
        elif mode.lower().strip() == "dict":
            return diccionario.dropTable(database, name_table)
        elif mode.lower().strip() == "hash":
            return hash.dropTable(database, name_table)
        elif mode.lower().strip() == "isam":
            return isam.dropTable(database, name_table)
        elif mode.lower().strip() == "json":
            return json.dropTable(database, name_table)

    
def insert(database, name_table, register):
    ModeDB,indexDB = exist_Alter(database)
    if ModeDB:
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.insert(database, name_table, register)
        elif mode.lower().strip() == "b":
            return b.insert(database, name_table, register)
        elif mode.lower().strip() == "bplus":
            return bplus.insert(database, name_table, register)
        elif mode.lower().strip() == "dict":
            return diccionario.insert(database, name_table, register)
        elif mode.lower().strip() == "hash":
            return hash.insert(database, name_table, register)
        elif mode.lower().strip() == "isam":
            return isam.insert(database, name_table, register)
        elif mode.lower().strip() == "json":
            return json.insert(database, name_table, register)
        
        
def extractRow(database, name_table, columns):
    ModeDB,indexDB = exist_Alter(database)  
    if ModeDB:       
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "b":
            return b.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "bplus":
            return bPlus.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "dict":
            return diccionario.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "hash":
            return hash.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "isam":
            return isam.extractRow(database, name_table, columns)
        elif mode.lower().strip() == "json":
            return json.update(database, name_table, register, columns)
    return db.extractRow(database, name_table, columns)

def update(database, name_table, register, columns):
    ModeDB,indexDB = exist_Alter(database)  
    if ModeDB:       
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.update(database, name_table, register, columns)
        elif mode.lower().strip() == "b":
            return b.update(database, name_table, register, columns)
        elif mode.lower().strip() == "bplus":
            return bPlus.update(database, name_table, register, columns)
        elif mode.lower().strip() == "dict":
            return diccionario.update(database, name_table, register, columns)
        elif mode.lower().strip() == "hash":
            return hash.update(database, name_table, register, columns)
        elif mode.lower().strip() == "isam":
            return isam.update(database, name_table, register, columns)
        elif mode.lower().strip() == "json":
            return json.update(database, name_table, register, columns)

def loadCSV(file, database, name_table):
    ModeDB,indexDB = exist_Alter(database)  
    if ModeDB:       
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "b":
            return b.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "bplus":
            return bPlus.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "dict":
            return diccionario.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "hash":
            return hash.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "isam":
            return isam.loadCSV(file, database, name_table)
        elif mode.lower().strip() == "json":
            return json.loadCSV(file, database, name_table)

def delete(database, name_table, columns):
    ModeDB,indexDB = exist_Alter(database)  
    if ModeDB:       
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.delete(database, name_table, columns)
        elif mode.lower().strip() == "b":
            return b.delete(database, name_table, columns)
        elif mode.lower().strip() == "bplus":
            return bPlus.delete(database, name_table, columns)
        elif mode.lower().strip() == "dict":
            return diccionario.delete(database, name_table, columns)
        elif mode.lower().strip() == "hash":
            return hash.delete(database, name_table, columns)
        elif mode.lower().strip() == "isam":
            return isam.delete(database, name_table, columns)
        elif mode.lower().strip() == "json":
            return json.delete(database, name_table, columns)

def truncate(database, name_table):
    ModeDB,indexDB = exist_Alter(database)  
    if ModeDB:       
        mode = ModeDB.get_mode()
        if mode.lower().strip() == "avl":
            return avl.truncate(database, name_table)
        elif mode.lower().strip() == "b":
            return b.truncate(database, name_table)
        elif mode.lower().strip() == "bplus":
            return bPlus.truncate(database, name_table)
        elif mode.lower().strip() == "dict":
            return diccionario.truncate(database, name_table)
        elif mode.lower().strip() == "hash":
            return hash.truncate(database, name_table)
        elif mode.lower().strip() == "isam":
            return isam.truncate(database, name_table)
        elif mode.lower().strip() == "json":
            return json.truncate(database, name_table)   
