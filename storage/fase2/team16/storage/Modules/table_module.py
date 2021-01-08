# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from ..path import *
from .handler import Handler
from .Complements.checksum import *
from .Complements.security import Blockchain
import zlib as zl
from .tuple_module import TupleModule


class Table:
    def __init__(self, name: str, mode: str, numberColumns: int):
        self.name = name
        self.mode = mode
        self.numberColumns = numberColumns
        self.pk = []
        self.security = None
        self.compress = False


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
                    return eval(action)
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
                    action = actionCreator(_table.mode, 'extractRangeTable',
                                           ['database', 'table', 'columnNumber', 'lower', 'upper'])
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
                    action = actionCreator(_table.mode, 'alterAddPK', ['database', 'table', 'columns'])
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
                    action = actionCreator(_table.mode, 'alterAddColumn', ['database', 'table', 'default'])
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
        try:
            tp = TupleModule()
            actualTable = None
            mode = ""
            if level not in [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if level == 0:
                    return 0
                return 4
            if not isinstance(database, str) or self.handler.invalid(database):
                raise Exception()
            self.databases = self.handler.rootinstance()
            for i in self.databases:
                if database.upper() == i.name.upper():
                    mode = i.mode
                    for tabla in i.tables:
                        if tabla.name == table:
                            if tabla.compress:
                                return 0
                            actualTable = tabla
                            break
                    break

            if actualTable != None:
                original_content = self.extractTable(database, table)
                tp.truncate(database, table)
                compressContent = self._compress(original_content, level)
                try:
                    for tupla in compressContent:
                        tp.insert(database, table, tupla)
                    databases = self.handler.rootinstance()
                    for base in databases:
                        if database.upper() == base.name.upper():
                            for tabla in base.tables:
                                if tabla.name == table:
                                    tabla.compress = True
                                    # falta guardar el estado de la tabla
                                    #self.handler.tableupdate(mode, database, table, actualTable)
                                    break
                            break
                    return 0
                except:
                    for tupla in original_content:
                        tp.insert(database, table, tupla)
                    return 1
            return 2
        except:
            return 1

    def alterTableDecompress(self, database: str, table: str) -> int:
        try:
            tp = TupleModule()
            actualTable = None
            mode = ""
            if not isinstance(database, str) or self.handler.invalid(database):
                raise Exception()
            self.databases = self.handler.rootinstance()
            for i in self.databases:
                if database.upper() == i.name.upper():
                    mode = i.mode
                    for tabla in i.tables:
                        if tabla.name == table:
                            if tabla.compress is False:
                                return 0
                            actualTable = tabla
                            break
                    break

            if actualTable != None:
                original_content = self.extractTable(database, table)
                tp.truncate(database, table)
                decompressContent = self._decompress(original_content)
                try:
                    for tupla in decompressContent:
                        tp.insert(database, table, tupla)
                    databases = self.handler.rootinstance()
                    for base in databases:
                        if database.upper() == base.name.upper():
                            for tabla in base.tables:
                                if tabla.name == table:
                                    tabla.compress = True
                                    # falta guardar el estado de la tabla
                                    # self.handler.tableupdate(mode, database, table, actualTable)
                                    break
                            break
                    return 0
                except:
                    for tupla in original_content:
                        tp.insert(database, table, tupla)
                    return 1
            return 2
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

    def _compress(self, content, level):
        result = []
        for tupla in content:
            aux = []
            for columna in tupla:
                try:
                    val = int(columna)
                except:
                    try:
                        columna = zl.compress(columna.encode(), level)
                    except:
                        continue
                finally:
                    aux.append(columna)
            result.append(aux)

        return result

    def _decompress(self, content):
        result = []
        for tupla in content:
            aux = []
            for columna in tupla:
                try:
                    val = int(columna)
                except:
                    try:
                        columna = zl.decompress(columna).decode()
                    except:
                        continue
                finally:
                    aux.append(columna)
            result.append(aux)

        return result
