#Manager (administrador)
from DataBase import DataBase
from Binary import verify_string, verify_columns
from ArbolAVLManager import ArbolAVLDB
class Manager:
    def __init__(self):
        self.__database = None
        self.__tree__db = ArbolAVLDB()  # Guarda todas las databases

    # Retorna el nombre de la base de datos
    def get_database(self):
        return self.__database

    # Setea el nuevo nombre de la base de datos
    def set_database(self, database):
        self.__database = database

    # Retorna el arbol donde esta guardado las datatables
    def get_tree_db(self):
        return self.__tree__db


    #funciones para las database
    def createDataBase(self, db_nombre):
        if verify_string(db_nombre):
            if self.__tree__db.search_value(db_nombre) is None:
                new_db = DataBase(db_nombre)
                self.__tree__db.add(new_db)
                return 0
            else:
                return 2
        else:
            return 1

    #retorna la lista de las databases existentes
    def showDatabases(self):
        lista2 = list()
        lista = self.__tree__db.get_databases()
        for lista in lista:
            lista2.append(lista.get_database())
        return lista2

    def alterDatabase(self,old_db,new_db):
        bandera = self.__tree__db.search_value(new_db)
        if bandera is None:
            if verify_string(new_db):
                db = self.__tree__db.search_value(old_db)
                if db is not None:
                    self.__tree__db.delete_nodo(db.get_element().get_database())
                    db = db.get_element()
                    db.set_database(new_db)
                    self.__tree__db.add(db)
                    return 0
                else:
                    return 2
            else:
                return 1
        else:
            return 3

    def dropDatabase(self,db_name):
        if verify_string(db_name):
            db_search = self.__tree__db.search_value(db_name)
            if db_search is not None:
                self.__tree__db.delete_nodo(db_name)
                return 0
            else:
                return 2
        else:
            return 1


    #funciones para las tables
    def createTable(self,database,table_name,number_columns):
        db = self.__tree__db.search_value(database)
        if db is not None:
            respuesta = db.get_element().create_table(table_name,number_columns)
        else:
            return 2
        return respuesta

    def showTables(self,database):
        db = self.__tree__db.search_value(database)
        if db is not None:
            tablas = db.get_element().show_tables()
        else:
            return None
        return tablas
