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
        self.tablesName = []

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

                result = 1
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

    def dropAll(self):
        self.handler.reset()
