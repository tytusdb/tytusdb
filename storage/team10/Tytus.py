from DataBase import Database
from Hash import TablaHash

class Tytus:
    def __init__(self):
        self.databases = []

    """
    @return
        0 operación exitosa
        1 error en la operación 
        2 base de datos existente
    """
    def createDatabase(self, nameDB):
        try:
            if self.buscarDB(nameDB) != None:
                print("Base de datos existente")
                return 2
            else:
                self.databases.append(Database(nameDB))
                # print("Operación exitosa")
                return 0
        except: 
            print("Error en la operación")
            return 1

    """
    @return 
        una lista de nombres de la base de datos
    """
    def showDatabases(self):
        listNamesDB = []
        for db in self.databases:
            if db != None:
                listNamesDB.append(db.getName())
        return listNamesDB

    """
    @return 
        0 operación exitosa
        1 Error en la operación
        2 databaseOld no existente
        3 databaseNew existente
    """
    def alterDatabase(self, databaseOld, databaseNew):
        try:
            banderaDB = self.buscarDB(databaseOld)
            if banderaDB != None:
                if self.buscarDB(databaseNew) != None:
                    print("databaseNew existente")
                    return 3
                else:
                    self.databases[banderaDB].setName(databaseNew)
                    # print("operación exitosa")
                    return 0
            else:
                print("dtabaseOld no existente")
                return 2
        except Exception as e:
            print("Error de la operación")
            print(e)
            return 1

    """
    @return
        0 Operación exitosa
        1 Error en la operación
        2 Base de datos no existente
    """
    def dropDatabase(self, nameDB):
        try:
            banderaDB = self.buscarDB(nameDB)
            if banderaDB != None:
                self.databases.pop(banderaDB)
            else:
                print("Base de datos no existente")
                return 2
        except:
            print("Error en la operación")
            return 1

    """
    prototype method
    """
    def buscarDB(self, name):
        if len(self.databases) != 0:
            for db in self.databases:
                if name == db.getName():
                    #econtrada
                    return self.databases.index(db)
            return None

    def createTable(self, database, table, nCols):
        try:
            flagDB = self.buscarDB(database)
            if flagDB != None:
                db = self.databases[flagDB]
                db.createTable(10, table, nCols)
            else:
                print("Base de datos no existente")
                return 2
        except:
            print("Error en operacion")
            return 1

    def dropTable(self, database, table):
        try:
            indiceDB = self.buscarDB(database)
            if indiceDB != None:
                indiceTabla = self.databases[indiceDB].buscarTable(table)
                if indiceTabla != None:
                    # exito 0, o error 1
                    return self.databases[indiceDB].dropTable(indiceTabla)
                else:
                    print("Table no existe")
                    return 3
            else:
                print("Database no existe") 
                return 2
        except:
            print("Error en la operación")
            return 1

    def showTables(self, database):
        tables = []
        for db in self.databases:
            if db.name == database:
                tables = db.showTables()
                break
            else:
                pass            ##16/12/2020 Cristian
        if tables==[]:
            return None        
        return tables

    def alterAddPK(self, database, table, columns):
        try:
            flagDB = self.buscarDB(database)
            if flagDB != None:
                db = self.databases[flagDB]
                db.alterAddPK(table, columns)
            else:
                print("Base de datos no existente")
                return 2
        except:
            print("Error en operacion")
            return 1

    def insert(self, database, table, register):
        try:
            flagDB = self.buscarDB(database)
            if flagDB != None:
                db = self.databases[flagDB]
                db.insert(table, register)
            else:
                print("Base de datos no existente")
                return 2
        except:
            print("Error en operacion")
            return 1

    """
    loadCSV()
    @return
        0 Operación exitosa
        1 Error en la operación
        2 Database no existente
        3 Tabla no existe
        4 Llave primaria duplicada
        5 Columnas fuera de límites
    """
    def loadCSV(self, fileCSV, db, table,):
        try:
            import csv
            #verifica que la base de datos exista
            indiceDB = self.buscarDB(db)
            if indiceDB != None:
                #verifica que la tabla exista en la base de datos
                indiceTabla = self.databases[indiceDB].buscarTable(table)
                if  indiceTabla != None:
                    #aquie va lo de la llave primaria y las columnas
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$")
                    tb = self.databases[indiceDB].getTable(indiceTabla).getName()
                    print(tb)
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$")
                    #-------------------leee el csv
                    with open(fileCSV, 'r') as fileCsv:
                        lector = csv.reader(fileCsv, delimiter = ',')
                        for f in lector:
                            print(f)
                    #-------------------termina leer csv
                else:
                    print("Tabla no existe")
                    return 3
            else:
                print("Database no existente")  
                return 2
        except Exception as e:
            print(e)

            print("Error en la operación")
            return 1

    ##16/12/2020 CRISTIAN
    def extractTable(self,database,table):
        try:
            flagDB = self.buscarDB(database)
            if flagDB != None:
                db = self.databases[flagDB]
                return db.extractTable2(table)
            else:
                print("Base de datos no existente")
                return 2
        except:
            print("Error en la operacion")
            return 1      

    def extractRangeTable(self,database,table,columnNumber,lower,upper):
        try:
            flagDB = self.buscarDB(database)
            if flagDB != None:
                db = self.databases[flagDB]
                return db.extractRangeTable2(table,columnNumber,lower,upper) ##Cambiar esto
            else:
                print("Base de datos no existente")
                return 2
        except:
            print("Error en la operacion")
            return 1     
