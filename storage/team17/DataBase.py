
class DB():
    def __init__(self):
        self.dicDB = {}
        self.dicTB = {}

    #---------------------FUNCIONES BASES DE DATOS----------------------#

    # CREAR BASE DE DATOS

    def createDatabase(self, database):
        if self.identify(database):
            ready = False
            if self.searchDB(database):
                return 2
            else:
                self.dicDB[database] = self.dicTB
                ready = True
            if ready:
                return 0
            else:
                return 1
        else:
            return 1

    # LISTA DE BASES DE DATOS ALMACENADAS

    def showDatabases(self):
        keys = list()
        for key in self.dicDB:
            keys.append(key)
        print(keys)
        return keys

    # CAMBIAR NOMBRE DE UNA BASE DE DATOS

    def alterDatabase(self, databaseOld, databseNew):
        if self.identify(databaseOld) and self.identify(databseNew):
            ready = False
            if self.searchDB(databaseOld):
                if self.searchDB(databseNew):
                    return 3
                else:
                    tmp = {}
                    for key, value in self.dicDB.items():
                        if key == databaseOld:
                            key = databseNew
                        tmp[key] = value
                    self.dicDB = tmp
                    ready = True
            else:
                return 2
            if ready:
                return 0
            else:
                return 1
        else:
            return 1

    # ELIMINAR BASE DE DATOS

    def dropDatabase(self, database):
        if self.identify(database):
            ready = False
            if self.searchDB(database):
                self.dicDB.pop(database)
                ready = True
            else:
                return 2
            if ready:
                return 0
            else:
                return 1
        else:
            return 1

    # ---------------------FUNCIONES TABLAS----------------------#

    # CREAR TABLA EN UNA DETERMINADA BASE DE DATOS

    def createTable(self, database, table, numberColumns):
        t = Table()
        ready = False
        if self.searchDB(database):
            if self.searchTB(database,table):
                return 3
            else:
                self.dicDB.get(database)[table] = t.create(table, numberColumns)
                ready = True
            if ready:
                return 0
            else:
                return 1
        else:
            return 2
        
    # LISTA DE TABLAS AGREGADAS EN UNA DETERMINADA BASE DE DATOS
    
    def showTables(self, database):
        if self.searchDB(database):
            l = list()
            for key in self.dicDB.get(database).keys():
                l.append(key)
            return l
        else:
            return None
        
    # OBTIENE REGISTROS DE UNA TABLA EN UNA DETERMINADA BASE DE DATOS
    
    def extractTable(self, database, table):
        t = Table()
        if self.searchDB(database):
            if self.searchTB(database, table):
                return self.dicDB.get(database).get(table)
            else:
                return None
        else:
            return None


    #--------------------UTILIDADES--------------------#

    # VALIDA EL NOMBRE CON LAS REGLAS DE IDENTIFICADORES DE SQL

    def identify(self, id):
        special = ["[","@", "_", "o", "#"]
        if id[0].isalpha():
            return True
        else:
            if id[0].isdigit():
                return False
            elif id[0] in special:
                if id[0] != '"' and id[0] != '[':
                    return True
                else:
                    if id[0] == "[":
                        if id[len(id) - 1] == "]":
                            return True
                        else:
                            return False
            else:
                return False

    # BUSCAR SI EXISTE LA BASE DE DATOS

    def searchDB(self, key):
        if key in self.dicDB.keys():
            return True
        else:
            return False
        
    # BUSCAR SI EXISTE LA TABLA EN UNA DETERMINADA BASE DE DATOS

    def searchTB(self, database,table):
        if table in self.dicDB[database]:
            return True
        else:
            return False  
      

