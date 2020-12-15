from DataAccessLayer.handler import Handler


class Database:
    def __init__(self, name):
        self.name = str(name)
        self.tables = []

    def __repr__(self) -> str:
        return str(self.name)


class DatabaseModule:
    def __init__(self):
        self.handler = Handler()
        self.databases = self.handler.rootInstance()

    def createDatabase(self, database):
        try:
            for element in self.databases:
                if database == element.name:
                    return 2
            self.databases.append(Database(database))
            self.handler.rootUpdate(self.databases)
            return 0
        except:
            return 1

    def showDatabases(self):
        tmp = []
        for database in self.databases:
            tmp.append(database.name)
        return tmp

    def alterDatabase(self, old, new):
        try:
            index = -1
            for database in self.databases:
                if str(new) == database.name:
                    return 3

            for database in self.databases:
                if str(old) == database.name:
                    index = self.databases.index(database)
                    break
            if index != -1:
                self.databases[index].name = new
                self.handler.rootUpdate(self.databases)
                return 0
            return 2
        except:
            return 1

    def dropDatabase(self, database):
        try:
            for i in range(len(self.databases)):
                if str(database) == self.databases[i].name:
                    self.databases.pop(i)
                    self.handler.rootUpdate(self.databases)
                    return 0
            return 2
        except:
            return 1
