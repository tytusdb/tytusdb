# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from ..path import *
from .handler import Handler
from .Complements.security import Blockchain


class Table:
    def __init__(self, name: str, mode: str, numberColumns: int):
        self.name = name
        self.mode = mode
        self.numberColumns = numberColumns
        self.pk = []


class TableModule:
    def __init__(self):
        self.handler = Handler()
        self.dbs = None

    def createTable(self, database: str, table: str, numberColumns: int) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or (
                    not isinstance(numberColumns, int) or numberColumns < 0):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if not table.lower() in listtmp:
                    result = 1
                    action = actionCreator(tmp.mode, 'createTable', ['database', 'table', 'numberColumns'])
                    result = eval(action)
                    if result == 0:
                        self.dbs[index].tables.append(Table(table, tmp.mode, numberColumns))
                        self.handler.rootupdate(self.dbs)
                    return result
                return 3
            return 2
        except:
            return 1

    def showTables(self, database: str) -> list:
        try:
            if not isinstance(database, str):
                raise
            self.dbs = self.handler.rootinstance()
            for i in self.dbs:
                if database.upper() == i.name.upper():
                    tables = [x.name for x in i.tables]
                    return tables
            return None
        except:
            return None

    def extractTable(self, database: str, table: str) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'extractTable', ['database', 'table'])
                    return eval(action)
            return None
        except:
            return None

    def extractRangeTable(self, database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columnNumber, int):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'extractRangeTable',
                                           ['database', 'table', 'columnNumber', 'lower', 'upper'])
                    return eval(action)
            return None
        except:
            return None

    def alterAddPK(self, database: str, table: str, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list) or \
                    len(columns) == 0:
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    result = 1
                    action = actionCreator(tmp.mode, 'alterAddPK', ['database', 'table', 'columns'])
                    result = eval(action)
                    if result == 0:
                        element = next(x for x in tmp.tables if x.name.lower() == table.lower())
                        self.dbs[index].tables[self.dbs[index].tables.index(element)].pk = columns
                        self.handler.rootupdate(self.dbs)
                    return result
                return 3
            return 2
        except:
            return 1

    def alterDropPK(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    result = 1
                    action = actionCreator(tmp.mode, 'alterDropPK', ['database', 'table'])
                    result = eval(action)
                    if result == 0:
                        element = next(x for x in tmp.tables if x.name.lower() == table.lower())
                        self.dbs[index].tables[self.dbs[index].tables.index(element)].pk = []
                        self.handler.rootupdate(self.dbs)
                    return result
                return 3
            return 2
        except:
            return 1

    def alterTable(self, database: str, tableOld: str, tableNew: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(tableOld, str) or not isinstance(tableNew, str) or \
                    self.handler.invalid(tableNew):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if tableOld.lower() in listtmp:
                    if not tableNew.lower() in listtmp:
                        result = 1
                        action = actionCreator(tmp.mode, 'alterTable', ['database', 'tableOld', 'tableNew'])
                        result = eval(action)
                        if result == 0:
                            i = 0
                            for x in listtmp:
                                if x == tableOld.lower():
                                    i = listtmp.index(x)
                                    break
                            self.dbs[index].tables[i].name = tableNew
                            self.handler.rootupdate(self.dbs)
                        return result
                    return 4
                return 3
            return 2
        except:
            return 1

    def alterAddColumn(self, database: str, table: str, default: any) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'alterAddColumn', ['database', 'table', 'default'])
                    result = eval(action)
                    if result == 0:
                        element = next(x for x in tmp.tables if x.name.lower() == table.lower())
                        self.dbs[index].tables[self.dbs[index].tables.index(element)].numberColumns += 1
                        self.handler.rootupdate(self.dbs)
                    return result
                return 3
            return 2
        except:
            return 1

    def alterDropColumn(self, database: str, table: str, columnNumber: int) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columnNumber, int):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'alterDropColumn', ['database', 'table', 'columnNumber'])
                    result = eval(action)
                    if result == 0:
                        element = next(x for x in tmp.tables if x.name.lower() == table.lower())
                        self.dbs[index].tables[self.dbs[index].tables.index(element)].numberColumns -= 1
                        self.handler.rootupdate(self.dbs)
                    return result
                return 3
            return 2
        except:
            return 1

    def dropTable(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if table.lower() in listtmp:

                    result = 1
                    action = actionCreator(tmp.mode, 'dropTable', ['database', 'table'])
                    result = eval(action)
                    if result == 0:
                        aux = next(x for x in tmp.tables if x.name.lower() == table.lower())
                        self.dbs[index].tables.remove(aux)
                        self.handler.rootupdate(self.dbs)
                    return result

                return 3
            return 2
        except:
            return 1

    def alterTableAddFK(self, database: str, table: str, indexName: str, columns: list, tableRef: str,
                        columnsRef: list) -> int:
        pass

    def alterTableDropFK(self, database: str, table: str, indexName: str) -> int:
        pass

    def alterTableAddUnique(self, database: str, table: str, indexName: str, columns: list) -> int:
        pass

    def alterTableDropUnique(self, database: str, table: str, indexName: str) -> int:
        pass

    def alterTableAddIndex(self, database: str, table: str, indexName: str, columns: list) -> int:
        pass

    def alterTableDropIndex(self, database: str, table: str, indexName: str) -> int:
        pass

    def alterTableCompress(self, database: str, table: str, level: int) -> int:
        pass

    def alterTableDecompress(self, database: str, table: str) -> int:
        pass

    def safeModeOn(self, database: str, table: str) -> int:
        pass

    def safeModeOff(self, database: str, table: str) -> int:
        pass

    def _exist(self, database: str):
        tmp = None
        index = -1
        for db in self.dbs:
            if db.name.upper() == database.upper():
                index = self.dbs.index(db)
                tmp = db
                break
        return tmp, index
