# import BaseDatos

class ListaBaseDatos:

    def __init__(self):

        self.lista_bases_datos=[]


    def Buscar(self, database):

        for base_datos in self.lista_bases_datos:

            if base_datos.Name==database:

                return base_datos

        else: return False
            

    def createDatabase(self, database):

        if database:

            for base_datos in self.lista_bases_datos:

                if base_datos.Nombre==database:
                    print("Base de datos '"+database+"' ya existente, no se pudo crear")

            else:
                #self.lista_bases_datos.append(BaseDatos(database))
                print("Base de datos '"+database+"' creada con éxito")

        else:
            print("Se necesita un nombre para la base de datos")


    def showDatabases(self):

        print("//==============================//")
        print(" - -   BD EN ALMACENAMIENTO   - -")

        for base_datos in self.lista_bases_datos:
            #print(base_datos.Name)
            pass
        
        print("//==============================//")


    def alterDatabase(self, databaseNew, databaseOld):

        temp=self.Buscar(databaseNew)

        if temp:
            #temp.Name=databaseOld
            pass

        else:            
            print("Base de datos '"+databaseNew+"' no encontrada")


    def dropDatabase(self, database):

        temp=self.Buscar(database)

        if temp:
            self.lista_bases_datos.remove(temp)
            print("Base de datos '"+databaseNew+"' eliminada con éxito")

        else:
            print("Base de datos '"+database+"' no encontrada")



#======= LLAMADA A FUNCIONES IMPORTADAS ========


#   ~~>  ESTAS FUNCIONES DEBERÍAN SER MOVIDAS A UN ARCHIVO MAIN  <~~

storage=ListaBaseDatos()

#==//== funciones con respecto a BaseDatos ==//==

def createTable(database, tableName, numberColumns):

    temp=storage.Buscar(database)

    if temp:
        #temp.createTable(tableName, numberColumns)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")


def showTables(database):

    temp=storage.Buscar(database)

    if temp:
        #temp.showTables()
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")

        
def alterTable(database, tableOld, tableNew):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.alterTable(tableOld, tableNew)
        pass

    else:
        print("Base de datos '"+database+"' no contiene tablas")


def dropTable(database, tableName):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.dropTable(tableName)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")


def alterAdd(database, tableName, columnName):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.alterAdd(tableName, columnName)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")


def alterDrop(database, tableName, columnName):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.alterDrop(tableName, columnName)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")


def extractTable(database, tableName):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.extractTable(tableName)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")


#==//== funciones con respecto a Tabla ==//==

def insert(database, table, columns):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.insert(table, columns)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")


def update(database, table, id, columnNumber, value):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.update(table, id, columnNumber, value)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")
        

def deleteTable(database, tableName, id):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.deleteTable(table, columns)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")
        

def truncate(database, tableName):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.truncate(tableName)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")


def extractRow(database, table, id):
    
    temp=storage.Buscar(database)

    if temp:
        #temp.extractRow(table, id)
        pass

    else:
        print("Base de datos '"+database+"' no encontrada")
