
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

    # ---------------------EXTRAS----------------------#

    # CREAR Y AÑADIR UNA TABLA

    def addTable(self, key, name, content):
        if self.searchDB(key):
            if self.dicDB.get(key):
                if self.searchTB(key, name):
                    print("Ya existe una tabla con ese nombre")
                else:
                    dict2 = self.dicDB.get(key)
                    dict2[name] = content
                    self.dicDB[key] = dict2
            else:
                self.dicDB[key] = {name:content}
        else:
            print("No existe la base de datos")

    # BUSCAR SI EXISTE LA TABLA EN UNA BASE DE DATOS

    def searchTB(self, key, name):
        if name in self.dicDB.get(key).keys():
            return True
        else:
            False

    # ELIMINAR TABLA DE UNA BASE DE DATOS

    def deleteTB(self, key, name):
        self.dicDB.get(key).pop(name)

    # MOSTRAR BASES DE DATOS ALMACENADAS

    def print(self):
        n = 0
        for key in self.dicDB:
            print("[" + str(n) + "]","Base:", key, "| Tablas:", self.dicDB.get(key))
            n +=1

    # MOSTRAR TABLAS ALMACENDAS

    def print(self):
        n = 0
        for key in self.dicDB.keys():
            print(key + ":")
            for i in self.dicDB.get(key).keys():
                print("  "+i + ":")
                for j in self.dicDB.get(key).get(i).keys():
                    print("    "+j+":")
                    for k in self.dicDB.get(key).get(i).get(j):
                        print("     "+str(k))

