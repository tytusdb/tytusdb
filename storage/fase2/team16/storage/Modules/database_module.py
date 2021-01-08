# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from .Complements.checksum import *
from .handler import Handler
from ..path import *
from .table_module import TableModule

modes = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
codes = ['ascii', 'iso-8859-1', 'utf8']


class Database:
    def __init__(self, name, mode, encoding='ascii'):
        self.name = str(name)
        self.mode = mode
        self.encoding = encoding
        self.tables = []
        self.compress = False

    def __repr__(self) -> str:
        return str(self.name)


class DatabaseModule:
    def __init__(self):
        self.handler = Handler()
        self.databases = self.handler.rootinstance()

    def createDatabase(self, database: str, mode: str, encoding: str) -> int:
        try:
            if not isinstance(database, str) or self.handler.invalid(database):
                raise Exception()
            self.databases = self.handler.rootinstance()
            for i in self.databases:
                if database.upper() == i.name.upper():
                    return 2
            if not mode.lower() in modes:
                return 3
            if not encoding.lower() in codes:
                return 4
            self.databases.append(Database(database, mode, encoding))
            self.handler.rootupdate(self.databases)
            return 0
        except:
            return 1

    def showDatabases(self) -> list:
        temporal = []
        self.databases = self.handler.rootinstance()
        for i in self.databases:
            temporal.append(i.name)
        return temporal

    def alterDatabase(self, databaseOld: str, databaseNew: str) -> int:
        try:
            if not isinstance(databaseOld, str) or not isinstance(databaseNew, str) or self.handler.invalid(
                    databaseNew):
                raise Exception()
            index = -1
            self.databases = self.handler.rootinstance()
            for i in self.databases:
                if databaseOld.upper() == i.name.upper():
                    index = self.databases.index(i)
                    tables = [x.name for x in i.tables]
                    break
            if index != -1:
                for i in self.databases:
                    if databaseNew.upper() == i.name.upper():
                        return 3
                for t in tables:
                    self.handler.rename(t.mode, databaseOld + '_' + t.name + '.tbl',
                                        databaseNew + '_' + t.name + '.tbl')
                self.databases[index].name = databaseNew
                self.handler.rootupdate(self.databases)
                return 0
            return 2
        except:
            return 1

    def dropDatabase(self, database: str) -> int:
        try:
            if not isinstance(database, str):
                raise Exception()
            index = -1
            self.databases = self.handler.rootinstance()
            for i in range(len(self.databases)):
                if database.upper() == self.databases[i].name.upper():
                    index = i
                    tables = [x.name for x in self.databases[i].tables]
                    break
            if index != -1:
                for t in tables:
                    self.handler.delete('.data/' + t.mode + '/' + database + '_' + t.name + '.tbl')
                self.databases.pop(index)
                self.handler.rootupdate(self.databases)
                return 0
            return 2
        except:
            return 1

    def alterDatabaseMode(self, database: str, mode: str) -> int:
        try:
            if not isinstance(database, str):
                raise Exception()
            if not mode.lower() in modes:
                return 4
            self.databases = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            if db.mode == mode:
                return 1
            tables = db.tables[:]
            for table in tables:
                tuples = result = eval(actionCreator(table.mode, 'extractTable', ['database', 'table.name']))
                if result or result == []:
                    if eval(actionCreator(mode, 'createTable', ['database', 'table.name', 'table.numberColumns'])) != 0:
                        raise Exception()
                    if len(table.pk) != 0:
                        if eval(actionCreator(mode, 'alterAddPK',
                                              ['database', 'table.name', 'table.pk'])) != 0:
                            raise Exception()
                    if len(result) == 0:
                        continue
                    file = 'tmp.csv'
                    self.handler.writer('tmp', tuples)
                    read = eval(actionCreator(mode, 'loadCSV', ['file', 'database', 'table.name']))
                    self.handler.delete(file)
                    if len(read) == 0:
                        raise Exception()
                else:
                    raise Exception()
            for table in tables:
                self.handler.delete('./data/' + table.mode + "/" + database + "_" + table.name + ".tbl")
            self.handler.clean(self.databases[index].mode)
            self.databases[index].mode = mode
            for x in self.databases[index].tables:
                x.mode = mode
            self.handler.rootupdate(self.databases)
            return 0
        except:
            for table in tables:
                self.handler.delete('./data/' + mode + "/" + database + "_" + table.name + ".tbl")
            return 1

    def alterTableMode(self, database: str, table: str, mode: str) -> int:
        try:
            if not isinstance(database, str):
                raise Exception()
            if not mode.lower() in modes:
                return 4
            self.databases = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            tmp = next((x for x in db.tables if x.name.lower() == table.lower()), None)
            if not tmp:
                return 3
            elif tmp.mode == mode:
                return 1

            tuples = result = eval(actionCreator(tmp.mode, 'extractTable', ['database', 'table']))
            if result or result == []:
                if eval(actionCreator(mode, 'createTable', ['database', 'table', 'tmp.numberColumns'])) != 0:
                    raise Exception()
                if len(tmp.pk) != 0:
                    if eval(actionCreator(mode, 'alterAddPK',
                                          ['database', 'table', 'tmp.pk'])) != 0:
                        raise Exception()
                if len(result) != 0:
                    file = 'tmp.csv'
                    self.handler.writer('tmp', tuples)
                    read = eval(actionCreator(mode, 'loadCSV', ['file', 'database', 'table']))
                    self.handler.delete(file)
                    if len(read) == 0:
                        raise Exception()
            else:
                raise Exception()
            self.handler.delete('./data/' + tmp.mode + "/" + database + "_" + tmp.name + ".tbl")
            self.handler.clean(self.databases[index].mode)
            self.databases[index].tables[self.databases[index].tables.index(tmp)].mode = mode
            self.handler.rootupdate(self.databases)
            return 0
        except:
            self.handler.delete('./data/' + mode + "/" + database + "_" + tmp.name + ".tbl")
            return 1

    def alterDatabaseEncoding(self, database: str, encoding: str) -> int:
        try:
            if not isinstance(database, str):
                raise Exception()
            if not encoding.lower() in codes:
                return 3
            self.databases = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            if encoding == db.encoding:
                return 1
            tables = db.tables[:]
            for table in tables:
                tuples = result = eval(actionCreator(table.mode, 'extractTable', ['database', 'table.name']))
                if result:
                    [str(x).encode(encoding) for x in tuples]
            db.encoding = encoding
            self.handler.rootupdate(self.databases)
            return 0
        except:
            return 1

    def checksumDatabase(self, database: str, mode: str) -> str:
        try:
            if not isinstance(database, str) or not mode.upper() in algorithms:
                raise Exception()
            self.databases = self.handler.rootinstance()
            db, index = self._exist(database)
            if db:
                return checksum_DB(database, db.mode, mode.upper())
            raise Exception()
        except:
            pass

    def alterDatabaseCompress(self, database: str, level: int) -> int:
        try:
            tm = TableModule()
            if level not in [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if level == 0:
                    return 0
                return 4
            if not isinstance(database, str) or self.handler.invalid(database):
                raise Exception()
            self.databases = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                if tmp.compress:
                    return 0
                for tabla in tmp.tables:
                    tm.alterTableCompress(database, tabla.name, level)
                self.databases = self.handler.rootinstance()
                tmp, index = self._exist(database)
                self.databases[index].compress = True
                self.handler.rootupdate(self.databases)
                return 0
            return 2
        except:
            return 1

    def alterDatabaseDecompress(self, database: str) -> int:
        try:
            tm = TableModule()
            if not isinstance(database, str) or self.handler.invalid(database):
                raise Exception()
            self.databases = self.handler.rootinstance()
            tmp, index = self._exist(database)
            if tmp:
                if not tmp.compress:
                    return 0
                for tabla in tmp.tables:
                    tm.alterTableDecompress(database, tabla.name)
                self.databases[index].compress = False
                self.handler.rootupdate(self.databases)
                return 0
            return 2
        except:
            return 1

    def dropAll(self):
        self.handler.reset()

    def _exist(self, database: str):
        tmp = None
        index = -1
        for db in self.databases:
            if db.name.upper() == database.upper():
                index = self.databases.index(db)
                tmp = db
                break
        return tmp, index
