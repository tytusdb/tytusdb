from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.dict import DictMode as diccionario
from storage.isam import ISAMMode as isam
from storage.hash import HashMode as hash
from storage.json import jsonMode as json

modes = {
    "avl": avl,
    "b": b,
    "bplus": bplus,
    "hash": hash,
    "isam": isam,
    "dict": diccionario,
    "json": json
}


class Database:
    def __init__(self, name_database, mode, enconding):
        self.name_database = name_database
        self.mode = mode
        self.enconding = enconding
        self.dict_tables = dict()

    def set_name_database(self, name_database):
        self.name_database = name_database

    def get_name_database(self):
        return self.name_database

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode

    def set_encondig(self, encondig):
        self.enconding = encondig

    def get_encondig(self):
        return self.enconding

    def create_table(self, name_table, number_columns, mode):
        new_table = Table(self.name_database, name_table, number_columns, mode)
        self.dict_tables.setdefault(name_table, new_table)

    def drop_table(self, name_table):
        return self.dict_tables.pop(name_table)

    def get_table(self, name_table):
        return self.dict_tables.get(name_table)
    
    def get_tab(self):
        return self.dict_tables

    def alter_table(self, old_name, new_name):
        table_old: Table = self.dict_tables.get(old_name)
        if table_old:
            new_table = Table(self.name_database, new_name, table_old.get_nums_colums(), table_old.get_mode())
            self.dict_tables.pop(old_name)
            self.dict_tables.setdefault(new_name, new_table)
            return 0
        else:
            return 1


class Table:
    def __init__(self, database, name_table, number_colums, mode):
        self.database = database
        self.name_table = name_table
        self.number_colums = number_colums
        self.mode = mode
        self.compress = False
        self.fk = FK(self.database, self.name_table, self.mode)
        self.unique = UNIQUE(self.database, self.name_table, self.mode)
        self.index = INDEX(self.database, self.name_table, self.mode)
        self.pk_list = list()

    def set_name(self, name_table):
        self.name_table = name_table

    def get_name_table(self):
        return self.name_table

    def set_nums_colums(self, nums_colums):
        self.number_colums = nums_colums

    def get_nums_colums(self):
        return self.number_colums

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode

    def set_compress(self, compress):
        self.compress = compress

    def get_compress(self):
        return self.compress

    def add_pk_list(self, lista: list):
        self.pk_list = lista

    def get_pk_list(self):
        return self.pk_list


class FK:
    def __init__(self, database, table, mode):
        self.mode = mode
        self.database = database
        self.table = "FK_" + table
        self.createForeign()

    def createForeign(self):
        for mode, struct in modes.items():
            if self.mode == mode:
                struct.createTable(self.database, self.table, 5)
                struct.alterAddPK(self.database, self.table, [0])                

    def alterForeign(self, table):
        for mode, struct in modes.items():
            if self.mode == mode:
                aux_Table = self.table
                self.table = "FK_" + table
                return struct.alterTable(self.database, aux_Table, self.table)

    def dropForeign(self):
        for mode, struct in modes.items():
            if self.mode == mode:
                return struct.dropTable(self.database, self.table)

    def insertFK(self, data):        
        for mode, struct in modes.items():
            if self.mode == mode:                
                return struct.insert(self.database, self.table, data)        

    def deleteFK(self, name):
        for mode, struct in modes.items():
            if self.mode == mode:
                return struct.delete(self.database, self.table, [name])
    
    def extractForeign(self):        
        for mode, func in modes.items():
            if self.mode == mode:
                return func.extractTable(self.database, self.table)

    def alterForeignMode(self, database: str, table: str, mode: str):
                                
        data = self.extractForeign()
        self.mode = mode

        self.dropForeign()
        self.createForeign()

        for register in data:
            self.insertFK(register)

        return 0
  
class UNIQUE:
    def __init__(self, database, table, mode):
        self.mode = mode
        self.database = database
        self.table = "UNIQUE_" + table
        self.createUnique()

    def createUnique(self):
        for mode, struct in modes.items():
            if self.mode == mode:
                struct.createTable(self.database, self.table, 3)
                struct.alterAddPK(self.database, self.table, [0])                

    def alterUnique(self, table):
        for mode, struct in modes.items():
            if self.mode == mode:
                aux_Table = self.table
                self.table = "UNIQUE_" + table
                return struct.alterTable(self.database, aux_Table, self.table)

    def dropUnique(self):
        for mode, struct in modes.items():
            if self.mode == mode:
                return struct.dropTable(self.database, self.table)

    def insertUnique(self, data):        
        for mode, struct in modes.items():
            if self.mode == mode:                
                return struct.insert(self.database, self.table, data)        

    def deleteUnique(self, name):
        for mode, struct in modes.items():
            if self.mode == mode:
                return struct.delete(self.database, self.table, [name])
    
    def extractUnique(self):        
        for mode, func in modes.items():
            if self.mode == mode:
                return func.extractTable(self.database, self.table)

    def alterUniqueMode(self, database: str, table: str, mode: str):
                                
        data = self.extractUnique()
        self.mode = mode

        self.dropUnique()
        self.createUnique()

        for register in data:
            self.insertUnique(register)

        return 0
  
class INDEX:
    def __init__(self, database, table, mode):
        self.mode = mode
        self.database = database
        self.table = "INDEX_" + table
        self.createIndex()

    def createIndex(self):
        for mode, struct in modes.items():
            if self.mode == mode:
                struct.createTable(self.database, self.table, 3)
                struct.alterAddPK(self.database, self.table, [0])                

    def alterIndex(self, table):
        for mode, struct in modes.items():
            if self.mode == mode:
                aux_Table = self.table
                self.table = "INDEX_" + table
                return struct.alterTable(self.database, aux_Table, self.table)

    def dropIndex(self):
        for mode, struct in modes.items():
            if self.mode == mode:
                return struct.dropTable(self.database, self.table)

    def insertIndex(self, data):        
        for mode, struct in modes.items():
            if self.mode == mode:                
                return struct.insert(self.database, self.table, data)        

    def deleteIndex(self, name):
        for mode, struct in modes.items():
            if self.mode == mode:
                return struct.delete(self.database, self.table, [name])
    
    def extractIndex(self):        
        for mode, func in modes.items():
            if self.mode == mode:
                return func.extractTable(self.database, self.table)

    def alterIndexMode(self, database: str, table: str, mode: str):
                                
        data = self.extractIndex()
        self.mode = mode

        self.dropIndex()
        self.createIndex()

        for register in data:
            self.insertIndex(register)

        return 0
