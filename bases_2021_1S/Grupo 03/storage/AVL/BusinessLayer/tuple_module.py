# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from storage.AVL.DataAccessLayer.handler import Handler
from storage.AVL.Models.avl_tree import AVLTree


class TupleModule:

    def __init__(self):
        self.handler = Handler()
        self.dbs = None

    def insert(self, database: str, table: str, register: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(register, list):
                raise
            filtro = False
            self.dbs = self.handler.rootinstance()
            for db in self.dbs:
                if db.name.upper() == database.upper():
                    if self.handler.exists(database, table):
                        filtro = True
                        break
                    else:
                        return 3
            if filtro:
                avl = self.handler.tableinstance(database, table)
                if len(register) != avl.numberColumns:
                    return 5
                if not len(avl.pklist) == 0:
                    auxPk = ""
                    for key in avl.pklist:
                        auxPk += "-" + str(register[key])
                    auxPk = auxPk[1:]
                    if avl.search(auxPk):
                        return 4
                    else:
                        avl.add(auxPk, register)
                else:
                    index = avl.hidden
                    while True:
                        if avl.search(str(index)):
                            index += 1
                            continue
                        avl.add(str(index), register)
                        break
                    avl.hidden = index
                self.handler.tableupdate(avl)
                return 0
            else:
                return 2
        except:
            return 1

    def loadCSV(self, file: str, database: str, table: str) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not file.endswith(".csv"):
                raise
            reader = self.handler.readcsv(file)
            self.dbs = self.handler.rootinstance()
            for db in self.dbs:
                if db.name.upper() == database.upper():
                    if self.handler.exists(database, table):
                        result = []
                        avl = self.handler.tableinstance(database, table)
                        for fila in reader:
                            result.append(self.__insert(avl, fila))
                        self.handler.tableupdate(avl)
                        return result
                    else:
                        return []
            return []
        except:
            return []

    def extractRow(self, database: str, table: str, columns: list) -> list:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise
            self.dbs = self.handler.rootinstance()
            for db in self.dbs:
                if db.name.upper() == database.upper():
                    if self.handler.exists(database, table):
                        avl = self.handler.tableinstance(database, table)
                        node = avl.search(self.__concat(columns))
                        if node:
                            return node
                        return []
                    else:
                        return []
            return []
        except:
            return []

    def update(self, database: str, table: str, register: dict, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise
            self.dbs = self.handler.rootinstance()
            existeDB = False
            for db in self.dbs:
                if db.name.upper() == database.upper():
                    existeDB = True
                    break

            if self.handler.exists(database, table) and existeDB:
                avl = self.handler.tableinstance(database, table)
                auxStr = ""
                for key in columns:
                    auxStr += "-" + str(key)
                auxStr = auxStr[1:]
                avltmp = avl.search(auxStr)
                if avltmp:
                    if len(register) <= avl.numberColumns:
                        simple = True
                        for key in register:
                            if key in avl.pklist:
                                simple = False
                        content = avltmp
                        oldcontent = avltmp[:]
                        for key in register:
                            content[key] = register[key]
                        if simple:
                            avl.update(auxStr, content)
                            self.handler.tableupdate(avl)
                        else:
                            tmp = []
                            for key in avl.pklist:
                                tmp.append(oldcontent[key])
                            self.delete(database, table, tmp)
                            self.insert(database, table, content)
                        return 0
                    else:
                        return 1
                else:
                    return 4
            elif existeDB is False:
                return 2
            else:
                return 3
        except:
            return 1

    def delete(self, database: str, table: str, columns: list) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str) or not isinstance(columns, list):
                raise
            self.dbs = self.handler.rootinstance()
            for db in self.dbs:
                if db.name.upper() == database.upper():
                    if self.handler.exists(database, table):
                        avl = self.handler.tableinstance(database, table)
                        pk = self.__concat(columns)
                        if avl.search(pk):
                            avl.delete(pk)
                            self.handler.tableupdate(avl)
                            return 0
                        return 4
                    else:
                        return 3
            return 2
        except:
            return 1

    def truncate(self, database: str, table: str) -> int:
        try:
            if not isinstance(database, str) or not isinstance(table, str):
                raise
            self.dbs = self.handler.rootinstance()
            for base in self.dbs:
                if base.name.upper() == database.upper():
                    if self.handler.exists(database, table):
                        avl = self.handler.tableinstance(database, table)
                        newAvl = AVLTree(
                            database, table, avl.numberColumns, avl.pklist)
                        self.handler.tableupdate(newAvl)
                        return 0
                    else:
                        return 3
            return 2
        except:
            return 1

    @staticmethod
    def __concat(keys) -> str:
        res = ""
        for pk in keys:
            res += "-" + str(pk)
        res = res[1:]
        return res

    @staticmethod
    def __insert(avl, register: list) -> int:
        try:
            if not isinstance(register, list):
                raise
            if len(register) != avl.numberColumns:
                return 5
            if not len(avl.pklist) == 0:
                auxPk = ""
                for key in avl.pklist:
                    auxPk += "-" + str(register[key])
                auxPk = auxPk[1:]
                if avl.search(auxPk):
                    return 4
                else:
                    avl.add(auxPk, register)
            else:
                index = avl.hidden
                while True:
                    if avl.search(str(index)):
                        index += 1
                        continue
                    avl.add(str(index), register)
                    break
                avl.hidden = index

            return 0
        except:
            return 1
