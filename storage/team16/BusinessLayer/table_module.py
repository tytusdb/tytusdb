from DataAccessLayer.handler import Handler
from Models.avl_tree import AVLTree

class TableModule:
    def __init__(self):
        self.handler = Handler()

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
                    print(i.tablesName)
                    return i.tablesName
            print("No existe la base de datos")
            return None
        except:
            return None
    
    def extractTable(self ,database: str, table: str) -> list:
        try:
            if self.handler.siExiste(database,table):
                tmp = []
                avl = self.handler.leerArchivoTB(database,table)
                if avl.root != None:
                    # Hacer append al tmp[] por cada nodo presente en arbol
                    avl.inorder() # !!<- solo por prueba para que imprima valores
                    print(avl.numberColumns)
                    print(avl.columns)
                    print(avl.pklist)
                else:
                    print("Tabla sin registros")
                return tmp
            else:
                print("No existe la tabla o la DB")
                return None
        except:
            return None
    
    def extractRangeTable(self, database: str, table: str, lower: any, upper: any) -> list: #pendiente
        pass
    
    def alterAddPK(self, database: str, table: str, columns: list) -> int: #si ya existen y se agrega o modifica, eliminar la actual recalculando el indice
        try:
            databases = self.handler.leerArchivoDB() #si hay registros duplicados al querer agregar llave primaria en esa columna retornar error
            for i in databases:
                if database == i.name:
                    if self.handler.siExiste(database,table):
                        avl = self.handler.leerArchivoTB(database,table)
                        if avl.root == None:
                            avl.pklist = columns
                            return 0
                        else: #pendiente con el arbol...

                            #if avl.pklist es de llaves escondidas: 
                                #entonces reestructurar los indices del arbol con la actual llave primaria
                            #if avl.pklist es de llave preestablecida anteriormente:
                                #entonces eliminar las llaves actuales recalculando los indices con la(s) nueva llave
                            return 0
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
                        # falta agregar a todos los nodos del arbol el parametro default en la ultima columna
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
                        if columnNumber > avl.numberColumns:
                            return 5
                        elif columnNumber == avl.numberColumns or columnNumber in avl.pklist:
                            return 4
                        else:
                            avl.numberColumns -= 1
                            # falta eliminar todos los registros pertenecientes a esa columna
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
