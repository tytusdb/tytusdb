# -⁻- coding: UTF-8 -*-
from Estructura_ArbolB import *
import Serializable as serializar
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

    def alterDatabase(self, databaseOld, databseNew):
        if self.identify(databaseOld) and self.identify(databseNew):
            if self.searchDB(databaseOld):
                if self.searchDB(databseNew):
                    return 3
                else:
                    try:
                        tmp = {}
                        for key, value in self.dicDB.items():
                            if key == databaseOld:
                                key = databseNew
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
        if self.searchDB(database):
            if self.searchTB(database, table):
                return 3
            else:
                try:
                    self.dicDB.get(database)[table] = [arbolB(self.grade), int(numberColumns), None]
                    return 0
                except:
                    return 1
        return 2

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
            columnNumber = int(columnNumber)
            if self.searchDB(database):
                if self.searchTB(database, table):
                    if len(self.dicDB[database][table][0].registros()) != 0:
                        if columnNumber >= 0 and columnNumber < self.dicDB[database][table][1]:
                            registros = list()
                            for tupla in self.extractTable(database, table):
                                if str(tupla[columnNumber]).isdigit() and str(lower).isdigit() and str(upper).isdigit():
                                    if tupla[columnNumber] >= lower and tupla[columnNumber] <= upper:
                                        registros.append(tupla)
                                elif str(tupla[columnNumber]) >= str(lower) and str(tupla[columnNumber]) <= str(upper):
                                    registros.append(tupla)
                            return registros
                        return None
                    return []
                return None
            return None
        except:
            return None

    # AGREGAR LISTA DE LLAVES PRIMARIAS A UNA TABLA

    def alterAddPK(self, database, table, columns):
        if self.searchDB(database):
            if self.searchTB(database, table):
                try:
                    columns[0] = columns[0]
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
        if self.searchDB(database):
            if self.searchTB(database, tableOld):
                if not self.searchTB(database, tableNew):
                    try:
                        tmp = {}
                        for key, value in self.dicDB[database].items():
                            if key == tableOld:
                                key = tableNew
                            tmp[key] = value
                        self.dicDB[database] = tmp
                        return 0
                    except:
                        return 1
                return 4
            return 3
        return 2
    
    # ELIMINAR UNA TABLA DE LA BASE DE DATOS

    def dropTable(self, database, table):
        if self.searchDB(database):
            if self.searchTB(database, table):
                try:
                    self.dicDB[database].pop(table)
                    return 0
                except:
                    return 1
            return 3
        return 2

    # AGREGAR UN NUEVO REGISTRO A LAS TABLAS EXISTENTES

    def alterAddColumn(self, database, table, default):
        if self.searchDB(database):
            if self.searchTB(database, table):
                try:
                    self.dicDB[database][table][1] += 1
                    self.dicDB[database][table][0].agregarValor(default)
                    serializar.commit(self.dicDB[database][table][0], database + "-" + table + "-B")
                    return 0
                except:
                    return 1
            return 3
        return 2

    # ELIMINA TODOS LOS REGISTROS DE UNA TABLA

    def truncate(self, database, table):
        if self.searchDB(database):
            if self.searchTB(database, table):
                try:
                    self.dicDB[database][table][0] = arbolB(self.grade)
                    return 0
                except:
                    return 1
            return 3
        return 2

    # -------------------------UTILIDADES-------------------------#

    # VALIDA EL NOMBRE CON LAS REGLAS DE IDENTIFICADORES DE SQL

    def identify(self, id):
        id = str(id)
        special = ["[", "@", "_", "o", "#"]
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

    def searchTB(self, database, table):
        if table in self.dicDB[database]:
            return True
        else:
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
        tmp = arbolB(self.grade)
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
        tmp = arbolB(self.grade)
        for i in registros:
            pk = ""
            for j in columns:
                pk += str(i[j]) + "_"
            pk = pk[:-1]
            tmp.insertar([pk, i])
        return self.searchRepeat(tmp.Keys())
