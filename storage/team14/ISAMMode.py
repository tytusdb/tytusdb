from DataBase import DataBase
from Table import Table
import os
import pickle


*----------------------------------databases CRUD-------------------------------------------*

# crea una instancia de base de datos y la guarda en la lista 
def createDatabase(database: str) -> int:
    checkDirs()
    try:
        if not identifierValidation(database):
            return 1
        for i in showDatabases():
            if i.lower() == database.lower():
                return 2
        databases = rollback('databases')
        databases.append(DataBase(database.lower()))
        commit(databases, 'databases')
        return 0
    except:
        return 1


# devuelve una lista con los nombres de las bases de datos existentes
def showDatabases() -> list:
    checkDirs()
    databasesNames = []
    databases = rollback('databases')
    for i in databases:
        databasesNames.append(i.name)
    return databasesNames


*---------------------------------------others----------------------------------------------*

# guarda un objeto en un archivo binario
def commit(objeto, fileName):
    file = open("data/" + fileName + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()


# lee un objeto desde un archivo binario
def rollback(fileName):
    file = open("data/" + fileName + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)
