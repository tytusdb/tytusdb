# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from ..path import *
from .handler import Handler
from .Complements.compress import Compression
from .Complements.checksum import *
from .Complements.security import Blockchain


class Table:
    def __init__(self, name: str, mode: str, compress, numberColumns: int):
        self.name = name
        self.mode = mode
        self.numberColumns = numberColumns
        self.pk = []
        self.security = None
        self.compress = compress
        self.fk = []
        self.unique = []
        self.index = []


class TableModule:
    def __init__(self):
        self.handler = Handler()
        self.dbs = None

    def createTable(self, database: str, table: str, numberColumns: int) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or (
                    not isinstance(numberColumns, int) or numberColumns < 0):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if not table.lower() in listtmp:
                    action = actionCreator(tmp.mode, 'createTable', ['database', 'table', 'numberColumns'])
                    result = eval(action)
                    if result == 0:
                        self.dbs[index].tables.append(Table(table, tmp.mode, tmp.compress, numberColumns))
                        self.handler.rootupdate(self.dbs)
                    return result
                return 3
            return 2
        except:
            return 1

    def showTables(self, database: str) -> list:
        try:
            if not isinstance(database, str):
                raise Exception()
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
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    action = actionCreator(_table.mode, 'extractTable', ['database', 'table'])
                    tuples = eval(action)
                    return tuples if not _table.compress else _table.compress.decompress(tuples)
            return None
        except:
            return None

    def extractRangeTable(self, database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columnNumber, int):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    _lower = lower if not _table.compress else _table.compress.compressText(lower)
                    _upper = lower if not _table.compress else _table.compress.compressText(upper)
                    action = actionCreator(_table.mode, 'extractRangeTable',
                                           ['database', 'table', 'columnNumber', '_lower', '_upper'])
                    return eval(action)
            return None
        except:
            return None

    def alterAddPK(self, database: str, table: str, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list) or \
                    len(columns) == 0:
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    _columns = columns if not _table.compress else (_table.compress.compress([columns]))[0]
                    action = actionCreator(_table.mode, 'alterAddPK', ['database', 'table', '_columns'])
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
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    action = actionCreator(_table.mode, 'alterDropPK', ['database', 'table'])
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
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                listtmp = [x.name.lower() for x in tmp.tables]
                if tableOld.lower() in listtmp:
                    if not tableNew.lower() in listtmp:
                        _table = next((x for x in tmp.tables if x.name.lower() == tableOld.lower()), None)
                        action = actionCreator(_table.mode, 'alterTable', ['database', 'tableOld', 'tableNew'])
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
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    _default = default if not _table.compress else _table.compress.compressText(default)
                    action = actionCreator(_table.mode, 'alterAddColumn', ['database', 'table', '_default'])
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
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    action = actionCreator(_table.mode, 'alterDropColumn', ['database', 'table', 'columnNumber'])
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
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    action = actionCreator(_table.mode, 'dropTable', ['database', 'table'])
                    result = eval(action)
                    if result == 0:
                        aux = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                        self.dbs[index].tables.remove(aux)
                        self.handler.rootupdate(self.dbs)
                    return result

                return 3
            return 2
        except:
            return 1

    def alterTableAddFK(self, database: str, table: str, indexName: str, columns: list, tableRef: str,
                        columnsRef: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(indexName, str) \
                    or not isinstance(columns, list) or not isinstance(tableRef, str) or not \
                    isinstance(columnsRef, list):
                raise
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            _tableRef = next((x for x in db.tables if x.name.lower() == tableRef.lower()), None)
            if not _table or not _tableRef:
                return 3
            if len(columns) != len(columnsRef):
                return 4
            if len(columns) == 0:
                raise
            for x in columns:
                if x >= _table.numberColumns:
                    raise
            for x in columnsRef:
                if x >= _tableRef.numberColumns:
                    raise
            name = "_PKSTRUCTURE__"
            pk = [0]
            numberColumns = 5
            register = [indexName, table, columns, tableRef, columnsRef]
            if not db.fk:
                eval(actionCreator(db.mode, 'createTable', ['database', 'name', 'numberColumns']))
                eval(actionCreator(db.mode, 'alterAddPK', ['database', 'name', 'pk']))
            if eval(actionCreator(db.mode, 'insert', ['database', 'name', 'register'])) != 0:
                raise
            db.fk = True
            _table.fk.append(register)
            self.handler.rootupdate(self.dbs)
            return 0
        except:
            return 1

    def alterTableDropFK(self, database: str, table: str, indexName: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(indexName, str):
                raise
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if not _table:
                return 3
            indexName = [indexName]
            name = "_PKSTRUCTURE__"
            result = eval(actionCreator(db.mode, 'delete', ['database', 'name', 'indexName']))
            if result == 4:
                return 4
            if result != 0:
                raise
            reg = next((x for x in _table.fk if x[0].lower() == indexName[0].lower()), None)
            _table.fk.remove(reg)

            res = eval(actionCreator(db.mode, 'extractTable', ['database', 'name']))
            if res or res == []:
                if len(res) == 0:
                    eval(actionCreator(_table.mode, 'dropTable', ['database', 'name']))
                    db.fk = False
            self.handler.rootupdate(self.dbs)
            return 0
        except:
            return 1

    def alterTableAddUnique(self, database: str, table: str, indexName: str, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or \
                    not isinstance(indexName, str) or not isinstance(columns, list):
                raise
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if not _table:
                return 3
            if len(columns) == 0:
                raise
            for x in columns:
                if x >= _table.numberColumns:
                    return 4
            used = []
            for c in _table.unique:
                for i in c[2]:
                    used.append(i)
            for x in columns:
                if x in used:
                    return 5

            name = "_UNIQUESTRUCTURE__"
            pk = [0]
            numberColumns = 3
            register = [indexName, table, columns]
            if not db.unique:
                eval(actionCreator(db.mode, 'createTable', ['database', 'name', 'numberColumns']))
                eval(actionCreator(db.mode, 'alterAddPK', ['database', 'name', 'pk']))
            if eval(actionCreator(db.mode, 'insert', ['database', 'name', 'register'])) != 0:
                raise
            db.unique = True
            _table.unique.append(register)
            self.handler.rootupdate(self.dbs)
            return 0
        except:
            return 1

    def alterTableDropUnique(self, database: str, table: str, indexName: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(indexName, str):
                raise
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if not _table:
                return 3
            indexName = [indexName]
            name = "_UNIQUESTRUCTURE__"
            result = eval(actionCreator(db.mode, 'delete', ['database', 'name', 'indexName']))
            if result == 4:
                return 4
            elif result != 0:
                raise
            reg = next((x for x in _table.unique if x[0].lower() == indexName[0].lower()), None)
            _table.unique.remove(reg)

            res = eval(actionCreator(db.mode, 'extractTable', ['database', 'name']))
            if res or res == []:
                if len(res) == 0:
                    eval(actionCreator(_table.mode, 'dropTable', ['database', 'name']))
                    db.unique = False
            self.handler.rootupdate(self.dbs)
            return 0
        except:
            return 1

    def alterTableAddIndex(self, database: str, table: str, indexName: str, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(indexName, str) \
                    or not isinstance(columns, list):
                raise
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if not _table:
                return 3
            if len(columns) == 0:
                raise
            for x in columns:
                if x >= _table.numberColumns:
                    return 4
            name = "_INDEXSTRUCTURE__"
            pk = [0]
            numberColumns = 3
            register = [indexName, table, columns]
            if not db.index:
                eval(actionCreator(db.mode, 'createTable', ['database', 'name', 'numberColumns']))
                eval(actionCreator(db.mode, 'alterAddPK', ['database', 'name', 'pk']))
            if eval(actionCreator(db.mode, 'insert', ['database', 'name', 'register'])) != 0:
                raise
            db.index = True
            _table.index.append(register)
            self.handler.rootupdate(self.dbs)
            return 0
        except:
            return 1

    def alterTableDropIndex(self, database: str, table: str, indexName: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(indexName, str):
                raise
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if not _table:
                return 3
            indexName = [indexName]
            name = "_INDEXSTRUCTURE__"
            result = eval(actionCreator(db.mode, 'delete', ['database', 'name', 'indexName']))
            if result == 4:
                return 4
            elif result != 0:
                raise
            reg = next((x for x in _table.index if x[0].lower() == indexName[0].lower()), None)
            _table.index.remove(reg)
            res = eval(actionCreator(db.mode, 'extractTable', ['database', 'name']))
            if res or res == []:
                if len(res) == 0:
                    eval(actionCreator(_table.mode, 'dropTable', ['database', 'name']))
                    db.index = False
            self.handler.rootupdate(self.dbs)
            return 0
        except:
            return 1

    def alterTableCompress(self, database: str, table: str, level: int) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            if level not in [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if level == 0:
                    return 0
                return 4
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if not _table:
                return 3
            if _table.compress:
                raise
            _comp = Compression(level, db.encoding)

            original = eval(actionCreator(_table.mode, 'extractTable', ['database', 'table']))
            if original or original == []:
                if len(original) != 0:
                    if eval(actionCreator(_table.mode, 'truncate', ['database', 'table'])) != 0:
                        raise
                    try:
                        compressContent = _comp.compress(original)
                        file = 'tmp.csv'
                        self.handler.writer('tmp', compressContent)
                        read = eval(actionCreator(_table.mode, 'loadCSV', ['file', 'database', 'table']))
                        self.handler.delete(file)
                        if len(read) == 0:
                            raise Exception()
                    except:
                        eval(actionCreator(_table.mode, 'truncate', ['database', 'table']))
                        file = 'tmp.csv'
                        self.handler.writer('tmp', original)
                        eval(actionCreator(_table.mode, 'loadCSV', ['file', 'database', 'table']))
                        self.handler.delete(file)
                        return 1
            else:
                raise
            _table.compress = _comp
            self.handler.rootupdate(self.dbs)
            return 0
        except:
            return 1

    def alterTableDecompress(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if not _table:
                return 3
            if not _table.compress:
                return 4
            compressContent = eval(actionCreator(_table.mode, 'extractTable', ['database', 'table']))
            if compressContent or compressContent == []:
                if len(compressContent) != 0:
                    if eval(actionCreator(_table.mode, 'truncate', ['database', 'table'])) != 0:
                        raise
                    try:
                        original = _table.compress.decompress(compressContent)
                        file = 'tmp.csv'
                        self.handler.writer('tmp', original)
                        read = eval(actionCreator(_table.mode, 'loadCSV', ['file', 'database', 'table']))
                        self.handler.delete(file)
                        if len(read) == 0:
                            raise Exception()
                    except:
                        eval(actionCreator(_table.mode, 'truncate', ['database', 'table']))
                        file = 'tmp.csv'
                        self.handler.writer('tmp', compressContent)
                        eval(actionCreator(_table.mode, 'loadCSV', ['file', 'database', 'table']))
                        self.handler.delete(file)
                        return 1
            else:
                raise
            _table.compress = None
            self.handler.rootupdate(self.dbs)
            return 0
        except:
            return 1

    def safeModeOn(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    if _table.security:
                        return 4
                    _table.security = Blockchain(database, table)
                    self.handler.rootupdate(self.dbs)
                    return 0
                return 3
            return 2
        except:
            return 1

    def safeModeOff(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise Exception()
            self.dbs = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                _table = next((x for x in tmp.tables if x.name.lower() == table.lower()), None)
                if _table:
                    if not _table.security:
                        return 4
                    _table.security = _table.security.destruction()
                    self.handler.rootupdate(self.dbs)
                    return 0
                return 3
            return 2
        except:
            return 1

    def checksumTable(self, database: str, table: str, mode: str) -> str:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not mode.upper() in algorithms:
                raise Exception()
            self.dbs = self.handler.rootinstance()
            db, index = self._exist(database)
            _table = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if db and _table:
                return checksum_TBL(database, table, _table.mode, mode.upper())
            raise Exception()
        except:
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

    def TBL_Safe(self, database: str) -> list:
        tbl_tmp = []
        self.dbs = self.handler.rootinstance()
        for db in self.dbs:
            if db.name.upper() == database.upper():
                for tbl in db.tables:
                    if tbl.security:
                        tbl_tmp.append(tbl.name)
        return tbl_tmp
