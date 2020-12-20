from ISAM import *
class TabsStruct:
    def __init__(self, db, name, cols, tuplas,ruta):
        # numero de columnas
        self.countCol = cols
        # nombre de la tabla
        self.name = name
        # nombre de la db
        self.db = db
        #llaves primarias
        self.pks=[0]
        # tuplas con estructura de ISAM
        self.tuplas = Indice(self.pks,ruta)


class Tables:
    def __init__(self):
        self.Tabs = {}

    def createTable(self, database, table, numberColumns,ruta):
        tab = TabsStruct(database, table, numberColumns, ruta)
        # self.Tabs[table]=[database,table,numberColumns]
        self.Tabs[table] = tab

    def showTables(self, db):
        # este a nivel de db
        names = []
        for tabs in self.Tabs:
            names.append(self.Tabs[tabs].name)
        return names

    def dropTable(self, database, table):
        del self.Tabs[table]

    def extractTable(self, database, table):
        # -******-*-*-*-*********-*-*-*-
        # extrae las tuplas de dicha tabla, por el momento solo la tabla
        return self.Tabs[table].tuplas

    def extractRangeTable(self,database, table, lower, upper):
        pass

    def alterAddPK(self,database, table, columns):
        self.Tabs[table].pks=columns
        self.Tabs[table].tuplas.pkey=columns

    def alterDropPK(self,database, table):
        self.Tabs[table].pks=[]

    def alterTable(self,database, tableOld, tableNew):
        temp = self.Tabs[tableOld]
        del self.Tabs[tableOld]
        self.createTable(temp.db, tableNew, temp.countCol)
        self.Tabs[tableNew].tuplas=temp.tuplas
        return 0

    def alterAddColumn(self,database, table, default):
        self.Tabs[table].countCol=self.Tabs[table].countCol+1

    def alterDropColumn(self,database, table, columnNumber):
        if self.Tabs[table].countCol > 0:
            self.Tabs[table].countCol=self.Tabs[table].countCol-1
            
    def truncate(self,table,ruta):
        pk=self.Tabs[table].tuplas.pkey
        self.Tabs[table].tuplas=Indice(pk,ruta)
