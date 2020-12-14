from os import name
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