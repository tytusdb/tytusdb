# File:     DataBase
# License:  Released under MIT License
# Notice:   Copyright (c) 2020 TytusDB Team

from . import Estructura_ArbolB as bt
from . import Serializable as serializar
import csv

class DB():
    def __init__(self):
        self.dicDB = {}
        self.dicTB = {}
        self.cont = 0
        self.grade = 5

    #---------------------FUNCIONES BASES DE DATOS----------------------#

    # CREAR BASE DE DATOS

    def createDatabase(self, database):
        if self.identify(str(database)):
            if self.searchDB(database):
                return 2
            else:
                try:
                    self.dicDB[database] = {}
                    return 0
                except:
                    return 1
        return 1

    # LISTA DE BASES DE DATOS ALMACENADAS

    def showDatabases(self):
        keys = list()
        for key in self.dicDB:
            keys.append(key)
        return keys

    # CAMBIAR NOMBRE DE UNA BASE DE DATOS

    def alterDatabase(self, databaseOld, databaseNew):
        if self.identify(databaseOld) and self.identify(databaseNew):
            if self.searchDB(databaseOld):
                if self.searchDB(databaseNew):
                    return 3
                else:
                    try:
                        tmp = {}
                        for key, value in self.dicDB.items():
                            if key.lower() == databaseOld.lower():
                                key = databaseNew
                            tmp[key] = value
                        self.dicDB = tmp
                        return 0
                    except:
                        return 1
            return 2
        return 1

    # ELIMINAR BASE DE DATOS

    def dropDatabase(self, database):
        if self.identify(database):
            if self.searchDB(database):
                try:
                    self.dicDB.pop(database)
                    return 0
                except:
                    return 1
            return 2
        return 1

    # ---------------------FUNCIONES TABLAS----------------------#

    # CREAR TABLA EN UNA DETERMINADA BASE DE DATOS

    def createTable(self, database, table, numberColumns):
        if self.identify(database) and self.identify(table):
            if self.searchDB(database):
                if self.searchTB(database, table):
                    return 3
                else:
                    if self.identify(table):
                        try:
                            self.dicDB.get(database)[table] = [bt.arbolB(self.grade), int(numberColumns), None]
                            return 0
                        except:
                            return 1
                    return 1
            return 2
        return 1

    # LISTA DE TABLAS AGREGADAS A UNA BASE DE DATOS

    def showTables(self, database):
        if self.searchDB(database):
            l = list()
            for key in self.dicDB.get(database).keys():
                l.append(key)
            return l
        else:
            return None

    # LISTA DE REGISTROS DE UNA TABLA EN UN BASE DE DATOS

    def extractTable(self, database, table):
        if self.searchDB(database):
            if self.searchTB(database, table):
                return self.dicDB[database][table][0].registros()
            return None
        return None

    #LISTA REGISTROS EN UN RANGO DE UNA TABLA

    def extractRangeTable(self, database, table, columnNumber, lower, upper):
        try:
            if self.searchDB(database):
                if self.searchTB(database, table):
                    if len(self.dicDB[database][table][0].registros()) != 0:
                        if columnNumber >= 0 and columnNumber < self.dicDB[database][table][1]:
                            registros = list()
                            for tupla in self.extractTable(database, table):
                                if str(tupla[columnNumber]).isdigit() and str(lower).isdigit() and str(upper).isdigit():
                                    if int(tupla[columnNumber]) >= int(lower) and int(tupla[columnNumber]) <= int(upper):
                                        registros.append(tupla)
                                elif str(tupla[columnNumber]) >= str(lower) and str(tupla[columnNumber]) <= str(upper):
                                    registros.append(tupla)
                            return registros
                        return 3
                    return []
                return 2
            return 1
        except:
            return 0

    # AGREGAR LISTA DE LLAVES PRIMARIAS A UNA TABLA

    def alterAddPK(self, database, table, columns):
        try:
            for i in columns:
                int(i)
            table.lower()
        except:
            return 1
        if self.searchDB(database):
            if self.searchTB(database, table):
                try:
                    range = True
                    for i in columns:
                        if range:
                            if i >= self.dicDB[database][table][1]:
                                range = False
                    if range:
                        if not self.dicDB[database][table][2]:
                            if self.verifyPk(database, table, columns):
                                self.dicDB[database][table][2] = columns
                                self.updateTree(database, table)
                                serializar.commit(self.dicDB[database][table][0], database+"-"+table+"-B")
                                return 0
                            return 4
                        return 4
                    return 5
                except:
                    return 1
            return 3
        return 2

    # ELIMINAR LAS LLAVES PRIMARIAS DE UNA TABLA

    def alterDropPK(self, database, table):
        try:
            if self.searchDB(database):
                if self.searchTB(database,table):
                    if self.dicDB[database][table][2]:
                        self.dicDB[database][table][2] = None
                        return 0
                    return 4
                return 3
            return 2
        except:
            return 1

    # CAMBIAR EL NOMBRE DE UNA TABLA

    def alterTable(self, database, tableOld, tableNew):
        if self.identify(database) and self.identify(tableOld) and self.identify(tableNew):
            if self.searchDB(database):
                if self.searchTB(database, tableOld):
                    if not self.searchTB(database, tableNew):
                        try:
                            tmp = {}
                            for key, value in self.dicDB[database].items():
                                if key.lower() == tableOld.lower():
                                    key = tableNew
                                tmp[key] = value
                            self.dicDB[database] = tmp
                            return 0
                        except:
                            return 1
                    return 4
                return 3
            return 2
        return 1

    # AGREGAR UN NUEVO REGISTRO A LAS TABLAS EXISTENTES

    def alterAddColumn(self, database,  table, default):
        if self.identify(database) and self.identify(table):
            if self.searchDB(database):
                if self.searchTB(database, table):
                    try:
                        self.dicDB[database][table][1] += 1
                        self.dicDB[database][table][0].agregarValor(default)
                        serializar.commit(self.dicDB[database][table][0], database+"-"+table+"-B")
                        return 0
                    except:
                        return 1
                return 3
            return 2
        return 1

    # ELIMINAR UNA COLUMNA ESPECIFICA DE UNA TABLA

    def alterDropColumn(self, database, table, columnNumber):
        if self.searchDB(database):
            if self.searchTB(database, table):
                if columnNumber >= 0 and columnNumber < self.dicDB[database][table][1]:
                    if self.dicDB[database][table][1] > 1:
                        try:
                            columnNumber = int(columnNumber)
                            if self.dicDB[database][table][2] != None:
                                if columnNumber not in self.dicDB[database][table][2]:
                                    self.dicDB[database][table][1] -= 1
                                    self.dicDB[database][table][0].eliminarValor(columnNumber)
                                    pk = []
                                    for i in self.dicDB[database][table][2]:
                                        if i < columnNumber:
                                            pk.append(i)
                                        else:
                                            pk.append(i-1)
                                    self.dicDB[database][table][2] = pk
                                    serializar.commit(self.dicDB[database][table][0], database+"-"+table+"-B")
                                    return 0
                                return 4
                            else:
                                self.dicDB[database][table][1] -= 1
                                self.dicDB[database][table][0].eliminarValor(columnNumber)
                                serializar.commit(self.dicDB[database][table][0], database+"-"+table+"-B")
                                return 0
                        except:
                            return 1
                    return 4
                return 5
            return 3
        return 2

    # ELIMINAR UNA TABLA DE LA BASE DE DATOS

    def dropTable(self, database, table):
        try:
            if self.searchDB(database):
                if self.searchTB(database, table):
                    try:
                        self.dicDB[database].pop(table)
                        return 0
                    except:
                        return 1
                return 3
            return 2
        except:
            return 1

    # ---------------------FUNCIONES TUPLAS----------------------#

    # AÑADIR REGISTROS A UNA TABLA

    def insert(self, database, table, register):
        try:
            database.lower()
            table.lower()
            x = register[0]
        except:
            return 1
        if self.searchDB(database):
            if self.searchTB(database, table):
                if self.dicDB[database][table][1] == len(register):
                    try:
                        register[0] = register[0]
                        if not self.dicDB[database][table][2]:
                            while self.cont in self.dicDB[database][table][0].Keys():
                                self.cont += 1
                            self.dicDB[database][table][0].insertar([self.cont, register])
                            self.cont += 1
                            return 0
                        else:
                            pk = ""
                            for j in self.dicDB[database][table][2]:
                                pk += str(register[j]) + "_"
                            pk = pk[:-1]
                            if pk not in self.dicDB[database][table][0].Keys():
                                self.dicDB[database][table][0].insertar([pk, register])
                                return 0
                            return 4
                    except:
                        return 1
                else:
                    return 5
            else:
                return 3
        else:
            return 2

    # CARGA DE REGISTROS MEDIANTE UN CSV

    def loadCSV(self, file, database, table, tipado):
        try:
            tmp = list()
            with open(file, 'r', encoding='utf-8-sig') as file:
                reader = csv.reader(file, delimiter = ',')
                j = 0
                for row in reader:
                    if tipado:
                        i=0
                        for x in row:
                            if tipado[j][i] == bool:
                                if x == 'False':
                                    row[i] = bool(1)
                                else:
                                    row[i] = bool(0)
                            else:
                                row[i] = tipado[j][i](x)
                            i=i+1
                        j+=1
                    tmp.append(self.insert(database,table, row))
                return tmp
        except:
            return []

    # REGISTRO SEGUN LLAVE PRIMARIA

    def extractRow(self, database, table, columns):
        try:
            pk = ""
            for i in columns:
                pk += str(i) + "_"
            pk = pk[:-1]
            pk = pk.replace('[','')
            pk = pk.replace(']', '')
            for i in self.dicDB[database][table][0].Keys():
                if pk == str(i):
                    return self.dicDB[database][table][0].registros()[self.dicDB[database][table][0].Keys().index(i)]
            return []
        except:
            return []

    # MODIFICA UN REGISTRO EN ESPECIFICO

    def update(self, database, table, register, columns):
        if self.searchDB(database):
            if self.searchTB(database, table):
                try:
                    columns[0] = columns[0]
                    if self.dicDB[database][table][2] != None:
                        pk = ""
                        for i in columns:
                            pk += str(i) + "_"
                        pk = pk[:-1]
                        pk = pk.replace('[','')
                        pk = pk.replace(']', '')
                        print(type(self.dicDB[database][table][0].Keys()))
                        if pk in self.dicDB[database][table][0].Keys():
                            tupla = self.extractRow(database, table, columns)
                            for key, value in register.items():
                                tupla[key] = value
                            self.dicDB[database][table][0].update(tupla, pk)
                            self.updateTree(database,table)
                            serializar.commit(self.dicDB[database][table][0], database + "-" + table + "-B")
                            return 0
                        return 4
                    else:
                        pk = ""
                        for i in columns:
                            pk += str(i) + "_"
                        pk = pk[:-1]
                        if pk in self.dicDB[database][table][0].Keys():
                            tupla = self.extractRow(database, table, columns)
                            for key, value in register.items():
                                tupla[key] = value
                            self.dicDB[database][table][0].update(tupla, pk)
                            self.updateTree(database, table)
                            serializar.commit(self.dicDB[database][table][0], database + "-" + table + "-B")
                            return 0
                        return 4
                except:
                    return 1
            return 3
        return 2

    # ELIMINA UN REGISTRO EN ESPECIFICO

    def delete(self, database, table, columns):
        try:
            database.lower()
            table.lower()
        except:
            return 1
        if self.searchDB(database):
            if self.searchTB(database, table):
                try:
                    columns[0] = columns[0]
                    if self.dicDB[database][table][2] != None:
                        pk = ""
                        for i in columns:
                            pk += str(i) + "_"
                        pk = pk[:-1]
                        if pk in self.dicDB[database][table][0].Keys():
                            self.dicDB[database][table][0]._del(pk)
                            self.updateTree(database, table)
                            return 0
                        return 4
                    else:
                        pk = ""
                        for i in columns:
                            pk += str(i) + "_"
                        pk = pk[:-1]
                        if pk in self.dicDB[database][table][0].Keys():
                            self.dicDB[database][table][0]._del(pk)
                            # self.updateTree(database, table)
                            return 0
                        return 4
                except:
                    return 1
            return 3
        return 2

    # ELIMINA TODOS LOS REGISTROS DE UNA TABLA

    def truncate(self, database, table):
        try:
            if self.searchDB(database):
                if self.searchTB(database, table):
                    try:
                        self.dicDB[database][table][0] = bt.arbolB(self.grade)
                        return 0
                    except:
                        return 1
                return 3
            return 2
        except:
            return 1

    #-------------------------UTILIDADES-------------------------#

    # VALIDA EL NOMBRE CON LAS REGLAS DE IDENTIFICADORES DE SQL

    def identify(self, id):
        id = str(id)
        if id[0].isalpha():
            return True
        else:
            if id[0].isdigit():
                return False
        return False

    # BUSCAR SI EXISTE LA BASE DE DATOS

    def searchDB(self, key):
        for i in self.dicDB.keys():
            if key.lower() == i.lower():
                return True
        return False

    # BUSCAR SI EXISTE LA TABLA EN UNA DETERMINADA BASE DE DATOS

    def searchTB(self, database,table):
        for i in self.dicDB[database]:
            if table.lower() == i.lower():
                return True
        return False

    # VERIFICAR SI EXISTEN LLAVES REPETIDAS DENTRO DE UNA LISTA

    def searchRepeat(self, li):
        tmp = list()
        for i in li:
            if i not in tmp:
                tmp.append(i)
            else:
                return False
        return True

    # ACTUALIZAR LA TABLA CON LAS LLAVES PRIMARIAS OBTENIDAS

    def updateTree(self, database, table):
        registros = self.dicDB[database][table][0].registros()
        tmp = bt.arbolB(self.grade)
        for i in registros:
            pk = ""
            for j in self.dicDB[database][table][2]:
                pk += str(i[j]) + "_"
            pk = pk[:-1]
            tmp.insertar([pk, i])
        self.dicDB[database][table][0] = tmp
    
    # VERIFICAR SI NO HAY CONFLICTO ENTRE PK

    def verifyPk(self, database, table, columns):
        registros = self.dicDB[database][table][0].registros()
        tmp = bt.arbolB(self.grade)
        for i in registros:
            pk = ""
            for j in columns:
                pk += str(i[j]) + "_"
            pk = pk[:-1]
            tmp.insertar([pk, i])
        return self.searchRepeat(tmp.Keys())
