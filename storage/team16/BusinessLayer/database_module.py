class Database:
    def __init__(self, mode, name):
        self.mode = mode
        self.name = name


class DatabaseModule:
    def __init__(self):
        self.databases = []

    def createDatabase(self, mode, database):
        for i in self.databases:
            if database == i.name:
                return
        self.databases.append(Database(mode, database))

    def showDatabases(self):
        temporal = []
        for i in self.databases:
            temporal.append(i.name)
        return temporal

    def alterDatabase(self, old, new):
        for i in self.databases:
            if str(old) == str(i.name):
                i.name = new

    def dropDatabase(self, db):
        for i in range(len(self.databases)):
            if str(db) == str(self.databases[i].name):
                self.databases.pop(i)
                return

    def im(self):
        for i in self.databases:
            print("Nombre: " + str(i.name) + ", Modo: " + str(i.mode))
