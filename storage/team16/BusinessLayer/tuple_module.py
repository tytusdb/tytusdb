from DataAccessLayer.handler import Handler
from Models.avl_tree import AVLTree


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
                    auxPk = []
                    for i in range(len(register)):
                        if str(i) in tempAVL.pklist:
                            auxPk.append(register[i])

                    if len(register) > tempAVL.numberColumns: # más parametros de los esperado en register
                        return 5
                    elif tempAVL.find(auxPk) is False: # PK repetida
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
            return []
        except:
            return [None]

    def extractRow(self, database: str, table: str, columns: list) -> int:
        try:
            return 0
        except:
            return 1

    def update(self, database: str, table: str, register: dict, columns: list) -> int:
        try:
            return 0
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
                if tempAVL.find(columns) is True:
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
