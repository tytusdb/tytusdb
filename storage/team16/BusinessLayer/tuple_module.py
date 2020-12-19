from DataAccessLayer.handler import Handler
from Models.avl_tree import AVLTree
import csv


class TupleModule:

    def __init__(self):
        self.handler = Handler()

    def insert(self, database: str, table: str, register: list) -> int:
        try:
            filtro = False
            listaBases = self.handler.leerArchivoDB()
            for base in listaBases:
                if base.name == database:
                    if self.handler.siExiste(database, table):
                        filtro = True
                        break
                    else:
                        return 3
            if filtro:
                tempAVL = self.handler.leerArchivoTB(database, table)
                if len(register) > tempAVL.numberColumns:  # más parametros de los esperado en register
                    return 5
                # lista que almacena las columnas que son PK en el parametro
                auxPk = ""
                for el in tempAVL.pklist:
                    if el == tempAVL.pklist[0]:
                        auxPk = str(register[el])
                    else:
                        auxPk = auxPk + "-" + str(register[el])

                if tempAVL.search(auxPk) is not None:
                    return 4  # si no es nulo ya existe un dato con la misma pk
                else:
                    tempAVL.add(auxPk, register)
                    self.handler.actualizarArchivoTB(tempAVL, database, table)
                    return 0
            else:
                return 2
        except:
            return 1

    def loadCSV(self, file: str, database: str, table: str) -> list:
        if file.endswith(".csv") is False:
            return []
        try:
            reader = csv.reader(open(file, "r"), delimiter=",")

            dbList = self.handler.leerArchivoDB()
            for db in dbList:
                if db.name == database:
                    if self.handler.siExiste(database, table):
                        result = []
                        for fila in reader:
                            result.append(self.insert(database, table, fila))
                        return result
                    else:
                        return []
            return []
        except:
            return []

    def extractRow(self, database: str, table: str, columns: list) -> list:
        try:
            dbList = self.handler.leerArchivoDB()
            for db in dbList:
                if db.name == database:
                    if self.handler.siExiste(database, table):
                        tempAVL = self.handler.leerArchivoTB(database, table)
                        node = tempAVL.search(self.__concatKeys(columns))
                        if node is not None:
                            return node
                        return []
                    else:
                        return []
            return []
        except:
            return []

    def update(self, database: str, table: str, register: dict, columns: list) -> int:
        try:
            dbList = self.handler.leerArchivoDB()
            existeDB = False
            existeTable = False
            for db in dbList:
                if db.name == database:
                    existeDB = True
                    break
            existeTable = self.handler.leerArchivoTB(database, table)

            if existeTable is True and existeDB is True:
                tempAvl = self.handler.leerArchivoTB(database, table)
                auxStr = ""
                for el in columns:
                    if el == columns[0]:
                        auxStr = str(el)
                    else:
                        auxStr = auxStr + "-" + str(el)

                foundNode = tempAvl.find(auxStr)
                if foundNode is not None:
                    if len(register) <= tempAvl.numberColumns:
                        newContent = tempAvl.content
                        for key in register:
                            newContent[key] = register[key]

                        # actualizas el nodo auxStr-> concatenacion de las llaves y el newContent -> lista del content
                        tempAvl.update(auxStr, newContent)
                        self.handler.actualizarArchivoTB(tempAvl, database, table)
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
            dbList = self.handler.leerArchivoDB()
            for db in dbList:
                if db.name == database:
                    if self.handler.siExiste(database, table):
                        tempAVL = self.handler.leerArchivoTB(database, table)
                        pk = self.__concatKeys(columns)
                        if tempAVL.search(pk) is not None:
                            tempAVL.delete(pk)
                            self.handler.actualizarArchivoTB(tempAVL, database, table)
                            return 0
                        return 4
                    else:
                        return 3
            return 2
        except:
            return 1

    def truncate(self, database: str, table: str) -> int:
        try:
            listaBases = self.handler.leerArchivoDB()
            for base in listaBases:
                if base.name == database:
                    if self.handler.siExiste(database, table):
                        tempAVL = self.handler.leerArchivoTB(database, table)
                        newAvl = AVLTree(database, table, tempAVL.numberColumns, tempAVL.pklist)
                        self.handler.actualizarArchivoTB(newAvl, database, table)
                        return 0
                    else:
                        return 3
            return 2
        except:
            return 1

    def __concatKeys(self, llaves) -> str:
        res = ""
        for pk in llaves:
            if pk == llaves[0]:
                res = str(pk)
            else:
                res = res + "-" + str(pk)
        return res
