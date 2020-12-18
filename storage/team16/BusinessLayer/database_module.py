from DataAccessLayer.handler import Handler
from BusinessLayer.table_module import TableModule

class Database:
    def __init__(self, name, tablesName):
        self.name = name
        self.tablesName = tablesName

    def __repr__(self) -> str:
        return str(self.name)


class DatabaseModule:
    def __init__(self):
        self.handler = Handler()
        self.databases = self.handler.leerArchivoDB()

    
    def createDatabase(self, database: str) -> int:
        try:
            self.databases = self.handler.leerArchivoDB()
            for i in self.databases:
                if database == i.name:
                    return  2
            self.databases.append(Database(database,[]))
            self.handler.actualizarArchivoDB(self.databases)
            return 0
        except:
            return 1

    def showDatabases(self) -> list:
        self.databases = self.handler.leerArchivoDB()
        temporal = []
        for i in self.databases:
            temporal.append(i.name)
        print(temporal)
        return temporal

    def alterDatabase(self, databaseOld: str, databaseNew: str) -> int:
        try:
            self.databases = self.handler.leerArchivoDB()
            for i in self.databases:
                if str(databaseNew) == str(i.name):
                    return 3
            for i in self.databases:
                if str(databaseOld) == str(i.name):
                    print(i.tablesName)
                    tables_temp = self.handler.findCoincidences(databaseOld,i.tablesName)
                    i.name = databaseNew
                    for j in tables_temp:
                        avl_temp = self.handler.leerArchivoTB(databaseOld,j)
                        avl_temp.database = databaseNew
                        self.handler.renombrarArchivo(str(j)+'-'+str(databaseOld)+'.tbl',str(j)+'-'+str(databaseNew)+'.tbl')
                    self.handler.actualizarArchivoDB(self.databases)
                    return 0
            return 2
        except:
            return 1

    def dropDatabase(self, database: str) -> int:
        try:
            self.databases = self.handler.leerArchivoDB()
            aux = 0
            for i in range(len(self.databases)):
                if str(database) == str(self.databases[i].name):
                    tables_temp = self.handler.findCoincidences(database,self.databases[i].tablesName)
                    self.databases.pop(i)
                    for j in tables_temp:
                        self.handler.borrarArchivo(str(j)+'-'+str(database)+'.tbl')
                    self.handler.actualizarArchivoDB(self.databases)
                    return 0
                aux +=1
            return 2
        except:
            return 1
