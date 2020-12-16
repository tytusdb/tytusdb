class TabsStruct:
    def __init__(self, db, name, cols, tuplas):
        # numero de columnas
        self.countCol = cols
        # tuplas con estructura de ISAM
        self.tuplas = tuplas
        # nombre de la tabla
        self.name = name
        # nombre de la db
        self.db = db


class Tables:
    def __init__(self):
        self.Tabs = {}

    def createTable(self, database, table, numberColumns):
        tab = TabsStruct(database, table, numberColumns, [])
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
        pass

    def alterDropPK(self,database, table):
        pass

    def alterTable(self,database, tableOld, tableNew):
        temp = self.Tabs[tableOld]
        del self.Tabs[tableOld]
        self.createTable(temp.db, tableNew, temp.countCol)
        self.Tabs[tableNew].tuplas=temp.tuplas
        return 0

    def alterAddColumn(self,database, table, default):
        pass

    def alterDropColumn(self,database, table, columnNumber):
        pass
