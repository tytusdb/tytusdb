import ListaBaseDatos as Storage
import serealizar
import os
import re

storage = Storage.ListaBaseDatos()
main_path = os.getcwd()+"\\data\\hash"
db_name_pattern = "^[a-zA-Z][a-zA-Z0-9#@$_]*"
table_name_pattern = "^[a-zA-Z_][a-zA-Z0-9#@$_]*"


# Cambiar la ubicación del directorio data (por defecto se usará el directorio de consola)

def setDir(newPath: str) -> int:

    global main_path
    temp_path = newPath+"\\data"

    try:
        if os.path.isdir(newPath):

            if not os.path.isdir(temp_path):
                os.mkdir(temp_path)

            main_path = temp_path
            Storage.main_path = temp_path

            __init__()

            return 0
        
        else:
            return 1

    except:
        return 1


# ==//== inicialización del sistema de directorios ==//==

def __init__():

    if not os.path.isdir(os.getcwd()+"\\data"):
        os.mkdir(os.getcwd()+"\\data")

    if not os.path.isdir(os.getcwd()+"\\data\\hash"):
        os.mkdir(os.getcwd()+"\\data\\hash")
        
    for db in os.listdir(main_path):
        storage.createDatabase(db)
        
__init__()

# ==//== funciones con respecto a ListaBaseDatos ==//==
# Se llama la función sobre la clase ListaBaseDatos

def createDatabase(database: str) -> int:

    if re.search(db_name_pattern, database):
        return storage.createDatabase(database)

    else:
        return 1


def showDatabases() -> list:

    return storage.showDatabases()


def alterDatabase(databaseOld: str, databaseNew: str) -> int:

    if re.search(db_name_pattern, databaseOld) and re.search(db_name_pattern, databaseNew):
        return storage.alterDatabase(databaseOld, databaseNew)

    else:
        return 1


def dropDatabase(database: str) -> int:

    return storage.dropDatabase(database)


# ==//== funciones con respecto a BaseDatos ==//==
# Primero se busca la base de datos y luego se llama la función sobre la clase BaseDatos

def createTable(database: str, table: str, numberColumns: int) -> int:

    temp = storage.Buscar(database)

    if temp:
        return temp.createTable(table, numberColumns)

    else:
        return 2


def showTables(database: str) -> list:

    temp = storage.Buscar(database)

    if temp:
        return temp.showTables()

    else:
        return None


def extractTable(database: str, table: str) -> list:

    temp = storage.Buscar(database)

    if temp:
        return temp.extractTable(table)

    else:
        return None


def extractRangeTable(database: str, table: str, lower: any, upper: any) -> list:

    temp = storage.Buscar(database)

    if temp:
        return temp.extractRangeTable(table, lower, upper)

    else:
        return None


def alterAddPK(database: str, table: str, columns: list) -> int:

    temp = storage.Buscar(database)

    if temp:
        return temp.alterAddPK(table, columns)

    else:
        return 2


def alterDropPK(database: str, table: str, columns: list) -> int:

    temp = storage.Buscar(database)

    if temp:
        return temp.alterDropPK(table, columns)
        
    else:
        return 2


def alterAddFK(database: str, table: str, references: dict) -> int:

    #codigo en proceso (FASE 2)
    pass


def alterAddIndex(database: str, table: str, references: dict) -> int:

    #codigo en proceso (FASE 2)
    pass


def alterTable(database: str, tableOld: str, tableNew: str) -> int:

    temp = storage.Buscar(database)

    if temp:
        return temp.alterTable(tableOld, tableNew)

    else:
        return 2


def alterAddColumn(database:str, table:str) -> int:

    temp = storage.Buscar(database)

    if temp:
        return temp.alterAddColumn(table)

    else:
        return 2


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:

    temp = storage.Buscar(database)

    if temp:
        return temp.alterDropColumn(table, columnNumber)

    else:
        return 2


def dropTable(database: str, table: str) -> int:

    temp = storage.Buscar(database)

    if temp:
        return temp.dropTable(table)

    else:
        return 2


# ==//== funciones con respecto a Tabla ==//==
# Primero se busca la base de datos, luego la tabla, y luego se llama la función sobre la clase Tabla

def insert(database: str, table: str, register: list) -> int:

    temp = storage.Buscar(database)

    if temp:

        b = temp.Buscar(table)        
        nombre = temp.list_table[b[1]]
        
        tabla = serealizar.rollback(nombre, main_path+"\\"+database)

        if b[0]:
            var = tabla.insertar(register)            
            serealizar.commit(tabla, table, main_path+"\\"+database)

            return var

        else:
            return 3

    else:
        return 2


def loadCSV(file: str, database: str, table: str) -> int:

    try:
        archivo = open(file)

    except:
        return 1

    temp = storage.Buscar(database)

    if temp:

        b = temp.Buscar(table)        
        nombre = temp.list_table[b[1]]
        
        tabla = serealizar.rollback(nombre, main_path+"\\"+database)

        if b[0]:
            
            temp_registros = archivo.readlines()

            registros = []

            for registro in temp_registros:                
                registros.append(registro.replace("\n", "").split(","))

            for registro in registros:
                
                valor = tabla.insertar(registro)

                if valor:
                    serealizar.commit(tabla, table, main_path+"\\"+database)
                    return valor

            else:
                serealizar.commit(tabla, table, main_path+"\\"+database)
                return 0

        else:
            return 3

    else:
        return 2
        

def extractRow(database: str, table: str, columns: list) -> int:

    temp = storage.Buscar(database)

    if temp:

        temp = temp.Buscar(table)

        if temp:
            return temp.extractRow(columns)

        else:
            return 3

    else:
        return 2


def update(database: str, table: str, register: dict, columns: list) -> int:

    temp = storage.Buscar(database)

    if temp:

        b = temp.Buscar(table)        
        nombre = temp.list_table[b[1]]
        
        tabla = serealizar.rollback(nombre, main_path+"\\"+database)

        if b[0]:
            var = tabla.update(columns, register)            
            serealizar.commit(tabla, table, main_path+"\\"+database)

            return var

        else:
            return 3

    else:
        return 2


def delete(database: str, table: str, columns: list) -> int:

    temp = storage.Buscar(database)

    if temp:

        b = temp.Buscar(table)        
        nombre = temp.list_table[b[1]]
        
        tabla = serealizar.rollback(nombre, main_path+"\\"+database)

        if b[0]:
            var = tabla.deleteTable(columns)            
            serealizar.commit(tabla, table, main_path+"\\"+database)

            return var

        else:
            return 3

    else:
        return 2


def truncate(database: str, table: str) -> int:

    temp = storage.Buscar(database)

    if temp:

        b = temp.Buscar(table)        
        nombre = temp.list_table[b[1]]
        
        tabla = serealizar.rollback(nombre, main_path+"\\"+database)

        if b[0]:
            var = tabla.truncate()            
            serealizar.commit(tabla, table, main_path+"\\"+database)

            return var

        else:
            return 3

    else:
        return 2
