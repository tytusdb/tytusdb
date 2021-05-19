# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from storage.AVL.DataAccessLayer.handler import Handler


class Database:
    def __init__(self, name):
        self.name = str(name)
        self.tablesName = []

    def __repr__(self) -> str:
        return str(self.name)


class DatabaseModule:
    def __init__(self):
        self.handler = Handler()
        self.databases = self.handler.rootinstance()

    def createDatabase(self, database: str) -> int:
        try:
            if not isinstance(database, str) or self.handler.invalid(database):
                raise
            self.databases = self.handler.rootinstance()
            for i in self.databases:
                if database.upper() == i.name.upper():
                    return 2
            self.databases.append(Database(database))
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
                raise
            index = -1
            self.databases = self.handler.rootinstance()
            for i in self.databases:
                if databaseOld.upper() == i.name.upper():
                    index = self.databases.index(i)
                    tables_temp = self.handler.findCoincidences(
                        databaseOld, i.tablesName)
                    break
            if index != -1:
                for i in self.databases:
                    if databaseNew.upper() == i.name.upper():
                        return 3
                for j in tables_temp:
                    avl_temp = self.handler.tableinstance(databaseOld, j)
                    avl_temp.database = databaseNew
                    self.handler.rename(databaseOld + '_' + j + '.tbl',
                                        databaseNew + '_' + j + '.tbl')
                    self.handler.tableupdate(avl_temp)
                self.databases[index].name = databaseNew
                self.handler.rootupdate(self.databases)
                return 0
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
                    tables_temp = self.handler.findCoincidences(
                        database, self.databases[i].tablesName)
                    break
            if index != -1:
                for j in tables_temp:
                    self.handler.delete(database + '_' + j + '.tbl')
                self.databases.pop(index)
                self.handler.rootupdate(self.databases)
                return 0
            return 2
        except:
            return 1

    def dropAll(self):
        self.handler.reset()
