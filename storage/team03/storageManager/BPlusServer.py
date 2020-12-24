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

    ###############
    # Tables CRUD #
    ###############

    def createT(self, database, nombre, columnas):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Crear un nuevo objeto de Tabla
        nuevaT = Tabla(nombre, columnas)
        #Se inserta la nueva tabla en el arbol
        dbBuscada.objeto.estructura.insertar(nuevaT)

    def showT(self, database):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se retorna la lista de nombres de las tablas
        return dbBuscada.objeto.estructura.getListaNombres()

    def extractT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        #Se retorna una lista con los registros que existen en la tabla
        return tableBuscada.objeto.estructura.extractTable()
        

    def extractRangeT(self, database, table, columnNumber, lower, upper):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        #Se retorna un rango de registros (en la columna dada) que existen en la tabla
        return tableBuscada.objeto.estructura.extractRangeTable(columnNumber, lower, upper)

    def alterADDPK(self, database, table, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Se retorna un numero entero: 0 operación exitosa, 1 error en la operación
        #4 llave primaria existente, 5 columnas fuera de límites.
        return tableBuscada.objeto.estructura.alterAddPK(columns)

    def alterDROPPK(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Se elimina la llave primaria actual en la información de la tabla
        return tableBuscada.objeto.estructura.alterDropPK()
        

    def alterT(self, database, tableOld, tableNew):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Traer el arbol de tablas de la base de datos requerida
        table_tree = dbBuscada.objeto.estructura
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(tableOld)
        tableBuscada = table_tree.buscarObjeto(idTable, tableOld)

        #Crear una nueva Tabla con el nombre nuevo y por default columnas:0
        nuevaT = Tabla(tableNew, 0)

        #Copiar los datos del nodo a cambiarle el nombre en nuevaT
        nuevaT.estructura = tableBuscada.objeto.estructura
        nuevaT.columnas = tableBuscada.objeto.columnas

        #Eliminar la Tabla vieja por medio del objeto del nodo
        dbBuscada.objeto.estructura.eliminar(tableBuscada.objeto)
        #Insertar la Tabla nueva
        dbBuscada.objeto.estructura.insertar(nuevaT)

    def alterAddC(self, database, table, default):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Se agrega una columna al final de cada registro de la tabla con un atributo default.
        #Retorna un valor entero: 0 operación exitosa, 1 error en la operación
        return tableBuscada.objeto.estructura.alterAddColumn(default)

    def alterDropC(self, database, table, columnNumber):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        #Retorna un valor entero: 1 error en la operación
        #4 llave no puede eliminarse o tabla quedarse sin columnas, 5 columna fuera de límites.
        return tableBuscada.objeto.estructura.alterDropColumn(columnNumber)

    def dropT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Se elimina la tabla buscada por medio del objeto contenido en el nodo
        dbBuscada.objeto.estructura.eliminar(tableBuscada.objeto)

    ##################
    # Registers CRUD #
    ##################

    def insert(self, database, table, register):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Se inserta el registro y retorna un valor entero: 1 error en la operación
        #4 llave primaria duplicada, 5 columnas fuera de límites.        
        return tableBuscada.objeto.estructura.insert(register)
    
    def cargarCSV(self, filepath, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Se carga el archivo y retorna una lista con los valores enteros que devuelve el insert
        #por cada fila del CSV, si ocurrió un error o el archivo CSV no tiene filas devuelve una lista vacía [].
        return tableBuscada.objeto.estructura.loadCSV(filepath)

    def extractR(self, database, table, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Retorna una lista con los registros segun la columna enviada
        #Si no hay registros retorna una lista vacia []
        return tableBuscada.objeto.estructura.extractRow(columns)

    def actualizarDatos(self, database, table, register, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Actualiza y retorna un valor entero: 0 operación exitosa, 1 error en la operación
        #4 llave primaria no existe.
        return tableBuscada.objeto.estructura.update(register, columns)
        

    def eliminarRegistro(self, database, table, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Elimina el registro y retorna un valor entero: 0 operación exitosa, 1 error en la operación
        #4 llave primaria no existe.
        return tableBuscada.objeto.estructura.delete(columns)

    def truncateT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Se pone en None la raiz de la estructura B+ de la tabla especificada
        tableBuscada.objeto.estructura.truncateRaiz()

    