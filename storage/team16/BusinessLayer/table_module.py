import sys
import os
sys.path.append(os.path.abspath('.'))
from DataAccessLayer.handler import Handler
from Models.avl_tree import AVLTree

class TableModule:
    def __init__(self):
        self.handler = Handler()
        self.avl = AVLTree()

    def createTable(self, database: str, table: str, numberColumns: int) -> int:
        try:
            if not self.handler.siExiste(database, table):
                databases = self.handler.leerArchivoDB()
                for i in databases:
                    if database == i.name:
                        i.tablesName.append(str(table))
                        self.handler.actualizarArchivoDB(databases)
                        self.handler.actualizarArchivoTB(AVLTree(database,table,numberColumns,[]), database, table)
                        return 0
                return 2
            return 3 
        except:
            return 1
    
    def showTables(self, database: str) -> list:
        try:
            databases = self.handler.leerArchivoDB()
            for i in databases:
                if database == i.name:
                    return i.tablesName
            return None
        except:
            return None
    
    def extractTable(self ,database: str, table: str) -> list:
        try:
            if self.handler.siExiste(database,table):
                tmp = []
                avl = self.handler.leerArchivoTB(database,table)
                if avl.root != None:
                    tmp = avl.list()
                return tmp
            else:
                return None
        except:
            return None
    
    def extractRangeTable(self, database: str, table: str, lower: any, upper: any) -> list:
        try:
            if self.handler.siExiste(database,table):
                tmp = []
                avl = self.handler.leerArchivoTB(database,table)
                if avl.root != None:
                    for i in avl.list():
                        #Considerando que la primera columna es la clave primaria
                        if type(i[0]) == type(3):
                            if int(i[0]) >= int(lower) and int(i[0]) <= int(upper):
                                tmp.append(i)
                        elif type(i[0]) == type("string"):
                            if str(i[0]) >= str(lower) and str(i[0]) <= str(upper):
                                tmp.append(i)
                        elif type(i[0]) == type(3.1):
                            if float(i[0]) >= float(lower) and float(i[0]) <= float(upper):
                                tmp.append(i)
                return tmp
            else:
                return None
        except:
            return None
    
    def alterAddPK(self, database: str, table: str, columns: list) -> int: #si ya existen y se agrega o modifica, eliminar la actual recalculando el indice
        try:
            databases = self.handler.leerArchivoDB() #si hay registros duplicados al querer agregar llave primaria en esa columna retornar error
            for i in databases:
                if database == i.name:
                    if self.handler.siExiste(database,table):
                        avl = self.handler.leerArchivoTB(database,table)
                        if avl.pklist == []:
                            for i in columns:
                                if i < 0 or i >= avl.numberColumns:
                                    return 5
                            if avl.root == None:
                                avl.pklist = columns
                                return 0
                            else:
                                if avl.hidden:
                                    #reestructurar los indices del arbol con la actual llave primaria
                                else:
                                    return 1
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
            databases = self.handler.leerArchivoDB()
            for i in databases:
                if database == i.name:
                    if self.handler.siExiste(database, table):
                        avl = self.handler.leerArchivoTB(database,table)
                        if avl.pklist != []:
                            avl.pklist = []
                        else:
                            return 4
                    else:
                        return 3
            return 2
        except:
            return 1
    
    def alterAddFK(self, database: str, table: str, references: dict) -> int: #para fase 2
        pass

    def alterAddIndex(self, database: str, table: str, references: dict) -> int: #para fase 2
        pass
    
    def alterTable(self, database: str, tableOld: str, tableNew: str) -> int:
        try:
            databases = self.handler.leerArchivoDB()
            for i in databases:
                if database == i.name:
                    if not self.handler.siExiste(database, tableNew):
                        if self.handler.siExiste(database, tableOld):
                            for j in range(len(i.tablesName)):
                                if i.tablesName[j] == tableOld:
                                    i.tablesName[j] = tableNew
                            self.handler.actualizarArchivoDB(databases)
                            avl = self.handler.leerArchivoTB(database,tableOld)
                            avl.name = tableNew
                            self.handler.renombrarArchivo(str(tableOld)+'-'+str(database)+'.tbl',str(tableNew)+'-'+str(database)+'.tbl')
                            return 0
                        else:
                            return 3
                    else:
                        return 4
            return 2
        except:
            return 1
    
    def alterAddColumn(self, database: str, table: str, default: any) -> int:
        try:
            databases = self.handler.leerArchivoDB()
            for i in databases:
                if database == i.name:
                    if self.handler.siExiste(database, table):
                        avl = self.handler.leerArchivoTB(database,table)
                        avl.numberColumns += 1
                        avl.addColumn(default)
                        return 0
                    else:
                        return 3
            return 2
        except:
            return 1
    
    def alterDropColumn(self, database: str, table: str, columnNumber: int) -> int: #no se puede eliminar una columna que sea llave primaria (validar)
        try:
            databases = self.handler.leerArchivoDB()
            for i in databases:
                if database == i.name:
                    if self.handler.siExiste(database, table):
                        avl = self.handler.leerArchivoTB(database,table)
                        if columnNumber > avl.numberColumns or columnNumber < 0:
                            return 5
                        elif columnNumber == avl.numberColumns or columnNumber in avl.pklist:
                            return 4
                        else:
                            avl.numberColumns -= 1
                            avl.dropColumn(columnNumber)
                            return 0
                    else:
                        return 3
            return 2
        except:
            return 1
    
    def dropTable(self, database: str, table: str) -> int: 
        try:
            databases = self.handler.leerArchivoDB()
            for i in databases:
                if database == i.name:
                    if self.handler.siExiste(database, table):
                        i.tablesName.remove(table)
                        self.handler.actualizarArchivoDB(databases)
                        self.handler.borrarArchivo(str(table)+'-'+str(database)+'.tbl')
                        return 0
                    else:
                        return 3
            return 2
        except:
            return 1
