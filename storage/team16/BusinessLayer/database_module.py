import pickle
import os

class Database:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return str(self.name)


class DatabaseModule:
    def __init__(self):
        self.databases = self.leerArchivoDB()

    
    def createDatabase(self, database):
        try:
            for i in self.databases:
                if database == i.name:
                    return  2
            self.databases.append(Database(database))
            self.databases = self.crearArchivoDB(self.databases)
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
                    self.databases = self.crearArchivoDB(self.databases)
                    return 0
            return 2
        except:
            return 1

    def dropDatabase(self, db):
        try:
            for i in range(len(self.databases)):
                if str(db) == str(self.databases[i].name):
                    self.databases.pop(i)
                    self.databases = self.crearArchivoDB(self.databases)
                    return 0
            return 2
        except:
            return 1
            
    
    @staticmethod
    def crearArchivoDB(databases):
        f = open('databases','wb')
        pickle.dump(databases, f)
        return databases
    
    @staticmethod
    def leerArchivoDB() -> list:
        try:
            if os.path.getsize('databases') > 0:
                with open('databases', 'rb') as f:
                    return pickle.load(f)
            return []
        except:
            f = open("databases",'wb')
            f.close()
