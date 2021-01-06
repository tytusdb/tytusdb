from ArbolAVLDB import ArbolAVLT
from Binary import verify_string, verify_columns
from Table import Table


class DataBase:
    # -----------------------------------------------> Database methods <-----------------------------------------------
    def __init__(self, database):
        self.__database = database
        self.__tree__table = ArbolAVLT()  # Guarda todas las tablas pertenecientes a la base de datos

    # Retorna el nombre de la base de datos
    def get_database(self):
        return self.__database

    def set_arbol(self, arbol):
        self.__tree__table = arbol

    # Setea el nuevo nombre de la base de datos
    def set_database(self, database):
        self.__database = database

    # Retorna el arbol donde esta guardado las tablas pertencientes a la tabla
    def get_tree_table(self):
        return self.__tree__table

    # Metodo funciona para agregar una nueva tabla que pertence a una base de datos
    def create_table(self, table, number_columns):
        if verify_string(table):
            if self.__tree__table.search_value(table) is None:
                new_table = Table(table, number_columns)
                self.__tree__table.add(new_table)

                return 0
            else:
                return 3
        else:
            return 1

    # Metodo que sierve para definir la llave primaria
    def alter_add_pk(self, table_name, columns):
        table = self.__tree__table.search_value(table_name)
        if table:
            table = table.get_element()
            bandera = verify_columns(table.get_nums_columns(), columns)
            if bandera and isinstance(bandera, bool):
                return self.__tree__table.update_table_pk_r(table_name, columns)
            elif not bandera and isinstance(bandera, bool):
                return 5
            elif isinstance(bandera, int):
                return bandera

        else:
            return 3

    def alter_drop_pk(self, table_name):
        table = self.__tree__table.search_value(table_name)
        if table:
            status = self.__tree__table.alter_drop_pk(table_name)
            return status
        else:
            return 3

    # Muestra todas las tablas que pertenencen a una base de datos especifica  -> Retorna una list
    def show_tables(self):
        if self.__tree__table.get_root():
            return self.__tree__table.get_tables()
        else:
            return []

    # Metodo que funciona para modificar el nombre de la tabla
    def alter_table(self, table_old, table_new):
        bandera = self.__tree__table.search_value(table_new)
        if bandera is None:
            if verify_string(table_new):
                table = self.__tree__table.search_value(table_old)
                if table:
                    self.__tree__table.delete_nodo(table.get_element().get_table_name())
                    table = table.get_element()
                    table.set_table_name(table_new)
                    self.__tree__table.add(table)
                    return 0
                else:
                    return 3
            else:
                return 1
        else:
            return 4

    # Metodo que sirve para eliminar una tabla por completo
    def drop_table(self, table):
        if verify_string(table):
            table_search = self.__tree__table.search_value(table)
            if table_search:
                self.__tree__table.delete_nodo(table)
                return 0
            else:
                return 3
        else:
            return 1

    # Agrega una columna al final de cada columna de la tabla
    def alter_add_column(self, table_name, default):
        table = self.__tree__table.search_value(table_name)
        if table:
            status = self.__tree__table.alterAddColumn(table_name, default)
            return status
        else:
            return 3

    # Elimina una n-esima columna de cada registro de la tabla
    def alter_drop_column(self, table_name: str, column_number: int):
        table = self.__tree__table.search_value(table_name)
        if table:
            status = self.__tree__table.alterDropColumn(table_name, column_number)
            return status
        else:
            return 3

    # Extrae y devuelve una lista con elementos que corresponde a cada registro
    def extract_table(self, table_name):
        table = self.__tree__table.search_value(table_name)
        if table:
            table = table.get_element()
            return table.extractTable()
        else:
            return None

    def extract_range_table(self, table_name, column_number, lower, upper):
        table = self.__tree__table.search_value(table_name)
        if table:
            table = table.get_element()
            return table.extractRangeTable(column_number, lower, upper)
        else:
            return None

    # -----------------------------------------------> Record methods <------------------------------------------------
    def insert(self, table_name, register):
        table = self.__tree__table.search_value(table_name)
        if table:
            status = self.__tree__table.insert_tupla(table_name, register)
            return status
        else:
            return 3

    def load_csv(self, file, table_name):
        table = self.__tree__table.search_value(table_name)
        if table:
            status = self.__tree__table.load_csv(table_name, file)
            return status
        else:
            return 3

    def extract_row(self, table_name, columns):
        table = self.__tree__table.search_value(table_name)
        if table:
            status = self.__tree__table.extract_row(table_name, columns)
            return status
        else:
            return 3

    def update(self, table_name, register, columns):
        table = self.__tree__table.search_value(table_name)
        if table:
            status = self.__tree__table.update(table_name, register, columns)
            return status
        else:
            return 3

    def delete(self, table_name, columns):
        table = self.__tree__table.search_value(table_name)
        if table:
            status = self.__tree__table.delete_register(table_name, columns)
            return status
        else:
            return 3

    def truncate(self, table_name):
        status = self.__tree__table.truncate(table_name)
        if status:
            return 0
        else:
            return 3

    def graficar(self, table_name):
        status = self.__tree__table.search_value(table_name)
        return status.get_element().graficar()

    def graficar_tables(self):
        return self.__tree__table.grafica()
