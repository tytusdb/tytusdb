import ListaBaseDatos as Storage
import os

storage=Storage.ListaBaseDatos()
main_path= os.getcwd()+"\\tmp"

#==//== funciones con respecto a ListaBaseDatos ==//==
# Se llama la función sobre la clase ListaBaseDatos

def createDatabase(mode: int, databaseName: str):

    if databaseName:

        if mode in range(1, 6):
            storage.createDatabase(5, databaseName)

        else:
            return 3

    else:
        return 2


def showDatabases():

    storage.showDatabases()


def alterDatabase(databaseOld, databaseNew):

    if databaseOld and databaseNew:

        storage.alterDatabase(databaseOld, databaseNew)

    else:
        print("Se necesita un nuevo nombre para la base de datos")


def dropDatabase(databaseName):

    if databaseName:
        storage.dropDatabase(databaseName)

    else:
        print("Se necesita un nombre para la base de datos")


#==//== funciones con respecto a BaseDatos ==//==
# Primero se busca la base de datos y luego se llama la función sobre la clase BaseDatos

def createTable(databaseName, tableName, numberColumns):

    temp=storage.Buscar(databaseName)

    if temp:
        temp.createTable(tableName, numberColumns)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


def showTables(databaseName):

    temp=storage.Buscar(databaseName)

    if temp:
        temp.showTables()
        
    else:
        print("Base de datos '"+databaseName+"' no encontrada")

        
def alterTable(databaseName, tableOld, tableNew):
    
    temp=storage.Buscar(databaseName)

    if temp:
        temp.alterTable(tableOld, tableNew)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


def dropTable(databaseName, tableName):
    
    temp=storage.Buscar(databaseName)

    if temp:
        temp.dropTable(tableName)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


def alterAdd(databaseName, tableName, columnName):
    
    temp=storage.Buscar(databaseName)

    if temp:
        temp.alterAdd(tableName, columnName)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


def alterDrop(databaseName, tableName, columnName):
    
    temp=storage.Buscar(databaseName)

    if temp:
        temp.alterDrop(tableName, columnName)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


def extractTable(databaseName, tableName):
    
    temp=storage.Buscar(databaseName)

    if temp:
        temp.extractTable(tableName)

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


#==//== funciones con respecto a Tabla ==//==
# Primero se busca la base de datos, luego la tabla, y luego se llama la función sobre la clase Tabla

def insert(databaseName, tableName, columns):
    
    temp=storage.Buscar(databaseName)

    if temp:

        temp=temp.Buscar(tableName)

        if temp:

            temp.insertar(columns)

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


def update(databaseName, tableName, id, columnNumber, value):
    
    temp=storage.Buscar(databaseName)

    if temp:

        temp=temp.Buscar(tableName)

        if temp:

            temp.update(id, columnNumber, value)

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")
 

def deleteTable(databaseName, tableName, id):
    
    temp=storage.Buscar(databaseName)

    if temp:

        temp=temp.Buscar(tableName)

        if temp:

            temp.deleteTable(id)

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


def truncate(databaseName, tableName):
    
    temp=storage.Buscar(databaseName)

    if temp:

        temp=temp.Buscar(tableName)

        if temp:

            temp.truncate()

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


def extractRow(databaseName, tableName, id):
   
    temp=storage.Buscar(databaseName)

    if temp:

        temp=temp.Buscar(tableName)

        if temp:

            temp.extractRow(id)

        else:
            print("Tabla '"+tableName+"' no creada")

    else:
        print("Base de datos '"+databaseName+"' no encontrada")


#==//== inicialización del sistema de directorios ==//==

def init():
    
    db_list=[]

    if os.path.isdir(main_path):
        
        for db in os.listdir(main_path):
            storage.createDatabase(5, db)

    else:
        os.mkdir(main_path)

    print(">> Se cargaron:")
    showDatabases()


init()


