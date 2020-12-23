#Manager (administrador)
from DataBase import DataBase
from Binary import verify_string, commit, rollback
from ArbolAVLManager import ArbolAVLDB


class Manager:
    def __init__(self):
        self.__database = None
        self.__tree__db = ArbolAVLDB()  # Guarda todas las databases
        self.__file_name = "index"
        self.__roolback_tables()

    # Retorna el nombre de la base de datos
    def get_database(self):
        return self.__database

    # Setea el nuevo nombre de la base de datos
    def set_database(self, database):
        self.__database = database

    # Retorna el arbol donde esta guardado las datatables
    def get_tree_db(self):
        return self.__tree__db

    # funciones para las database
    def createDatabase(self, db_nombre):
        if verify_string(db_nombre):
            if self.__tree__db.search_value(db_nombre) is None:
                new_db = DataBase(db_nombre)
                self.__tree__db.add(new_db)
                self.__save()
                return 0
            else:
                return 2
        else:
            return 1

    # retorna la lista de las databases existentes
    def showDatabases(self):
        # lista2 = list()
        if self.__tree__db.get_root():
            return self.__tree__db.get_databases()
        else:
            return []

        # for lista in lista:
        #     lista2.append(lista.get_database())

    def alterDatabase(self, old_db, new_db):
        bandera = self.__tree__db.search_value(new_db)
        if bandera is None:
            if verify_string(new_db):
                db = self.__tree__db.search_value(old_db)
                if db is not None:
                    self.__tree__db.delete_nodo(db.get_element().get_database())
                    db = db.get_element()
                    db.set_database(new_db)
                    self.__tree__db.add(db)
                    self.__save()
                    return 0
                else:
                    return 2
            else:
                return 1
        else:
            return 3

    def dropDatabase(self, db_name):
        if verify_string(db_name):
            db_search = self.__tree__db.search_value(db_name)
            if db_search is not None:
                self.__tree__db.delete_nodo(db_name)
                self.__save()
                return 0
            else:
                return 2
        else:
            return 1

    # funciones para las tables
    def createTable(self, database, table_name, number_columns):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                respuesta = db.get_element().create_table(table_name, number_columns)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def showTables(self, database):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                tablas = db.get_element().show_tables()
            else:
                return None
            return tablas
        else:
            return 1

    def extractTable(self, database, table_name):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                respuesta = db.get_element().extract_table(table_name)
            else:
                return None
            return respuesta
        else:
            return 1

    def extractRangeTable(self, database, table_name, columnNumber, lower, upper):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                respuesta = db.get_element().extract_range_table(table_name, columnNumber, lower, upper)
            else:
                return None
            return respuesta
        else:
            return 1

    # no tiene el retorno 5 columnas fuera de limites
    def alterAddPK(self, database, table_name, columns):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                respuesta = db.get_element().alter_add_pk(table_name, columns)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    # no tiene retorno 4 pk no existente
    def alterDropPK(self, database, table_name):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                respuesta = db.get_element().alter_drop_pk(table_name)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    # funciones para segunda fase
    # def alterAddFK(self,database, table_name, references):
    # return 1

    # def alterAddIndex(self,database, table_name, references):
    # return 1

    def alterTable(self, database, tableOld, tableNew):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                respuesta = db.get_element().alter_table(tableOld, tableNew)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def alterAddColumn(self, database, table_name, default):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                respuesta = db.get_element().alter_add_column(table_name, default)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def alterDropColumn(self, database, table_name, columnNumber):
        if verify_string(database):
            db = self.__tree__db.search_value(database)
            if db is not None:
                respuesta = db.get_element().alter_drop_column(table_name, columnNumber)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def dropTable(self, database, table_name):
        if verify_string(database):
            db_search = self.__tree__db.search_value(database)
            if db_search is not None:
                respuesta = db_search.get_element().drop_table(table_name)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    # funciones para las tuplas
    # no retorna los errores 4 llave primari a duplicada, 5 columnas fuera de limites.
    def insert(self, database, table_name, register):
        if verify_string(database):
            db_search = self.__tree__db.search_value(database)
            if db_search is not None:
                respuesta = db_search.get_element().insert(table_name, register)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def loadCSV(self, file, database, table_name):

        if verify_string(database):
            db_search = self.__tree__db.search_value(database)
            if db_search is not None:
                respuesta = db_search.get_element().load_csv(file, table_name)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def extractRow(self, database, table_name, columns):
        if verify_string(database):
            db_search = self.__tree__db.search_value(database)
            if db_search is not None:
                respuesta = db_search.get_element().extract_row(table_name, columns)
            else:
                return 2
            return respuesta
        else:
            return 1

    def update(self, database, table_name, register, columns):
        if verify_string(database):
            db_search = self.__tree__db.search_value(database)
            if db_search is not None:
                respuesta = db_search.get_element().update(table_name, register, columns)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def delete(self, database, table_name, columns):
        if verify_string(database):
            db_search = self.__tree__db.search_value(database)
            if db_search is not None:
                respuesta = db_search.get_element().delete(table_name, columns)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def truncate(self, database, table_name):
        if verify_string(database):
            db_search = self.__tree__db.search_value(database)
            if db_search is not None:
                respuesta = db_search.get_element().truncate(table_name)
                self.__save()
            else:
                return 2
            return respuesta
        else:
            return 1

    def graficarRegistros(self, database, table_name):
        if verify_string(database):
            db_search = self.__tree__db.search_value(database)
            if db_search is not None:
                return db_search.get_element().graficar(table_name)
        else:
            return 1

    def graficarTabla(self, database):
        search = self.__tree__db.search_value(database)
        if search:
            return search.get_element().graficar_tables()
        else:
            return 1

    def graficarDB(self):
        return self.__tree__db.grafica()

    def __save(self):
        commit(self.__tree__db, self.__file_name)

    def __roolback_tables(self):
        list_temp = rollback(self.__file_name)
        self.__tree__db = list_temp if list_temp is not None else self.__tree__db
        return list_temp

