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
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    try:
                        [str(x).encode(tmp.encoding) for x in register]
                    except:
                        raise Exception('Registro no codificable')
                    else:
                        action = actionCreator(_table.mode, 'insert', ['database', 'table', 'register'])
                        result = eval(action)
                        if result == 0 and _table.security:
                            _table.security.insert(database, table, register)
                            self.handler.rootupdate(self.dbs)
                        return result
                return 3
            return 2
        except:
            return 1

    def loadCSV(self, file: str, database: str, table: str) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not file.endswith(".csv"):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    action = actionCreator(_table.mode, 'loadCSV', ['file', 'database', 'table'])
                    return eval(action)
            return []
        except:
            return []

    def extractRow(self, database: str, table: str, columns: list) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    action = actionCreator(_table.mode, 'extractRow', ['database', 'table', 'columns'])
                    return eval(action)
            return []
        except:
            return []

    def update(self, database: str, table: str, register: dict, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    try:
                        [str(x).encode(tmp.encoding) for x in register]
                    except:
                        raise Exception('Registro no codificable')
                    else:
                        if _table.security:
                            row = self.extractRow(database, table, columns)
                            if not row:
                                raise Exception()
                        action = actionCreator(_table.mode, 'update', ['database', 'table', 'register', 'columns'])
                        result = eval(action)
                        if result == 0 and _table.security:
                            _table.security.update(database, table, register, row)
                            self.handler.rootupdate(self.dbs)
                        return result
                return 3
            return 2
        except:
            return 1

    def delete(self, database: str, table: str, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    if _table.security:
                        row = self.extractRow(database, table, columns)
                        if not row:
                            raise Exception()
                    action = actionCreator(_table.mode, 'delete', ['database', 'table', 'columns'])
                    result = eval(action)
                    if result == 0 and _table.security:
                        _table.security.delete(database, table, row)
                        self.handler.rootupdate(self.dbs)
                    return result
                return 3
            return 2
        except:
            return 1

    def truncate(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    action = actionCreator(_table.mode, 'truncate', ['database', 'table'])
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

    def getprev(self, mode: str, database: str, table: str):
        pass
