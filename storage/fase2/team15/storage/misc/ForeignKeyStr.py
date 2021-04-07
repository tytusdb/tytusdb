# -------------------------------
# Released under MIT License
# Copyright (c) 2020 TytusDb Team


from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.dict import DictMode as dict
from storage.hash import HashMode as hash
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as json

import traceback

modos = {
    "avl": avl,
    "b": b,
    "bplus": bplus,
    "hash": hash,
    "isam": isam,
    "dict": dict,
    "json": json
}


class ForeignKeyStr:

    def __init__(self, modo, database, table):

        self.modo = modo
        self.database = database
        self.table = table + "_fk_str"
        
        self.createTable()

    
    def createTable(self):
    
        for modo, func in modos.items():

            if self.modo == modo:

                var = []

                var.append(func.createTable(self.database, self.table, 5))
                var.append(func.alterAddPK(self.database, self.table, [0]))

                return var
    

    def alterTable(self, table):
    
        for modo, func in modos.items():

            if self.modo == modo:

                table_old = self.table
                self.table = table + "_fk_str"
                return func.alterTable(self.database, table_old, self.table)


    def dropTable(self):

        for modo, func in modos.items():

            if self.modo == modo:

                return func.dropTable(self.database, self.table)


    def insert(self, registro):
        
        for modo, func in modos.items():

            if self.modo == modo:

                return func.insert(self.database, self.table, registro)


    def delete(self, nombre):
        
        for modo, func in modos.items():

            if self.modo == modo:

                return func.delete(self.database, self.table, [nombre])


    def extractTable(self):
        
        for modo, func in modos.items():

            if self.modo == modo:

                return func.extractTable(self.database, self.table)


    def extractRow(self, nombre):
        
        for modo, func in modos.items():

            if self.modo == modo:

                return func.extractRow(self.database, self.table, [nombre])


    def alterTableMode(self, mode: str) -> int:

        try:
                            
            registros = self.extractTable()
            self.modo = mode

            self.dropTable()
            self.createTable()

            for registro in registros:
                self.insert(registro)

            return 0
  

        except Exception:
            print("="*30)
            traceback.print_exc()
            return -1
