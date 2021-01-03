import switchMode as switch

class main():
    def __init__(self):
        #self.godGuide2 = {}
        self.godGuide = {'avl': {}, 'b': {}, 'bplus': {}, 'dict': {}, 'isam': {}, 'json': {}, 'hash': {}}
        self.guiaModos = {}
        self.DB = {}
        self.listMode = ['avl', 'hash', 'b', 'bplus', 'dict', 'isam', 'json']
        self.listEncoding = ['ascii', 'iso-8859-1', 'utf8']
        
    #---------------------FUNCIONES BASES DE DATOS (NUEVAS)----------------------#

    # CREAR BASE DE DATOS

    def createDatabase(self, database, mode, encoding):
        if self.identify(str(database)):
            if self.verifyMode(mode):
                if not self.searchDB2(database):
                    if self.verifyEncoding(encoding):
                        try:
                            self.godGuide[mode][database] = [{}, encoding]
                            self.guiaModos[database] = mode
                            switch.switchMode(mode).createDatabase(database)
                            return 0
                        except:
                            return 1
                    return 4
                return 2
            return 3
        return 1
    
    # CAMBIA EL MODO DE UNA TABLA
    
    def alterTableMode(self, database, table, mode):
        if self.identify(str(database)):
            if self.verifyMode(mode):
                if self.searchDB2(database):
                    if self.searchTB(database, table):
                        try:
                            if database in switch.switchMode(mode).showDatabases():
                                if table not in switch.switchMode(mode).showTables(database):
                                    for i in self.listMode:
                                        if database in self.godGuide[i].keys():
                                            if table in self.godGuide[i][database][0].keys():
                                                lis = self.godGuide[i][database][0].pop(table)
                                    self.godGuide[mode][database][0][table] = lis
                                    tabla = self.extTB(database, table)
                                    self.delTB(database, table)
                                    switch.switchMode(mode).createTable(database, table, lis[0])
                                    for i in tabla:
                                        switch.switchMode(mode).insert(database, table, i)
                                else:
                                    return 1
                            else:
                                for i in self.listMode:
                                    if database in self.godGuide[i].keys():
                                        if table in self.godGuide[i][database][0].keys():
                                            encoding = self.godGuide[i][database][1]
                                            lis = self.godGuide[i][database][0].pop(table)
                                self.godGuide[mode][database] = [{}, encoding]
                                self.godGuide[mode][database][0][table] = lis

                                #self.createDatabase(database, mode, encoding)
                                switch.switchMode(mode).createDatabase(database)
                                tabla = self.extTB(database, table)
                                self.delTB(database, table)
                                switch.switchMode(mode).createTable(database, table, lis[0])
                                for i in tabla:
                                    switch.switchMode(mode).insert(database, table, i)
                            return 0
                        except:
                            return 1
                    return 3
                return 2
            return 4
        return 1

    # CAMBIA EL MODO DE UNA BASE DE DATOS
    
    def alterDatabaseMode(self, database, mode):
        if self.identify(str(database)):
            if self.verifyMode(mode):
                if self.searchDB2(database):
                    try:
                        for i in self.listMode:
                            if i != mode:
                                if database in switch.switchMode(i).showDatabases():
                                    if len(switch.switchMode(i).showTables(database)) == 0:
                                        modoA = i
                                        lis = self.godGuide[modoA].pop(database)
                                        self.guiaModos[database] = mode
                                        self.godGuide[mode][database] = lis
                                        #self.createDatabase(database, mode, lis[1])
                                        switch.switchMode(mode).createDatabase(database)
                                    else:
                                        modoA = i
                                        self.guiaModos[database] = mode
                                        for j in switch.switchMode(i).showTables(database):
                                            self.alterTableMode(database, j, mode)
                                        self.godGuide[modoA].pop(database)
                                        #self.godGuide[mode][database] = lis
                                    switch.switchMode(i).dropDatabase(database)
                        return 0
                    except:
                        return 1
                return 2
            return 4
        return 1
    #---------------------FUNCIONES BASES DE DATOS (ANTERIORES)----------------------#

    # LISTA DE BASES DE DATOS ALMACENADAS

    def showDatabases(self):
        re = []
        for i in self.listMode:
            re = re + switch.switchMode(i).showDatabases()
        return re

    # CAMBIAR NOMBRE DE UNA BASE DE DATOS

    def alterDatabase(self, databaseOld, databaseNew):
        re = 1
        for i in self.listMode:
            if self.searchDB(databaseOld, i):
                for i in self.listMode:
                    if not self.searchDB2(databaseNew):                        
                        re = switch.switchMode(i).alterDatabase(databaseOld, databaseNew)
        if re == 0:

            ward = self.guiaModos.pop(databaseOld)
            self.guiaModos[databaseNew] = ward

            for i in self.listMode:
                if databaseOld in self.godGuide[i].keys():
                    ward = self.godGuide[i].pop(databaseOld)
                    self.godGuide[i][databaseNew] = ward
        return re

    # ELIMINAR BASE DE DATOS

    def dropDatabase(self, database):
        re = 1
        for i in self.listMode:
            if self.searchDB(database, i):
                re = switch.switchMode(i).dropDatabase(database)
        if re == 0:
            self.guiaModos.pop(database)
            for i in self.listMode:
                if database in self.godGuide[i].keys():
                    self.godGuide[i].pop(database)
        return re
        
    # -------------------------UTILIDADES-------------------------#

    def identify(self, id):
        id = str(id)
        if id[0].isalpha():
            return True
        else:
            if id[0].isdigit():
                return False
        return False
    
    def verifyMode(self, mode):
        if mode in self.listMode:
            return True
        return False

    def verifyEncoding(self, encoding):
        if encoding in self.listEncoding:
            return True
        return False

    def searchDB(self, key, mode):
        if key in switch.switchMode(mode).showDatabases():
            return True
        return False
    
    def searchDB2(self, key):
        for i in self.listMode:
            if key in switch.switchMode(i).showDatabases():
                return True
        return False
