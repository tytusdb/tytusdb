from DataAccessLayer.handler import Handler
from Models.avl_tree import AVLTree
import csv


class TupleModule:

    def __init__(self):
        self.handler = Handler()

    def insert(self, database: str, table: str, register: list) -> int:
        try:
            listaBases = self.handler.leerArchivoDB()
            existe = False
            for base in listaBases:
                if database == base.name:
                    existe = True
                    break
            if existe == True:
                tabla = self.handler.siExiste(database, table)
                if tabla == True:
                    tempAVL = self.handler.leerArchivoTB(database, table)

                    # lista que almacena las columnas que son PK en el parametro
                    auxPk = ""
                    for i in range(len(register)):
                        if str(i) in tempAVL.pklist:
                            if i == 0:
                                auxPk = register[i]
                            else:
                                auxPk = auxPk + "-" + register[i]

                    if len(register) > tempAVL.numberColumns: # más parametros de los esperado en register
                        return 5
                    elif tempAVL.find(auxPk) is None: # PK repetida
                        return 4
                    else:
                        if len(tempAVL.pklist) < 0:
                            tempAVL.add(auxPk, register)    # cuando no exista PK
                        else:
                            tempAVL.add(tempAVL.pklist, register)  # Cuando existe PK

                        # export table
                        self.handler.actualizarArchivoTB(tempAVL, database, table)
                        return 0
                else:
                    return 3
            else:
                return 2
        except:
            return 1

    def loadCSV(self, file: str, database: str, table: str) -> list:
        try:
            # validando ruta y extención del archivo
            if file.endswith(".csv") is False:
                return [None]
            archivo = open(file,"r")
            lector = csv.reader(archivo)

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
                result = []
                for columna in lector:
                    if len(columna) <= tempAvl.numberColumns:
                        result.append(self.insert(database, table, columna))
                self.handler.actualizarArchivoTB(tempAvl, database, table)
                return result
            elif existeDB is False:
                return [2]
            else:
                return [3]
        except:
            return [None]

    def extractRow(self, database: str, table: str, columns: list) -> list:
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
                    return foundNode.content
                else:
                    return [4]
            elif existeDB is False:
                return [2]
            else:
                return [3]
        except:
            return [1]

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
            listaBases = self.handler.leerArchivoDB()
            existe = False
            for base in listaBases:
                if database == base.name:
                    existe = True
                    break
            tabla = self.handler.siExiste(database, table)
            if existe is False:
                return 2
            elif tabla is False:
                return 3
            elif tabla is True and existe is True:
                tempAVL = self.handler.leerArchivoTB(database, table)
                if tempAVL.find(columns) is None:
                    keyAux = ""
                    for i in range(len(columns)):
                        if i == 0:
                            keyAux = columns[i]
                        else:
                            keyAux = keyAux + "-" + columns[i]

                    tempAVL.delete(keyAux)
                    self.handler.actualizarArchivoTB(tempAVL, database, table)
                    return 0
                else:
                    return 4
        except:
            return 1

    def truncate(self, database: str, table: str) -> int:
        try:
            listaBases = self.handler.leerArchivoDB()
            existe = False
            for base in listaBases:
                if database == base.name:
                    existe = True
                    break
            if existe == True:
                tabla = self.handler.siExiste(database, table)
                if tabla == True:
                    tempAVL = self.handler.leerArchivoTB(database, table)
                    newAvl = AVLTree(database, table, tempAVL.numberColumns, tempAVL.pklist)
                    self.handler.actualizarArchivoTB(newAvl, database, table)
                    return 0
                else:
                    return 3
            else:
                return 2
        except:
            return 1
