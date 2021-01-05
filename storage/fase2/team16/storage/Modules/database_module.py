# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16

from .handler import Handler
from ..path import *


class Database:
    def __init__(self, name, mode, encoding):
        self.name = str(name)
        self.mode = mode
        self.encoding = encoding
        self.tables = []

    def __repr__(self) -> str:
        return str(self.name)


class DatabaseModule:
    def __init__(self):
        self.handler = Handler()
        self.databases = self.handler.rootinstance()
        self.mode = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
        self.encoding = ['ascii', 'iso-8859-1', 'utf8']

    def createDatabase(self, database: str, mode: str, encoding: str) -> int:
        try:
            if not isinstance(database, str) or self.handler.invalid(database):
                raise
            self.databases = self.handler.rootinstance()
            for i in self.databases:
                if database.upper() == i.name.upper():
                    return 2
            if not mode.lower() in self.mode:
                return 3
            if not encoding.lower() in self.encoding:
                return 4

            mode = mode.lower()
            result = 1
            action = actionCreator(mode, 'createDatabase', ['database'])
            result = eval(action)

            if result == 0:
                self.databases.append(Database(database, mode, encoding))
                self.handler.rootupdate(self.databases)
            return result
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
                raise
            index = -1
            self.databases = self.handler.rootinstance()
            for i in self.databases:
                if databaseOld.upper() == i.name.upper():
                    index = self.databases.index(i)
                    break
            if index != -1:
                for i in self.databases:
                    if databaseNew.upper() == i.name.upper():
                        return 3

                action = actionCreator(self.databases[index].mode, 'alterDatabase', ['databaseOld', 'databaseNew'])
                result = eval(action)

                if result == 0:
                    self.databases[index].name = databaseNew
                    self.handler.rootupdate(self.databases)
                return result
            return 2
        except:
            return 1

    def dropDatabase(self, database: str) -> int:
        try:
            if not isinstance(database, str):
                raise
            index = -1
            self.databases = self.handler.rootinstance()
            for i in range(len(self.databases)):
                if database.upper() == self.databases[i].name.upper():
                    index = i
                    break
            if index != -1:
                result = 1
                action = actionCreator(self.databases[index].mode, 'dropDatabase', ['database'])
                result = eval(action)

                if result == 0:
                    self.databases.pop(index)
                    self.handler.rootupdate(self.databases)
                return 0
            return 2
        except:
            return 1

    def alterDatabaseMode(self, database: str, mode: str) -> int:
        try:
            if not isinstance(database, str):
                raise
            if not mode.lower() in self.mode:
                return 4
            self.databases = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            result = eval(actionCreator(mode, 'createDatabase', ['database']))
            if result != 0:
                raise

            tables = db.tables[:]
            for table in tables:
                tuples = result = eval(actionCreator(table.mode, 'extractTable', ['database', 'table.name']))
                if result:
                    if eval(actionCreator(mode, 'createTable', ['database', 'table.name', 'table.numberColumns'])) != 0:
                        raise
                    if len(table.pk) != 0:
                        if eval(actionCreator(mode, 'alterAddPK',
                                              ['database', 'table.name', 'table.pk'])) != 0:
                            raise
                    if len(result) == 0:
                        continue
                    file = 'tmp.csv'
                    self.handler.writer('tmp', tuples)
                    read = eval(actionCreator(mode, 'loadCSV', ['file', 'database', 'table.name']))
                    if len(read) == 0:
                        raise
                    self.handler.delete(file)
                else:
                    raise
            eval(actionCreator(db.mode, 'dropDatabase', ['database']))
            self.databases[index].mode = mode
            for x in self.databases[index].tables:
                x.mode = mode
            self.handler.rootupdate(self.databases)
            return 0
        except:
            eval(actionCreator(mode, 'dropDatabase', ['database']))
            return 1

    def alterTableMode(self, database: str, table: str, mode: str) -> int:
        try:
            if not isinstance(database, str):
                raise
            if not mode.lower() in self.mode:
                return 4
            self.databases = self.handler.rootinstance()
            db, index = self._exist(database)
            if not db:
                return 2
            tmp = next(x for x in db.tables if x.name.lower() == table.lower())
            if not tmp:
                return 3
            elif tmp.mode == mode:
                raise
            if eval(actionCreator(mode, 'createDatabase', ['database'])) != 0:
                raise

            tuples = result = eval(actionCreator(tmp.mode, 'extractTable', ['database', 'table']))
            if result:
                if eval(actionCreator(mode, 'createTable', ['database', 'table', 'tmp.numberColumns'])) != 0:
                    raise
                if len(tmp.pk) != 0:
                    if eval(actionCreator(mode, 'alterAddPK',
                                          ['database', 'table', 'tmp.pk'])) != 0:
                        raise
                if len(result) != 0:
                    file = 'tmp.csv'
                    self.handler.writer('tmp', tuples)
                    read = eval(actionCreator(mode, 'loadCSV', ['file', 'database', 'table']))
                    self.handler.delete(file)
                    if len(read) == 0:
                        raise
            else:
                raise
            previous = tmp.mode
            self.databases[index].tables[self.databases[index].tables.index(tmp)].mode = mode
            if not next((x for x in db.tables if x.mode.lower() == previous.lower()), None):
                eval(actionCreator(previous, 'dropDatabase', ['database']))
            else:
                eval(actionCreator(previous, 'dropTable', ['database', 'table']))
            self.handler.rootupdate(self.databases)
            return 0
        except:
            eval(actionCreator(mode, 'dropDatabase', ['database']))
            return 1

    def alterDatabaseEncoding(self, database: str, encoding: str) -> int:
        pass

    def alterDatabaseCompress(self, database: str, level: int) -> int:
        pass

    def alterDatabaseDecompress(self, atabase: str) -> int:
        pass

    def dropAll(self):
        self.handler.reset()
        hash.__init2__()

    def _exist(self, database: str):
        tmp = None
        index = -1
        for db in self.databases:
            if db.name.upper() == database.upper():
                index = self.databases.index(db)
                tmp = db
                break
        return tmp, index
