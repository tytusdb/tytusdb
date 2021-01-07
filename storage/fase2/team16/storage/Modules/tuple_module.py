# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from .handler import Handler
from ..path import *


class TupleModule:

    def __init__(self):
        self.handler = Handler()
        self.dbs = None

    def insert(self, database: str, table: str, register: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(register, list):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'insert', ['database', 'table', 'register'])
                    return eval(action)
                return 3
            return 2
        except:
            return 1

    def loadCSV(self, file: str, database: str, table: str) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not file.endswith(".csv"):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'loadCSV', ['file', 'database', 'table'])
                    return eval(action)
            return []
        except:
            return []

    def extractRow(self, database: str, table: str, columns: list) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'extractRow', ['database', 'table', 'columns'])
                    return eval(action)
            return []
        except:
            return []

    def update(self, database: str, table: str, register: dict, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'update', ['database', 'table', 'register', 'columns'])
                    return eval(action)
                return 3
            return 2
        except:
            return 1

    def delete(self, database: str, table: str, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'delete', ['database', 'table', 'columns'])
                    return eval(action)
                return 3
            return 2
        except:
            return 1

    def truncate(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'truncate', ['database', 'table'])
                    return eval(action)
                return 3
            return 2
        except:
            return 1

    def _exist(self, database: str):
        tmp = None
        index = -1
        for db in self.dbs:
            if db.name.upper() == database.upper():
                index = self.dbs.index(db)
                tmp = db
                break
        return tmp, index
