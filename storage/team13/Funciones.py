from os import name
import re
from AVL_DB import Avl as AvlDb
from AVL_Table import Avl as AvlT

DataBase = AvlDb()

def createDatabase(nameDb):
    busqueda = DataBase.buscar(str(nameDb))
    if busqueda == None:
        tabla = AvlT()
        DataBase.insertar(tabla,nameDb)
        return 0
    elif busqueda != None:
        return 2
    else: 
        return 1

def showDatabases():
    bases = DataBase.recorrido()
    lista = bases.split(' ')
    lista.pop()
    return lista

def alterDatabase(databaseOld, databaseNew):
    if re.match(r'[_]?[A-Za-z]+[_]?[_0-9]*[_]?', databaseNew):
        db = DataBase.buscar(str(databaseOld))
        db_new = DataBase.buscar(str(databaseNew))
        if db is None:
            return 2
        elif db_new is not None:
            return 3
        elif db is not None:
            db.name = databaseNew
            return 0
        else:
            return 1
    else:
        return 1
