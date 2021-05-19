# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from storage.AVL.DataAccessLayer.handler import Handler
from storage.AVL.Models.avl_tree import AVLTree


class TableModule:
    def __init__(self):
        self.handler = Handler()
        self.dbs = None

    def createTable(self, database: str, table: str, numberColumns: int) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or (
                    not isinstance(numberColumns, int) or numberColumns < 0):
                raise
            self.dbs = self.handler.rootinstance()
            if not self.handler.exists(database, table):
                for i in self.dbs:
                    if database.upper() == i.name.upper():
                        if self.handler.invalid(table):
                            raise
                        i.tablesName.append(table)
                        self.handler.rootupdate(self.dbs)
                        self.handler.tableupdate(
                            AVLTree(database, table, numberColumns))
                        return 0
                return 2
            return 3
        except:
            return 1

    def showTables(self, database: str) -> list:
        try:
            if not isinstance(database, str):
                raise
            self.dbs = self.handler.rootinstance()
            for i in self.dbs:
                if database.upper() == i.name.upper():
                    return i.tablesName
            return None
        except:
            return None

    def extractTable(self, database: str, table: str) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            if self.handler.exists(database, table):
                avl = self.handler.tableinstance(database, table)
                return avl.tolist()
            else:
                return None
        except:
            return None

    def extractRangeTable(self, database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columnNumber, int):
                raise
            if self.handler.exists(database, table):
                avl = self.handler.tableinstance(database, table)
                return avl.range(columnNumber, lower, upper)
            else:
                return None
        except:
            return None

    def alterAddPK(self, database: str, table: str, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list) or \
                    len(columns) == 0:
                raise
            self.dbs = self.handler.rootinstance()
            for db in self.dbs:
                if database.upper() == db.name.upper():
                    if self.handler.exists(database, table):
                        avl = self.handler.tableinstance(database, table)
                        if len(avl.pklist) == 0:
                            for i in columns:
                                if not isinstance(i, int):
                                    raise
                                if i not in range(avl.numberColumns):
                                    return 5
                            if avl.root is None:
                                avl.pklist = columns
                            else:
                                used = []
                                nodes = avl.tolist()
                                for tpl in nodes:
                                    pk = ""
                                    for col in columns:
                                        pk += "-" + str(tpl[col])
                                    pk = pk[1:]
                                    if pk in used:
                                        return 1
                                    used.append(pk)
                                newavl = AVLTree(
                                    database, table, avl.numberColumns, columns)
                                c = 0
                                for tpl in nodes:
                                    newavl.add(used[c], tpl)
                                    c += 1
                                avl = newavl
                            self.handler.tableupdate(avl)
                            return 0
                        else:
                            return 4
                    else:
                        return 3
            return 2
        except:
            return 1

    def alterDropPK(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            for i in self.dbs:
                if database.upper() == i.name.upper():
                    if self.handler.exists(database, table):
                        avl = self.handler.tableinstance(database, table)
                        if len(avl.pklist) != 0:
                            avl.pklist = []
                            self.handler.tableupdate(avl)
                            return 0
                        else:
                            return 4
                    else:
                        return 3
            return 2
        except:
            return 1

    # region Phase 2
    def alterAddFK(self, database: str, table: str, references: dict) -> int:  # para fase 2
        pass

    def alterAddIndex(self, database: str, table: str, references: dict) -> int:  # para fase 2
        pass

    # endregion

    def alterTable(self, database: str, tableOld: str, tableNew: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(tableOld, str) or not isinstance(tableNew, str) or \
                    self.handler.invalid(tableNew):
                raise
            self.dbs = self.handler.rootinstance()
            for db in self.dbs:
                if database.upper() == db.name.upper():
                    if self.handler.exists(database, tableOld):
                        if not self.handler.exists(database, tableNew):
                            for j in range(len(db.tablesName)):
                                if db.tablesName[j].upper() == tableOld.upper():
                                    db.tablesName[j] = tableNew
                            self.handler.rootupdate(self.dbs)
                            avl = self.handler.tableinstance(
                                database, tableOld)
                            avl.name = tableNew
                            self.handler.rename(database + '_' + tableOld + '.tbl',
                                                database + '_' + tableNew + '.tbl')
                            self.handler.tableupdate(avl)
                            return 0
                        else:
                            return 4
                    else:
                        return 3
            return 2
        except:
            return 1

    def alterAddColumn(self, database: str, table: str, default: any) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            for db in self.dbs:
                if database.upper() == db.name.upper():
                    if self.handler.exists(database, table):
                        avl = self.handler.tableinstance(database, table)
                        avl.numberColumns += 1
                        avl.massiveupdate("add", default)
                        self.handler.tableupdate(avl)
                        return 0
                    else:
                        return 3
            return 2
        except:
            return 1

    def alterDropColumn(self, database: str, table: str, columnNumber: int) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columnNumber, int):
                raise
            self.dbs = self.handler.rootinstance()
            for db in self.dbs:
                if database.upper() == db.name.upper():
                    if self.handler.exists(database, table):
                        avl = self.handler.tableinstance(database, table)
                        if columnNumber not in range(avl.numberColumns):
                            return 5
                        elif avl.numberColumns == 1 or columnNumber in avl.pklist:
                            return 4
                        else:
                            avl.numberColumns -= 1
                            avl.massiveupdate("drop", int(columnNumber))
                            c = 0
                            for key in avl.pklist:
                                if key > columnNumber:
                                    key -= 1
                                    avl.pklist[c] = key
                                c += 1
                            self.handler.tableupdate(avl)
                            return 0
                    else:
                        return 3
            return 2
        except:
            return 1

    def dropTable(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            for i in self.dbs:
                if database.upper() == i.name.upper():
                    if self.handler.exists(database, table):
                        i.tablesName.remove(table)
                        self.handler.rootupdate(self.dbs)
                        self.handler.delete(database + '_' + table + '.tbl')
                        return 0
                    else:
                        return 3
            return 2
        except:
            return 1
