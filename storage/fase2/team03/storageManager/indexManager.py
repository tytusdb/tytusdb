from storage.avl import avl_mode as avl
from storage.b import b_mode as b
from storage.bplus import bplus_mode as bplus
from storage.dict import dict_mode as d
from storage.hash import hash_mode as ha
from storage.isam import isam_mode as isam
from storage.json import json_mode as j

class indexManager:

    def __init__(self, modo, database, table, columns, typeIndex):

        self.modo = modo
        self.database = database
        self.type = typeIndex
        self.table = table + self.type
        self.columnas = columns
        
        self.createDatabase()
        self.createTable()

    def createDatabase(self):

        if self.modo == "avl":
            avl.createDatabase(self.database)
        elif self.modo == "b":
            b.createDatabase(self.database)
        elif self.modo == "bplus":
            bplus.createDatabase(self.database)
        elif self.modo == "hash":
            ha.createDatabase(self.database)
        elif self.modo == "isam":
            isam.createDatabase(self.database)
        elif self.modo == "json":
            j.createDatabase(self.database)
        elif self.modo == "dict":
            d.createDatabase(self.database)

    def createTable(self):
    
        if self.modo == "avl":
            avl.createTable(self.database, self.table, self.columnas)
            avl.alterAddPK(self.database, self.table, [0])
        elif self.modo == "b":
            b.createTable(self.database, self.table, self.columnas)
            b.alterAddPK(self.database, self.table, [0])
        elif self.modo == "bplus":
            bplus.createTable(self.database, self.table, self.columnas)
            bplus.alterAddPK(self.database, self.table, [0])
        elif self.modo == "hash":
            ha.createTable(self.database, self.table, self.columnas)
            ha.alterAddPK(self.database, self.table, [0])
        elif self.modo == "isam":
            isam.createTable(self.database, self.table, self.columnas)
            isam.alterAddPK(self.database, self.table, [0])
        elif self.modo == "json":
            j.createTable(self.database, self.table, self.columnas)
            j.alterAddPK(self.database, self.table, [0])
        elif self.modo == "dict":
            d.createTable(self.database, self.table, self.columnas)
            d.alterAddPK(self.database, self.table, [0])

    def dropTable(self):

        estado = 1

        if self.modo == "avl":
            estado = avl.dropTable(self.database, self.table)
        elif self.modo == "b":
            estado = b.dropTable(self.database, self.table)
        elif self.modo == "bplus":
            estado = bplus.dropTable(self.database, self.table)
        elif self.modo == "hash":
            estado = ha.dropTable(self.database, self.table)
        elif self.modo == "isam":
            estado = isam.dropTable(self.database, self.table)
        elif self.modo == "json":
            estado = j.dropTable(self.database, self.table)
        elif self.modo == "dict":
            estado = d.dropTable(self.database, self.table)

        return estado

    def insert(self, registro):

        estado = 1

        if self.modo == "avl":
            estado = avl.insert(self.database, self.table, registro)
        elif self.modo == "b":
            estado = b.insert(self.database, self.table, registro)
        elif self.modo == "bplus":
            estado = bplus.insert(self.database, self.table, registro)
        elif self.modo == "hash":
            estado = ha.insert(self.database, self.table, registro)
        elif self.modo == "isam":
            estado = isam.insert(self.database, self.table, registro)
        elif self.modo == "json":
            estado = j.insert(self.database, self.table, registro)
        elif self.modo == "dict":
            estado = d.insert(self.database, self.table, registro)

        return estado

    def delete(self, indexName):

        estado = 1

        if self.modo == "avl":
            estado = avl.delete(self.database, self.table, [indexName])
        elif self.modo == "b":
            estado = b.delete(self.database, self.table, [indexName])
        elif self.modo == "bplus":
            estado = bplus.delete(self.database, self.table, [indexName])
        elif self.modo == "hash":
            estado = ha.delete(self.database, self.table, [indexName])
        elif self.modo == "isam":
            estado = isam.delete(self.database, self.table, [indexName])
        elif self.modo == "json":
            estado = j.delete(self.database, self.table, [indexName])
        elif self.modo == "dict":
            estado = d.delete(self.database, self.table, [indexName])

        return estado

    def extractTable(self):

        estado = 1

        if self.modo == "avl":
            estado = avl.extractTable(self.database, self.table)
        elif self.modo == "b":
            estado = b.extractTable(self.database, self.table)
        elif self.modo == "bplus":
            estado = bplus.extractTable(self.database, self.table)
        elif self.modo == "hash":
            estado = ha.extractTable(self.database, self.table)
        elif self.modo == "isam":
            estado = isam.extractTable(self.database, self.table)
        elif self.modo == "json":
            estado = j.extractTable(self.database, self.table)
        elif self.modo == "dict":
            estado = d.extractTable(self.database, self.table)

        return estado

    def extractRow(self, indexName):

        estado = 1

        if self.modo == "avl":
            estado = avl.extractRow(self.database, self.table, [indexName])
        elif self.modo == "b":
            estado = b.extractRow(self.database, self.table, [indexName])
        elif self.modo == "bplus":
            estado = bplus.extractRow(self.database, self.table, [indexName])
        elif self.modo == "hash":
            estado = ha.extractRow(self.database, self.table, [indexName])
        elif self.modo == "isam":
            estado = isam.extractRow(self.database, self.table, [indexName])
        elif self.modo == "json":
            estado = j.extractRow(self.database, self.table, [indexName])
        elif self.modo == "dict":
            estado = d.extractRow(self.database, self.table, [indexName])

        return estado

    def alterTableMode(self,mode: str) -> int:

        try:              
            registros = self.extractTable()
            self.modo = mode

            self.dropTable()
            self.createTable()

            for registro in registros:
                self.insert(registro)

            return 0
        except:
            return 1
