# Package:      B+ Server
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Herberth Avila

from storageManager.Arbol_AVL import Arbol_AVL
from storageManager.Base_Datos import Base_Datos
from storageManager.Tabla import Tabla

import pickle
import os

class BPlusServer:
    def __init__(self):
        self.__db_Tree = Arbol_AVL()

    ##################
    # Databases CRUD #
    ##################
    
    def createDB(self, nombre):
        nuevaDB = Base_Datos(nombre)
        self.__db_Tree.insertar(nuevaDB)

    def alterDB(self, old, new):
        #Buscar el nodo con el nombre viejo
        idBuscado = self.__getNombreASCII(old)
        buscado = self.__db_Tree.buscarObjeto(idBuscado, old)
        #Crear una nueva DB con el nombre nuevo
        nuevaDB = Base_Datos(new)
        #Copiar los datos del nodo a cambiarle el nombre en nuevaDB
        nuevaDB.estructura = buscado.objeto.estructura
        #Eliminar la DB vieja
        self.__db_Tree.eliminar(buscado.objeto)
        #Insertar la DB nueva
        self.__db_Tree.insertar(nuevaDB)

    def showDB(self):
        #Se retorna la lista de nombres de las bases de datos
        return self.__db_Tree.getListaNombres()

    def dropDB(self, nombre):
        #Buscar el nodo a eliminar y traerlo
        idBuscado = self.__getNombreASCII(nombre)
        buscado = self.__db_Tree.buscarObjeto(idBuscado, nombre)
        #Elimina por medio del objeto db que tenia el nodo
        self.__db_Tree.eliminar(buscado.objeto)

    