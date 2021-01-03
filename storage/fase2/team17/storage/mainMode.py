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
