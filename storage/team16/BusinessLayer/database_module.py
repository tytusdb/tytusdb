class Database:
    def __init__(self, name):
        self.name = name


class DatabaseModule:
    def __init__(self):
        self.databases = []

    def createDatabase(self, database):
        try:
            for i in self.databases:
                if database == i.name:
                    return  2
            self.databases.append(Database(database))
            return 0
        except:
            return 1
        

    def showDatabases(self):
        temporal = []
        for i in self.databases:
            temporal.append(i.name)
        return temporal

    def alterDatabase(self, old, new):
        try:
            for i in self.databases:
                if str(new) == str(i.name):
                    return 3
                if str(old) == str(i.name):
                    i.name = new
                    return 0
            return 2
        except:
            return 1

    def dropDatabase(self, db):
        try:
            for i in range(len(self.databases)):
                if str(db) == str(self.databases[i].name):
                    self.databases.pop(i)
                    return 0
            return 2
        except:
            return 1
            

    def im(self):
        for i in self.databases:
            print("Nombre: " + str(i.name))
